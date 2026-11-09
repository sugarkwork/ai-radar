---
repo: "davila7/claude-code-templates"
name: "claude-code-templates"
genre: "coding-agent"
url: "https://github.com/davila7/claude-code-templates"
author: "Daniel Ávila (@dani_avila7)"
license: "MIT"
stars: 33210
language: "Python"
created: "2025-07-04"
updated: "2026-11-08"
forks: 3896
open_issues: 456
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
size_kb: 301379
archived: false
last_release: "v1.29.7"
last_release_at: "2026-10-09"
fetched_at: "2026-11-08T17:50:16Z"
source_post: "https://x.com/opensourcelab9/status/2113238959862284769"
sources: ["https://www.aitmpl.com", "https://x.com/dani_avila7/status/2109822699174559748", "https://x.com/opensourcelab9/status/2113238959862284769"]
first_seen: "2026-11-08"
added: "2026-11-08"
flags: ["unverified"]
risk_notes: "Turn Inspector の描画は Claude Code 2.1.287+ の実機では未実行で、リポジトリ同梱の README・hooks 実装・テストファイルと作者のデモ動画に基づく確認。インストールコマンド自体（npx claude-code-templates@latest --mod ui/turn-inspector）は空ディレクトリで実行し、6ファイルが配置されることを実測した。ブロック別トークン数は概算（約4文字/トークン）で、正確なのはリクエスト単位の入出力合計のみ。mod は v0.1.0 と新しく、GitHub Releases は v1.29.7（2026-10-09）で npm の 1.32.2（2026-11-07）より遅れている。"
type: "repo"
---

# claude-code-templates — Claude Code 部品カタログと Turn Inspector

## 出来ること

- Claude Code の設定部品を1つのカタログから入れる CLI。README の表では skills 918 / agents 422 / commands 288 / MCPs 119 / settings 80 / hooks 63 / mods 50 / loops 18 / templates 14 / sandboxes 11 で計1,980超。各ファイルを所定の場所へ書き込み、既存設定は上書きせずマージする。
- `--mod` で入るのが「Mod」＝Claude Code 自体の UI・挙動を変える function-hooks プラグイン（50種）。secret-redactor や stack-viewer などと並び、turn-inspector もこの1つ。
- Turn Inspector は「モデルへの1リクエスト＝1ターン」としてセッションを並べ、各ターンの入力（システムプロンプト＋ツール定義＋メモリ、過去ターン、今回のユーザー発話やツール結果）と出力（thinking / 本文 / ツール呼び出し）を積み上げ表示し、コンテキストウィンドウの占有率をバーで出す。
- `/turns` で開く。行をクリック（または Tab + Enter）で展開し、`follow` / `collapse` / `close` を切り替える。`/turns clear` は記録の破棄、`/turns stop` はペインを閉じる。
- 入力が前のターンより減った場合は `compacted before this turn`、出力上限やウィンドウ超過で切れた場合は `Cut off` として明示する。

## 目的・背景

- Claude Code の設定は skills・subagents・slash commands・hooks・MCP・settings という小さなファイル群に分かれ、置き場所も形式もばらばら。claude-code-templates はそれを aitmpl.com のカタログにまとめ、CLI 一発で配置するためのレジストリ兼インストーラ。
- 作者は Daniel Ávila（X: @dani_avila7、GitHub: davila7）。2025-07 作成、2026-11 時点で★33,210 / fork 3,896。PR は Claude Code の plugin validator と NVIDIA SkillSpector で検査されると README に記載がある。
- Turn Inspector の動機は「コンテキストが何で埋まっているか見えない」こと。Anthropic の context-window 図と同じ描き方で、ターンごとに何が積み上がったかを横に出し、重くなった原因を勘で探さなくて済むようにする。

## 依存関係

- 導入は Node.js + npx のみ（グローバルインストール不要）。npm パッケージ claude-code-templates の最新は 1.32.2（MIT、2026-11-07 公開）。
- mod 本体は TypeScript 2ファイル＋plugin.json＋hooks.json で、サードパーティの実行時依存は無い。Claude Code のプラグイン実行環境（`claude-code` モジュールの Register / RenderChildren などの型）に依存する。
- Claude Code 2.1.287+ が前提。2.1.259〜2.1.286 では `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1` が必要。README は 2.1.296 で動作確認、リポジトリ内の 2.1.283 宣言に対して書かれたと記す。
- ライセンスはリポジトリ（GitHub API の SPDX は MIT）、npm パッケージ、mod の plugin.json の3か所すべて MIT。

## 実行条件

- 導入先プロジェクトが Claude Code で trusted であること。`.claude/skills/turn-inspector/` は `turn-inspector@skills-dir` として自動読み込みされる。
- 全画面レイアウトで横にドックするには端末幅110桁以上（`/tui fullscreen`）。クラシックレイアウトではプロンプトの上に出る。Claude Desktop ではセッションのサイドパネルに出る。
- 記録は mod を読み込んだ時点から始まる（ペインを開くのが遅れても、それまでのターンは残っている）。サブエージェントのリクエストは一覧に出ない（`agent-flow` mod の担当）。
- 正確なのはリクエスト単位の入出力合計だけ。ブロック別の数字は約4文字/トークンの概算で `~` が付き、再開セッションでは system/tools が `/context` の推定にフォールバックする。

## 最短手順

- 1. プロジェクトのディレクトリで `npx claude-code-templates@latest --mod ui/turn-inspector` を実行（v1.32.2 で、`.claude/skills/turn-inspector/` に6ファイルが入ることを実測）。
- 2. Claude Code を trusted なプロジェクトで起動し、`/turns` を打つ。ペインが開き、以降のリクエストが1行ずつ増える。
- 3. 横に並べたい場合は `/tui fullscreen`。幅は `pluginConfigs["turn-inspector@skills-dir"].options.columns`（36–120、既定56）、保持ターン数は `maxTurns`（既定200）、起動時に開くなら `openOnStart: true`。
- 4. `/turns` が候補に出ないときは読み込まれていない。`claude --debug` を実行し、`~/.claude/debug/latest` に `hooks module turn-inspector@… loaded` があるか確認する。
- 5. 動作を自分で確かめるなら `claude plugin test .claude/skills/turn-inspector`（同梱テストが turn モデルと端末／デスクトップ両サーフェスの描画を検証する）。

## 変更履歴

- 2026-11-09: 初回登録
