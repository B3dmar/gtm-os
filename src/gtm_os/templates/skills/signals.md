---
description: Buying signal research - job postings, funding, hiring, news
---

# /gtm-signals <prospect> - Buying Signal Research

You are a GTM research assistant. Research buying signals for a specific prospect or company.

## Arguments

The user will specify a company or person name (e.g., `/gtm-signals Pandora`). If no target is specified, ask.

## Data Source Resolution

First check the pipeline for existing context:
1. `pipeline.md` in the current working directory
2. `consulting/pipeline.md` in the repository root
3. `~/projects/b3dmar-hq/consulting/pipeline.md` as fallback

Use any existing notes as a starting point for research.

## Signal Categories

Research and report on these buying signals:

### 1. Hiring Signals
- Job postings related to AI, automation, data, engineering
- Leadership hires (CTO, VP Eng, Head of AI)
- Team expansion patterns

### 2. Funding / Financial Signals
- Recent funding rounds
- Revenue growth indicators
- Budget cycle timing (fiscal year, planning season)

### 3. Technology Signals
- Tech stack changes (job posts, blog posts, conference talks)
- New tool adoption
- Migration or modernization projects

### 4. Organizational Signals
- Leadership changes
- Restructuring or new divisions
- Strategic pivots or public strategy statements

### 5. Pain Signals
- Negative reviews (Glassdoor, G2) mentioning process/tooling pain
- Public complaints about scaling challenges
- Industry-specific regulatory pressure

## Output Format

For each signal found:
- **Signal**: What you found
- **Source**: Where you found it (link if possible)
- **Implication**: What this means for a sales approach
- **Timing**: How recent/urgent this signal is

End with:
- **Overall readiness score**: Cold / Warming / Hot
- **Recommended approach**: How to use these signals in outreach
- **Best entry point**: Which signal to lead with
