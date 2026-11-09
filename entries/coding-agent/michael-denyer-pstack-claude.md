---
repo: "michael-denyer/pstack-claude"
name: "pstack-claude"
genre: "coding-agent"
url: "https://github.com/michael-denyer/pstack-claude"
license: "MIT"
stars: 4144
language: "JavaScript"
created: "2026-05-26"
updated: "2026-11-07"
forks: 377
open_issues: 10
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
size_kb: 5955
archived: false
last_release: "v0.9.133"
last_release_at: "2026-11-07"
flags: ["unverified"]
risk_notes: "投稿の media は対象と無関係な日本語ニュース系の転載（静止画は著名人のポートレートで、リポジトリやAIツールの内容を含まない）。動画 mp4 は vision で内容を確認できないため評価に使っていない。effectiveness は README の記述＝作者の主張で、第三者による効果測定は公開されていない。Codex / Copilot / Pi などの対応は各ランタイム向けマッピングと synthetic provider のスモークテストに基づく自己申告で、実モデルの遵守は一部しか確認されていないと docs/reference.md に注記がある。"
type: "repo"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/opensourcelab9/status/2112876589075841167"]
fetched_at: "2026-11-08T15:50:08Z"
---

# pstack-claude — 失敗の再現から検証証拠までを返すエージェント用スキル集（poteto-mode）

## 出来ること

- 入口は poteto-mode というスキル。依頼を渡すとタスク種別に応じた playbook を選び、バグ修正では「失敗の再現 → how / why で原因調査 → 修正の委任 → 失敗ケースの再実行」まで進める。返るのは修正と、失敗していた時・通った時の両方の証拠（README の Getting started の記述）。
- 公開スキル43個と原則集24個を同梱。計画、機能追加、リファクタ、性能調査、プロトタイプ、PR 保守、リリース、長期プロジェクト向けの playbook が用意されている。
- 個別スキルを直接呼べる。原因調査の how / why、設計前の architect、複数案の並列比較 arena、差分を3モデルで叩く interrogate、並列ワーカーの swarm、失敗テスト先行の tdd、計測値の妥当性確認 benchmark-checklist、変更の影響範囲 blast-radius など。
- 同じスキルツリーを複数ハーネスへ配布する。Claude Code を基準に、Codex・GitHub Copilot・Pi・Muse・Kimi Code CLI・OMP・OpenCode 2・Antigravity・MiniMax Code・Grok Build・Gemini CLI 向けのツール名／モデル名マッピングを持つ。
- 対応ランタイムでは SessionStart フックで通常の依頼を poteto-mode へ自動ルーティングする（Claude Code、Codex、Copilot、Muse、MiniMax Code、Antigravity、Pi、Kimi、OMP、OpenCode 2）。
- setup-pstack でロールごとのモデルと reasoning effort を設定できる（例: arena runners を opus @xhigh に）。

## 目的・背景

- 上流は Lauren Tan（poteto）が Cursor 向けに作ったスキル集 pstack。本リポジトリはその移植版で、Cursor のスキル名をエージェントに実行時変換させる方式をやめ、インストール前に Claude Code 向けへ翻訳しておく点を違いとして挙げている（README の Built for Claude Code）。
- 思想は「速く行きたいなら、まず深く」。コードは短く単純に、仕事は検証済みで返すことを原則集として明文化している（package.json の説明、SKILL.md の Principles）。
- 上流 c742dd6（v0.15.36）と thermos 1.0.0 を追跡し、Cursor 固有の自動化や UI チュートリアルは除外。移植側の独自変更は fork として宣言する運用。
- 投稿の「プラグイン2行で入る」「Codex・Pi・Copilot 版もある」は README のインストール節と一致する。一方「失敗と成功の証拠が返る」はスキル文中の指示として実装されているもので、自動テストで保証される機能ではない。

## 依存関係

- 基本は Markdown のスキルとローカルスクリプトのみ。サーバーもテレメトリも無く、スキルが読ませた内容は利用中のモデル提供者へ送られる（README の Data handling）。
- ワークフロー次第で追加が必要: GitHub CLI（gh、PR 監視・出荷。gh auth login）、Bun（watch-pr スクリプトの依存導入）、Claude Code の plugin-dev スキル（automate-me / reflect / poteto-mode のオーサリング時）。
- Pi 版は @earendil-works/pi-coding-agent と typebox を任意の peerDependency として持つ。
- モデルは各ランタイムが提供するものを使う。既定は Claude 系で、setup-pstack によりロール単位で上書きできる。

## 実行条件

- Claude Code は 2.1.292 以降。マーケットプレイス登録とプラグイン導入の2行で入る。
- Codex は /hooks でフックを信頼する必要があり、Muse は muse plugins approve pstack が必要。Copilot は初回に setup-pstack でモデルを選ぶ。
- ライセンスは MIT（© 2026 Michael Denyer）。上流 pstack は Lauren Tan、取り込んだ cursor-team-kit と thermos は Cursor の著作で、それぞれ別ライセンス表記と NOTICE がある。
- 効果は作者の記述によるもので、独立した評価は公開されていない。対応表の一部は synthetic provider でのスモークテスト止まりで、実モデルの遵守は未検証と docs/reference.md に注記がある。
- star 4144 / fork 377 / open issue 10、直近30日で100コミット以上・最新リリース v0.9.133（2026-11-07）と更新は活発。

## 最短手順

- Claude Code を起動し、次の2行を実行する。
- /plugin marketplace add michael-denyer/pstack-claude
- /plugin install pstack@pstack-claude
- タスクを poteto-mode 指名で依頼する。例: Use poteto-mode to fix the search filter resetting when I change pages.
- 自動ルーティングを切り替えたいときやモデル割り当てを変えたいときは setup-pstack を実行する。

## 変更履歴

- 2026-11-09: 初回登録
