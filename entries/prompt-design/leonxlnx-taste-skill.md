---
repo: "Leonxlnx/taste-skill"
name: "Taste Skill"
genre: "prompt-design"
url: "https://github.com/Leonxlnx/taste-skill"
license: "MIT"
stars: 112762
language: "JavaScript"
created: "2026-02-19"
updated: "2026-11-08"
forks: 7588
open_issues: 3
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 104213
archived: false
last_release: "v2.5.1"
flags: ["unverified"]
risk_notes: "導入と生成結果は独立に実測しておらず、スキル導入前後の品質差や発見投稿の医療ダッシュボードへの寄与は未確認。最新リリースの公開日時は年とタイムゾーンを含む形式で確認できなかった。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/thegreatest_sv/status/2117998992126591399"]
fetched_at: "2026-11-10T11:21:22+00:00"
---

# Taste Skill｜ウェブ制作のデザイン指針とブラウザー検査をエージェントに追加

## 出来ること

- コーディングエージェントに、レイアウト、写真、タイポグラフィ、動きの設計ルールを渡す。完了前にブラウザーでレイアウトやフォーム、アクセシビリティの一部を確認し、コピーも検査する。

## 目的・背景

- 似通ったランディングページを減らすために、設計ルールと検査を制作フローに組み込む。リリースノートでは作者が前版のサイト制作テストをもとに、モバイルでの要素の重なりなどを改善したと報告している。生成品質の改善幅は独立に測定していない。

## 依存関係

- スキルに対応するコーディングエージェントと、検査用スクリプトを動かす Node.js 22 以上、Chrome・Edge・Chromium のいずれかが必要。写真の WebP 出力やモバイル向け切り抜きには任意で ffmpeg を使う。

## 実行条件

- ブラウザーが標準外の場所にある場合は CHROME_PATH を指定する。追加の写真やアイコンの取得にはネット接続が必要。スキル自体は MIT ライセンスで、写真の利用条件は素材ごとに確認する。

## 最短手順

- 公式README記載の `npx skills add https://github.com/Leonxlnx/taste-skill --skill design-taste-frontend` で導入する。対応エージェントの新規セッションで `design-taste-frontend` を使うよう明示し、サイトの目的・対象読者・必要なページを渡して、実装とブラウザー検査を依頼する。

## 変更履歴

- 2026-11-10: 初回登録
