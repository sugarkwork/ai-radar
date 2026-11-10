---
repo: JCodesMore/ai-website-cloner-template
name: ai-website-cloner-template
genre: agent-framework
url: https://github.com/JCodesMore/ai-website-cloner-template
license: MIT
stars: 38914
language: TypeScript
created: 2026-03-13
updated: "2026-10-19"
added: 2026-11-05
first_seen: 2026-11-04
source_post: https://x.com/thegreatest_sv/status/2117687388214272339
sources: []
flags: []
risk_notes: "第三者のサイトを丸ごと複製する用途は著作権・商標・利用規約に抵触しうる。学習用のレイアウト分析や自作サイトの移行など、権利のある範囲で使うこと。"
forks: 5791
open_issues: 12
commits_30d: 0
size_kb: 1466
archived: false
commits_90d: 15
commit_cadence: "monthly"
fetched_at: "2026-11-09T21:33:25Z"
last_release: "v0.6.1"
last_release_at: "2026-10-05"
---

# ai-website-cloner-template

## 出来ること

- コーディングエージェントにURLを渡すと、そのサイトを**編集可能な Next.js アプリとして再構築**するテンプレート。`/clone-website <url>` のスキルを同梱する。
- 4段階の手順で進む:
  1. **Map** — 元サイトのURLをローカルのルートへ対応づけ、既存の作業を壊さない。
  2. **Observe** — デスクトップ／モバイルの表示、実アセットとフォント、ホバーなどの別状態を確認して抽出。
  3. **Build** — 編集可能なコンポーネントと動作するインタラクションとして実装（独立セクションは並行作業に委譲）。
  4. **Compare** — 元ページとローカルページを同じサイズ・状態で突き合わせ、差分を修正して本番ビルドのチェックを実行。
- Framer のページやアニメーション主体のサイトには専用の指示が含まれる。
- 素のテンプレートとしても使える（GitHub の「Use this template」で自分のリポジトリを作る）。

## 目的・背景

「スクリーンショットを見ながら手で写経する」作業を、エージェントが実ブラウザで観察 → 実装 → 比較修正まで回す形に置き換える。出力先を Next.js 16 + React 19 + Tailwind CSS v4 + shadcn/ui に固定することで、生成物がそのまま編集・量産できる構成になっている。

## 依存関係

- Node.js 24 以上。
- ブラウザ操作ができるAIコーディングエージェント。README の推奨は Claude Code + Opus 5.5。Codex CLI、Cursor、OpenCode も対応表に載っている。
- Tailwind CSS v4、shadcn/ui、Lucide React。

## 実行条件

- サイトの複製は著作権・商標・利用規約の制約を受ける。権利のないサイトを公開物として再配布する用途には使えない。
- 直近30日のコミットは0（最終push 2026-10-19、v0.6.1）。活発に更新されている最中ではない点は把握しておく。
- ★3.9万・fork 5,735・open issue 11件。

## 最短手順

```text
# エージェントに貼る（プロジェクトの作成から依存導入まで行う）
Set up https://github.com/JCodesMore/ai-website-cloner-template
as a standalone project in a new folder on my computer.
Ask me where to put it. Clone the repository, remove its origin remote,
install dependencies, and run npm run check.

# 以降、ブラウザアクセスを有効にしたエージェントで
/clone-website https://example.com
```

## 変更履歴

- 2026-11-05: 初回登録（★38,631 / pushed 2026-10-19 / MIT / v0.6.1）
