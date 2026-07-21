#!/usr/bin/env python3
"""NOBU + LDK Entertainment Agreement — 6-month extension (Aug 1 2026 - Jan 31 2027).
Verbatim from the signed template; only the term dates + Fee (new NOBU weekday/weekend
split) change. On-brand (logo + cyan). LDK unchanged."""
import json
OUT="/home/brightears/nobu/contracts"
fonts=json.load(open("/home/brightears/BrightEars-Ops/data/brand/inter-fonts-base64.json"))
import base64
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

TERM="August 1st 2026 &ndash; January 31st 2027"

fee_box=f"""
<div class="feebox">
  <div class="fl"><div class="d">Le Du Kaan <small>&mdash; 2 DJs, 6 hours (18:00&ndash;24:00)</small></div>
    <div class="n">THB 6,900 + 483 (7% VAT) &minus; 207 (3% WHT) = <b>THB 7,176</b> / night</div></div>
  <div class="fl"><div class="d">NOBU &middot; Sunday&ndash;Thursday <small>&mdash; 1 DJ, 4 hours (20:00&ndash;24:00)</small></div>
    <div class="n">THB 4,600 + 322 (7% VAT) &minus; 138 (3% WHT) = <b>THB 4,784</b> / night</div></div>
  <div class="fl"><div class="d">NOBU &middot; Friday &amp; Saturday <small>&mdash; 2 DJs, 4 hours (20:00&ndash;24:00)</small></div>
    <div class="n">THB 10,000 + 700 (7% VAT) &minus; 300 (3% WHT) = <b>THB 10,400</b> / night</div></div>
</div>"""

HTML=f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
  <div class="hdr"><img src="data:image/png;base64,{LOGO}" alt="Bright Ears"/>
    <div><div class="wordmark">BRIGHT <span class="be">EARS</span></div>
    <div class="tagline">DJ Booking · Scheduling · Management</div></div></div>

  <h1>ENTERTAINMENT AGREEMENT</h1>
  <div class="date">July 2026</div>

  <p>This agreement is made between <span class="b">TCC Hotel Collection Co., Ltd.</span>, located at 1 Empire Tower G, 53, 56, 57, 58 Floor, South Sathorn Road, Yannawa, Sathorn, Bangkok 10120, Thailand (TEL: 024071645, TAX ID: 0105546025131, Branch 00015), hereinafter referred to as the &ldquo;Venue&rdquo; and <span class="b">Bright Ears Co., Ltd.</span>, with its Head Office at Garden Home Village, Phaholyothin Road, Amphur Kookot, Lum Luk Ka District, Pathum Thani, Thailand (TEL: 0856644142, TAX ID: 0105550096659), hereinafter referred to as the &ldquo;Agency.&rdquo;</p>

  {sec("Performance Details", f"The Venue hereby engages the Agency to provide entertainment services at Le Du Kaan &amp; NOBU. The Agency&rsquo;s entertainers agree to perform as DJs from Monday &ndash; Sunday, from {TERM}.")}

  {sec("Working Schedule", "The working schedule shall be mutually agreed upon between the Agency and the Venue. Any changes to the schedule must be communicated at least 48 hours in advance unless otherwise agreed by both parties.")}

  <section class="hours"><h2>Hours of Work</h2>
    <p>Normal working hours shall be in accordance with the Venue&rsquo;s rules and regulations for 7 nights per week from Monday to Sunday from {TERM}, as follows:</p>
    <p><span class="b">Le Du Kaan:</span> 18:00 &ndash; 24:00 (6 hours), with 2 DJs each performing 3 hours per night</p>
    <p><span class="b">NOBU:</span> 20:00 &ndash; 24:00 (4 hours), with 1 DJ Sunday to Thursday, and 2 DJs on Friday &amp; Saturday</p>
    <p>Total daily performance hours: 10 hours</p>
  </section>

  {sec("Duties and Responsibilities", "The Entertainer will ensure that particular attention is given to building up the atmosphere each night in accordance with the audience type. Music must be played in continuous mode during each set of performance. An appropriate level of energy is expected at all times.")}

  {sec("Equipment", "The Venue shall provide all necessary music equipment for the performance. The Entertainer will be responsible for taking good care of and maintaining the equipment provided by the Venue during performance hours. The Venue shall maintain appropriate insurance coverage for its own equipment.")}

  <section class="fee"><h2>Fee</h2>
    <p>The Venue agrees to pay the Agency the following nightly rates:</p>
    {fee_box}
    <p>The Agency&rsquo;s entertainers will perform seven nights per week, from Monday to Sunday, from {TERM}.</p>
    <p>Payment will be made monthly, after receiving the attendance worksheet and invoice. The invoice must be submitted to the accounting department by the 30th of each month to process the payment. The fee will be paid via direct bank transfer to the Agency&rsquo;s account by the 25th of the following month.</p>
  </section>

  <section><h2>Bank Information</h2>
    <p style="margin:2px 0">BANK OF AYUDHYA PUBLIC COMPANY LIMITED<br>Fortune Town BR, C.P. Tower II, Ratchadapisek Road, Dindaeng, Bangkok 10400, Thailand<br>Account Name: Co.,Ltd. Bright Ears &middot; Saving Number: 253-1-43635-5 &middot; Swift Code: AYUDTHBK</p>
  </section>

  {sec("Weather", "The Venue reserves the right to cancel the performance in the event of adverse weather conditions by giving notice at least 3 hours before the scheduled performance time. In case of such weather-related cancellation, no charges will apply.")}
  {sec("Force Majeure", "Neither party shall be liable for any failure or delay in performing their obligations under this Agreement due to causes beyond their reasonable control, including but not limited to acts of God, natural disasters, pandemics, government actions or orders, civil unrest, strikes, or other events that could not have been reasonably anticipated or prevented. The affected party shall notify the other party as soon as practicable of such event and its expected duration.")}
  {sec("Cancellation", "Both parties have the option to terminate this agreement by giving 30 days notice in writing.")}
  {sec("Duty Meal", "Each Entertainer is entitled to 3 selected non-alcoholic drinks on the working day, 1 glass per hour (maximum 3 glasses per day).")}
  {sec("Laundry", "Not provided by the Venue.")}
  {sec("Uniform", "The Entertainer may wear proper private attire matching the Venue&rsquo;s concept.")}
  {sec("Social Security &amp; Insurance", "The Entertainer will bear the cost of social security contributions and related formalities, as well as personal insurance.")}
  {sec("Emergency Absence / Leave", "In the event that the Entertainer is unable to perform according to the working schedule, the Agency will provide a suitable replacement.")}
  {sec("Media and Recording Rights", "The Venue may photograph or video record the Entertainer&rsquo;s performance for internal documentation and promotional purposes on the Venue&rsquo;s official channels. Any commercial use of such recordings beyond standard promotional activities requires prior written consent from the Agency. The Entertainer retains all rights to their original music productions and mixes.")}
  {sec("Indemnification", "Each party agrees to indemnify, defend, and hold harmless the other party from any claims, damages, losses, or expenses (including reasonable legal fees) arising from their own negligence, willful misconduct, or breach of this Agreement.")}
  {sec("Dispute Resolution and Governing Law", "This Agreement shall be governed by and construed in accordance with the laws of the Kingdom of Thailand. Any disputes arising from or relating to this Agreement shall first be attempted to be resolved through good faith negotiation between the parties. If the dispute cannot be resolved within 30 days of written notice, either party may pursue resolution through the courts of Thailand having jurisdiction.")}
  {sec("General Agreement",
      "The Entertainer will attend and organize rehearsals necessary to maintain entertainment trends and agrees to conform to house rules and regulations of the establishment. The Entertainer will have no monetary claim on the Venue for attending these rehearsals.",
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

open(f"{OUT}/Bright-Ears-Entertainment-Agreement-Aug2026-Jan2027.html","w").write(HTML)
print("built contract:", TERM)
