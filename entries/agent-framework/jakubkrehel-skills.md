---
repo: jakubkrehel/skills
name: jakubkrehel/skills（UI デザインスキル集）
genre: agent-framework
url: https://github.com/jakubkrehel/skills
license: MIT
stars: 10894
language: Markdown
created: 2026-07-10
updated: 2026-11-02
added: 2026-11-05
first_seen: 2026-10-22
source_post: https://x.com/sumika45379/status/2113397508152111418
sources:
  - https://jakub.kr/skills
flags: []
risk_notes: ""
forks: 421
open_issues: 11
size_kb: 741
archived: false
---

# jakubkrehel/skills（UI デザインスキル集）

## 出来ること

AI エージェントに「画面の見た目」を任せるためのスキル14本。中身は Markdown の指示書で、コードは入っていない。

- `better-interface` … 画面・フロー・UI 全体を、アクセシビリティ／レイアウト／文言／タイポグラフィ／配色／仕上げの6観点で点検し、順位付きのレポートを1枚返す。
- `better-ui` … 角の丸み、光学アライメント、影、アイコンの状態、アニメーションを**具体的な値**で詰める。
- `better-typography` / `better-colors` … 文字のスケール・字間・禁則・フォント機能と、パレット生成・セマンティックトークン・色形式の変換・コントラスト測定。
- `better-accessibility` … キーボードとフォーカス、ARIA、フォーム、スクリーンリーダー、モーション、ズームを WCAG 2.2 に照らして直す。
- `better-layout` / `better-writing` … グルーピング・整列・読み順・レスポンシブと、ラベル・エラー・空状態の文言。
- `build-design`（Figma やデザイン画像から UI を組む）、`teardown`（対象を技術イラストにして SVG/PNG/PDF で書き出す）、`variant`（複数案を作って選ぶ）、`break`（到達しうる全シナリオで部品を叩く）、`state-machine`（全状態を並べる）、`interface-review` / `explain-interface`。

## 目的・背景

作者は個人サイト jakub.kr とデザインエンジニア向け雑誌 Interfaces を書いている人。記事で扱ってきた UI の原則を、そのままエージェントが読む形に落としたもの。「動くけど見た目がもう一歩」を、毎回の指示ではなくスキル側の基準で埋めるのが狙い。

## 依存関係

- スキル本体は Markdown のみ。`npx skills add jakubkrehel/skills`（skills CLI）か、Claude Code のプラグインとして導入する。
- Claude Code 以外でも、`.agents/skills` 相当のディレクトリを読むエージェントなら動く。

## 実行条件

- MIT。
- 効果が出るのは UI を書かせる場面。バックエンドのみの案件では使う場面がない。
- `teardown` は SVG/PNG/PDF を書き出すので、実行側に描画の依存が要る場合がある（未確認）。

## 最短手順

```bash
npx skills add jakubkrehel/skills
```

```text
# Claude Code のプラグインとして
/plugin marketplace add jakubkrehel/skills
/plugin install interfaces@interfaces
```

## 変更履歴

- 2026-11-05: 初回登録（★10,894 / MIT / Markdown / 最終push 2026-11-02）
