---
description: Build DJ roster presentation for venue approval
allowed-tools: Read, Write, Glob, Bash(ls:*)
argument-hint: [output-format]
---

Build the DJ roster presentation for Dan (venue GM).

Output format: $1 (default: markdown for GAMMA import)

## Instructions

1. Read all DJ profiles from `djs/profiles/`
2. Check for branding assets in `branding/`
3. Organize DJs by recommended venue:
   - NOBU section
   - Le Du Kaan Early section
   - Le Du Kaan Late section

## Presentation Structure

### Cover
- Title: "DJ Roster Proposal"
- Subtitle: "Le Du Kaan & NOBU"
- Bright Ears branding

### Per Venue Section
For each venue, include:
- Venue name and music direction
- DJ cards with:
  - Photo placeholder reference
  - Stage name
  - Music style
  - Brief bio (1-2 sentences)

### Summary
- Total DJs in roster
- Coverage plan (7 days/week)

## Output
Save to `presentations/dj-roster-[date].md`
