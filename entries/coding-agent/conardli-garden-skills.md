---
repo: "ConardLi/garden-skills"
name: "Garden Skills"
genre: "coding-agent"
url: "https://github.com/ConardLi/garden-skills"
flags: ["unverified"]
risk_notes: "レビューではインストールや生成を実行しておらず、出力品質、知識検索によるコンテキスト削減量、エージェント間の動作差、各スキルの追加依存と外部サービスの料金・素材の利用条件は未確認。GitHubの /releases/latest は motion-showreel v0.1.0 を表示したが、公開一覧には同スキルの v0.2.0 もあるため、リポジトリ全体の最新版と公開日時は記載していない。"
stars: 14851
forks: 1710
open_issues: 26
size_kb: 76325
language: "JavaScript"
created: "2026-04-21"
updated: "2026-11-08"
archived: false
license: "MIT"
commits_30d: 11
commits_90d: 21
commit_cadence: "weekly"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/AISuperDomain/status/2118356546698760516"]
fetched_at: "2026-11-10T09:48:43+00:00"
---

# Garden Skills — Web制作・動画・記事化などをAIエージェントに追加するスキル集

## 出来ること

- READMEは、コードで短編動画を作る motion-showreel、Web動画・プレゼン用の web-video-presentation、Web制作の web-design-engineer、画像生成とプロンプト作成の gpt-image-2、資料を記事にする beautiful-article、ローカル知識検索の kb-retriever を紹介している。[README](https://github.com/ConardLi/garden-skills/blob/main/README.md)
- web-design-engineer の定義には、ページやダッシュボードなどの制作に加え、要件整理、デザイン資料の収集、ブラウザでの確認が含まれる。成果物の品質は未計測。[スキル定義](https://github.com/ConardLi/garden-skills/blob/main/skills/web-design-engineer/SKILL.md)

## 目的・背景

- 作業の適用条件と手順を SKILL.md にまとめ、エージェントが必要に応じて読み込む。スキルには補足資料、スクリプト、素材も同梱できる。[README](https://github.com/ConardLi/garden-skills/blob/main/README.md#what-is-a-skill)

## 依存関係

- CLIで導入する場合は npx が使える環境と、スキル読み込みに対応するエージェントを使う。READMEには手動コピーや、タグで導入元を固定する方法もある。[インストール手順](https://github.com/ConardLi/garden-skills/blob/main/README.md#install)

## 実行条件

- READMEの互換表は Claude Code、Cursor、Codex CLI などを作者側のテスト済みとして掲載している。このレビューでの動作確認は未実施。[互換表](https://github.com/ConardLi/garden-skills/blob/main/README.md#compatibility)
- リポジトリのライセンスはMIT。外部サービスの料金や個別素材の利用条件は未確認。[README](https://github.com/ConardLi/garden-skills/blob/main/README.md)

## 最短手順

- 作業プロジェクトで `npx skills add ConardLi/garden-skills -s web-design-engineer` を使い、対象エージェントにWeb制作スキルを導入する。[CLI導入手順](https://github.com/ConardLi/garden-skills/blob/main/README.md#install)
- 導入先のAIエージェントで『web-design-engineer を使って、HTML/CSSで製品紹介ページの試作を作って』と依頼する。[スキル定義](https://github.com/ConardLi/garden-skills/blob/main/skills/web-design-engineer/SKILL.md)

## 変更履歴

- 2026-11-10: 初回登録
