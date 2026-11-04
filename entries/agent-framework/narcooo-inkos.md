---
repo: Narcooo/inkos
name: InkOS
genre: agent-framework
url: https://github.com/Narcooo/inkos
license: AGPL-3.0
language: TypeScript
created: 2026-03-12
updated: 2026-10-24
added: 2026-11-04
first_seen: 2026-11-04
sources:
  - https://x.com/awe0_io/status/2117581510547312710
flags: []
risk_notes: "AGPL-3.0。ネットワーク経由で提供する場合はソース公開義務が生じる。生成物の権利・出版条件は利用者側で確認。"
stars: 10990
forks: 2002
open_issues: 249
commits_30d: 6
commits_90d: 100
commit_cadence: weekly
size_kb: 31015
archived: false
fetched_at: "2026-11-04T01:24:08Z"
last_release: v1.8.0
last_release_at: 2026-08-17
---

# InkOS

## 出来ること

- **長編の物語創作に特化した AI エージェント**。世界観・人物設定・伏筆（伏線）・校閲・改稿を1つのワークフローに統合する。
- 長編・短編・脚本・インタラクティブ・ストーリーに対応。多言語出力。
- 独自の状態管理: AI は**増分JSONだけを出力**し、プログラム側で検証して物語状態を更新する。これで長編にありがちな設定矛盾を抑える。
- Studio（GUI）・TUI・CLI の3つの操作形態。

## 目的・背景

2026-03 公開、★10,990 / fork 2,002、v1.8.0。LLM に長編を書かせると、章が進むほど設定が崩れる。全文を毎回プロンプトに入れるのではなく、物語の状態を構造化データとして持ち、差分だけをモデルに書かせる設計で解決を狙っている。

## 依存関係

- Node.js / TypeScript
- LLM の API キー（OpenAI 互換）
- SQLite（状態管理）

## 実行条件

- 長編になるとコンテキストと API 課金が増える（差分方式で抑制しているが、校閲・改稿で追加消費）。
- AGPL-3.0。Web サービスとして公開する場合はソース開示が必要。
- 生成物の出版・商用利用の条件は別途確認。

## 最短手順

```bash
git clone https://github.com/Narcooo/inkos
# README の手順でセットアップし、Studio / TUI / CLI のいずれかで開始
```

## 変更履歴

- 2026-11-04: 初回登録（★10,990 / v1.8.0 / AGPL-3.0）
