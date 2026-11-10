---
type: "repo"
repo: "googleworkspace/cli"
name: "Google Workspace CLI (gws)"
genre: "other"
url: "https://github.com/googleworkspace/cli"
author: "googleworkspace (Google)"
license: "Apache-2.0"
stars: 32212
language: "Rust"
created: "2026-03-02"
updated: "2026-11-03"
forks: 1988
open_issues: 136
commits_30d: 1
commits_90d: 1
commit_cadence: "monthly"
size_kb: 10738
archived: false
last_release: "v0.22.5"
last_release_at: "2026-03-31"
flags: ["unverified"]
risk_notes: "README 冒頭に「This is not an officially supported Google product.」と明記されており、googleworkspace org 配下でも公式サポート製品ではない。Claude/Anthropic への言及はなく、Claude Code から使えるかは Bash ツール経由で CLI を呼ぶ一般経路の推測で、リポジトリ側の検証はない。最終リリースは 2026-03-31、90日コミットは 2026-10-30 の CI 修正1件のみで開発は停滞している。README はスキル数を 40+ と 100+ の両方で書いており、実際の skills/ は95ディレクトリ。API の課金額は各 GCP プロジェクトのクォータ次第で、料金表は確認していない。"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/thegreatest_sv/status/2114326860326723736"]
fetched_at: "2026-11-09T21:41:03Z"
---

# Google Workspace CLI (gws) — Gmail/Drive/Calendar を1つの CLI と Agent Skills で操作

## 出来ること

- Gmail・Drive・Calendar・Sheets・Docs・Chat・Admin など Workspace の各 API を `gws <service> <resource> <method>` の1コマンドで呼び、結果を JSON で返す（例: `gws drive files list --params '{"pageSize": 5}'`）。
- コマンド体系は固定リストではなく、実行時に Google の Discovery Service から生成される。Google が API を追加すると gws 側も自動で追随する。
- 読み取り専用ではなく、送信・作成・アップロードもできる（`gws gmail +send`、`gws gmail +reply`、`gws drive +upload`、`gws sheets +append`、`gws calendar +insert`）。
- SKILL.md 形式の Agent Skills を95個同梱（`gws-gmail-read`、`gws-drive`、`gws-calendar-agenda`、`gws-sheets` など）。エージェントはスキルを読んで適切なコマンドを選べる。
- `--dry-run` でリクエストのプレビュー、`--page-all` でページングを NDJSON 出力、`--sanitize` で Google Cloud Model Armor を通したプロンプトインジェクション検査ができる。
- `gws workflow +standup-report` / `+meeting-prep` / `+weekly-digest` / `+email-to-task` など、複数 API をまたぐ補助コマンドも同梱する。

## 目的・背景

- Workspace API ごとに curl やクライアント実装を書き分ける代わりに、単一の CLI にまとめ、人間とエージェントの両方から同じコマンドで扱えるようにする。
- 配布元は GitHub の `googleworkspace` org（Google の組織アカウント）。Rust 製、Apache-2.0、32,203 stars / 1,987 forks / 136 open issues。
- ただし README 冒頭で「This is not an officially supported Google product.」と明記されている。org 配下というだけで Google の公式サポートや SLA があるわけではない。
- 開発は 2026-03-02 の公開から 2026-03-31 の v0.22.5 までに集中し、その後は 2026-10-30 の CI ワークフロー修正1件のみ。90日コミットは 1 件で、新機能の追加は見込めない。

## 依存関係

- 実行バイナリ: GitHub Releases のプリビルト（macOS/Linux/Windows）。npm の `@googleworkspace/cli` は Node.js 18+ で動く薄いラッパーで、postinstall が Releases からバイナリを取得する（依存パッケージなし、bin は `gws`）。
- Google Cloud プロジェクトと OAuth クレデンシャルが必須。`gws auth setup` は gcloud CLI を呼び、プロジェクト作成・API 有効化・ログインをまとめて行う。
- Google アカウント（Workspace でも個人の @gmail.com でも可）と、利用する API（Gmail API、Drive API、Calendar API など）の有効化。
- 任意: Model Armor のテンプレート（`--sanitize` 利用時）。導入経路は Homebrew（`brew install googleworkspace-cli`）、cargo、Nix flake もある。

## 実行条件

- 初回は `gws auth setup` → `gws auth login`。資格情報は AES-256-GCM で暗号化され、鍵は OS キーチェーンに保存される。
- OAuth アプリが未検証（testing）だと同意できるスコープは約25個まで。`recommended` プリセット（85+ スコープ）は失敗するため、`gws auth login -s drive,gmail,calendar` のように必要なサービスだけ指定する。
- CI・ヘッドレスでは、ブラウザのある環境で `gws auth export --unmasked` した資格情報を `GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE` に渡すか、サービスアカウント鍵を使う。
- API 呼び出しは自分の GCP プロジェクトのクォータに計上される。API 未有効化だと 403 `accessNotConfigured` が返り、エラー内の enable_url から有効化する。gws 本体は Apache-2.0 で無償。
- MCP サーバではない。AI からは Bash / ターミナルツールで `gws ...` を実行する形で、HTTP で常駐するツールサーバではない。

## 最短手順

- 1. インストール: `npm install -g @googleworkspace/cli`（または Releases のバイナリを PATH に置く）。
- 2. 認証: `gws auth setup`（gcloud が必要。GCP プロジェクト作成と API 有効化を行う）→ `gws auth login -s drive,gmail,calendar`。
- 3. 動作確認: `gws drive files list --params '{"pageSize": 5}'`、`gws gmail +triage`、`gws calendar +agenda`。
- 4. AI に呼ばせる: CLI を一度認証したうえで `npx skills add https://github.com/googleworkspace/cli` を実行し、SKILL.md 群をエージェントのスキルディレクトリへ入れる。あとは「`gws gmail +read --id <ID>` を実行して本文を要約して」のようにコマンド単位で指示する。
- 5. Gemini CLI なら `gemini extensions install https://github.com/googleworkspace/cli` で拡張として導入でき、認証済みの gws を継承する。
- 6. Claude Code 向けの専用拡張は用意されていない（README に Claude/Anthropic の記載なし）。Bash ツールから gws を叩くか、CLAUDE.md に使うコマンド例を書いて運用する。

## 変更履歴

- 2026-11-09: 初回登録
