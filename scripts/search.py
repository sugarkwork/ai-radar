#!/usr/bin/env python3
"""Full-text search over the catalog body text (search.json).

query.py filters metadata; this finds words inside the entries.

Examples:
  python3 scripts/search.py comfyui
  python3 scripts/search.py "音声 変換" --type repo --min-stars 1000
  python3 scripts/search.py prompt --genre prompt-design --json
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SEARCH = ROOT / "search.json"


def snippet(text: str, terms: list[str], width: int = 90) -> str:
    low = text.lower()
    pos = min((low.find(t) for t in terms if low.find(t) >= 0), default=0)
    start = max(0, pos - width // 2)
    cut = text[start:start + width].replace("\n", " ")
    return ("…" if start else "") + cut.strip() + ("…" if start + width < len(text) else "")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("terms", nargs="+")
    ap.add_argument("--type", choices=["repo", "prompt", "link", "article"])
    ap.add_argument("--genre")
    ap.add_argument("--min-stars", type=int)
    ap.add_argument("--limit", type=int, default=15)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if not SEARCH.exists():
        raise SystemExit("search.json missing — run scripts/build_index.py")

    terms = [t.lower() for t in args.terms]
    rows = json.loads(SEARCH.read_text(encoding="utf-8"))["items"]

    hits = []
    for r in rows:
        if args.type and r.get("type") != args.type:
            continue
        if args.genre and r.get("genre") != args.genre:
            continue
        if args.min_stars is not None and (r.get("stars") or 0) < args.min_stars:
            continue
        text = (r.get("text") or "")
        low = text.lower()
        name_low = (r.get("name") or "").lower()
        if not all(t in low for t in terms):
            continue
        # 名前一致を強く、出現回数を加点
        score = sum(low.count(t) for t in terms) + 10 * sum(t in name_low for t in terms)
        hits.append((score, r, snippet(text, terms)))

    hits.sort(key=lambda h: -h[0])
    hits = hits[: args.limit]

    if args.json:
        print(json.dumps([{**r, "score": s, "snippet": sn} for s, r, sn in hits],
                         ensure_ascii=False, indent=1))
        return 0

    if not hits:
        print("該当なし")
        return 0
    for score, r, sn in hits:
        mark = " ⚑" if r.get("flags") else ""
        label = r.get("name") or r.get("repo") or r.get("url")
        print(f"- **[{label}]({r['path']})**{mark} — {r.get('type')} / {r.get('genre')}"
              + (f" / ★{r['stars']:,}" if isinstance(r.get("stars"), int) else ""))
        print(f"  {sn}")
    print(f"\n{len(hits)} 件")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
