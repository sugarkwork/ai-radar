---
repo: "leepokai/jev-guard"
name: "jev-guard"
genre: "other"
url: "https://github.com/leepokai/jev-guard"
author: "leepokai"
license: "MIT"
stars: 150
language: "JavaScript"
created: "2026-09-17"
updated: "2026-10-02"
forks: 24
open_issues: 4
commits_30d: 0
commits_90d: 27
commit_cadence: "monthly"
size_kb: 7549
archived: false
last_release: "v0.3.1"
last_release_at: "2026-09-17"
flags: ["unverified"]
risk_notes: "料金『1,000チェックあたり約4セント』は README の想定（1コール約1kトークン）と Vercel AI Gateway の $0.042/1M input 単価からの試算で、実測の請求額ではない。APIキーは必須（キー未設定時は明示的にエラー）だが、無料枠の有無は一次情報で確認できない。有効性は開発者自身の計測（662スキル走査、ライブAPIでのClaude Code/OpenCode検証）のみで、第三者評価は無い。既定は fail-open（API不達なら許可）で、フックを通らない経路や設定ミスでは回避され得る。README 自身が『guardrail, not a sandbox』と明記している。"
type: "repo"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/thegreatest_sv/status/2114326860326723736"]
fetched_at: "2026-11-09T21:41:09Z"
---

# jev-guard — コーディングエージェントのツール実行を Jev で検査するフック

## 出来ること

- ツール実行前に Jev へ risk / approval / user_requested / from_untrusted の型付き質問を投げ、deny・ask・allow を判定する。判定は src/guard.js の閾値で決まり、risk 2.5 以上で拒否、1.5 以上または承認確率 0.75 以上で承認要求、ユーザーが明示的に依頼した操作は ask を allow に変える。
- 破壊的なコマンドを拒否する。README の実測では `rm -rf /` は risk 3.0 で deny、`rm -rf node_modules && npm install` は risk 1.6 で ask。すべての rm -rf を一律に止めるのではなく、危険度に応じて拒否と承認要求を分ける。
- ツール結果（Webページ、ファイル、MCP出力、コマンド出力）を走査し、AI 宛ての指示（injection / canary）を検出して untrusted として記録する。200文字未満の結果とローカルの編集・検索ツールは対象外、約60k文字を超える結果は head+tail に切り詰める。
- スキル、プラグイン、rules、CLAUDE.md / AGENTS.md をセッション開始時・ロード時・`jev-guard scan-skills` で検査し、exfiltration / covert execution / instruction override / canary / unrelated side effects を分類する。
- Claude Code、Codex、GitHub Copilot CLI、Antigravity CLI、Gemini CLI、Cursor、pi、OpenCode、ACP（Zed / JetBrains）向けの薄いアダプタを同梱し、同じポリシーとセッション記憶を共有する。

## 目的・背景

- Claude Code の auto mode が行う『実行前の分類器による検査』を、独自モデルではなく Jev への型付き質問として実装し、Claude Code 以外のエージェントにも同じ検査を持ち込むためのツール。README は auto mode の説明を引用し、risk / user_requested / from_untrusted の3問で同じ仕事をすると位置づけている。
- LLM に文章で判定させるのではなく、risk を 0–3 のスコア、承認や注入判定を確率で返させ、ポリシーを20行程度の読めるコード（src/guard.js）に置く設計。
- セッションごとに ~/.jev-guard/sessions/ へユーザーの直近プロンプト、エージェントの意図、直前の判定、検出した untrusted 内容の抜粋を保存し、『ユーザーが頼んだことか』『読んだ内容に仕込まれた指示か』を文脈付きで判定する。

## 依存関係

- Node.js 20.3 以上（npm の engines 指定）。npm の実行時依存はゼロで、ビルド手順も不要。
- pi で使う場合のみ @earendil-works/pi-coding-agent が任意の peerDependency。
- Jev API の資格情報が必要。TypeSafe のキー（console.typesafe.ai）、Vercel AI Gateway の `vck_…` キー、OpenRouter の `sk-or-…` キーのいずれか、または JEV_BASE_URL で指定する System One 互換サーバ。
- 判定はリモート呼び出しに依存する。README の計測では直接 API で約0.75秒/コール、AI Gateway 経由で p50 約580ms。

## 実行条件

- API キーが無いと `no credentials: run jev-guard key <key> ...` で失敗する。キーは ~/.jev-guard/config.json に 0600 で保存され、環境変数（JEV_API_KEY / AI_GATEWAY_API_KEY / VERCEL_OIDC_TOKEN / OPENROUTER_API_KEY）が優先される。
- ツール名・引数・cwd、またはツール結果が TLS で Jev 側へ送られる。機密リポジトリで使う前に TypeSafe のプライバシーポリシーを確認する必要がある。
- 既定は fail-open で、Jev に到達できない場合は警告を出して許可する。拒否に倒すには JEV_GUARD_FAIL_CLOSED を設定する。
- フックとして動くため、エージェントがフックを通らない経路（内蔵 web fetch など）は検査されない。ACP プロキシもクライアントを通る操作だけが対象。
- 料金は Jev の入力トークン従量（$0.042/1M input、output 無料）。1コール約1kトークンと仮定した場合に1,000回で約4セントというのが README の試算で、実際の請求額は利用量に依存する。無料枠の有無は一次情報では未確認。

## 最短手順

- Node.js 20.3 以上を用意し、`npm i -g jev-guard` でインストールする。
- `jev-guard key "<APIキー>"` を実行する。キーは TypeSafe（console.typesafe.ai）、Vercel AI Gateway の `vck_…`、OpenRouter の `sk-or-…` のいずれか。~/.jev-guard/config.json に保存される。
- `jev-guard install claude` を実行すると ~/.claude/settings.json に PreToolUse / PostToolUse などのフックが追記される（冪等）。codex・copilot・gemini・agy・cursor・pi・opencode も同じコマンド形式で指定できる。
- Claude Code のプラグインとして入れる場合は、Claude Code 内で `/plugin marketplace add leepokai/jev-guard` の後に `/plugin install jev-guard@jev-guard` を実行する。
- 動作確認は `jev-guard check Bash '{"command":"rm -rf /"}'`（拒否なら exit 2 と DENY 表示）と `jev-guard check Bash '{"command":"ls -la"}'`（許可なら exit 0）。既存スキルの一括検査は `jev-guard scan-skills`。

## 変更履歴

- 2026-11-09: 初回登録
