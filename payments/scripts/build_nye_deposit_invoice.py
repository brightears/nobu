#!/usr/bin/env python3
"""NOBU + LDK — New Year's Eve 2026: 20% DEPOSIT invoice.
One-off deposit invoice for the NYE special-event engagement (4 DJs on standby,
Joyyly / Zara Gift / Funktastic / Riot Huntt, 31 Dec 2026, both venues).
Norbert-confirmed 2026-08-25 (msg 5501): 20% downpayment for all DJs on signing.

Deposit invoices the 20% FEE portion of the THB 220,000 engagement:
  fee 44,000 + 7% VAT 3,080 = 47,080 gross ; less 3% WHT 1,320 = 45,760 net.
The 80% balance (fee 176,000) is invoiced separately after the event.

Reuses the house invoice template + amount_to_words from generate_invoice.py.
Provisional invoice number passed via --invoice-no (does NOT touch invoice_config.json —
this is a draft for Norbert's review; renumber/persist on his approval).
Usage: python3 build_nye_deposit_invoice.py --invoice-no 3712 [--date DD.MM.YYYY]"""
import argparse
from decimal import Decimal, ROUND_HALF_UP
from datetime import date
from pathlib import Path
from string import Template
import generate_invoice as gi

PORTION = Decimal('0.20')          # 20% deposit
FEE_TOTAL = Decimal('220000')      # 4 x 55,000 full engagement fee (ex-VAT)
VAT_RATE = Decimal('0.07'); WHT_RATE = Decimal('0.03')

def fmt(a): return f"{a:,.2f} THB"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--invoice-no', type=int, required=True)
    ap.add_argument('--date', help='DD.MM.YYYY (default today)')
    ap.add_argument('--html-only', action='store_true')
    args = ap.parse_args()

    dep_fee = (FEE_TOTAL * PORTION).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)  # 44,000
    sub_total = dep_fee
    vat = (sub_total * VAT_RATE).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)      # 3,080
    grand = sub_total + vat                                                             # 47,080
    wht = (sub_total * WHT_RATE).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)      # 1,320
    net = grand - wht                                                                   # 45,760
    assert (sub_total, vat, grand, wht, net) == (Decimal('44000.00'), Decimal('3080.00'),
        Decimal('47080.00'), Decimal('1320.00'), Decimal('45760.00')), (sub_total,vat,grand,wht,net)

    desc = ("New Year&rsquo;s Eve 2026 &mdash; DJ Standby, four (4) DJs "
            "(Joyyly, Zara Gift, Funktastic, Riot Huntt) &middot; NOBU Bangkok &amp; Le Du Kaan "
            "&middot; <b>20% Deposit</b> of THB 220,000.00 engagement fee")
    line = f"""    <tr>
      <td class="col-no">1</td>
      <td class="col-desc">{desc}</td>
      <td class="col-date">31.12.2026</td>
      <td class="col-time">All night</td>
      <td class="col-price">{fmt(dep_fee)}</td>
      <td class="col-amount">{fmt(dep_fee)}</td>
    </tr>"""

    tpl = Template((Path(gi.__file__).parent.parent / 'templates' / 'invoice-template.html').read_text())
    inv_date = args.date or date.today().strftime('%d.%m.%Y')
    html = tpl.safe_substitute(
        INVOICE_NO=f'# {args.invoice_no}', INVOICE_DATE=inv_date, TAX_NO=gi.TAX_NO,
        CUSTOMER_NAME=gi.CUSTOMER['name'], CUSTOMER_ADDRESS=gi.CUSTOMER['address'],
        CUSTOMER_CITY=gi.CUSTOMER['city'], CUSTOMER_TAX_ID=gi.CUSTOMER['tax_id'],
        LINE_ITEMS_HTML=line, SUB_TOTAL=fmt(sub_total), VAT_AMOUNT=fmt(vat),
        GRAND_TOTAL=fmt(grand), WHT_AMOUNT=fmt(-wht), NET_AMOUNT=fmt(net),
        WRITTEN_AMOUNT=gi.amount_to_words(net))

    outdir = Path(gi.__file__).parent.parent / '2026-12'
    outdir.mkdir(exist_ok=True)
    base = f"invoice-{args.invoice_no}-nobuldk-nye-deposit-dec2026"
    hp = outdir / f"{base}.html"; hp.write_text(html)
    print(f"HTML: {hp}")
    print(f"Deposit {fmt(sub_total)} +VAT {fmt(vat)} = {fmt(grand)} -WHT {fmt(wht)} = NET {fmt(net)}")
    print(f"Written: {gi.amount_to_words(net)}")
    if not args.html_only:
        pp = outdir / f"{base}.pdf"; gi.generate_pdf(str(hp.resolve()), str(pp.resolve()))
        print(f"PDF:  {pp}")

if __name__ == '__main__':
    main()
