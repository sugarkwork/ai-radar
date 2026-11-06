---
repo: OpenBMB/PilotDeck
name: PilotDeck
genre: agent-framework
url: https://github.com/OpenBMB/PilotDeck
license: AGPL-3.0
stars: 4981
language: TypeScript
created: 2026-05-22
updated: 2026-11-06
added: 2026-11-05
first_seen: 2026-10-20
source_post: https://x.com/opensourcelab9/status/2112514206511837503
sources:
  - https://x.com/OpenBMB/status/2110364065822646570
  - https://pilotdeck.openbmb.cn
flags: [unverified]
risk_notes: "投稿の Workbuddy Bench 79.1点（Qwen3.6-35B-A3B）は README の表に該当がなく一次情報で確認できない。採用した数値は README 側のみ。"
forks: 560
open_issues: 180
size_kb: 76479
archived: false
commits_30d: 100
commits_90d: 100
commit_cadence: daily
fetched_at: "2026-11-06T22:53:58Z"
last_release: v2026.11.06
last_release_at: 2026-11-05
---

# PilotDeck

## 出来ること

- 「WorkSpace」を単位に、ファイル・メモリ・スキルをプロジェクトごとに分離する。並行して複数の仕事を走らせても文脈が混ざらない。
- **ホワイトボックスメモリ**: メモリの生成・抽出・保存・検索が画面から追え、誤った記憶を1件単位で直せる。アイドル時間に記憶を整理する Dream Mode と、一括ロールバックがある。
- **スマートルーティング**: タスクの難易度を見て、難しい呼び出しは上位モデル、簡単な呼び出しは軽いモデルへ振り分ける。トークン消費をタスク単位で表示する。
- **常時稼働**: 指示を待たずに候補タスクを探し、長時間の監視を回し、成果物をローカルファイルとして置いて要約を残す。
- Word / Excel / PowerPoint の資料作成向けスキルを同梱（2.0 で「ワンクリックで事務資料を仕上げる」とうたっている）。
- MCP ネイティブ。Web / CLI / IM のフロントで同じ動作。
- **動画生成とマルチモーダル設定**（v2026.11.06）: 動画生成ツールとプレビュー、生成ジョブの保存・復旧が入り、モデルや入出力のマルチモーダル設定を画面から扱えるようになった。

## 目的・背景

清華大学 THUNLP・ModelBest・OpenBMB・AI9Stars の共同開発。Claude Code や Cursor が「プログラミング」、Cowork が「デスクトップの知識作業」、WorkBuddy が「IM 連携」に寄せているのに対し、こちらは**長時間・複数プロジェクトの事務作業**を主戦場に据えている。README は「メモリが追跡できるか」「トークン費をタスク単位で把握できるか」「難易度でモデルを自動で振り分けられるか」「席を外しても仕事が進むか」の4点を設計課題として挙げている。

## 依存関係

- **Node.js 22.13 以上かつ 23 未満**（組み込みの `node:sqlite` を使うため。範囲外だと起動しない）。
- macOS / Linux はワンラインインストーラ、Windows は PowerShell 版インストーラ。ソースから入れる場合は `corepack enable` のうえ `corepack pnpm install --frozen-lockfile`。
- ネイティブ依存（`node-pty` / `better-sqlite3` / `bcrypt` / `sharp`）は prebuild が使われるが、取得できない環境では Visual Studio Build Tools と Python が要る。

## 実行条件

- ライセンスは **AGPL-3.0**。社内配布や SaaS 化を考える場合はこの条件を確認する。
- 初回起動後にプロバイダと API キーを画面から設定する。キーがないと動かない。
- 既定の UI は `http://localhost:3001`。
- README のベンチマーク（Workbuddy Bench、260タスク、gpt-5.6-sol を判定役に3回ずつ）は**作者側の計測**。表があるのは DeepSeek-V4.1-Flash と GLM-5.3 の2条件で、第三者による追試は確認していない。

## 最短手順

```bash
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/OpenBMB/PilotDeck/main/install.sh | bash
pilotdeck
```

```powershell
# Windows（PowerShell）
irm https://raw.githubusercontent.com/OpenBMB/PilotDeck/main/install.ps1 | iex
pilotdeck
```

## 変更履歴

- 2026-11-05: 初回登録（★4,980 / AGPL-3.0 / TypeScript / 最終push 2026-11-05）
- 2026-11-06: 動画生成ツールとマルチモーダル設定を追記（v2026.11.06 / 83660cc9）
