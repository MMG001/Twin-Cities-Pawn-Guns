# -*- coding: utf-8 -*-
"""Integrity checker for the injected Schema.org JSON-LD.

For every page it:
  1. Extracts and JSON-parses the <script type="application/ld+json"> block.
  2. Collects all @id values DEFINED in the graph (nodes carrying @id + a @type).
  3. Walks the graph and collects all @id REFERENCES ({"@id": ...} with no @type).
  4. Asserts every reference resolves to a definition on the SAME page.
  5. Asserts the Rule 11 traps are absent:
        - no `audience` on the PawnShop/business node
        - no `about` or `inLanguage` on any Service node
        - no `inLanguage` on any EntryPoint node
        - no ContactAction type anywhere
        - no `field-input` PropertyValueSpecification outside SearchAction.query-input

Prints PASS/FAIL per file and exits non-zero if any file fails.

Run: python3 tools/check_schema.py
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import schema_config as cfg  # noqa: E402

LD_SCRIPT_RE = re.compile(
    r'<script type=["\']application/ld\+json["\']>(.*?)</script>',
    re.DOTALL | re.IGNORECASE,
)


def as_type_set(node):
    t = node.get("@type")
    if isinstance(t, list):
        return set(t)
    if isinstance(t, str):
        return {t}
    return set()


def collect_defined(obj, defined):
    """A node DEFINES an @id when it carries both @id and @type."""
    if isinstance(obj, dict):
        if "@id" in obj and "@type" in obj:
            defined.add(obj["@id"])
        for v in obj.values():
            collect_defined(v, defined)
    elif isinstance(obj, list):
        for v in obj:
            collect_defined(v, defined)


def collect_refs(obj, refs):
    """A REFERENCE is a dict {"@id": ...} with no @type (just a pointer)."""
    if isinstance(obj, dict):
        if "@id" in obj and "@type" not in obj and len(obj) == 1:
            refs.append(obj["@id"])
        for v in obj.values():
            collect_refs(v, refs)
    elif isinstance(obj, list):
        for v in obj:
            collect_refs(v, refs)


def walk_nodes(obj):
    """Yield every dict node in the graph."""
    if isinstance(obj, dict):
        yield obj
        for v in obj.values():
            yield from walk_nodes(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from walk_nodes(v)


def check_rule11(graph):
    errors = []
    for node in walk_nodes(graph):
        types = as_type_set(node)

        # ContactAction does not exist.
        if "ContactAction" in types:
            errors.append("ContactAction type used (does not exist)")

        # No `audience` on the business node.
        if "PawnShop" in types and "audience" in node:
            errors.append("`audience` present on PawnShop node")

        # No `about` / `inLanguage` on Service nodes.
        if "Service" in types:
            if "about" in node:
                errors.append("`about` present on Service %s" % node.get("@id"))
            if "inLanguage" in node:
                errors.append("`inLanguage` present on Service %s" % node.get("@id"))

        # No `inLanguage` on EntryPoint nodes.
        if "EntryPoint" in types and "inLanguage" in node:
            errors.append("`inLanguage` present on EntryPoint node")

        # No field-input PropertyValueSpecification outside SearchAction.query-input.
        if "PropertyValueSpecification" in types and "SearchAction" not in types:
            # A bare PropertyValueSpecification anywhere in these graphs is a trap.
            errors.append("PropertyValueSpecification (field-input) present outside SearchAction")

    return errors


def check_page(slug):
    path = os.path.join(ROOT, slug)
    with open(path, "r", encoding="utf-8") as fh:
        html = fh.read()

    blocks = LD_SCRIPT_RE.findall(html)
    if len(blocks) == 0:
        return False, ["no JSON-LD block found"]
    if len(blocks) > 1:
        return False, ["%d JSON-LD blocks found (expected 1)" % len(blocks)]

    try:
        data = json.loads(blocks[0])
    except json.JSONDecodeError as e:
        return False, ["JSON parse error: %s" % e]

    errors = []

    if data.get("@context") != "https://schema.org":
        errors.append("missing/incorrect @context")
    graph = data.get("@graph")
    if not isinstance(graph, list) or not graph:
        return False, ["missing or empty @graph"]

    # Referenced @ids must all be defined on the same page.
    defined = set()
    collect_defined(graph, defined)
    refs = []
    collect_refs(graph, refs)
    for ref in refs:
        if ref not in defined:
            errors.append("dangling @id reference: %s" % ref)

    # Rule 11 traps.
    errors.extend(check_rule11(graph))

    return (len(errors) == 0), errors


def main():
    all_pass = True
    for slug in cfg.PAGES:
        ok, errors = check_page(slug)
        status = "PASS" if ok else "FAIL"
        print("[%s] %s" % (status, slug))
        if not ok:
            all_pass = False
            for e in errors:
                print("        - %s" % e)
    print("-" * 48)
    print("ALL PASS" if all_pass else "SOME FILES FAILED")
    sys.exit(0 if all_pass else 1)


if __name__ == "__main__":
    main()
