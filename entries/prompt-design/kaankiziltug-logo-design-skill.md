---
name: "logo-design-skill"
genre: "prompt-design"
repo: "kaankiziltug/logo-design-skill"
url: "https://github.com/kaankiziltug/logo-design-skill"
last_release: "v1.4.5"
flags: ["unverified"]
risk_notes: "作者の手順と掲載例を確認した。スクリプトの実行、エージェント間の再現性、16 pxでの可読性や既存商標との類似性は独立検証していない。最新リリースは公開ページの表示で確認し、公開日時の完全な値は未確認。"
stars: 6462
forks: 513
open_issues: 6
size_kb: 6755
language: "HTML"
created: "2026-09-26"
updated: "2026-11-06"
archived: false
license: "MIT"
commits_30d: 8
commits_90d: 31
commit_cadence: "weekly"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/opensourcelab9/status/2116138074505900234"]
fetched_at: "2026-11-10T12:53:35Z"
---

# logo-design-skill — ロゴのSVG案を実寸で比較し、採用案を展開するAIスキル

## 出来ること

- 白黒のSVG候補を比較し、64・32・16 pxの表示と推奨案を確認してから方向を選ぶ。選んだ案を配色、ロゴの組み合わせ、ファビコン、利用ガイドへ展開する。
- SVG監査は形状の複雑さや細部を点検し、比較シートでは単色・反転や競合と並べた見え方を確認できる。

## 目的・背景

- 配色や納品物を作り込む前に、ロゴの形と小サイズでの見え方を比較できるよう、候補選択を工程に組み込む。
- 作者のREADMEによると、業種や技法で検索できる実在ロゴの参照資料が1,400ファイル以上ある。

## 依存関係

- 付属スクリプトはPython 3.8以上と標準ライブラリを使用する。PNG・ICOの書き出しにはCairoSVG、rsvg-convert、Inkscape、Chromium系ブラウザー、macOS Quick Lookなど、利用可能なレンダラーを使う。

## 実行条件

- スキルを読み込めるAIエージェントで利用する。作者はClaude CodeとCodex向けの導入方法を案内している。
- スキル本文、スクリプト、テンプレート、カタログデータはMIT。参照用の実在ロゴSVGは各権利者の商標で、MITの適用範囲外。

## 最短手順

- Claude Codeで `/plugin marketplace add kaankiziltug/logo-design-skill` と `/plugin install logo-design@logo-design-skill` を実行して導入する。Codexでは `skills/logo-design/` をエージェントのスキルフォルダーに配置する方法も作者が案内している。
- 導入したエージェントに『スペシャルティコーヒー店のロゴ案を3案作って』と依頼する。白黒の比較シートと推奨理由を見て1案を選び、SVGの派生版と利用ガイドを依頼する。

## 変更履歴

- 2026-11-11: 初回登録
