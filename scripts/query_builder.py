#!/usr/bin/env python3
"""
query_builder.py - Standalone CLI tool to construct Boolean Conjunctive Normal Form (CNF) search queries.

Usage:
  python query_builder.py -f "Mamba" "State Space Models" "S4" \
                          -f "genomics" "DNA sequence" "nucleotide foundation model" \
                          -f "long context" "linear memory"

Flags:
  -f, --facet    Specify a facet cluster. Pass one or more synonym strings.
  --broad        Generate high-recall (fewer mandatory conjuncts, relaxed terms).
  --targeted     Generate high-precision (quoted exact terms, all conjuncts).
  --syntax       Target database syntax: scholar, arxiv, pubmed, ieee (default: scholar).
"""

import argparse
import sys
from typing import List


def format_term(term: str, quote_multiword: bool = True) -> str:
    cleaned = term.strip()
    if quote_multiword and " " in cleaned and not (cleaned.startswith('"') and cleaned.endswith('"')):
        return f'"{cleaned}"'
    return cleaned


def build_cnf_query(facets: List[List[str]], syntax: str = "scholar", mode: str = "standard") -> str:
    conjuncts = []
    
    for facet in facets:
        if not facet:
            continue
        
        quote_phrases = (mode != "broad")
        formatted_terms = [format_term(t, quote_multiword=quote_phrases) for t in facet]
        
        # Format disjunction
        if len(formatted_terms) == 1:
            conjuncts.append(formatted_terms[0])
        else:
            if syntax == "pubmed":
                disjunction = " OR ".join(f"{t}" for t in formatted_terms)
            else:
                disjunction = " OR ".join(formatted_terms)
            conjuncts.append(f"({disjunction})")
            
    if syntax == "arxiv":
        # arXiv query format: all:term AND all:term
        pass

    return " AND ".join(conjuncts)


def main():
    parser = argparse.ArgumentParser(
        description="Build Boolean CNF search strings for academic search engines from facet clusters."
    )
    parser.add_argument(
        "-f",
        "--facet",
        action="append",
        nargs="+",
        metavar="SYNONYM",
        help="A facet group with one or more synonyms/terms.",
        required=True,
    )
    parser.add_argument(
        "--syntax",
        choices=["scholar", "arxiv", "pubmed", "ieee"],
        default="scholar",
        help="Target academic database syntax formatting (default: scholar).",
    )
    parser.add_argument(
        "--mode",
        choices=["standard", "broad", "targeted", "both"],
        default="both",
        help="Query generation mode: standard, broad (high recall), targeted (high precision), or both (default: both).",
    )

    args = parser.parse_args()

    print("\n" + "=" * 60)
    print("  Boolean CNF Academic Query Builder")
    print("=" * 60)
    print(f"Target Database Syntax: {args.syntax.upper()}")
    print("-" * 60)

    for i, facet in enumerate(args.facet, start=1):
        print(f"  Facet {i}: {', '.join(facet)}")
    print("-" * 60)

    if args.mode in ["targeted", "both"]:
        targeted_query = build_cnf_query(args.facet, syntax=args.syntax, mode="targeted")
        print("\n[Targeted Query - High Precision (CNF)]:")
        print(f"  {targeted_query}")

    if args.mode in ["broad", "both"]:
        # Broad uses top 2 facets or unquoted terms
        broad_facets = args.facet[:2] if len(args.facet) > 2 else args.facet
        broad_query = build_cnf_query(broad_facets, syntax=args.syntax, mode="broad")
        print("\n[Broad Query - High Recall (Relaxed Facets)]:")
        print(f"  {broad_query}")

    if args.mode == "standard":
        std_query = build_cnf_query(args.facet, syntax=args.syntax, mode="standard")
        print("\n[Standard Query]:")
        print(f"  {std_query}")

    print("\n" + "=" * 60 + "\n")


if __name__ == "__main__":
    main()
