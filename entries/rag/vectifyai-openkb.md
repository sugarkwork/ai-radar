---
repo: "VectifyAI/OpenKB"
name: "OpenKB"
genre: rag
url: "https://github.com/VectifyAI/OpenKB"
license: "Apache-2.0"
stars: 4846
language: "Python"
created: "2026-04-04"
updated: 2026-07-22
added: "2026-11-03"
first_seen: "2026-11-03"
sources: []
flags: []
risk_notes: ""
forks: 503
open_issues: 84
commits_30d: 0
commits_90d: 0
commit_cadence: stale
size_kb: 33441
archived: false
fetched_at: "2026-11-03T22:58:24Z"
last_release: v0.4.5
last_release_at: 2026-07-20
---

# OpenKB

## 出来ること

- 生の文書（PDF / Word / Markdown / PowerPoint / HTML / Excel / CSV / テキスト / URL）を LLM で読み、要約・概念ページ・エンティティページ・相互リンクを持つ wiki 形式の知識ベースに「コンパイル」する CLI。
- ベクトル DB を使わない。長文書は PageIndex のツリー索引で構造を保ったまま検索し、推論ベースで必要箇所に到達する。
- 図表や画像も対象にするマルチモーダル検索。`openkb query` の単発質問と `openkb chat` のマルチターン（セッション永続）に対応。
- 生成側の機能: wiki からエージェント向けスキルを蒸留する Skill Factory、レポート等への変換。
- wiki は素の `.md` とリンクなので Obsidian でそのまま開ける。ブラウザ用の Knowledge Workbench（Web UI）も同梱。Google の Open Knowledge Format（OKF）に準拠。

## 目的・背景

従来の RAG は問い合わせのたびに知識をゼロから探し直すため、何も蓄積しない。OpenKB は Karpathy が投稿した「LLM が要約・概念ページ・相互参照を自動で維持し、知識が複利で増える」という構想にもとづき、知識を一度コンパイルして更新し続ける方式を取る。矛盾はフラグされ、相互参照は最初から存在する。

## 依存関係

- `pip install openkb`（GitHub 直インストール、editable も可）。
- LLM の API キー（`openkb init` 時に設定）。

## 実行条件

- コンパイル時に LLM のトークンを消費する。文書量が多いほど初回コストが大きい。
- ベクトル DB サーバを別途立てる必要はない。
- 最終 push は 2026-07-22。活発に更新中というわけではない。

## 最短手順

```bash
pip install openkb
mkdir my-kb && cd my-kb
openkb init
openkb add paper.pdf
openkb add https://arxiv.org/pdf/2509.11420
openkb query "What are the main findings?"
openkb chat
```

## 変更履歴

- 2026-11-03: 初回登録（star 4,846 / pushed 2026-07-22 / Apache-2.0）
