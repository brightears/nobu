#!/usr/bin/env python3
"""
Generate monthly invoice for Bright Ears DJ services.
Generates separate invoices per venue: NOBU or Le Du Kaan.
Usage: python generate_invoice.py YYYY-MM --venue nobu|ldk [options]
"""

import argparse
import json
import re
import subprocess
import sys
from calendar import monthrange
from datetime import date
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from string import Template

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

TOTAL_DAILY_RATE = Decimal('11500')  # THB 11,500/day for all 3 slots
HOURLY_RATE = TOTAL_DAILY_RATE / 10  # THB 1,150/hr (10 total DJ hours/day)
VAT_RATE = Decimal('0.07')
WHT_RATE = Decimal('0.03')

# Venue-specific rates (split by hours: NOBU 4hrs, LDK 6hrs = 10hrs total)
VENUES = {
    'nobu': {
        'daily_rate': HOURLY_RATE * 4,   # 4,600/day
        'description': 'NOBU DJ Service',
        'time': '20:00 - 24:00',
        'label': 'NOBU',
        'file_tag': 'nobu',
    },
    'ldk': {
        'daily_rate': HOURLY_RATE * 6,   # 6,900/day
        'description': 'Le Du Kaan DJ Service',
        'time': '18:00 - 24:00',
        'label': 'Le Du Kaan',
        'file_tag': 'ldk',
    },
}

CUSTOMER = {
    'name': 'TCC Hotel Collection Co., Ltd. (Branch 00015)',
    'address': '1 Empire Tower G, 53, 56, 57, 58 Floor, South-Sathorn Road, Yannawa',
    'city': 'Sathorn, Bangkok 10120 Thailand',
    'tax_id': '0105546025131',
}

TAX_NO = '0105550096659'  # Bright Ears tax number

MONTH_NAMES = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

MONTH_FULL = ['', 'January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']

CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

# ---------------------------------------------------------------------------
# Number to words (with hyphens for compound numbers, decimal support)
# ---------------------------------------------------------------------------

ONES = ['', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN',
        'EIGHT', 'NINE', 'TEN', 'ELEVEN', 'TWELVE', 'THIRTEEN',
        'FOURTEEN', 'FIFTEEN', 'SIXTEEN', 'SEVENTEEN', 'EIGHTEEN', 'NINETEEN']
TENS = ['', '', 'TWENTY', 'THIRTY', 'FORTY', 'FIFTY',
        'SIXTY', 'SEVENTY', 'EIGHTY', 'NINETY']


def number_to_words(n):
    """Convert integer to English words (up to 999,999)."""
    if n == 0:
        return 'ZERO'
    if n < 20:
        return ONES[n]
    if n < 100:
        tens, ones = divmod(n, 10)
        return TENS[tens] + ('-' + ONES[ones] if ones else '')
    if n < 1000:
        hundreds, remainder = divmod(n, 100)
        return ONES[hundreds] + ' HUNDRED' + (' ' + number_to_words(remainder) if remainder else '')
    if n < 1000000:
        thousands, remainder = divmod(n, 1000)
        return number_to_words(thousands) + ' THOUSAND' + (' ' + number_to_words(remainder) if remainder else '')
    return str(n)


def amount_to_words(amount):
    """Convert decimal amount to English words for invoice."""
    amount_str = f"{amount:.2f}"
    integer_part, decimal_part = amount_str.split('.')

    words = number_to_words(int(integer_part))

    cents = int(decimal_part)
    if cents > 0:
        words += ' POINT ' + number_to_words(cents)

    return words + ' BAHT'


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def ordinal(n):
    """Return ordinal suffix: 1->st, 2->nd, 3->rd, else->th."""
    if 11 <= n % 100 <= 13:
        return 'th'
    return {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')


def format_date_range(year, month):
    """Format as DD.MM.YY - DD.MM.YY for base charge line."""
    days = monthrange(year, month)[1]
    yy = str(year)[-2:]
    return f"01.{month:02d}.{yy} - {days:02d}.{month:02d}.{yy}"


def format_date_single(year, month, day):
    """Format as DD.MM.YYYY for adjustment lines."""
    return f"{day:02d}.{month:02d}.{year}"


def fmt(amount):
    """Format Decimal amount for display: 3,711.34 THB"""
    return f"{amount:,.2f} THB"


# ---------------------------------------------------------------------------
# Line item builder
# ---------------------------------------------------------------------------

def build_line_items(year, month, venue_config, no_days=None, extra_hours=None,
                     credits=None, additions=None, flat_additions=None):
    """Build invoice line items for a specific venue.

    Args:
        year, month: invoice period
        venue_config: dict with daily_rate, description, time, label
        no_days: list of day numbers where no service was provided
        extra_hours: list of dicts {'day': int, 'time': str, 'hours': int}
        credits: list of dicts {'day': int, 'hours': int, 'description': str}
        additions: list of dicts {'day': int, 'hours': int, 'time': str, 'description': str}
        flat_additions: list of dicts {'day': int, 'amount': Decimal, 'time': str, 'description': str}

    Returns: list of line item dicts
    """
    days_in_month = monthrange(year, month)[1]
    month_abbr = MONTH_NAMES[month]
    daily_rate = venue_config['daily_rate']

    # Base charge: venue daily rate x days in month
    base_amount = daily_rate * days_in_month

    items = [{
        'no': 1,
        'description': venue_config['description'],
        'date': format_date_range(year, month),
        'time': venue_config['time'],
        'price': base_amount,
        'amount': base_amount,
    }]

    # Deductions for cancelled days
    line_no = 2
    if no_days:
        for day in sorted(no_days):
            items.append({
                'no': line_no,
                'description': f'No DJ Service on {month_abbr} {day}<sup>{ordinal(day)}</sup>',
                'date': format_date_single(year, month, day),
                'time': '-',
                'price': -daily_rate,
                'amount': -daily_rate,
            })
            line_no += 1

    # Credits — partial hour deductions on otherwise full days (e.g., DJ late arrival)
    if credits:
        for cr in credits:
            day = cr['day']
            hours = cr['hours']
            credit_amount = (HOURLY_RATE * hours).quantize(
                Decimal('0.01'), rounding=ROUND_HALF_UP
            )
            desc = cr.get('description') or f'Credit: {hours}hr on {month_abbr} {day}<sup>{ordinal(day)}</sup>'
            items.append({
                'no': line_no,
                'description': desc,
                'date': format_date_single(year, month, day),
                'time': '-',
                'price': -credit_amount,
                'amount': -credit_amount,
            })
            line_no += 1

    # Extra hours (partial day charges on cancelled days)
    if extra_hours:
        for eh in extra_hours:
            day = eh['day']
            time_range = eh['time']
            hours = eh['hours']
            partial_amount = (HOURLY_RATE * hours).quantize(
                Decimal('0.01'), rounding=ROUND_HALF_UP
            )

            already_deducted = no_days and day in no_days
            if not already_deducted:
                items.append({
                    'no': line_no,
                    'description': f'No DJ Service on {month_abbr} {day}<sup>{ordinal(day)}</sup>',
                    'date': format_date_single(year, month, day),
                    'time': '-',
                    'price': -daily_rate,
                    'amount': -daily_rate,
                })
                line_no += 1

            desc = eh.get('description', f'DJ Service on {month_abbr} {day}<sup>{ordinal(day)}</sup>')
            items.append({
                'no': line_no,
                'description': desc,
                'date': format_date_single(year, month, day),
                'time': time_range,
                'price': partial_amount,
                'amount': partial_amount,
            })
            line_no += 1

    # Additions — extra charges (e.g., additional DJ at another venue)
    if additions:
        for add in additions:
            day = add['day']
            hours = add['hours']
            time_range = add.get('time', '-')
            add_amount = (HOURLY_RATE * hours).quantize(
                Decimal('0.01'), rounding=ROUND_HALF_UP
            )
            desc = add['description']
            items.append({
                'no': line_no,
                'description': desc,
                'date': format_date_single(year, month, day),
                'time': time_range,
                'price': add_amount,
                'amount': add_amount,
            })
            line_no += 1

    # Flat additions — fixed-amount charges not based on hourly rate (e.g., percussionist)
    if flat_additions:
        for fa in flat_additions:
            day = fa['day']
            flat_amount = fa['amount'].quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            time_range = fa.get('time', '-')
            desc = fa['description']
            items.append({
                'no': line_no,
                'description': desc,
                'date': format_date_single(year, month, day),
                'time': time_range,
                'price': flat_amount,
                'amount': flat_amount,
            })
            line_no += 1

    return items


def build_line_items_html(items):
    """Convert line items to HTML table rows."""
    rows = []
    for item in items:
        price_str = fmt(item['price'])
        amount_str = fmt(item['amount'])
        rows.append(f"""    <tr>
      <td class="col-no">{item['no']}</td>
      <td class="col-desc">{item['description']}</td>
      <td class="col-date">{item['date']}</td>
      <td class="col-time">{item['time']}</td>
      <td class="col-price">{price_str}</td>
      <td class="col-amount">{amount_str}</td>
    </tr>""")
    return '\n'.join(rows)


# ---------------------------------------------------------------------------
# Invoice config (number tracking)
# ---------------------------------------------------------------------------

def get_config_path():
    return Path(__file__).parent.parent / 'invoice_config.json'


def get_next_invoice_no():
    config_path = get_config_path()
    if config_path.exists():
        config = json.loads(config_path.read_text())
        return config['last_invoice_no'] + 1
    return None


def save_invoice_no(invoice_no, month_str):
    config_path = get_config_path()
    config = {'last_invoice_no': invoice_no, 'last_invoice_month': month_str}
    config_path.write_text(json.dumps(config, indent=2) + '\n')


# ---------------------------------------------------------------------------
# PDF generation
# ---------------------------------------------------------------------------

def generate_pdf(html_path, pdf_path):
    """Convert HTML to PDF using Chrome headless."""
    cmd = [
        CHROME,
        '--headless=new',
        '--disable-gpu',
        f'--print-to-pdf={pdf_path}',
        '--print-to-pdf-no-header',
        f'file://{html_path}',
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Warning: PDF generation may have issues: {result.stderr[:200]}")
    return True


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_extra_arg(extra_str):
    """Parse --extra argument: 'DAY:START-END' -> dict"""
    parts = extra_str.split(':')
    if len(parts) < 2:
        print(f"Error: Invalid --extra format: {extra_str}")
        print("Expected: DAY:START-END (e.g., 17:17:00-19:00)")
        sys.exit(1)

    day = int(parts[0])
    time_range = ':'.join(parts[1:])

    time_match = re.match(r'(\d+):(\d+)-(\d+):(\d+)', time_range)
    if time_match:
        start_h = int(time_match.group(1))
        end_h = int(time_match.group(3))
        hours = end_h - start_h
        if hours < 0:
            hours += 24
    else:
        hours = 2

    return {
        'day': day,
        'time': time_range.replace('-', ' - '),
        'hours': hours,
    }


def parse_credit_arg(credit_str):
    """Parse --credit argument: 'DAY:HOURS:Description text' -> dict"""
    parts = credit_str.split(':', 2)
    if len(parts) < 2:
        print(f"Error: Invalid --credit format: {credit_str}")
        print("Expected: DAY:HOURS[:DESCRIPTION] (e.g., 18:1:Late arrival Le Du Kaan)")
        sys.exit(1)

    day = int(parts[0])
    hours = int(parts[1])
    description = parts[2] if len(parts) > 2 else None

    return {'day': day, 'hours': hours, 'description': description}


def parse_add_arg(add_str):
    """Parse --add argument: 'DAY:HOURS:START-END:Description text' -> dict"""
    parts = add_str.split(':', 3)
    if len(parts) < 4:
        print(f"Error: Invalid --add format: {add_str}")
        print("Expected: DAY:HOURS:START-END:DESCRIPTION")
        print("  e.g., 27:4:19:00-23:00:DJ Service 57 Event Terrace")
        sys.exit(1)

    day = int(parts[0])
    hours = int(parts[1])
    remainder = ':'.join(parts[2:])
    time_match = re.match(r'(\d+:\d+\s*-\s*\d+:\d+):(.*)', remainder)
    if time_match:
        time_range = time_match.group(1).replace('-', ' - ').replace('  ', ' ')
        description = time_match.group(2)
    else:
        time_range = '-'
        description = remainder

    return {'day': day, 'hours': hours, 'time': time_range, 'description': description}


def parse_flat_add_arg(flat_str):
    """Parse --flat-add argument: 'DAY:AMOUNT:START-END:Description text' -> dict
    For fixed-amount charges not based on hourly rate (e.g., percussionist)."""
    parts = flat_str.split(':', 3)
    if len(parts) < 4:
        print(f"Error: Invalid --flat-add format: {flat_str}")
        print("Expected: DAY:AMOUNT:START-END:DESCRIPTION")
        print("  e.g., 1:6315.79:11:30-15:30:Percussionist - NOBU Brunch")
        sys.exit(1)

    day = int(parts[0])
    amount = Decimal(parts[1])
    remainder = ':'.join(parts[2:])
    time_match = re.match(r'(\d+:\d+\s*-\s*\d+:\d+):(.*)', remainder)
    if time_match:
        time_range = time_match.group(1).replace('-', ' - ').replace('  ', ' ')
        description = time_match.group(2)
    else:
        time_range = '-'
        description = remainder

    return {'day': day, 'amount': amount, 'time': time_range, 'description': description}


def parse_args():
    parser = argparse.ArgumentParser(description='Generate Bright Ears monthly invoice (per venue)')
    parser.add_argument('month', help='Invoice month (YYYY-MM)')
    parser.add_argument('--venue', required=True, choices=['nobu', 'ldk'],
                        help='Venue: nobu or ldk (Le Du Kaan)')
    parser.add_argument('--invoice-no', type=int, help='Invoice number (auto-increments if omitted)')
    parser.add_argument('--date', help='Invoice date (DD.MM.YYYY, defaults to today)')
    parser.add_argument('--no-day', action='append', type=int, help='Day with no service (e.g., --no-day 15)')
    parser.add_argument('--credit', action='append', help='Hour credit on a full day: DAY:HOURS[:DESCRIPTION]')
    parser.add_argument('--extra', action='append', help='Extra partial hours on cancelled day: DAY:START-END')
    parser.add_argument('--add', action='append', help='Additional charge: DAY:HOURS:START-END:DESCRIPTION')
    parser.add_argument('--flat-add', action='append', help='Fixed-amount charge: DAY:AMOUNT:START-END:DESCRIPTION')
    parser.add_argument('--html-only', action='store_true', help='Skip PDF generation')
    parser.add_argument('--dry-run', action='store_true', help='Preview calculations only')
    return parser.parse_args()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    args = parse_args()

    year, month = map(int, args.month.split('-'))
    month_str = f"{year}-{month:02d}"
    venue_config = VENUES[args.venue]

    # 1. Invoice number
    if args.invoice_no:
        invoice_no = args.invoice_no
    else:
        invoice_no = get_next_invoice_no()
        if invoice_no is None:
            print("Error: No previous invoice found. Use --invoice-no to set the first number.")
            sys.exit(1)

    # 2. Collect cancelled days
    no_days = args.no_day or []
    if no_days:
        print(f"Cancelled days: {sorted(no_days)}")

    # 3. Parse adjustments
    extra_hours = [parse_extra_arg(e) for e in args.extra] if args.extra else None
    credits = [parse_credit_arg(c) for c in args.credit] if args.credit else None
    additions = [parse_add_arg(a) for a in args.add] if args.add else None
    flat_additions = [parse_flat_add_arg(f) for f in args.flat_add] if args.flat_add else None

    # 4. Build line items
    items = build_line_items(year, month, venue_config, no_days or None,
                             extra_hours, credits, additions, flat_additions)

    # 5. Calculate totals
    sub_total = sum(item['amount'] for item in items)
    vat = (sub_total * VAT_RATE).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    grand_total = sub_total + vat
    wht = (sub_total * WHT_RATE).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    net_amount = grand_total - wht

    # 6. Print summary
    print(f"\n{'='*50}")
    print(f"Invoice #{invoice_no} — {venue_config['label']} — {MONTH_FULL[month]} {year}")
    print(f"{'='*50}")
    print(f"\nLine items:")
    for item in items:
        desc = re.sub(r'<[^>]+>', '', item['description']).replace('&amp;', '&')
        print(f"  {item['no']:>2}. {desc:<40} {item['amount']:>12,.2f}")
    print(f"\n  {'Sub Total:':<42} {sub_total:>12,.2f} THB")
    print(f"  {'VAT 7%:':<42} {vat:>12,.2f} THB")
    print(f"  {'Grand Total:':<42} {grand_total:>12,.2f} THB")
    print(f"  {'WHT 3%:':<42} {-wht:>12,.2f} THB")
    print(f"  {'Net Amount:':<42} {net_amount:>12,.2f} THB")
    print(f"\n  Written: {amount_to_words(net_amount)}")

    if args.dry_run:
        print("\n[Dry run — no files generated]")
        return

    # 7. Load template and generate HTML
    template_path = Path(__file__).parent.parent / 'templates' / 'invoice-template.html'
    template = Template(template_path.read_text())

    invoice_date = args.date or date.today().strftime('%d.%m.%Y')

    html = template.safe_substitute(
        INVOICE_NO=f'# {invoice_no}',
        INVOICE_DATE=invoice_date,
        TAX_NO=TAX_NO,
        CUSTOMER_NAME=CUSTOMER['name'],
        CUSTOMER_ADDRESS=CUSTOMER['address'],
        CUSTOMER_CITY=CUSTOMER['city'],
        CUSTOMER_TAX_ID=CUSTOMER['tax_id'],
        LINE_ITEMS_HTML=build_line_items_html(items),
        SUB_TOTAL=fmt(sub_total),
        VAT_AMOUNT=fmt(vat),
        GRAND_TOTAL=fmt(grand_total),
        WHT_AMOUNT=fmt(-wht),
        NET_AMOUNT=fmt(net_amount),
        WRITTEN_AMOUNT=amount_to_words(net_amount),
    )

    # 8. Write output
    output_dir = Path(__file__).parent.parent / month_str
    output_dir.mkdir(exist_ok=True)

    month_abbr = MONTH_NAMES[month].lower()
    venue_tag = venue_config['file_tag']
    filename_base = f"invoice-{invoice_no}-{venue_tag}-{month_abbr}{year}"

    html_path = output_dir / f"{filename_base}.html"
    html_path.write_text(html)
    print(f"\nHTML: {html_path}")

    # 9. Generate PDF
    if not args.html_only:
        pdf_path = output_dir / f"{filename_base}.pdf"
        print(f"Generating PDF...")
        generate_pdf(str(html_path.resolve()), str(pdf_path.resolve()))
        print(f"PDF:  {pdf_path}")

    # 10. Update invoice counter
    save_invoice_no(invoice_no, month_str)
    print(f"\nInvoice #{invoice_no} ({venue_config['label']}) generated successfully.")


if __name__ == '__main__':
    main()
