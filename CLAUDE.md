# Bright Ears DJ Management - Nobu & Le Du Kaan

## Project Overview

Bright Ears Co., Ltd. manages DJ entertainment at two high-end Bangkok venues owned by TCC Hotel Collection Co., Ltd.

**Contract Period:** February 1, 2026 - July 31, 2026

---

## Venues & Schedule

| Venue | Hours | DJs per Night | Total Hours |
|-------|-------|---------------|-------------|
| NOBU | 20:00-24:00 | 1 | 4 hours |
| Le Du Kaan | 18:00-24:00 | 2 | 6 hours (3+3) |

**Total daily performance:** 10 hours

### NOBU Brunch (1st Sunday of Every Month)
Starting March 2026, the 1st Sunday of each month moves the NOBU evening performance to Brunch:
- **Time:** 11:30-15:30 (4 hours)
- **DJ:** Same Sunday DJ (performs at brunch instead of evening — no evening set that night)
- **Sir i Sax (Bongo):** Plays alongside the DJ for 3 hours
- **Billing:** DJ at regular rates (4 hrs × THB 1,000). Bongo player invoiced as extra line: THB 6,315.79 + 7% VAT.
- **First date:** March 1, 2026

### Le Du Kaan Timeslots
- **Early (18:00-21:00):** 1 DJ, 3 hours
- **Late (21:00-24:00):** 1 DJ, 3 hours

---

## Music Guidelines

### NOBU (Manager: Leila)
- **Style:** Afro House, Organic House, trendy house genres
- **Vibe:** Cool, sophisticated, elegant
- **DJ Aesthetic:** Elegant, fashionable, good-looking

### Le Du Kaan (Manager: Terry)

**Early Slot (18:00-21:00):**
- House with Indie Dance
- Pop remixes
- More fun, upbeat energy

**Late Slot (21:00-24:00):**
- Cool, trendy international pop
- Flexible/adaptable to guest profiles
- **IMPORTANT: NO Afro House** (per Terry's explicit instruction)
- Note: DJs can play K-pop/Thai pop if needed, but primary direction is international pop

**DJ Aesthetic:** Fashionable with slightly indie vibe

---

## Key Contacts

| Name | Role | Venue |
|------|------|-------|
| **Dan Jamme** | Multi Restaurants GM | Main contact (both venues) |
| **Leila** | Manager | NOBU |
| **Terry** | Manager | Le Du Kaan |
| **Simon Bell** | General Manager | TCC Hotel Collection |
| **Rajesh Dewan** | Director of Finance | TCC Hotel Collection |

---

## Payment Structure

### Bright Ears Invoices to TCC
| Item | Amount |
|------|--------|
| Base rate | THB 11,500/day |
| + VAT (7%) | THB 805 |
| - WHT (3%) | THB 345 |
| **Net per day** | **THB 11,960** |

### Bright Ears Pays DJs
- **Rate:** THB 1,000/hour
- **Deduction:** 5% withholding tax

### DJ Earnings per Shift
| Slot | Hours | Gross | WHT 5% | Net |
|------|-------|-------|--------|-----|
| NOBU | 4 hrs | 4,000 | 200 | 3,800 |
| Le Du Kaan (each) | 3 hrs | 3,000 | 150 | 2,850 |

### Bongo Player (NOBU Brunch — 1st Sunday/month, starting March 2026)
| Item | Amount |
|------|--------|
| We charge NOBU | THB 6,315.79 + 7% VAT = THB 6,757.89 |
| We pay Sir i Sax | THB 2,000/hr × 3 hrs = THB 6,000 gross |
| WHT 5% deduction | THB 300 |
| Net to Sir i Sax | THB 5,700 |

*Added as extra line item on NOBU monthly invoice. DJ still performs 4 hrs at regular rate.*

### Monthly Invoice Timeline
- **Submit invoice:** By 30th of each month
- **Payment received:** By 25th of following month

---

## Operational Rules

- **Schedule changes:** 48 hours advance notice required
- **Weather cancellation:** 3 hours notice, no charge
- **Termination:** 30 days written notice by either party
- **Equipment:** Provided by venue
- **Dress code:** Private attire matching venue concept
- **Benefits:** 3 non-alcoholic drinks per DJ per day

---

## File Organization

```
NOBU/
├── CLAUDE.md                # This file - project knowledge
├── contracts/               # Signed agreements
├── djs/
│   ├── profiles/           # Individual DJ profile docs (markdown)
│   └── images/             # DJ photos (promotional use)
├── schedules/
│   └── 2026-02/            # Monthly schedule folders
├── presentations/           # Venue presentations
├── payments/
│   ├── scripts/
│   │   ├── generate_invoice.py   # Invoice generator (--venue nobu|ldk)
│   │   └── fill_wht_form.py      # WHT form filler (pypdf)
│   ├── templates/
│   │   ├── invoice-template.html # Invoice HTML/CSS template
│   │   └── wht-{dj}.pdf         # 7 DJ WHT templates (+ more to add)
│   ├── invoice_config.json       # Tracks invoice numbers (starts #3701)
│   └── {YYYY-MM}/               # Monthly output folders
├── branding/                # Bright Ears logo & brand guide
└── .claude/
    ├── commands/            # Slash commands (user-invoked)
    └── agents/              # Subagents (auto-delegated)
```

---

## Available Subagents

Claude will automatically delegate to these based on task context:

| Subagent | Model | Triggers On |
|----------|-------|-------------|
| `dj-profiler` | Sonnet | Processing DJ info, creating profiles |
| `schedule-builder` | Opus | Creating/managing monthly schedules |
| `presentation-builder` | Opus | Building DJ presentations for venues |
| `payment-calculator` | Sonnet | Calculating payments, generating summaries |

---

## Available Slash Commands

| Command | Purpose |
|---------|---------|
| `/add-dj [name]` | Quick DJ profile creation |
| `/list-djs` | Show roster grouped by venue |
| `/build-presentation` | Generate DJ presentation |
| `/schedule [month]` | View/create schedules |
| `/calculate-pay [month]` | Calculate DJ payments |
| `/project-status` | Quick status overview |

---

## DJ Profile Template

When adding a new DJ, create a markdown file in `djs/profiles/` with:
- Stage name / Real name
- Photo filename (stored in `djs/images/`)
- Music genres/specialties
- Suitable venues (NOBU / Le Du Kaan Early / Le Du Kaan Late)
- Brief bio
- Contact info
- Availability notes

---

## Bright Ears Branding

**Website:** https://brightears.io

### Logo
- **Primary:** `branding/BE_Logo_Transparent.png` - High-res with "BRIGHTEARS" text, transparent background (use this for presentations)
- **Icon only:** `branding/BE_Logo_White.jpg` - Circle mark only, for small uses
- **Style:** Circular "BE" monogram with cyan ring, white text on transparent/dark

### Color Palette

| Color | Hex | Usage |
|-------|-----|-------|
| Brand Cyan | `#00bbe4` | Primary accent, highlights |
| Deep Teal | `#2f6364` | Secondary accent, headers |
| Soft Lavender | `#d59ec9` | Tertiary (use sparingly) |
| Earthy Brown | `#a47764` | Warm accent |
| Luxury Black | `#0a0a0a` | Dark backgrounds |
| Off-White | `#f7f7f7` | Light backgrounds |
| Dark Gray | `#333333` | Body text |

### Typography
- **Headlines:** Playfair (elegant serif)
- **Body:** Inter (modern sans-serif)

### Visual Style
- Modern luxury aesthetic
- Glassmorphism (backdrop blur, translucent cards)
- Gradient overlays (cyan → teal → lavender)
- Soft shadows, rounded corners
- High contrast light/dark sections

---

## Common Mistakes to Avoid

- Do NOT book Afro House DJs for Le Du Kaan late slot
- Do NOT schedule changes without 48 hours notice
- Do NOT miss invoice deadline (30th of month)
- Do NOT forget to match DJ aesthetic to venue (elegant for NOBU, indie for Le Du Kaan)

---

## Current Status

- **Contract signed:** January 2026
- **Start date:** February 1, 2026
- **Today:** February 16, 2026

### Current Task: Presentations Complete
- **DJ Roster Presentation:** Complete (15 DJs) → `presentations/dj-roster-presentation.pdf`
- **February Schedule:** Final → `presentations/february-2026-schedule.pdf` (3 pages)
- **DJ Profiles for Clients:** Complete (12 DJs) → `presentations/dj-profiles-for-clients.pdf` (8 pages)
- **Sales Team Rates:** Complete → `presentations/sales-team-rates.pdf`
- **Status:** All presentations ready. February schedule live.
- **Next:** Continue with brightears.io website enhancements

### Key February Changes (Post-Launch)
- **Tom FKG:** Left roster after Feb 1 (played only that day)
- **Eskay expanded:** Now plays Sat Late + Sun Early + Tue Early (Feb 10, 17)
- **DJ Enjoy:** Covers Tue Early on Feb 3 and Feb 24

### Current DJ Roster (18 DJs + 1 Musician)

| DJ | Primary Venue | Style |
|---|---|---|
| RabbitDisco | NOBU | Nu Disco/Indie Dance |
| Benji | NOBU only (removed from LDK Mar 13) | Afro/Organic House |
| Izaar | NOBU | Deep/Soulful House |
| Manymaur | LDK Late | House/Tech House/Afro House |
| UFO | NOBU (Sun only) | Afro/Organic House |
| DJ Mint | NOBU | Nu Disco/Tech House/Afro House (hotel circuit) |
| DJ Enjoy | Le Du Kaan Early (sub) | House, uplifting energy (10+ yrs) |
| Mizuyo | Le Du Kaan Early (inactive) | Funk/Disco/Latin/World Fusion (25+ yrs, Japanese) |
| DJ Furry | Le Du Kaan Early | House/Commercial/Open Format (clubs + bars) |
| Linze | NOBU | International Pop/Open Format/Dance |
| DJ Pound | On bench (was LDK Late+Early) | Open Format/Pop Charts/R&B/Hip Hop (20 yrs) |
| Scotty B | Le Du Kaan Late | Open Format/Nu Disco (Tue + Fri + Sat Late, 30+ yrs) |
| Yui Truluv | Le Du Kaan Late + Early | Open Format/Commercial/R&B/Hip Hop (10+ yrs) |
| Eskay | LDK Early | Hip Hop/R&B/Afro House/Open Format (Tue E + Wed E + Sat E) |
| Vita | NOBU | Open Format/Pop/K-Pop/R&B (weekend availability) |
| Joyyly | Le Du Kaan Early + Late | House/Commercial House/Nu Disco (Mon L + Thu L + Sun E) |
| Lupø | Le Du Kaan Early | Nu Disco/Indie Dance/House/Organic House (Mon E from Mar 16) |
| Zara Gift | Le Du Kaan Early | House/Progressive/Top 40 (Mon E Mar 23) |
| T-Gecko | NOBU | Organic/Deep/Afro/Tech/Melodic House (Sun 8, 22 only) |
| **Sir i Sax** | **NOBU Brunch** | **Saxophone/Bongo/Flute — 1st Sunday of month (musician, not DJ)** |

**Venue Coverage (March):**
- NOBU: 8 DJs (added T-Gecko for Sun 8, 22)
- Le Du Kaan Early: 4 DJs (Lupø, Eskay, Furry, Joyyly) + DJ Enjoy sub
- Le Du Kaan Late: 4 DJs (Joyyly, Scotty B, Manymaur, Yui)
- Total: 18 DJs in roster (some work multiple venues, some inactive)

---

## DJ Availability Summary

### By Day of Week (Available DJs)

| Day | NOBU (20:00-24:00) | LDK Early (18:00-21:00) | LDK Late (21:00-24:00) |
|-----|-------------------|------------------------|----------------------|
| **Mon** | RabbitDisco, Benji, UFO | Benji, DJ Enjoy, Furry | Linze (flex), Pound, Yui |
| **Tue** | Benji, Izaar | DJ Enjoy, Linze, Eskay, Furry | Scotty B, Yui |
| **Wed** | Izaar, Manymaur, UFO, Mint | DJ Enjoy, Furry, Mizuyo* | Manymaur |
| **Thu** | Izaar, Linze, Mint | Furry | Scotty B, Yui |
| **Fri** | Mint | Pound | UFO |
| **Sat** | Vita | Yui, Mizuyo* | Eskay |
| **Sun** | UFO, Mint | Eskay, Mizuyo* | Yui |

### Individual DJ Availability

| DJ | Venue | Mon | Tue | Wed | Thu | Fri | Sat | Sun | Notes |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| **Benji** | NOBU | ✓ | ✓ | - | - | early | - | - | 20:00-24:00; Fri only 18:00-21:00 |
| **Izaar** | NOBU | - | ✓ | ✓ | ✓ | - | - | - | All evening |
| **Manymaur** | NOBU | - | - | ✓ | - | - | - | - | Wednesday only |
| **UFO** | NOBU | ✓ | - | ✓ | - | ✓ | - | ✓ | Fri 21:00-24:00 only; Feb 1 & 14 N/A |
| **DJ Mint** | NOBU | - | - | ✓ | ✓ | ✓ | - | ✓ | All evening |
| **RabbitDisco** | NOBU | ✓ | - | - | - | - | - | - | Monday only |
| **Eskay** | LDK Late/Early | - | ✓ | - | - | - | ✓ | ✓ | Sat Late + Sun/Tue Early |
| **DJ Enjoy** | LDK Early | ✓ | ✓ | ✓ | - | - | - | - | All evening |
| **Mizuyo** | LDK Early | * | * | * | - | - | * | * | Feb specific dates only |
| **DJ Furry** | LDK Early | ✓ | ✓ | ✓ | ✓ | - | - | - | 18:00-21:00 only |
| **Linze** | LDK Late | late | ✓ | - | ✓ | - | - | - | Mon 21:00-24:00; Tue/Thu 18:00-21:00 |
| **DJ Pound** | LDK Late | ✓ | - | - | - | ✓ | - | - | Mon, Fri only |
| **Scotty B** | LDK Late | - | - | - | ✓ | - | ✓ | - | Thu, Sat only |
| **Yui Truluv** | LDK Late | ✓ | ✓ | - | ✓ | - | - | ✓ | Anytime |
| **Vita** | NOBU/LDK | - | - | - | - | ? | ✓ | - | Sat NOBU confirmed; Fri TBC |

### Mizuyo February 2026 Specific Dates
Available (full evening): Feb 10 (Mon), 11 (Tue), 12 (Wed), 15 (Sat), 16 (Sun), 17 (Mon), 23 (Sun), 24 (Mon), 25 (Tue), 26 (Wed)

### UFO February 2026 Exceptions
NOT available: Feb 14 (Sun - Valentine's Day)

---

## February 2026 Final Schedule

### Weekly Assignments (FINAL)

| Day | NOBU (20:00-24:00) | LDK Early (18:00-21:00) | LDK Late (21:00-24:00) |
|-----|-------------------|------------------------|----------------------|
| **Mon** | RabbitDisco | Benji | DJ Pound |
| **Tue** | Benji | Enjoy/Eskay | Scotty B |
| **Wed** | Izaar | DJ Enjoy | Manymaur |
| **Thu** | Linze | DJ Furry | Yui Truluv |
| **Fri** | DJ Mint | DJ Pound | UFO |
| **Sat** | Vita | Yui Truluv | Eskay |
| **Sun** | UFO | Eskay | Yui Truluv |

### Special Dates / Exceptions
- **Feb 2 (Mon):** Yui Truluv at LDK Early (Benji unavailable, DJ Furry sick)
- **Tuesdays LDK Early:** DJ Enjoy (Feb 3, 24), Eskay (Feb 10, 17)
- **Feb 11 (Wed):** Mizuyo at LDK Early (instead of DJ Enjoy)
- **Feb 14 (Sat):** Valentine's Day - Mizuyo at LDK Early (instead of Yui)
- **Feb 17 (Tue):** Yui Truluv at LDK Late (Scotty B away)
- **Feb 18 (Wed):** DJ Furry at LDK Early (instead of DJ Enjoy)
- **Feb 25 (Wed):** DJ Furry at LDK Early (instead of Mizuyo/DJ Enjoy)

*Note: Scotty B away Feb 14-21. Tom FKG left roster after Feb 1.*

### Schedule Files
- `schedules/2026-02/february-schedule.md` - Full calendar details with shift counts
- `presentations/february-2026-schedule.html` - Source HTML (3-page compact design)
- `presentations/february-2026-schedule.pdf` - For venue managers (3 pages)

---

## March 2026 Schedule (DRAFT)

### Weekly Assignments

| Day | NOBU (20:00-24:00) | LDK Early (18:00-21:00) | LDK Late (21:00-24:00) |
|-----|-------------------|------------------------|----------------------|
| **Mon** | RabbitDisco | Lupø | Joyyly |
| **Tue** | Benji | Eskay | Scotty B |
| **Wed** | Izaar | Eskay | Manymaur |
| **Thu** | Linze | DJ Furry | Joyyly |
| **Fri** | DJ Mint | DJ Furry | Scotty B |
| **Sat** | Vita | Eskay | Scotty B |
| **Sun** | UFO | Joyyly | Yui Truluv |

### Key Changes from February
- **Joyyly (NEW):** Mon Late + Thu Late + Sun Early (14 shifts) - LDK manager's pick
- **Lupø (NEW from Mar 16):** Mon Early (3 shifts) - replaces Benji at LDK
- **Benji removed from LDK (Mar 13):** LDK manager unhappy. Stays at NOBU Tue only. Played LDK Mon Early on Mar 2, 9.
- **Eskay:** Tue Early + Wed Early + Sat Early (12 shifts) - expanded early role
- **Scotty B:** Tue Late + Fri Late + Sat Late (13 shifts) - expanded from Feb
- **DJ Furry:** Thu + Fri Early (8 shifts) - expanded from Feb
- **UFO:** Off LDK schedule (Fri L → Scotty B). NOBU Sun only.
- **Yui Truluv:** Sun Late only (Sat E → Eskay). 5 shifts.
- **DJ Pound:** Off LDK schedule (slots absorbed by Joyyly + Furry)
- **DJ Enjoy:** Off regular rotation (sub only)
- **Mizuyo:** Not playing in March
- **NOBU:** No changes from February

### Exceptions / Special Events
- **Mar 1 (Sun):** NOBU Brunch — UFO (11:30-15:30) + Sir i Sax (Bongo, 3 hrs). No evening set.
- **Mar 2, 9 (Mon):** Benji at LDK Early (last shifts before removal)
- **Mar 4 (Wed):** DJ Enjoy at LDK Early (Eskay unavailable)
- **Mar 8, 22 (Sun):** T-Gecko at NOBU (instead of UFO)
- **Mar 16, 30 (Mon):** Lupø at LDK Early (replaces Benji)
- **Mar 23 (Mon):** Zara Gift at LDK Early (replaces Lupø)

### Schedule Files
- `schedules/2026-03/march-schedule.md` - Full calendar details with shift counts
- `presentations/march-2026-schedule.html` - Source HTML (3-page compact design)
- `presentations/march-2026-schedule.pdf` - For venue managers (3 pages)

---

### Pending Items
- [ ] Get venue approval from Dan for schedule + DJ roster
- [ ] Add WHT templates for remaining DJs: rabbitdisco, mint, vita, enjoy, furry, yui, eskay, mizuyo, joyyly, tgecko, sirisax, lupo
- [x] ~~Generate first invoice (#3701) for February 2026~~ Split into 2 invoices (see below)
- [ ] Website enhancements (brightears.io):
  - [ ] Create `/apply` page on brightears.io
  - [ ] Add i18n translations for DJ CTA section
  - [ ] Build venue portal (see Next Project section below)

### Completed
- [x] Project folder structure created
- [x] Contract copied to project
- [x] CLAUDE.md created with project knowledge
- [x] DJ profile template created
- [x] Subagents configured (4)
- [x] Slash commands created (6)
- [x] 14 DJ profiles created with photos
- [x] Bright Ears branding assets saved (logo, colors, brand guide)
- [x] **DJ Presentation built** → `presentations/dj-roster-presentation.pdf`
- [x] GAMMA API integrated (key in `.env`, but not needed - we generate PDFs directly via HTML+Chrome)
- [x] Transparent logo created: `branding/BE_Logo_Transparent.png` (use this for presentations)
- [x] DJ Enjoy photo updated (action shot behind decks)
- [x] Mizuyo added (Japanese DJ, 25+ yrs, Funk/Disco/Latin/World - Le Du Kaan Early)
- [x] Yui Truluv added (10+ yrs, Open Format/Commercial/R&B - Le Du Kaan Late)
- [x] **All DJ availability recorded** (Jan 21, 2026)
- [x] Slowlygreen removed from database (pending proper details)
- [x] **Vita added** (LDK Late/NOBU, Sat confirmed, SO/ Bangkok resident)
- [x] **DJ Furry added** (LDK Early, Mon-Thu 18:00-21:00, club + bar versatile)
- [x] **DJ Mint Friday availability** added - covers Friday NOBU slot
- [x] **February 2026 schedule finalized** (Jan 25, 2026)
- [x] **Presentation updated** with correct venue assignments
- [x] **February schedule PDF created** for venue managers
- [x] **Manymaur & UFO profiles updated** - can play Commercial for LDK Late
- [x] **February schedule PDF redesigned** (Jan 25) - compact 3-page layout with calendar grid + DJ photos
- [x] **Mizuyo schedule adjusted** - 2 shifts (Feb 11, 14); Feb 15 reverted to Eskay, Feb 25 to DJ Furry
- [x] **DJ Application CTA added** to brightears.io landing page (pending /apply page)
- [x] **Missing DJ images recovered** from iCloud Trash (benji, mint, mizuyo, pound)
- [x] **Fixed HTML bugs** - enjoy-photo1→photo2, Scotty B duplicate slide removed
- [x] **UFO available Feb 1** - schedule simplified (no exception needed)
- [x] **Monday LDK Late changed** from Yui to DJ Pound (Yui now Tue+Sun only)
- [x] **February schedule PDF finalized** (Jan 25) - ready for venue approval
- [x] **RabbitDisco moved to NOBU** Monday (was LDK Early)
- [x] **Benji moved to LDK Early** Monday (was NOBU)
- [x] **Justin Mills removed** - unavailable for February
- [x] **Yui Truluv added to LDK Early** Saturday (exc Feb 14)
- [x] **Scotty B moved to Tuesday** LDK Late (was Saturday)
- [x] **Eskay added** (Jan 30) - LDK Late Saturday, Hip Hop/R&B/Open Format (15+ yrs, French)
- [x] **Mizuyo Feb 14** added - covers LDK Early on Valentine's Day
- [x] **Tom FKG** left roster completely after Feb 1 - Eskay/Enjoy now cover his slots
- [x] **DJ Profiles for Clients** created (Feb 2) - 8-page client-facing presentation for NOBU to share with private event clients
- [x] **Sales Team Rates** document created (Feb 2) - internal reference with rates, lead times, booking process
- [x] **DJ Profiles image fix** (Feb 3) - top-anchored photos to preserve faces; UFO/Benji/Eskay use center positioning
- [x] **Schedule mid-month update** (Feb 16) - Feb 15: Eskay stays at LDK Early (Mizuyo out); Feb 25: DJ Furry replaces Mizuyo at LDK Early. Mizuyo down to 2 shifts (Feb 11, 14).
- [x] **Payment infrastructure set up** (Feb 25) - Invoice generator, WHT form filler, invoice template adapted from CRU. 7 shared WHT templates copied (manymaur, izaar, benji, scotty, pound, ufo, linze). Invoice sequence starts at #3701.
- [x] **Split invoices per venue** (Feb 25) - Finance requested separate NOBU + LDK invoices. Script updated with `--venue nobu|ldk` flag. Rate split: NOBU ฿4,600/day (4hrs), LDK ฿6,900/day (6hrs).
- [x] **February 2026 invoices generated** (Feb 25):
  - #3701 NOBU: ฿133,400 sub total (28 days + 57 Event Terrace extra DJ Feb 27), net ฿138,736
  - #3702 LDK: ฿192,050 sub total (28 days - 1hr late arrival credit Feb 18), net ฿199,732
- [x] **DJ Joyyly added** (Feb 25) - House/Commercial/Nu Disco DJ, 10+ yrs. LDK only (NOBU declined). Mon Late + Thu Late + Sun Early.
- [x] **March 2026 schedule created** (Feb 25) - Major LDK reshuffle: Joyyly 14 shifts, Scotty B 13 (Tue+Fri+Sat L), Eskay 12 (Tue+Wed+Sat E), Furry 8. DJ Pound, DJ Enjoy, UFO off LDK. Mizuyo inactive.
- [x] **DJ T-Gecko added** (Feb 26) - Organic/Deep/Afro House, Half Moon Festival organizer. NOBU Sun Mar 8 + 22 (2 shifts, covering UFO).
- [x] **NOBU Brunch + Sir i Sax added** (Feb 26) - 1st Sunday of each month: NOBU evening → Brunch (11:30-15:30). Sir i Sax (Bongo/Sax/Flute) performs 3 hrs alongside DJ. Extra invoice line: THB 6,315.79 + VAT. First date: Mar 1.
- [x] **DJ Lupø added** (Mar 13) - Nu Disco/Indie Dance/House/Organic House. Italian-German, Berlin underground roots, multiple Bangkok residencies. LDK Early Monday from Mar 16.
- [x] **Benji removed from LDK** (Mar 13) - LDK manager unhappy with performance. Off LDK from Mar 13 onward, stays at NOBU Tue. Lupø replaces at LDK Early Monday.

### Presentation Status (Feb 2, 2026)

**Files:**
- `presentations/dj-roster-presentation.pdf` - DJ Introduction for Dan (internal)
- `presentations/february-2026-schedule.pdf` - Monthly schedule for venue managers
- `presentations/dj-profiles-for-clients.pdf` - **NEW** Client-facing DJ profiles (for NOBU to share with private event clients)
- `presentations/sales-team-rates.html/.pdf` - **NEW** Internal sales team reference (rates + booking process)

**DJ Profiles for Clients (Feb 3, 2026 — schedule PDF updated Feb 16):**
- 8 pages, 2 DJs per page (luxury spread layout)
- **Client-focused content** - written for non-DJ-savvy people booking events
- Event-type tags instead of genre jargon (Weddings, Corporate, Birthdays, etc.)
- Bios explain which events each DJ is best suited for
- No direct contact CTA - "Speak with your NOBU representative to book"
- 12 DJs: Manymaur, Izaar, UFO, Benji, Scotty B, DJ Mint, RabbitDisco, Vita, Mizuyo, Eskay, Yui Truluv, Linze
- **Image positioning:** Top-anchored (faces preserved) for most DJs; UFO, Benji & Eskay use center positioning

**Sales Team Rates Document:**
- Private event rates: THB 6,000-12,000 + 7% VAT (3-6 hours)
- Lead time guidance, booking process, what's included
- Internal use only - not for clients

**Current lineup (15 DJs):**
- NOBU (7): RabbitDisco, Benji, Izaar, Linze, DJ Mint, Vita, UFO
- Le Du Kaan Early (5): Benji, DJ Enjoy, Mizuyo, DJ Furry, Yui Truluv
- Le Du Kaan Late (6): Eskay, Scotty B, DJ Pound, Yui Truluv, Manymaur, UFO

*Note: Some DJs work multiple venues. Eskay covers Sat Late + Sun/Tue Early. Tom FKG left after Feb 1.*

**February Schedule PDF:**
- 3 pages total
- Page 1: Cover + Weekly Overview table
- Page 2: Full month calendar grid (28 days)
- Page 3: DJ photos grouped by venue

### Technical Notes
- Presentations generated via HTML → Chrome headless → PDF
- To regenerate roster: `cd presentations && "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu --print-to-pdf="dj-roster-presentation.pdf" --no-margins --print-to-pdf-no-header "file://$(pwd)/dj-roster-presentation.html"`
- To regenerate schedule: same command with `february-2026-schedule.html`

### Invoice Auto-Generation

**Setup:** Feb 25, 2026 (adapted from CRU sister project)
**IMPORTANT:** Finance requires **2 separate invoices per month** (1 NOBU + 1 Le Du Kaan)

**Usage:**
```bash
cd payments && source ../.venv/bin/activate

# Always generate 2 invoices (--venue is required):
python3 scripts/generate_invoice.py 2026-03 --venue nobu              # NOBU invoice
python3 scripts/generate_invoice.py 2026-03 --venue ldk               # Le Du Kaan invoice
python3 scripts/generate_invoice.py 2026-03 --venue nobu --dry-run    # preview only

# Adjustment flags:
#   --no-day 15              full day cancellation
#   --credit "18:1:Reason"   partial hour deduction (DJ late etc.)
#   --add "27:4:19:00-23:00:Description"   extra charge (additional DJ etc.)
```

**Venue rate split** (THB 11,500/day total, split by hours):
- NOBU: 4 hrs → THB 4,600/day (20:00-24:00)
- Le Du Kaan: 6 hrs → THB 6,900/day (18:00-24:00, 2 DJs)
- Hourly rate: THB 1,150/hr (for credits/additions)

**Invoice sequence:** #3701+ (separate from CRU #3176+), 2 numbers per month
**Customer:** TCC Hotel Collection Co., Ltd. (Branch 00015)
**Customer address:** 1 Empire Tower G, 53, 56, 57, 58 Floor, South-Sathorn Road, Yannawa, Sathorn, Bangkok 10120
**Customer Tax ID:** 0105546025131

**WHT Form Templates (7 shared with CRU):**
manymaur, izaar, benji, scotty, pound, ufo, linze

**WHT templates still needed:**
rabbitdisco, mint, vita, enjoy, furry, yui, eskay, mizuyo, joyyly, tgecko, sirisax, lupo

**Sister project:** CRU/Cocoa XO at `../CRU/payments/` — same template layout, different rates & customer. CRU uses 1 combined invoice (not split by venue).

---

## Next Project: Brightears.io Website Enhancements

**Plan file:** `/Users/benorbe/.claude/plans/snug-chasing-floyd.md`
**Brightears codebase:** `/Users/benorbe/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding Projects/brightears/brightears/`
**Status:** IN PROGRESS - resuming after February schedule finalized

### Feature 1: DJ Application Button - STARTED

**DONE:**
- [x] Added "Apply as DJ" CTA section to landing page (`/app/[locale]/page.tsx`)
  - Gradient section with vinyl icon
  - "Are You a DJ?" heading
  - "Apply Now" button linking to `/apply`
  - Added between Client Logos and Contact sections

**TODO:**
- [ ] Create `/apply` page (`/app/[locale]/apply/page.tsx`)
- [ ] Add i18n translations for `landing.djCta.*` keys
- [ ] Test form submission

**Existing infrastructure (no changes needed):**
- `DJApplicationForm.tsx` component already exists
- API endpoint `/api/applications/submit` ready
- `apply.*` translations already exist for form fields

### Feature 2: Venue Portal (B2B Dashboard) - NOT STARTED

**Access:** Invite-only (Bright Ears creates accounts for venue managers)
**Design:** Match brightears.io aesthetic (dark gradients, brand-cyan, glassmorphism)
**First customers:** NOBU & Le Du Kaan

**Portal Features:**
1. **Dashboard** - Overview + quick stats
2. **Schedule view** - Calendar with DJ assignments
3. **DJ directory** - Profiles with photos/bios
4. **Feedback system** - Rate DJ performance after each night
5. **Statistics dashboard** - Track trends for contract reviews (key differentiator!)

**Database changes needed:**
- Add `VenueFeedback` model to `/prisma/schema.prisma`
- Fields: ratings (overall, crowd, professionalism), what went well, improvements, would rebook
- Optional venue data: crowd level, guest mix, notes

**Data sync:** Script to sync DJ profiles from this NOBU folder to brightears DB

**Route structure:**
```
/venue-portal/
├── /dashboard      → Overview + quick stats
├── /schedule       → Calendar view
├── /djs            → DJ directory
├── /feedback       → Submit & view ratings
├── /feedback/new   → Quick feedback form
├── /stats          → Analytics dashboard
```

**Implementation Phases:**
1. Foundation: DJ app button, portal layout, data sync
2. Core: Schedule calendar, DJ directory, feedback form
3. Stats: Analytics dashboard, reports, exports
4. Polish: Mobile responsive, Thai translations

**Deferred to future:**
- AI assistant (cost concerns)
- DJ sign-off system (paper forms at venue work fine)

### Brightears Codebase Summary

**Key files for website work:**
- Landing page: `/app/[locale]/page.tsx`
- DJ form: `/components/forms/DJApplicationForm.tsx`
- API: `/app/api/applications/submit/route.ts`
- Translations: `/messages/en.json`, `/messages/th.json`
- Auth: Clerk with CORPORATE role for venues
- DB: Prisma at `/prisma/schema.prisma`

**Tech stack:** Next.js 15, Clerk auth, Prisma, Tailwind, next-intl
