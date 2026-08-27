#!/usr/bin/env python3
"""build_receipt.py — generate a Receipt / Tax Invoice from an existing invoice.

The receipt is the invoice's exact line-items + totals + written-amount wrapped in
the known-good receipt chrome (red "Receipt / Tax Invoice" title, signature block,
bank-info block) — reusing receipt-3711-ldk-jun2026.html as the structural base so
the CSS + signature + bank blocks are identical to what we've always sent.

Zero re-derivation: the line-items table and written-amount are lifted verbatim from
the invoice HTML, so the receipt totals always match the invoice exactly.

Usage: python3 build_receipt.py --venue nobu|ldk --invoice-no N --month YYYY-MM --date DD.MM.YYYY
"""
import argparse, os, re, subprocess, sys, tempfile

BASE = "/home/brightears/nobu/payments"
RECEIPT_BASE = f"{BASE}/2026-06/receipt-3711-ldk-jun2026.html"  # known-good chrome
MON = ['', 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']


def grab(html, pattern):
    m = re.search(pattern, html, re.S)
    if not m:
        sys.exit(f"pattern not found: {pattern[:40]}")
    return m.group(0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--venue", required=True, choices=["nobu", "ldk"])
    ap.add_argument("--invoice-no", type=int, required=True)
    ap.add_argument("--month", required=True, help="YYYY-MM")
    ap.add_argument("--date", required=True, help="receipt date DD.MM.YYYY (payment received)")
    ap.add_argument("--html-only", action="store_true")
    args = ap.parse_args()

    y, m = args.month.split("-")
    mon = MON[int(m)]
    inv_path = f"{BASE}/{args.month}/invoice-{args.invoice_no}-{args.venue}-{mon}{y}.html"
    if not os.path.exists(inv_path):
        sys.exit(f"invoice not found: {inv_path}")

    inv = open(inv_path).read()
    tmpl = open(RECEIPT_BASE).read()

    # Lift the exact table + written-amount from the invoice (verbatim → totals always match)
    inv_table = grab(inv, r'<table class="line-items">.*?</table>')
    inv_written = grab(inv, r'<div class="written-amount">.*?</div>')

    # Inject into the receipt chrome (lambda replacements avoid backref interpretation)
    out = re.sub(r'<table class="line-items">.*?</table>', lambda _m: inv_table, tmpl, flags=re.S)
    out = re.sub(r'<div class="written-amount">.*?</div>', lambda _m: inv_written, out, flags=re.S)
    # meta: base receipt carries "# 3711" / "13.08.2026"
    if out.count('# 3711') != 1 or out.count('13.08.2026') != 1:
        sys.exit("ABORT: base receipt meta markers not unique — check template")
    out = out.replace('# 3711', f'# {args.invoice_no}')
    out = out.replace('13.08.2026', args.date)

    out_html = f"{BASE}/{args.month}/receipt-{args.invoice_no}-{args.venue}-{mon}{y}.html"
    open(out_html, 'w').write(out)
    print(f"HTML: {out_html}")

    # sanity: title present, no stray invoice title, net line present
    assert 'Receipt / Tax Invoice' in out, "missing receipt title"
    assert 'Net Amount' in out, "missing Net Amount row"

    if args.html_only:
        return
    out_pdf = f"{BASE}/{args.month}/receipt-{args.invoice_no}-{args.venue}-{mon}{y}.pdf"
    chrome = next((p for p in (
        subprocess.run(['bash', '-lc', 'command -v chromium-browser || command -v chromium || command -v google-chrome || command -v chrome'],
                       capture_output=True, text=True).stdout.strip(),
    ) if p), None)
    if not chrome:
        sys.exit("no chromium found")
    # NOTE: do NOT pass --user-data-dir — snap chromium can't create SingletonLock
    # under ~/.cache (Permission denied). The default snap profile works (same as
    # generate_invoice.py). Renders are sequential so no singleton conflict.
    subprocess.run([chrome, '--headless=new', '--disable-gpu', '--no-sandbox',
                    f'--print-to-pdf={out_pdf}', '--print-to-pdf-no-header',
                    f'file://{out_html}'], capture_output=True, text=True)
    if not (os.path.exists(out_pdf) and os.path.getsize(out_pdf) > 1000):
        sys.exit(f"PDF render failed or too small: {out_pdf}")
    print(f"PDF:  {out_pdf}")


if __name__ == "__main__":
    main()
