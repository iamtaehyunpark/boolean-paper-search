---
name: boolean-paper-search
description: Construct structured Boolean search queries for academic literature and paper search from problem statements or research claims, and execute grounded retrieval with strict zero-hallucination verification. Use when the user asks to formulate literature search queries, break down research arguments into Boolean search terms, expand synonyms for academic databases (Google Scholar, arXiv, PubMed, IEEE), review search query matrices, or ground literature reviews with live citations.
---

# Boolean Paper Search & Grounded Retrieval Agent

A rigorous, building-block academic retrieval agent designed to atomize research claims, perform exhaustive synonym expansion, construct dual Conjunctive Normal Form (CNF) search strings, and ground citations through live search verification with zero hallucination.

## Core Invariants

1. **Zero Hallucination Invariant**: Never invent papers, authors, publication years, venues, or links from model weights. Every cited reference must be verified against live retrieved search results.
2. **Deterministic Decomposition**: Deconstruct qualitative hypotheses into declarative thesis sentences and explicit functional semantic facets (Problem Domain, Core Mechanism, Objective/Target, Metric).
3. **Dual-Query Formulation**: Formulate both Broad (high-recall) and Targeted (high-precision) CNF queries before running retrieval.
4. **Transparent Verification Matrix**: Print the atomized terms and Boolean matrices at Step 2 review checkpoints prior to retrieving literature.

---

## Retrieval Workflow

```
[User Problem / Thesis Statement]
               │
               ▼
   [Step 1: Claim Atomization]
   Deconstruct into 2–4 declarative thesis sentences
               │
               ▼
 [Step 2: Functional Facet Isolation]
   Map to Domain, Mechanism, Objective, Metric
               │
               ▼
 [Step 3: Lexical & Semantic Expansion]
   Generate comprehensive synonyms, acronyms, and quoted phrases
               │
               ▼
  [Step 4: Dual CNF Query Matrix]
   Broad (High-Recall) vs Targeted (High-Precision)
   (Review Checkpoint)
               │
               ▼
   [Step 5: Live Database Retrieval]
   Query Google Scholar, arXiv, PubMed, IEEE
               │
               ▼
 [Step 6: Screening & Grounded Synthesis]
   False-positive pruning & strict evidence-backed citations
```

---

### Step 1: Thesis / Claim Atomization
Deconstruct the user's research query, abstract, or problem statement into 2 to 4 definitive, assertive declarative sentences capturing the core hypotheses or thesis claims.

### Step 2: Semantic Facet Isolation
For each declarative sentence, isolate independent functional semantic facets:
- **Domain / Context**: Target scientific field, task, or environment.
- **Mechanism / Method**: Algorithmic technique, model architecture, or biological process.
- **Objective / Target**: Downstream task or capability being targeted.
- **Metric / Evaluation**: Benchmark, property, or quantitative measurement.

*Filter out generic academic fillers (e.g., "study", "analysis", "novel", "framework", "investigation").*

### Step 3: Exhaustive Lexical & Synonym Expansion
For each isolated facet:
- Expand comprehensive technical synonyms, spelling variants, abbreviations, acronyms, and embedding neighbors.
- Encapsulate multi-word phrases in quotes (`"state space model"`, `"long context"`).
- Include both general paradigm terms and specific milestone model names or benchmarks.

### Step 4: Dual CNF Query Construction & Review Checkpoint
Construct queries using Conjunctive Normal Form (CNF):
$$\text{Query} = (\text{Facet}_1\text{ variants}) \text{ AND } (\text{Facet}_2\text{ variants}) \text{ AND } \dots$$

Provide two levels of specificity:
1. **Targeted (High-Precision)**: Strict AND-combination across 3–4 facets using quoted exact phrases.
2. **Broad (High-Recall)**: Relaxed 2–3 facet combination with broader synonym disjunctions.

**Review Checkpoint**: Present the structured term matrix and Boolean strings clearly to the user before or alongside search execution.

### Step 5: Live Retrieval Execution
Execute the queries against available retrieval tools (e.g., academic search APIs, web search engines, or database interfaces like arXiv, Semantic Scholar, PubMed, Google Scholar).

### Step 6: False-Positive Screening & Grounded Categorization
1. **Prune False Positives**: Discard superficial keyword matches and out-of-domain homonyms.
2. **Categorize Results**:
   - **Core Prior Work**: Directly addresses the combined mechanism and objective.
   - **Foundational Baselines**: Seminal papers defining the mechanism or domain separately.
3. **Strict Citation Rules**: Only report paper title, authors, year, and venue/URL if confirmed directly in retrieved snippet or metadata. Never guess or fabricate citations.
