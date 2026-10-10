# Boolean Operator & Syntax Matrix Across Academic Engines

Different academic engines and search tools handle Boolean logic, quotes, and nesting with distinct nuances. Use this matrix when adapting generated CNF queries to specific retrieval platforms.

---

## Quick Reference Comparison

| Search Platform | Case-Sensitive Operators | Parenthetical Grouping `(...)` | Exact Phrase Quotes `"..."` | Wildcards `*` | Max Query Length / Limits |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Google Scholar** | YES (`AND`, `OR`, `-`) | Limited / Flat precedence | YES | NO | ~256 characters / 32 words |
| **arXiv API / Web** | YES (`AND`, `OR`, `ANDNOT`)| YES | YES | YES | Moderate length limits |
| **PubMed (MEDLINE)**| YES (`AND`, `OR`, `NOT`) | YES (Strict nesting) | YES | YES (truncated stem) | ~4,000 characters |
| **IEEE Xplore** | YES (`AND`, `OR`, `NOT`) | YES (Up to 10 wildcards) | YES | YES | Max 40 search terms |
| **Semantic Scholar**| Default AND | Partial | YES | NO | Flexible natural language / keyword |
| **ACM Digital Library**| YES (`AND`, `OR`, `NOT`)| YES | YES | YES | Standard complex nesting |

---

## Database-Specific Nuances

### 1. Google Scholar
- **Default Conjunction**: Space implies `AND`.
- **OR Operator**: Must be uppercase `OR`.
- **Exclusion**: Use hyphen prefix `-excluded_term` (no space after hyphen).
- **Phrase Matching**: Double quotes `"..."` enforce strict consecutive word matching.
- **Limitation**: Deeply nested parentheses `((A OR B) AND (C OR D))` are often flattened or silently truncated. Keep to 2–3 conjuncts.

### 2. arXiv (Advanced / API)
- **Field Prefixing**: Prefix terms with fields for precision:
  - `ti:"term"` : Title only
  - `abs:"term"` : Abstract only
  - `all:"term"` : Full text, title, abstract
- **Example**:
  ```text
  (ti:"state space model" OR abs:"state space model") AND abs:genomics
  ```

### 3. PubMed (NCBI)
- **Automatic Term Mapping (ATM)**: If quotes are omitted, PubMed applies ATM to match MeSH terms.
- **Using Quotes**: Enclosing in quotes disables ATM and enforces strict phrase matching.
- **Parentheses**: Strictly evaluates left-to-right unless grouped with parentheses. Always group OR clusters with `(...)`.
- **Example**:
  ```text
  ("state space model"[Title/Abstract] OR "Mamba"[Title/Abstract]) AND ("genomics"[Title/Abstract] OR "DNA sequence"[Title/Abstract])
  ```

### 4. IEEE Xplore
- **Search Operators**: Supports complex Boolean nesting up to 40 search terms.
- **Quotes**: Multi-word phrases must be enclosed in double quotes.
- **Proximity Operators**: Supports `NEAR` and `ONEAR` (e.g., `"Mamba" NEAR/5 "genomics"`).
- **Example**:
  ```text
  (("State Space Models" OR "Mamba") AND ("genomics" OR "DNA"))
  ```
