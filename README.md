# Boolean Paper Search & Grounded Retrieval Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Multi-Platform](https://img.shields.io/badge/Platform-Claude%20Code%20%7C%20Claude.ai%20%7C%20Antigravity%20%7C%20CLI-blue.svg)](#multi-platform-deployment)

Construct structured Boolean search queries for academic literature from problem statements or research claims, formulate dual Conjunctive Normal Form (CNF) strings, and execute grounded retrieval across academic engines with **zero hallucination**.

---

## Directory Structure

```text
boolean-paper-search/
├── SKILL.md              # Complete agent instructions, workflows, and strict anti-hallucination rules
├── README.md             # Multi-platform install guide, CLI usage, and architecture
├── scripts/
│   └── query_builder.py  # Standalone CLI Python tool for terminal / automated query generation
└── references/
    └── search_syntax.md  # Boolean operator reference matrix across Scholar, arXiv, PubMed, IEEE
```

---

## Key Capabilities

1. **Thesis / Claim Atomization**: Deconstructs research hypotheses into declarative sentences and isolates functional semantic facets (*Domain, Mechanism, Objective, Metric*).
2. **Exhaustive Lexical Expansion**: Generates comprehensive synonyms, embedding neighbors, technical abbreviations, and quoted terms without arbitrary candidate limits.
3. **Review Checkpoint (Step 2)**: Formulates both Broad (High-Recall) and Targeted (High-Precision) CNF strings `(Syn1 OR Syn2) AND (TermA OR TermB)`, printing the matrix before retrieval.
4. **Live Retrieval Execution**: Formats queries for direct execution across Google Scholar, arXiv, PubMed, IEEE Xplore, and Semantic Scholar.
5. **Zero Hallucination Invariant**: Strictly forbids inventing papers, authors, venues, or links from memory—every cited work must be verified directly from live search results.
6. **False-Positive Screening**: Prunes out-of-domain homonyms and superficial matches, categorizing results into *Core Prior Work* and *Foundational Baselines*.

---

## Multi-Platform Deployment Guide

### 1. Claude Code

Install globally across all projects or locally within a specific repository:

```bash
# Global installation (recommended)
mkdir -p ~/.claude/skills
cp -r boolean-paper-search ~/.claude/skills/

# Project-scoped installation
mkdir -p .claude/skills
cp -r boolean-paper-search .claude/skills/
```

### 2. Antigravity & Antigravity CLI

Install into your Antigravity skills directory:

```bash
# Antigravity CLI global skill location
mkdir -p ~/.gemini/antigravity-cli/skills
cp -r boolean-paper-search ~/.gemini/antigravity-cli/skills/
```

### 3. claude.ai Web Interface

Package the directory into a zip archive and upload it in **Settings > Features > Skills**:

```bash
zip -r boolean-paper-search.zip boolean-paper-search/
```

### 4. Claude API / Anthropic Skills API

Upload the bundle via the `/v1/skills` endpoint or include the folder in your container deployment bundle.

### 5. Standalone Terminal / CLI Tool

Use the included Python query builder script directly in your terminal:

```bash
python scripts/query_builder.py \
  -f "Mamba" "State Space Models" "S4" \
  -f "genomics" "DNA sequence" "nucleotide foundation model" \
  -f "long context" "linear memory"
```

Output:
```text
[Targeted Query - High Precision (CNF)]:
  (Mamba OR "State Space Models" OR S4) AND (genomics OR "DNA sequence" OR "nucleotide foundation model") AND ("long context" OR "linear memory")

[Broad Query - High Recall (Relaxed Facets)]:
  (Mamba OR State Space Models OR S4) AND (genomics OR DNA sequence OR nucleotide foundation model)
```

---

## Academic Search Engine Operator Reference

See [`references/search_syntax.md`](references/search_syntax.md) for complete details:
- **Google Scholar**: Uppercase `AND` / `OR`, quotes for phrases, 256 char limit.
- **arXiv**: Supports boolean logic and field tags (`ti:`, `abs:`, `all:`).
- **PubMed**: Strict left-to-right evaluation, requires parentheses for nested disjunctions.
- **IEEE Xplore**: Supports wildcards, phrases, and proximity operators (`NEAR/5`).

---

## License

MIT License. See LICENSE for details.
