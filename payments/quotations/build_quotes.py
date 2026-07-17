#!/usr/bin/env python3
"""Generate two NOBU quotations (A4, print/finance-grade, elevated Bright Ears layout):
  Q1 — Aug 4 & 5 opening (special, itemised)
  Q2 — monthly DJ programming rate card
Money doc: numbers computed with Decimal; verified after render."""
from decimal import Decimal, ROUND_HALF_UP

OUT = "/home/brightears/nobu/payments/quotations"
q = lambda x: x.quantize(Decimal("0.01"), ROUND_HALF_UP)
def money(x): return f"{x:,.2f}"

QUOTE_DATE = "17.07.2026"
VALID_UNTIL = "16.08.2026"

# ---- Bright Ears + customer ----
SELLER = dict(
    name="Bright Ears CO., LTD. (Head Office)",
    lines=["11/10, Soi Panjit 3, Garden Home Village",
           "Phaholyothin Road, Amphur Kookot",
           "Lum Luk Ka District, Pathum Thani, Thailand"],
    tel="+66 (0) 85 664 4142", email="office@brightears.com", tax="0105550096659")
CUSTOMER = dict(
    name="TCC Hotel Collection Co., Ltd. (Branch 00015)",
    lines=["1 Empire Tower G, 53, 56, 57, 58 Floor,",
           "South-Sathorn Road, Yannawa Sathorn, Bangkok 10120 Thailand"],
    tax="0105546025131")
BANK = ["BANK OF AYUDHYA PUBLIC COMPANY LIMITED",
        "Fortune Town BR, C.P. Tower II, Ratchadapisek Road, Dindaeng, Bangkok 10400, Thailand.",
        "Account Name: Co.,Ltd. Bright Ears", "Saving Number: 253-1-43635-5", "Swift Code: AYUDTHBK"]

CSS = """
@page { size: A4; margin: 0; }
* { margin:0; padding:0; box-sizing:border-box; }
:root{ --ink:#1c1a17; --muted:#6b6558; --faint:#938c7e; --line:#e4dfd5; --accent:#9c7a2e; --wash:#faf8f3; }
body{ font-family:'Helvetica Neue',Arial,sans-serif; color:var(--ink); font-size:11px; line-height:1.5; }
.page{ width:210mm; min-height:297mm; padding:10mm 16mm 8mm; }
.serif{ font-family:Georgia,'Times New Roman',serif; }

/* header */
.head{ display:flex; justify-content:space-between; align-items:flex-start; }
.co-name{ font-weight:700; font-size:13px; margin-bottom:3px; }
.co p{ line-height:1.55; color:#2c2924; }
.co .contact{ color:var(--muted); margin-top:7px; }
.meta{ text-align:right; min-width:210px; }
.doc-title{ font-family:Georgia,serif; font-size:30px; letter-spacing:1px; color:var(--accent); font-weight:400; }
.doc-sub{ font-size:9px; letter-spacing:3px; text-transform:uppercase; color:var(--faint); margin-top:2px; }
.meta table{ margin-left:auto; margin-top:10px; border-collapse:collapse; }
.meta td{ padding:2px 0; font-size:10.5px; }
.meta td.k{ color:var(--muted); text-transform:uppercase; letter-spacing:1px; font-size:9px; padding-right:14px; text-align:left; }
.meta td.v{ text-align:right; font-weight:600; }
.rule{ height:2px; background:var(--accent); margin:12px 0 0; }
.rule.thin{ height:1px; background:var(--line); }

/* parties */
.parties{ display:flex; gap:40px; margin-top:13px; }
.party{ flex:1; }
.label{ font-size:9px; letter-spacing:2px; text-transform:uppercase; color:var(--accent); font-weight:700; margin-bottom:6px; }
.party .nm{ font-weight:600; }
.party p{ color:#2c2924; line-height:1.5; }
.party .tax{ color:var(--muted); margin-top:4px; }

.reline{ margin-top:12px; font-size:11.5px; }
.reline .label{ display:inline; margin-right:8px; }
.reline span.txt{ color:#2c2924; }

/* tables */
table.items{ width:100%; border-collapse:collapse; margin-top:11px; }
table.items th{ background:var(--ink); color:#f3efe6; font-size:9px; letter-spacing:1.2px; text-transform:uppercase;
                font-weight:600; padding:7px 12px; text-align:left; }
table.items th.r, table.items td.r{ text-align:right; }
table.items th.c, table.items td.c{ text-align:center; }
table.items td{ padding:6px 12px; border-bottom:1px solid var(--line); vertical-align:top; }
table.items tr.alt td{ background:var(--wash); }
.it-name{ font-weight:600; }
.it-sub{ color:var(--muted); font-size:10px; margin-top:2px; }
.hilite td{ background:#f6efdf !important; }
.hilite .it-name{ color:#6d5518; }

/* totals */
.totals{ margin-top:9px; margin-left:auto; width:290px; }
.totals tr td{ padding:3px 0; font-size:11px; }
.totals td.k{ color:var(--muted); }
.totals td.v{ text-align:right; font-variant-numeric:tabular-nums; }
.totals tr.grand td{ font-weight:700; font-size:12.5px; border-top:1px solid var(--line); padding-top:9px; }
.totals tr.net td{ font-weight:700; font-size:13px; color:var(--accent); border-top:2px solid var(--accent); padding-top:9px; }
.totals tr.wht td.v{ color:#9a3b3b; }
.words{ border:1px solid var(--line); background:var(--wash); text-align:center; font-size:9.5px; letter-spacing:.3px;
        padding:6px; margin-top:10px; color:#403b31; }

/* rate-card blocks */
.rate-note{ margin-top:6px; color:var(--muted); font-size:10px; }
.illus{ margin-top:14px; border:1px solid var(--line); border-radius:2px; overflow:hidden; }
.illus .ih{ background:var(--wash); padding:8px 14px; font-size:9px; letter-spacing:1.5px; text-transform:uppercase; color:var(--accent); font-weight:700; border-bottom:1px solid var(--line); }
.illus table{ width:100%; border-collapse:collapse; }
.illus td{ padding:6px 14px; font-size:11px; border-bottom:1px solid #efeadf; }
.illus td.r{ text-align:right; font-variant-numeric:tabular-nums; }
.illus tr:last-child td{ border-bottom:none; }
.illus tr.sum td{ font-weight:700; background:#fbf9f4; }

/* terms + footer */
.terms{ margin-top:13px; }
.terms h4{ font-size:9px; letter-spacing:2px; text-transform:uppercase; color:var(--accent); margin-bottom:5px; }
.terms ul{ list-style:none; }
.terms li{ position:relative; padding-left:16px; margin-bottom:3px; color:#3a362e; font-size:10.5px; line-height:1.45; }
.terms li::before{ content:"—"; position:absolute; left:0; color:var(--accent); }
.spacer{ height:6px; }
.sign{ display:flex; justify-content:space-between; align-items:flex-end; margin-top:10px; }
.sign .accept, .sign .by{ width:44%; }
.sign .sig-line{ border-top:1px solid #b9b3a5; margin-top:20px; padding-top:5px; font-size:10px; color:var(--muted); }
.sign .by .co-sign{ font-weight:700; margin-bottom:0; }
.sign .by .role{ color:var(--muted); font-size:10px; }
.bank{ margin-top:10px; border-top:1px solid var(--line); padding-top:7px; }
.bank .bh{ font-size:9px; letter-spacing:2px; text-transform:uppercase; color:var(--accent); font-weight:700; margin-bottom:6px; }
.bank p{ color:var(--muted); font-size:10px; line-height:1.55; }
.foot{ margin-top:6px; text-align:center; font-size:9px; letter-spacing:2px; text-transform:uppercase; color:var(--faint); }
"""

def header(no):
    seller_lines = "".join(f"<p>{l}</p>" for l in SELLER["lines"])
    return f"""
  <div class="head">
    <div class="co">
      <p class="co-name">{SELLER['name']}</p>
      {seller_lines}
      <p class="contact">Tel.: {SELLER['tel']} &nbsp;·&nbsp; {SELLER['email']}</p>
    </div>
    <div class="meta">
      <div class="doc-title">Quotation</div>
      <div class="doc-sub">Bright Ears · DJ Programming</div>
      <table>
        <tr><td class="k">Quotation No.</td><td class="v">{no}</td></tr>
        <tr><td class="k">Date</td><td class="v">{QUOTE_DATE}</td></tr>
        <tr><td class="k">Valid Until</td><td class="v">{VALID_UNTIL}</td></tr>
        <tr><td class="k">Tax No.</td><td class="v">{SELLER['tax']}</td></tr>
      </table>
    </div>
  </div>
  <div class="rule"></div>"""

def parties(re_text):
    cust_lines = "".join(f"<p>{l}</p>" for l in CUSTOMER["lines"])
    return f"""
  <div class="parties">
    <div class="party">
      <div class="label">Quotation To</div>
      <p class="nm">{CUSTOMER['name']}</p>
      {cust_lines}
      <p class="tax">Tax ID: {CUSTOMER['tax']}</p>
    </div>
  </div>
  <div class="reline"><span class="label">Re</span><span class="txt">{re_text}</span></div>"""

def signature_bank():
    bank = "".join(f"<p>{l}</p>" for l in BANK)
    return f"""
  <div class="sign">
    <div class="accept"><div class="sig-line">Accepted by (Customer) &nbsp;·&nbsp; Date</div></div>
    <div class="by">
      <p class="co-sign">Bright Ears Co., Ltd.</p>
      <div class="sig-line">Kullaphat Wittayaphan &nbsp;·&nbsp; Managing Director</div>
    </div>
  </div>
  <div class="bank">
    <div class="bh">Bank Information</div>
    {bank}
  </div>
  <div class="foot">Bright Ears — DJ Booking, Scheduling &amp; Management · Bangkok</div>"""

def wrap(no, body):
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head>
<body><div class="page">{header(no)}{body}{signature_bank()}</div></body></html>"""

# ============ QUOTATION 1 — opening ============
def q1():
    rate = Decimal("2500"); hrs = 4; dj = q(rate*hrs); mus = Decimal("10000")
    rows = [
        ("DJ Performance — Aopsher", "Tuesday 4 August 2026 · 20:00–24:00 · new-concept opening",
         "4 hrs", "2,500 / hr", dj),
        ("Live Musician — Violin (Champ)", "Tuesday 4 August 2026 · opening night", "1 night", "10,000 / night", mus),
        ("DJ Performance — Funktastic", "Wednesday 5 August 2026 · 20:00–24:00 · new-concept opening",
         "4 hrs", "2,500 / hr", dj),
        ("Live Musician — Saxophone (Sir I Sax)", "Wednesday 5 August 2026 · opening night", "1 night", "10,000 / night", mus),
    ]
    sub = sum((r[4] for r in rows), Decimal("0"))
    vat = q(sub*Decimal("0.07")); grand = sub+vat; wht = q(sub*Decimal("0.03")); net = grand-wht
    tr = ""
    for i,(nm,su,qty,pr,amt) in enumerate(rows):
        tr += f"""<tr class="{'alt' if i%2 else ''}">
          <td><div class="it-name">{nm}</div><div class="it-sub">{su}</div></td>
          <td class="c">{qty}</td><td class="r">{pr}</td><td class="r">{money(amt)}</td></tr>"""
    body = parties("DJ &amp; live-musician programming for the opening of the new NOBU concept — 4 &amp; 5 August 2026.") + f"""
  <table class="items">
    <tr><th>Description</th><th class="c">Qty</th><th class="r">Rate (THB)</th><th class="r">Amount (THB)</th></tr>
    {tr}
  </table>
  <table class="totals">
    <tr><td class="k">Sub Total</td><td class="v">{money(sub)} THB</td></tr>
    <tr><td class="k">VAT 7%</td><td class="v">{money(vat)} THB</td></tr>
    <tr class="grand"><td class="k">Grand Total</td><td class="v">{money(grand)} THB</td></tr>
    <tr class="wht"><td class="k">Less WHT 3%</td><td class="v">-{money(wht)} THB</td></tr>
    <tr class="net"><td class="k">Net Payable</td><td class="v">{money(net)} THB</td></tr>
  </table>
  <div class="words">{words_line(net)}</div>
  <div class="terms">
    <h4>Terms &amp; Conditions</h4>
    <ul>
      <li>Rates are exclusive of VAT; 7% VAT is added and 3% withholding tax is deducted at source (net payable as above).</li>
      <li>DJ &amp; sound equipment provided by the venue.</li>
      <li>Performance times may be adjusted by mutual agreement; changes require 48 hours' notice.</li>
      <li>This quotation is valid until {VALID_UNTIL}.</li>
    </ul>
  </div>
  <div class="spacer"></div>"""
    return wrap("QT-NOBU-2026-08-01", body), dict(sub=sub,vat=vat,grand=grand,wht=wht,net=net)

# ============ QUOTATION 2 — monthly rate card ============
def q2():
    wn = Decimal("1150"); wn_night = q(wn*4)          # 4,600
    we = Decimal("2500"); we_night = q(we*4)          # 10,000
    # illustrative week
    wk_wn = wn_night*5; wk_we = we_night*2; wk_sub = wk_wn+wk_we
    wk_vat = q(wk_sub*Decimal("0.07")); wk_grand = wk_sub+wk_vat; wk_wht=q(wk_sub*Decimal("0.03")); wk_net=wk_grand-wk_wht
    body = parties("Ongoing DJ programming for NOBU Bangkok (new floor / concept) — monthly, from August 2026.") + f"""
  <table class="items">
    <tr><th>Service</th><th>Schedule</th><th class="c">Set</th><th class="r">Rate</th><th class="r">Per Night (THB)</th></tr>
    <tr>
      <td><div class="it-name">Resident DJ — Weeknights</div><div class="it-sub">One DJ per night</div></td>
      <td>Sunday – Thursday<div class="it-sub">20:00 – 24:00</div></td>
      <td class="c">4 hrs</td><td class="r">1,150 / hr</td><td class="r">{money(wn_night)}</td>
    </tr>
    <tr class="hilite">
      <td><div class="it-name">DJ Programming — Weekends</div><div class="it-sub">Two DJs, two hours each — sustained energy</div></td>
      <td>Friday &amp; Saturday<div class="it-sub">20:00 – 24:00</div></td>
      <td class="c">4 hrs</td><td class="r">2,500 / hr</td><td class="r">{money(we_night)}</td>
    </tr>
  </table>
  <div class="rate-note">All rates exclusive of VAT. 7% VAT added; 3% withholding tax deducted at source. DJ &amp; sound equipment provided by the venue.</div>

  <div class="illus">
    <div class="ih">Illustrative weekly total &nbsp;·&nbsp; a standard week (5 weeknights + 2 weekend nights)</div>
    <table>
      <tr><td>Weeknights — 5 × {money(wn_night)}</td><td class="r">{money(wk_wn)} THB</td></tr>
      <tr><td>Weekends — 2 × {money(we_night)}</td><td class="r">{money(wk_we)} THB</td></tr>
      <tr class="sum"><td>Weekly Sub Total</td><td class="r">{money(wk_sub)} THB</td></tr>
      <tr><td>VAT 7%</td><td class="r">{money(wk_vat)} THB</td></tr>
      <tr><td>Less WHT 3%</td><td class="r">-{money(wk_wht)} THB</td></tr>
      <tr class="sum"><td>Weekly Net Payable</td><td class="r">{money(wk_net)} THB</td></tr>
    </table>
  </div>
  <div class="rate-note">Monthly invoice is calculated on actual nights performed (a month averages ~4.3 weeks). Figures above are illustrative for budgeting.</div>

  <div class="terms">
    <h4>Terms &amp; Conditions</h4>
    <ul>
      <li>Invoiced monthly in arrears on actual nights performed; payment per the existing Bright Ears – NOBU cycle.</li>
      <li>DJ &amp; sound equipment provided by the venue.</li>
      <li>Weather / venue cancellation with 3 hours' notice: no charge for that night.</li>
      <li>Schedule changes require 48 hours' notice.</li>
      <li>This rate applies to the proposed 6-month term and is valid until {VALID_UNTIL}.</li>
    </ul>
  </div>
  <div class="spacer"></div>"""
    return wrap("QT-NOBU-2026-08-02", body), dict(wn_night=wn_night, we_night=we_night, wk_sub=wk_sub, wk_net=wk_net)

# amount-in-words
_ones=['','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE','TEN','ELEVEN','TWELVE','THIRTEEN','FOURTEEN','FIFTEEN','SIXTEEN','SEVENTEEN','EIGHTEEN','NINETEEN']
_tens=['','','TWENTY','THIRTY','FORTY','FIFTY','SIXTY','SEVENTY','EIGHTY','NINETY']
def _w3(n):
    r=[]
    if n>=100: r.append(_ones[n//100]+' HUNDRED'); n%=100
    if n>=20: r.append(_tens[n//10]+(('-'+_ones[n%10]) if n%10 else '')); n=0
    if n>0: r.append(_ones[n])
    return ' '.join(r)
def _words(n):
    if n==0: return 'ZERO'
    parts=[]
    for div,name in [(1000000,'MILLION'),(1000,'THOUSAND'),(1,'')]:
        if n>=div: parts.append(_w3(n//div)+((' '+name) if name else '')); n%=div
    return ' '.join(parts).strip()
def words_line(net):
    b=int(net); d=int((net-b)*100)
    if d==0: return f"{_words(b)} BAHT"
    return f"{_words(b)} POINT {_words(d)} BAHT"

h1, t1 = q1(); h2, t2 = q2()
open(f"{OUT}/QT-NOBU-2026-08-01-opening.html","w").write(h1)
open(f"{OUT}/QT-NOBU-2026-08-02-monthly-ratecard.html","w").write(h2)
print("Q1 totals:", {k:str(v) for k,v in t1.items()})
print("Q2 rates:", {k:str(v) for k,v in t2.items()})
print("wrote 2 quotation HTML files to", OUT)
