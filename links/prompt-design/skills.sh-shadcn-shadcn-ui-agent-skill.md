---
name: "shadcn 公式スキル（shadcn/ui agent skill）"
genre: "prompt-design"
url: "https://skills.sh/shadcn/ui"
author: "shadcn（shadcn-ui/ui）"
pricing: "free"
pricing_detail: "スキル本体は MIT ライセンスのオープンソースで、skills.sh に料金ページ・有料プランはない。`npx skills add` は GitHub から直接取得するため課金もアカウント登録も不要。実行に必要なのは Node.js と npx のみ（skills CLI v1.7.6 は node >=22.20.0、shadcn CLI v4.23.0 は node >=20.18.1）。"
signup_required: false
flags: ["unverified"]
risk_notes: "未確認: (1) 生成される UI の品質・再現性は未実測。リポジトリに evals/evals.json はあるが、公開された採点結果や通過率は確認していない。(2) GitHub の stars は API がレート制限で取得できず、skills.sh 表示の 127.6K を採録（API 実測ではない）。(3) 見本ページ生成の一連の流れは design-system.md / design-system-page.md の記述に基づくもので、当方はアプリの scaffold から通しで実行していない。注意: スキルは SKILL.md 内の !`command` ディレクティブでシェルコマンドを実行し、エージェント権限で動く（skills.sh も警告、Socket 監査は Warn）。skills CLI は既定で匿名テレメトリを送る。DESIGN.md の配色はコミュニティが各ブランドを解釈したもので公式配色ではない（DESIGN.md 側の性質で、本スキルの欠陥ではない）。"
type: "link"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/sumika45379/status/2113608913451147569"]
fetched_at: "2026-11-09T03:24:00Z"
---

# shadcn 公式スキル — DESIGN.md から shadcn/ui のデザインシステムを組み立てる

## 目的

- コーディングエージェントに shadcn/ui の作法（コンポーネントの検索・追加・修正・スタイリング・構成）を守らせるための、shadcn 自身が配布する公式スキル。
- SKILL.md には「DESIGN.md やブランド仕様を shadcn/ui に適用する」用途が明記され、design-system.md が新規アプリの作成から見本ページの生成までの手順を定義している。X 投稿が紹介する「DESIGN.md を選んでスキルに渡す」使い方は、この手順に対応する。
- 読者は Claude Code などのエージェントで UI を作る人。スキルは人間が読むプロンプト集ではなく、エージェントが読み込んで従う指示書兼チェックリストである。

## 何ができるか

- 実体は shadcn-ui/ui リポジトリの skills/shadcn/ にある。入口の SKILL.md、DESIGN.md 適用手順の design-system.md、見本ページ仕様の design-system-page.md、禁止・推奨を Incorrect/Correct で示す rules/（styling, forms, composition, icons, chat, base-vs-radix）、網羅チェック用の scripts/showcase-coverage.mjs、コントラスト測定と状態マトリクスの assets/showcase/、CLI・MCP・レジストリ・カスタマイズの各リファレンス、evals/evals.json。
- DESIGN.md を渡したときの流れ: `npx shadcn@latest init --preset <code> --template vite --name <app> --no-monorepo -y` で新規案件を作り、`npx shadcn@latest add --all -y` で部品を全部入れ、DESIGN.md の frontmatter・Do's and Don'ts・Known Gaps を読んで、色役割を --background / --foreground / --primary / --muted などの CSS 変数へ写像する。角丸・影・フォント・type-* を固定し、コンポーネントの cva バリアントを編集して塗り直す。
- 最後に見本ページを生成する。13節構成で、色は「面＋前景」の組として並べ、ColorPair がコントラスト比を実測する。4.5:1 を下回る組は DESIGN.md が指定した値でも報告する。プリミティブは variant×state のマトリクスで状態を並べ、DESIGN.md の Do/Don't は描画した対で示す。
- 網羅性は記憶で語らせない。`add --all` の後にディスク上のコンポーネントファイルを数え、showcase-coverage.mjs で見本ページに未掲載の部品を洗ってゼロにする。仕上げにブラウザで typecheck・コンソールエラー・初期スクロール位置・375px/1280px の横溢れ・ダークモードを確認する。
- 副次的な機能として、shadcn CLI 同梱の MCP サーバ（`shadcn mcp`）があり、レジストリの検索・閲覧・導入を AI から呼べる。
- 限界: 生成物の品質と再現性は一次情報に実測がなく、エージェントの実力に依存する。DESIGN.md の配色はコミュニティの解釈であってブランド公式ではない。スキルはシェルコマンドを実行するため、エージェント権限で走る点に注意。

## 料金

- 無料。スキルは MIT ライセンスで公開されており、skills.sh に料金ページや有料プランはない。
- 費用がかかるのは実行環境側のみ。Node.js と npx が必要で、skills CLI v1.7.6 は node >=22.20.0、shadcn CLI v4.23.0 は node >=20.18.1 を要求する。API キーやサブスクリプションは不要。

## 登録の要否

- 不要。GitHub アカウントなしで `npx skills add shadcn/ui` が GitHub から clone して展開できた（認証プロンプトは出なかった）。
- リポジトリには shadcn と migrate-radix-to-base の2スキルがあるため、片方だけ入れるなら `npx skills add shadcn/ui --skill shadcn`。導入先はプロジェクトの .agents/skills/ などで、`--global` を付けるとユーザー階層に入る。
- skills CLI は既定で匿名テレメトリ（スキル名・ファイル・時刻）を送る。止めるには `DISABLE_TELEMETRY=1` を設定する。

## 変更履歴

- 2026-11-09: 初回登録
