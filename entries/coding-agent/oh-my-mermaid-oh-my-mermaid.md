---
repo: oh-my-mermaid/oh-my-mermaid
name: oh-my-mermaid（omm）
genre: coding-agent
url: https://github.com/oh-my-mermaid/oh-my-mermaid
license: MIT
stars: 3389
language: TypeScript
created: 2026-03-22
updated: "2026-04-07"
added: 2026-11-05
first_seen: 2026-10-26
source_post: https://x.com/opensourcelab9/status/2114847055210553442
sources: []
flags: []
risk_notes: ""
forks: 267
open_issues: 10
size_kb: 2359
archived: false
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
fetched_at: "2026-11-09T21:36:36Z"
last_release: "v0.2.0"
last_release_at: "2026-03-25"
---

# oh-my-mermaid（omm）

## 出来ること

- AI エージェントにコードベースを読ませ、**アーキテクチャ図**を Mermaid で書かせる。エージェント側では `/omm-scan` を呼ぶ。
- 1枚の図ではなく「視点（perspective）」単位で出力する。既定は全体構造・データの流れ・外部連携など。複雑な部品はさらに子の図を持つ階層構造になる。
- 各部品に説明・制約・懸念・TODO などのメモが付く（最大7項目）。生成物は `.omm/<perspective>/description.md` と `diagram.mmd` の木構造でディスクに残る。
- `omm view` でローカルのビューアが開き、階層をたどりながら読める。
- Claude Code・Codex・Cursor など5つのツールに対応（README の記載）。

## 目的・背景

「AI が数秒で書いたコードを、人間が何時間もかけて読む」状態を埋めるための道具。コードを読む代わりに、AI に**人間が読むための設計資料**を書かせる。図は生成物なので、コードが変われば再スキャンすればよい。

## 依存関係

- Node.js。`npm install -g oh-my-mermaid && omm setup` で入る。`omm setup` が対応エージェント側にスキルを配置する。
- 図の描画は Mermaid。ビューアは同梱のローカルサーバー。

## 実行条件

- MIT。
- **更新が 2026-04-07 で止まっている**（2026-11-05 時点で commits_30d = 0）。投稿は「★3,317」としているが、API の実測は ★3,380。
- 大規模リポジトリでは、階層化するほどスキャン時間とトークン消費が増える。対象を絞ってから走らせるのが現実的。
- 出力は Mermaid なので、読む側に Mermaid を表示できる環境（`omm view` か、GitHub のプレビュー）が要る。

## 最短手順

```bash
npm install -g oh-my-mermaid && omm setup
# エージェント側で
/omm-scan
# 結果を見る
omm view
```

## 変更履歴

- 2026-11-05: 初回登録（★3,380 / MIT / TypeScript / 最終push 2026-04-07）
