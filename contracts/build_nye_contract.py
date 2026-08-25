#!/usr/bin/env python3
"""NOBU + LDK — New Year's Eve 2026 Special-Event Entertainment Agreement.
Modeled verbatim on the regular NOBU/LDK agreement (build_contract.py); this is the
separate NYE special-event contract the regular agreement refers to. 4 DJs on standby,
NAMED (Norbert 2026-08-25 msg 5501 — confirmed 4 DJs: Joyyly, Zara Gift, Funktastic,
Riot Huntt; both venues NOBU+LDK). Rate 55,000/night ex-VAT per the approved quote
QT-NOBULDK-NYE-2026. Payment terms: 20% deposit on signing / 80% balance after event
(Norbert 5499/5501 — uniform 20% downpayment for all DJs). On-brand (logo + cyan)."""
import json, base64
OUT="/home/brightears/nobu/contracts"
fonts=json.load(open("/home/brightears/BrightEars-Ops/data/brand/inter-fonts-base64.json"))
LOGO=base64.b64encode(open("/home/brightears/BrightEars-Ops/data/brand/logo-light.png","rb").read()).decode()

CYAN="#00bbe4"; CYAN_D="#0093b5"; INK="#1a1a1a"; MUTED="#5f5f5f"; LINE="#dcdcdc"
FONTFACE=f"""
@font-face{{font-family:'Inter';font-weight:400;src:url(data:font/woff2;base64,{fonts['inter400']}) format('woff2');}}
@font-face{{font-family:'Inter';font-weight:600;src:url(data:font/woff2;base64,{fonts['inter600']}) format('woff2');}}
"""
CSS=f"""
{FONTFACE}
@page{{ size:A4; margin:15mm 18mm 14mm; }}
*{{ margin:0; padding:0; box-sizing:border-box; }}
body{{ font-family:'Inter',Arial,sans-serif; color:{INK}; font-size:10.5px; line-height:1.55; }}
.hdr{{ display:flex; align-items:center; gap:14px; padding-bottom:9px; border-bottom:2px solid {CYAN}; }}
.hdr img{{ width:42px; height:42px; }}
.wordmark{{ font-family:Georgia,serif; font-size:19px; letter-spacing:1.5px; }}
.wordmark .be{{ color:{CYAN_D}; }}
.tagline{{ font-size:7.5px; letter-spacing:2.5px; text-transform:uppercase; color:{MUTED}; margin-top:2px; }}
h1{{ text-align:center; font-family:Georgia,serif; font-weight:400; font-size:21px; letter-spacing:1px; color:{CYAN_D}; margin-top:16px; }}
.date{{ text-align:center; color:{MUTED}; font-size:11px; margin-top:3px; margin-bottom:12px; }}
h2{{ font-size:11px; font-weight:600; color:{CYAN_D}; text-transform:uppercase; letter-spacing:1px; margin:13px 0 4px; }}
p{{ margin:4px 0; text-align:justify; }}
.hours p, .fee p{{ margin:3px 0; }}
.b{{ font-weight:600; }}
.feebox{{ border:1px solid {LINE}; border-left:3px solid {CYAN}; border-radius:2px; padding:9px 13px; margin:7px 0; }}
.feebox .fl{{ display:flex; justify-content:space-between; padding:4px 0; border-bottom:1px solid #eee; }}
.feebox .fl:last-child{{ border-bottom:none; }}
.feebox .fl .d{{ font-weight:600; }} .feebox .fl .d small{{ font-weight:400; color:{MUTED}; }}
.feebox .fl .n{{ text-align:right; font-variant-numeric:tabular-nums; white-space:nowrap; }}
.feebox .fl .n b{{ color:{CYAN_D}; }}
.feebox .tot{{ display:flex; justify-content:space-between; padding:4px 0; border-top:1px solid #ddd; }}
.feebox .tot.grand{{ border-top:2px solid {CYAN}; }} .feebox .tot .n{{ font-variant-numeric:tabular-nums; }}
.feebox .tot .n b{{ color:{CYAN_D}; }}
.note{{ background:#f4fbfd; border-left:3px solid {CYAN}; border-radius:2px; padding:7px 12px; margin:8px 0; }}
.note p{{ margin:0; text-align:left; }}
section{{ page-break-inside:avoid; }}
.sig{{ page-break-inside:avoid; margin-top:22px; }}
.sig p.pre{{ font-style:italic; color:#333; margin-bottom:16px; }}
.sigtable{{ display:flex; gap:40px; }}
.sigcol{{ flex:1; }}
.sigcol .co{{ font-weight:600; margin-bottom:6px; }}
.sigblk{{ padding-top:48px; }}
.sigline{{ border-bottom:1px solid #999; height:1px; margin-bottom:5px; }}
.signame{{ font-weight:600; font-size:10.5px; }} .sigrole{{ color:{MUTED}; font-size:10px; }}
"""

def sec(h, *paras, cls=""):
    body="".join(f"<p>{x}</p>" for x in paras)
    return f'<section class="{cls}"><h2>{h}</h2>{body}</section>'

# ---- DJ line-up (Norbert-confirmed 2026-08-25 msg 5501) ----
DJ_NAMES=["Joyyly","Zara Gift","Funktastic","Riot Huntt"]
DJ_LIST="Joyyly, Zara Gift, Funktastic and Riot Huntt"

# ---- Fee figures (4 DJs @ 55,000 standby) — asserted ----
DJS=4; RATE=55000
SUB=DJS*RATE                    # 220,000
VAT=round(SUB*0.07)             # 15,400
GRAND=SUB+VAT                   # 235,400
WHT=round(SUB*0.03)             # 6,600
NET=GRAND-WHT                   # 228,800
assert (SUB,VAT,GRAND,WHT,NET)==(220000,15400,235400,6600,228800), (SUB,VAT,GRAND,WHT,NET)

# ---- 20% deposit / 80% balance split (Norbert 5499/5501) — asserted ----
DEP_GRAND=round(GRAND*0.20)     # 47,080
BAL_GRAND=GRAND-DEP_GRAND       # 188,320
DEP_WHT=round(WHT*0.20)         # 1,320
BAL_WHT=WHT-DEP_WHT             # 5,280
DEP_NET=DEP_GRAND-DEP_WHT       # 45,760
BAL_NET=BAL_GRAND-BAL_WHT       # 183,040
assert (DEP_GRAND,BAL_GRAND)==(47080,188320), (DEP_GRAND,BAL_GRAND)
assert DEP_NET+BAL_NET==NET, (DEP_NET,BAL_NET,NET)

def thb(n): return f"{n:,.2f}"

fee_box=f"""
<div class="feebox">
  <div class="fl"><div class="d">DJ Performance (standby) &mdash; four (4) DJs
      <small>&mdash; {DJ_LIST} &middot; New Year&rsquo;s Eve, 31 December 2026 &middot; NOBU Bangkok &amp; Le Du Kaan &middot; on standby all night</small></div>
    <div class="n">4 &times; THB 55,000 / night = <b>THB {thb(SUB)}</b></div></div>
  <div class="tot"><div class="d">Sub Total</div><div class="n">THB {thb(SUB)}</div></div>
  <div class="tot"><div class="d">VAT 7%</div><div class="n">THB {thb(VAT)}</div></div>
  <div class="tot grand"><div class="d b">Grand Total</div><div class="n"><b>THB {thb(GRAND)}</b></div></div>
  <div class="tot"><div class="d">Less Withholding Tax 3%</div><div class="n">&minus; THB {thb(WHT)}</div></div>
  <div class="tot grand"><div class="d b">Net Payable</div><div class="n"><b>THB {thb(NET)}</b></div></div>
</div>
<p style="text-align:center;color:{MUTED};font-size:9.5px;margin-top:2px">TWO HUNDRED TWENTY-EIGHT THOUSAND EIGHT HUNDRED BAHT</p>"""

pay_box=f"""
<div class="feebox">
  <div class="fl"><div class="d">Deposit &mdash; 20% on signing <small>&mdash; secures the engagement &amp; the DJs&rsquo; reservation for the date</small></div>
    <div class="n"><b>THB {thb(DEP_GRAND)}</b> <small>incl. VAT</small></div></div>
  <div class="fl"><div class="d">Balance &mdash; 80% after the event <small>&mdash; due upon the Agency&rsquo;s final invoice</small></div>
    <div class="n"><b>THB {thb(BAL_GRAND)}</b> <small>incl. VAT</small></div></div>
  <div class="tot grand"><div class="d b">Grand Total (incl. VAT)</div><div class="n"><b>THB {thb(GRAND)}</b></div></div>
  <div class="tot"><div class="d">Less Withholding Tax 3% (deducted at source across both instalments)</div><div class="n">&minus; THB {thb(WHT)}</div></div>
  <div class="tot grand"><div class="d b">Net Payable</div><div class="n"><b>THB {thb(NET)}</b></div></div>
</div>"""

HTML=f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
  <div class="hdr"><img src="data:image/png;base64,{LOGO}" alt="Bright Ears"/>
    <div><div class="wordmark">BRIGHT <span class="be">EARS</span></div>
    <div class="tagline">DJ Booking · Scheduling · Management</div></div></div>

  <h1>ENTERTAINMENT AGREEMENT</h1>
  <div class="date">Special Event &mdash; New Year&rsquo;s Eve, 31 December 2026</div>

  <p>This agreement is made between <span class="b">TCC Hotel Collection Co., Ltd.</span>, located at 1 Empire Tower G, 53, 56, 57, 58 Floor, South Sathorn Road, Yannawa, Sathorn, Bangkok 10120, Thailand (TEL: 024071645, TAX ID: 0105546025131, Branch 00015), hereinafter referred to as the &ldquo;Venue&rdquo; and <span class="b">Bright Ears Co., Ltd.</span>, with its Head Office at Garden Home Village, Phaholyothin Road, Amphur Kookot, Lum Luk Ka District, Pathum Thani, Thailand (TEL: 0856644142, TAX ID: 0105550096659), hereinafter referred to as the &ldquo;Agency.&rdquo;</p>

  {sec("Performance Details", f"The Venue hereby engages the Agency to provide entertainment services for its New Year&rsquo;s Eve programme at NOBU Bangkok and Le Du Kaan. The Agency&rsquo;s entertainers &mdash; {DJ_LIST} &mdash; agree to perform as DJs on the night of 31 December 2026.")}

  {sec("Working Schedule", "The working schedule for the event shall be mutually agreed upon between the Agency and the Venue. Any changes to the standby or performance arrangements must be communicated at least 48 hours in advance unless otherwise agreed by both parties.")}

  <section class="hours"><h2>Hours of Work</h2>
    <p>This engagement covers the New Year&rsquo;s Eve programme on <span class="b">31 December 2026</span>. <span class="b">Four (4) DJs &mdash; {DJ_LIST}</span> &mdash; shall be on standby for the full night across NOBU Bangkok and Le Du Kaan, performing as directed by the Venue to maintain the energy of the evening throughout.</p>
  </section>

  {sec("Duties and Responsibilities", "The Entertainer will ensure that particular attention is given to building up the atmosphere throughout the night in accordance with the audience type. Music must be played in continuous mode during each set of performance. An appropriate level of energy is expected at all times.")}

  {sec("Equipment", "The Venue shall provide all necessary music equipment for the performance. The Entertainer will be responsible for taking good care of and maintaining the equipment provided by the Venue during performance hours. The Venue shall maintain appropriate insurance coverage for its own equipment.")}

  <section class="fee"><h2>Fee</h2>
    <p>The Venue agrees to pay the Agency the following for the New Year&rsquo;s Eve engagement:</p>
    {fee_box}
    <p>Rates are exclusive of VAT; 7% VAT is added and 3% withholding tax is deducted at source, giving the Net Payable shown above.</p>
  </section>

  <section class="fee"><h2>Payment Terms</h2>
    <p>The fee shall be paid in two instalments by direct bank transfer to the Agency&rsquo;s account:</p>
    {pay_box}
    <p>A <span class="b">20% deposit (THB {thb(DEP_GRAND)}, inclusive of VAT)</span> is due upon signing of this Agreement to confirm the engagement and reserve the DJs for the date. The remaining <span class="b">80% balance (THB {thb(BAL_GRAND)}, inclusive of VAT)</span> is due after the event, upon receipt of the Agency&rsquo;s final invoice. Withholding tax of 3% (THB {thb(WHT)} in total) is deducted at source across the instalments, giving a net total payable of <span class="b">THB {thb(NET)}</span>.</p>
  </section>

  <section><h2>Bank Information</h2>
    <p style="margin:2px 0">BANK OF AYUDHYA PUBLIC COMPANY LIMITED<br>Fortune Town BR, C.P. Tower II, Ratchadapisek Road, Dindaeng, Bangkok 10400, Thailand<br>Account Name: Co.,Ltd. Bright Ears &middot; Saving Number: 253-1-43635-5 &middot; Swift Code: AYUDTHBK</p>
  </section>

  {sec("Weather", "In the event of adverse weather conditions affecting an outdoor portion of the programme, the Venue may relocate or adjust the performance by giving reasonable notice. Any cancellation of the engagement by the Venue on or after 31 December 2026 does not relieve the Venue of the agreed fee.")}
  {sec("Force Majeure", "Neither party shall be liable for any failure or delay in performing their obligations under this Agreement due to causes beyond their reasonable control, including but not limited to acts of God, natural disasters, pandemics, government actions or orders, civil unrest, strikes, or other events that could not have been reasonably anticipated or prevented. The affected party shall notify the other party as soon as practicable of such event and its expected duration.")}
  {sec("Cancellation", "Should the Venue cancel this engagement, written notice of at least fourteen (14) days before 31 December 2026 is required. Cancellation with less than 14 days&rsquo; notice may be subject to the full agreed fee, given the Agency&rsquo;s reservation of the DJs for this date.")}
  {sec("Duty Meal", "Each Entertainer is entitled to 3 selected non-alcoholic drinks on the working day, 1 glass per hour (maximum 3 glasses per day).")}
  {sec("Uniform", "The Entertainer may wear proper private attire matching the Venue&rsquo;s concept.")}
  {sec("Social Security &amp; Insurance", "The Entertainer will bear the cost of social security contributions and related formalities, as well as personal insurance.")}
  {sec("Emergency Absence / Leave", "In the event that any Entertainer is unable to perform according to the agreed arrangement, the Agency will provide a suitable replacement.")}
  {sec("Media and Recording Rights", "The Venue may photograph or video record the Entertainer&rsquo;s performance for internal documentation and promotional purposes on the Venue&rsquo;s official channels. Any commercial use of such recordings beyond standard promotional activities requires prior written consent from the Agency. The Entertainer retains all rights to their original music productions and mixes.")}
  {sec("Indemnification", "Each party agrees to indemnify, defend, and hold harmless the other party from any claims, damages, losses, or expenses (including reasonable legal fees) arising from their own negligence, willful misconduct, or breach of this Agreement.")}
  {sec("Dispute Resolution and Governing Law", "This Agreement shall be governed by and construed in accordance with the laws of the Kingdom of Thailand. Any disputes arising from or relating to this Agreement shall first be attempted to be resolved through good faith negotiation between the parties. If the dispute cannot be resolved within 30 days of written notice, either party may pursue resolution through the courts of Thailand having jurisdiction.")}
  {sec("General Agreement",
      "The Entertainer is an independent contractor and is not the employee of the Venue.",
      "The Entertainer should adhere to the house code of conduct.",
      "Matters not addressed in this Agreement shall be resolved through mutual discussion and agreement between both parties in good faith.")}

  <div class="sig">
    <p class="pre">I have read and agreed on the above terms and conditions of the agreement and undersigned for reference.</p>
    <div class="sigtable">
      <div class="sigcol"><div class="co">Bright Ears Co., Ltd.</div>
        <div class="sigblk"><div class="sigline"></div><div class="signame">Kullaphat Wittayaphan</div><div class="sigrole">Director</div></div>
      </div>
      <div class="sigcol"><div class="co">TCC Hotel Collection Co., Ltd.</div>
        <div class="sigblk"><div class="sigline"></div><div class="signame">Simon Bell</div><div class="sigrole">General Manager</div></div>
        <div class="sigblk"><div class="sigline"></div><div class="signame">Dan Jamme</div><div class="sigrole">Multi Restaurants General Manager</div></div>
        <div class="sigblk"><div class="sigline"></div><div class="signame">Rajesh Dewan</div><div class="sigrole">Director of Finance</div></div>
      </div>
    </div>
  </div>
</body></html>"""

open(f"{OUT}/Bright-Ears-NYE-2026-Agreement.html","w").write(HTML)
print("built NYE contract | 4 DJs | Sub %s VAT %s Grand %s WHT %s Net %s" % (SUB,VAT,GRAND,WHT,NET))
