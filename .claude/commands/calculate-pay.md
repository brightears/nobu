---
description: Calculate DJ payments for a period
allowed-tools: Read, Write, Glob
argument-hint: [month]
context: fork
model: claude-3-5-haiku-20241022
---

Calculate payments for: $1 (e.g., "2026-02")

## Payment Rates

**DJ Hourly Rate:** THB 1,000/hour
**Withholding Tax:** 5%

| Slot | Hours | Gross | WHT 5% | Net |
|------|-------|-------|--------|-----|
| NOBU | 4 | 4,000 | 200 | 3,800 |
| Le Du Kaan | 3 | 3,000 | 150 | 2,850 |

## Instructions

1. Read schedule from `schedules/[month]/schedule.csv`
2. Count shifts per DJ per venue
3. Calculate:
   - Total hours per DJ
   - Gross pay
   - WHT deduction
   - Net pay

## Output Format

### DJ Payment Summary - [Month]

| DJ | NOBU Shifts | LDK Shifts | Total Hours | Gross | WHT | Net |
|---|---|---|---|---|---|---|

### Bright Ears Invoice to TGC
- Days worked: X
- Rate: THB 11,960/day
- Total: THB X

Save to `payments/[month]-summary.md`
