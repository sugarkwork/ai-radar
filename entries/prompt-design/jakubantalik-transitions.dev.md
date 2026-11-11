---
name: "Transitions.dev"
genre: "prompt-design"
url: "https://github.com/Jakubantalik/transitions.dev"
repo: "Jakubantalik/transitions.dev"
license: "unknown"
stars: 6213
language: "HTML"
created: "2026-04-21"
updated: "2026-11-08"
forks: 295
open_issues: 14
commits_30d: 62
commit_cadence: "daily"
commits_90d: 100
size_kb: 53686
archived: false
flags: ["unverified"]
risk_notes: "GitHub API上のライセンスはunknown。READMEには個人・商用利用と改変・製品への同梱を認める説明がある一方、ライブラリ自体の競合配布を禁止し、ツール類はMITと記載されている。料金やPro機能の利用条件の詳細は未確認。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/thegreatest_sv/status/2116967509735747833"]
fetched_at: "2026-11-10T14:11:58.576375+00:00"
---

# Transitions.dev

## 出来ること

- READMEによると、12種類の操作パターンを示すインタラクティブなCSSトランジション集を提供し、各カードからコピー可能なCSSスニペットを取得できる。CLIでトランジションを追加でき、エージェントスキルとしても導入可能。UI生成向けスキルには、UI・テキスト・画像などの表示モードが記載されている。Refineは実行中のアプリにパネルを追加し、選択したCSS/Motionトランジションの調整案を提示するツールとして説明されている。

## 目的・背景

- トランジションのデモと、プロジェクトに持ち込めるCSSスニペットをまとめて提供する。READMEでは、スキルの内容をショーケースサイトのデモと一致させるため、index.htmlから生成すると説明している。

## 依存関係

- README記載の利用経路は、npm経由のCLIおよびskills CLIによるスキル導入。RefineのLLM連携例はCursor CLIを配線する手順を記載している。個々のCSSスニペットは自己完結型と説明され、UI生成スキルには依存のないランタイムと記載がある。

## 実行条件

- ローカル表示はREADMEに `python3 -m http.server 8765` の例がある。Proトランジションの追加は、パスワードレスのブラウザーサインイン後に認証済みAPIから取得すると説明されている。Refineの `--llm` オプションはCursor CLIを配線する。

## 最短手順

- CSSを手動で使う場合は、README記載のとおりサイトのカードからスニペットをコピーする。CLIを使う場合は `npx transitions-dev add card-resize`。スキルを導入する場合は `npx skills add Jakubantalik/transitions.dev`。

## 変更履歴

- 2026-11-11: 初回登録
