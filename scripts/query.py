#!/usr/bin/env python3
"""Filter the catalog. Works off index.json, so run build_index.py first.

Examples:
  python3 scripts/query.py --type repo --genre video-gen --min-stars 1000
  python3 scripts/query.py --type repo --cadence daily --updated-within 30 --sort commits
  python3 scripts/query.py --type link --pricing free
  python3 scripts/query.py --text comfyui
  python3 scripts/query.py --type repo --json --limit 5
"""
from __future__ import annotations

import argparse
import json
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.json"


def load() -> list[dict]:
    if not INDEX.exists():
        raise SystemExit("index.json missing — run scripts/build_index.py")
    return json.loads(INDEX.read_text(encoding="utf-8")).get("items", [])


def within(value: str | None, days: int) -> bool:
    if not value:
        return False
    try:
        d = date.fromisoformat(str(value)[:10])
    except ValueError:
        return False
    return d >= date.today() - timedelta(days=days)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--type", choices=["repo", "prompt", "link", "model", "article"])
    ap.add_argument("--genre")
    ap.add_argument("--min-stars", type=int)
    ap.add_argument("--min-forks", type=int)
    ap.add_argument("--cadence", choices=["daily", "weekly", "monthly", "stale"])
    ap.add_argument("--updated-within", type=int, help="上流の最終pushがN日以内")
    ap.add_argument("--fetched-within", type=int, help="メトリクス取得がN日以内")
    ap.add_argument("--license")
    ap.add_argument("--pricing", choices=["free", "freemium", "paid", "unknown"])
    ap.add_argument("--flagged", action="store_true", help="flags 付きのみ")
    ap.add_argument("--text", help="name/summary/url の部分一致")
    ap.add_argument("--sort", choices=["stars", "forks", "commits", "updated", "name"], default="stars")
    ap.add_argument("--limit", type=int, default=30)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    rows = load()
    if args.type:
        rows = [r for r in rows if r.get("type") == args.type]
    if args.genre:
        rows = [r for r in rows if r.get("genre") == args.genre]
    if args.min_stars is not None:
        rows = [r for r in rows if isinstance(r.get("stars"), int) and r["stars"] >= args.min_stars]
    if args.min_forks is not None:
        rows = [r for r in rows if isinstance(r.get("forks"), int) and r["forks"] >= args.min_forks]
    if args.cadence:
        rows = [r for r in rows if r.get("commit_cadence") == args.cadence]
    if args.updated_within:
        rows = [r for r in rows if within(r.get("updated"), args.updated_within)]
    if args.fetched_within:
        rows = [r for r in rows if within(r.get("fetched_at"), args.fetched_within)]
    if args.license:
        rows = [r for r in rows if args.license.lower() in str(r.get("license", "")).lower()]
    if args.pricing:
        rows = [r for r in rows if r.get("pricing") == args.pricing]
    if args.flagged:
        rows = [r for r in rows if r.get("flags")]
    if args.text:
        q = args.text.lower()
        rows = [r for r in rows if q in " ".join(str(r.get(k, "")) for k in ("name", "summary", "url", "repo")).lower()]

    key = {
        "stars": lambda r: r.get("stars") or 0,
        "forks": lambda r: r.get("forks") or 0,
        "commits": lambda r: r.get("commits_30d") or 0,
        "updated": lambda r: str(r.get("updated") or ""),
        "name": lambda r: str(r.get("name") or "").lower(),
    }[args.sort]
    rows.sort(key=key, reverse=args.sort != "name")
    rows = rows[: args.limit]

    if args.json:
        print(json.dumps(rows, ensure_ascii=False, indent=1))
        return 0

    if not rows:
        print("該当なし")
        return 0

    if args.type == "repo":
        print("| 名前 | ★ | fork | 更新頻度 | 30日commit | 最終push | 取得 | ライセンス |")
        print("|---|---:|---:|---|---:|---|---|---|")
        for r in rows:
            c30 = r.get("commits_30d")
            c30 = "100+" if isinstance(c30, int) and c30 >= 100 else (c30 if isinstance(c30, int) else "—")
            mark = " ⚑" if r.get("flags") else ""
            print(f"| [{r.get('name')}]({r['path']}){mark} | {r.get('stars') or 0:,} | {r.get('forks') or 0:,} "
                  f"| {r.get('commit_cadence') or '—'} | {c30} | {str(r.get('updated') or '')[:10]} "
                  f"| {str(r.get('fetched_at') or '')[:10]} | {r.get('license') or 'unknown'} |")
    else:
        for r in rows:
            bits = [str(r.get("genre") or "")]
            if r.get("pricing"):
                bits.append(str(r["pricing"]))
            if r.get("target"):
                bits.append(str(r["target"]))
            mark = " ⚑" if r.get("flags") else ""
            print(f"- **[{r.get('name')}]({r['path']})**{mark} — {' / '.join(b for b in bits if b)}")
            if r.get("summary"):
                print(f"  {r['summary']}")
    print(f"\n{len(rows)} 件")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
