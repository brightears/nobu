---
description: Create or view monthly DJ schedule
allowed-tools: Read, Write, Edit, Glob
argument-hint: [month] [action]
---

Work on the DJ schedule for: $1 (e.g., "2026-02")
Action: $2 (view/create/edit, default: view)

## Schedule Requirements

**Daily slots to fill:**
- NOBU 20:00-24:00 (1 DJ, 4 hours)
- Le Du Kaan 18:00-21:00 (1 DJ, 3 hours)
- Le Du Kaan 21:00-24:00 (1 DJ, 3 hours)

**Total:** 3 DJ slots per day, 7 days/week

## Rules
- Match DJ genres to venue requirements
- Check DJ availability notes in profiles
- Avoid scheduling same DJ at overlapping times
- Consider DJ preferences for specific venues
- Balance workload across DJs

## Schedule Format (CSV)
```
date,day,nobu_2000,ledukaan_1800,ledukaan_2100
2026-02-01,Sat,DJ Name,DJ Name,DJ Name
```

## File Location
`schedules/[month]/schedule.csv`
