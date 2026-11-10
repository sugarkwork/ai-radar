---
repo: "Motionsites-AI/claude-skill"
name: "MotionSites Web Builder"
genre: "coding-agent"
url: "https://github.com/Motionsites-AI/claude-skill"
license: "unknown"
stars: 1935
forks: 198
open_issues: 1
size_kb: 1942
language: "Python"
created: "2026-10-26"
updated: "2026-10-26"
archived: false
commits_30d: 2
commits_90d: 2
commit_cadence: "monthly"
last_release: "v1.0.0"
flags: ["unverified"]
risk_notes: "['作者のREADMEで手順を確認した。導入、スクリーンショットによる修正ループ、生成品質、外部配信素材の到達性は実測していない。', 'GitHubの公開ページで最新タグを確認した。公開日時の年とタイムゾーンは取得できなかった。'] GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/opensourcelab9/status/2117504564941508613"]
fetched_at: "2026-11-10T09:19:25Z"
---

# MotionSites Web Builder — ページを実装し、スクリーンショットで点検するClaudeスキル

## 出来ること

- Claudeが作例と映像素材を参照し、実装仕様を作ってランディングページを構築する。作者のREADMEによると、実装後はスクリーンショットとQAスクリプトで素材切れ、モバイル幅でのはみ出し、フォント、動画再生を点検する。
- コード生成の代わりに、Lovableやv0などに渡す制作プロンプトの作成も依頼できる。

## 目的・背景

- 作者は、曖昧な制作指示、実素材の不足、実装後の目視確認不足を課題に挙げている。仕様テンプレート、作例、演出レシピ、採点基準を組み合わせて制作と点検を進める。

## 依存関係

- Claude Codeではプラグインまたは手動配置で導入できる。スクリーンショットによる点検には、READMEが任意の構成としてPython版PlaywrightとChromiumを案内している。

## 実行条件

- Claude.aiまたはClaudeデスクトップで使う場合は、スキルをアップロードして有効化し、設定でコード実行を有効にする。
- READMEではスキルと同梱のサンプルを無料で公開している。LICENSEによると、指示・参照資料・スクリプトはMITで、作例プロンプトと素材はMotionSitesに著作権がある。同スキルで制作する顧客向けサイトにも利用できるが、プロンプト集・素材集としての再販売や再配布は禁止されている。

## 最短手順

- Claude Codeで `/plugin marketplace add Motionsites-AI/claude-skill`、続けて `/plugin install motionsites-web-builder@motionsites` を実行する。
- Claudeに『建築写真家のポートフォリオ用ランディングページを作り、スクリーンショットでモバイル表示を確認して修正して』と依頼する。READMEでは、サイト制作を依頼するとスキルが自動で起動すると説明している。

## 変更履歴

- 2026-11-10: 初回登録
