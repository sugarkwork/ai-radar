---
repo: "addyosmani/agent-skills"
name: "Agent Skills"
genre: "coding-agent"
url: "https://github.com/addyosmani/agent-skills"
license: "MIT"
stars: 114537
language: "JavaScript"
created: "2026-02-15"
updated: "2026-11-01"
forks: 11972
open_issues: 132
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 1943
archived: false
author: "Addy Osmani"
last_release: "0.6.15"
last_release_at: "2026-10-31"
flags: ["unverified"]
risk_notes: "品質改善の効果はメンテナ自身の trigger/挙動 eval と著者の主張に限られ、独立した第三者ベンチマークは未確認。コードを実行するツールではなく指示文の集合なので、効果はホストのモデルとルーティング精度に依存し、evals/README.md 自身が発火の不安定さ（TDD 系が 6 回中 1 回）を記録している。browser-testing-with-devtools は chrome-devtools MCP と実ブラウザが必須で、--autoConnect ではログイン済みプロファイルに触れるため取り扱いに注意。"
type: "repo"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/sumika45379/status/2112884125120319643"]
fetched_at: "2026-11-09T21:35:54Z"
---

# Agent Skills — AIコーディングエージェント向け開発スキル25個（Addy Osmani）

## 出来ること

- 企画・仕様・計画・実装・テスト・レビュー・出荷という開発ライフサイクルを、25個の SKILL.md ワークフローとしてエージェントに踏ませる。各スキルは手順・検証条件・「サボる口実への反論」・レッドフラグまで含む。
- 9つのスラッシュコマンド（/spec /plan /build /test /constraints /review /webperf /code-simplify /ship）が各段階の入口になり、対応するスキルを自動で起動する。
- 投稿が「addyosmani から5個」と挙げた context-engineering、debugging-and-error-recovery、browser-testing-with-devtools、code-simplification、code-review-and-quality は、いずれも skills/ 配下に実在する（全25スキル）。
- skills/ のほか、agents/ に4つのレビューペルソナ（code-reviewer、test-engineer、security-auditor、web-performance-auditor）、references/ に7つの共有チェックリストを同梱。

## 目的・背景

- 「AIコーディングエージェントは最短経路を取りがちで、仕様・テスト・セキュリティレビューを飛ばす」という問題意識から、シニアエンジニアの進め方を手順として固定するのが狙い。
- Google のエンジニアリング文化（Hyrum's Law、Beyonce Rule、テストピラミッド、Chesterton's Fence、トランクベース開発など）を各スキルの手順に埋め込んでいると README は説明する。
- 作者は Addy Osmani。MIT ライセンスで 2026-02-15 公開、2026-11-08 時点で stars 114,034 / forks 11,915 / open issues 132。最新リリースは 0.6.15（2026-10-31）。
- 投稿の「スター数」は親リポジトリ全体の値であり、個々のスキルの人気ではない点は投稿自身も断っている。

## 依存関係

- スキル本体は Markdown のみ。追加のサーバー、APIキー、SDK は不要。
- 一括導入の npx skills（vercel-labs/skills）を使う場合のみ Node.js（npx）が必要。Claude Code はプラグインマーケットプレイス、Codex は codex plugin、Gemini CLI は gemini skills install と、ホスト固有の仕組みでも入る。
- browser-testing-with-devtools は chrome-devtools MCP サーバーの設定が必須（npx chrome-devtools-mcp@latest）。実ブラウザで DOM・コンソール・ネットワーク・パフォーマンスを見る。
- スキルを1個だけ npx で入れるとリポジトリ直下の references/ がコピーされず、共有チェックリストへの参照が切れる既知の制約がある（issue #361）。フル構成ならリポジトリごと入れる。

## 実行条件

- SKILL.md を読める AI エージェントであること。Markdown の指示を受け付けるホストならよく、Claude Code、Cursor、Codex、GitHub Copilot、Gemini CLI、OpenCode、Windsurf などの手順が README にある。
- ホストが description による自動ルーティングに対応していれば自動で発火する。非対応なら using-agent-skills を常時読み込ませるか、スキル名を指定して呼ぶ。
- リポジトリ同梱の AGENTS.md / CLAUDE.md はこのリポジトリのコントリビュータ用なので、自分のプロジェクトへコピーしないよう README が注意している。
- 料金は無料、ライセンスは MIT。著作権表示と許諾文を残せば商用利用・改変・再配布が可能。

## 最短手順

- 一括導入（70以上のエージェント対応）: npx skills add addyosmani/agent-skills 。個別なら npx skills add addyosmani/agent-skills --skill context-engineering のように --skill で絞る。
- Claude Code: /plugin marketplace add addyosmani/agent-skills の後に /plugin install agent-skills@addy-agent-skills 。組み込みコマンドと名前が衝突する /review は /agent-skills:review の名前空間形式で呼ぶ。
- 手動配置: skills/<skill-name>/SKILL.md をホストのスキルディレクトリへ置く。Cursor は .cursor/skills/、OpenCode は .opencode/skills/、Codex はリポジトリ root の skills/ を .codex-plugin/plugin.json 経由で読む。SKILL.md の frontmatter は name（小文字ハイフン区切り）と description（Use when ... を含む発火条件）の2キーだけ。
- 呼び出し: スキル名を明示する（Claude Code なら /context-engineering、Codex なら @spec-driven-development）か、「新しいセッションを始める」「出力がずれてきた」など description に合う依頼を出す。1スキルだけ使うなら skills/<name>/ と references/ を同じ構成で置く。
- browser-testing-with-devtools を使う前に、プロジェクトの .mcp.json か Claude Code 設定へ {"mcpServers":{"chrome-devtools":{"command":"npx","args":["-y","chrome-devtools-mcp@latest","--isolated"]}}} を追加し、エージェントからブラウザを検査できるようにする。

## 変更履歴

- 2026-11-09: 初回登録
