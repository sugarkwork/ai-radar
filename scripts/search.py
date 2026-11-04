#!/usr/bin/env python3
"""Full-text search over the catalog body text (search.json).

query.py filters metadata; this finds words inside the entries.

**表記ゆれ対策**: この検索は部分一致しかできないので、同義語・言い換え・表記の違う
バリアントを5個以上渡すことを既定で要求する。足りない場合は検索せずにエラーを返す。
1語だけの即席検索は `--force` を付ける。

Examples:
  # 5つ以上のバリアントを渡す（推奨）
  python3 scripts/search.py "音声合成" "TTS" "voice" "読み上げ" "ボイス" --type repo
  # 1語で済ませたいとき
  python3 scripts/search.py comfyui --force
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
    ap.add_argument("--force", action="store_true",
                    help="バリアント5個未満でも検索する（精度は落ちる）")
    ap.add_argument("--min-variants", type=int, default=5)
    args = ap.parse_args()

    unique = list(dict.fromkeys(t.strip().lower() for t in args.terms if t.strip()))
    if not args.force and len(unique) < args.min_variants:
        print(f"エラー: 検索語が {len(unique)} 個しかありません（最低 {args.min_variants} 個）。")
        print("このスクリプトは部分一致しかできないため、表記ゆれ・同義語・言い換えを")
        print("自分で作って渡してください。例:")
        print('  python3 scripts/search.py "音声合成" "TTS" "voice" "読み上げ" "ボイス" --type repo')
        print("1語で強行する場合のみ --force を付けてください。")
        return 2

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
        matched = [t for t in terms if t in low]
        if not matched:
            continue
        # 一致したバリアント数・出現回数・名前一致を加点（OR検索）
        score = sum(low.count(t) for t in matched) + 10 * sum(t in name_low for t in matched)
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
