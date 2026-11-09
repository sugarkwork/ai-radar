---
repo: "VoltAgent/awesome-design-md"
name: "Awesome DESIGN.md"
genre: "prompt-design"
url: "https://github.com/VoltAgent/awesome-design-md"
license: "MIT"
stars: 126184
language: ""
created: "2026-03-31"
updated: "2026-10-28"
forks: 13960
open_issues: 311
commits_30d: 5
commit_cadence: "weekly"
commits_90d: 8
size_kb: 2406
archived: false
author: "VoltAgent"
last_release: ""
last_release_at: ""
flags: ["unverified"]
risk_notes: "ブランドの視覚的アイデンティティは各社に帰属し、READMEは「We do not claim ownership of any site's visual identity」と明記する。各DESIGN.mdは第三者による解釈（\"An inspired interpretation of X's design language\"）で公式配色の転載ではなく、実サイトと差異があり得る。84本中10本はYAMLフロントマター無し・11本はDo's and Don'ts節が無く、shadcnスキルが前提とする入力を満たさない。README/CONTRIBUTINGが言及するpreview.html / preview-dark.html はリポジトリに存在しない（プレビューはgetdesign.md側）。UI生成の品質・再現性は未実測で、リポジトリにベンチ・比較は無い。npmの@google/design.mdはlicense表記が無く、lintツールの再配布条件は未確認。skills CLIは既定でテレメトリ送信。"
type: "repo"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/sumika45379/status/2113608913451147569"]
fetched_at: "2026-11-09T03:16:03Z"
---

# Awesome DESIGN.md — 84製品のDESIGN.mdをAIエージェントに渡してUIの雰囲気を寄せる

## 出来ること

- 84製品分のDESIGN.md（Markdownのデザイン仕様書）を design-md/<brand>/DESIGN.md に収録。Stripe / Linear / Vercel / Notion / Figma / Apple / Shopify / Supabase など。
- 各ファイルはGoogle StitchのDESIGN.md形式で、YAMLフロントマター（colors・typographyのトークン）＋Overview / Colors / Typography / Layout / Elevation & Depth / Shapes / Components / Do's and Don'ts / Responsive Behavior / Iteration Guide の節を持つ。
- これは参照資料であって実行ツールではない。リポジトリにコード・CLI・API・MCPは無く、design-md/ 配下は .md のみ（DESIGN.md 84本 + README.md 83本、リポジトリ全体で約2.4MB）。UIを生成するのはDESIGN.mdを読む側のエージェントやスキル。
- shadcnの公式スキル（別リポジトリ shadcn-ui/ui の skills/shadcn）と組み合わせると、新規アプリ作成→全コンポーネント導入→DESIGN.mdでテーマ塗り直し→デザインシステムページ生成までを一続きで指示できる。
- 品質は均一ではない（2026-11-09実測）。YAMLフロントマターがあるのは84本中74本、Do's and Don'ts節があるのは73本。kraken, lamborghini, lovable, mastercard, runwayml, sanity, spotify, starbucks, tesla, theverge の10本はフロントマターが無い。
- 各ファイルは自ら "An inspired interpretation of X's design language" と記す第三者の解釈で、公式配色の転載ではない。色・書体・余白・角丸・影に加えてDo/Don't（禁止事項）まで文章で持つ点が、単なるスクリーンショット集との違い。

## 目的・背景

- READMEの説明では、DESIGN.mdはGoogle Stitchが提唱したプレーンテキストのデザインシステム文書。AGENTS.mdが「どう作るか」、DESIGN.mdが「どう見えるか」をエージェントに伝える役割分担。
- 元の使い方は「プロジェクト直下にコピーして、エージェントにこの見た目で作ってと言う」だけ。Figma書き出しもJSONスキーマも専用ツールも要らない。
- 運営はVoltAgent（MIT、Copyright 2026 VoltAgent）。プレビュー閲覧・個別リクエスト・スターターキット販売は getdesign.md 側で、リポジトリにはMarkdownしかない。READMEとCONTRIBUTINGは preview.html / preview-dark.html に触れるが、リポジトリ内に該当ファイルは無い。
- 投稿が言う「74製品」は現状と合わない。2026-11-09時点の実測は84ディレクトリ＝84本のDESIGN.md。

## 依存関係

- DESIGN.mdを読めるコーディングエージェント（Claude Code等）。コピーして渡すだけなら追加依存なし・APIキー不要。
- shadcn経由の場合: shadcn-ui/ui の skills/shadcn（SKILL.md 21.6KB、design-system.md、design-system-page.md、rules/、scripts/showcase-coverage.mjs）。SKILL.mdの説明文に「applying a DESIGN.md or brand spec to shadcn/ui」と明記されている。
- スキル導入: npx skills add shadcn/ui（skills.shのCLIは npx skills add <owner/repo> 形式）。既定で匿名テレメトリを送るので、避けるなら DISABLE_TELEMETRY=1。
- shadcn CLI: npx shadcn@latest init / add。テンプレートは vite か next。Node/npx が必要。
- 任意: npx @google/design.md lint DESIGN.md（npm @google/design.md 0.4.0、2026-07-27更新。レジストリにlicense表記なし）。

## 実行条件

- ネット接続（Raw取得・スキル導入に必要）。DESIGN.md自体はコピーすればオフラインでも読める。
- shadcnスキルを使う場合は Node/npx と vite か next のプロジェクト。DESIGN.mdはパス・URL・貼り付けのいずれでも渡せる。
- フロントマターの無い10本を渡すと、スキルの「DESIGN.mdのフロントマター・Do's and Don'ts・Known Gapsを読む」手順が空振りする。その場合は別の手本を選ぶか手で補う。
- 効果は未実測。リポジトリにベンチマークや比較は無く、仕上がりは各DESIGN.mdの記述精度とスキル側の検証手順に依存する。

## 最短手順

- 1. スキルを入れる: npx skills add shadcn/ui（shadcn-ui/ui の skills/ 配下がエージェントに登録される）。
- 2. 手本を1つ選びRaw URLを作る: https://raw.githubusercontent.com/VoltAgent/awesome-design-md/main/design-md/stripe/DESIGN.md （design-md/<brand>/DESIGN.md の形）。
- 3. エージェントに渡す文: 「shadcnスキルで新しいアプリを作り、このDESIGN.mdからデザインの決まりを作って、デザインシステムページまで仕上げて」＋上記Raw URL。
- 4. スキルは init（--template vite|next --no-monorepo -y）→ add --all -y → DESIGN.md読解 → トークン割当 → デザインシステムページ生成 → 検証（typecheck、375px/1280pxで横スクロール無し、コントラスト比）の順に進む。
- 5. 仕上がりの確認: コントラスト4.5:1未満の組と、DESIGN.mdから意図的に外した点の報告を受け取る。気に入らなければ別のDESIGN.mdでやり直す。
- 6. スキルを使わない場合: DESIGN.mdをプロジェクト直下にコピーし、「このDESIGN.mdの見た目で作って」と頼む。

## 変更履歴

- 2026-11-09: 初回登録
