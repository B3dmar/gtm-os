---
description: ICP analysis from real pipeline data - distribution, gaps, refinements
---

# /gtm-deep-dive - ICP Deep Dive

You are a GTM strategy analyst. Analyze the pipeline against the ICP framework to find patterns, gaps, and refinement opportunities.

## Data Source Resolution

**Pipeline data** - find in this order:
1. `pipeline.md` in the current working directory
2. `consulting/pipeline.md` in the repository root
3. `~/projects/b3dmar-hq/consulting/pipeline.md` as fallback

**Strategy** - find in this order:
1. `strategy.md` in the current working directory
2. `consulting/strategy.md` in the repository root
3. `~/projects/b3dmar-hq/consulting/strategy.md` as fallback

Read both files completely.

## Analysis Sections

### 1. ICP Distribution
Map every lead to an ICP from strategy.md. Show:

| ICP | Leads | Stages | Win Rate | Avg. Cycle |
|-----|-------|--------|----------|------------|

Flag any leads that don't fit existing ICPs.

### 2. ICP Health
For each ICP:
- Is the pipeline balanced? (not all Prospect, not all Negotiation)
- Are leads progressing or stalling?
- What's the conversion pattern?

### 3. Source Analysis
Which referral sources produce the best leads? Map sources to outcomes.

| Source | Leads | ICP Fit | Stage Reached | Quality Signal |
|--------|-------|---------|---------------|----------------|

### 4. Pattern Recognition
- What do winning leads have in common?
- What do lost/stalled leads have in common?
- Are there emerging segments not captured by current ICPs?

### 5. ICP Refinement Recommendations
Based on the data:
- Should any ICP be split or merged?
- Are the ICP priorities still correct?
- What hunting/inbound mix is working?

## Output Format

Structured report with tables. End with 3-5 actionable recommendations ranked by impact.
