---
repo: "Usagi-org/ai-goofish-monitor"
name: "ai-goofish-monitor"
genre: "other"
url: "https://github.com/Usagi-org/ai-goofish-monitor"
license: "MIT"
stars: 19101
language: "Python"
created: "2025-07-16"
updated: "2026-10-10"
forks: 3116
open_issues: 52
commits_30d: 0
commit_cadence: "monthly"
commits_90d: 9
size_kb: 9584
archived: false
last_release: "2.5"
flags: ["unverified"]
risk_notes: "判定精度、通知遅延、現行の闲鱼環境での動作、モデルAPIの実利用料金、最新リリースの公開日時は未確認。プラットフォームの利用条件への適合性は利用形態に依存する。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/Ryrenz/status/2117642992232112463"]
fetched_at: "2026-11-10T10:07:12+00:00"
---

# ai-goofish-monitor｜闲鱼の中古出品を画像と説明で選別し通知

## 出来ること

- キーワード、価格帯、送料無料、出品時期、地域で絞り込んで定期監視し、AIが推奨した商品を企業微信、Bark、Telegram、Webhookなどへ通知できる。タスク、実行ログ、結果はWeb UIで確認できる。

## 目的・背景

- 中古品の新着検索と候補の確認を省力化する。READMEによると、自然言語の要望から判定基準を生成し、Playwrightで取得した商品情報と画像をモデルで評価する。タスク、結果、価格履歴はSQLiteに保存する。

## 依存関係

- 画像入力対応のOpenAI互換APIが必要。ローカル起動にはPython 3.10以上、Node.jsとnpm、Playwright CLIおよび対応ブラウザーが必要。公開DockerイメージにはChromiumが含まれる。

## 実行条件

- 実際の監視には闲鱼のログイン状態を設定する。コードはMITライセンスで、モデルAPIの料金は利用先に依存する。公式READMEは闲鱼の利用規約とrobots.txtの順守を求めている。

## 最短手順

- 公式リポジトリの.env.exampleから.envを作り、OPENAI_API_KEY、OPENAI_BASE_URL、OPENAI_MODEL_NAMEを設定して、docker compose up -dで起動する。
- http://127.0.0.1:8000 のWeb UIで闲鱼のログイン状態を設定し、AIモードで要望を入力してタスクを作成する。
- AIクライアントからタスクを作成する場合は、起動先の /docs で認証と入力スキーマを確認し、decision_mode=aiでPOST /api/tasks/generateを呼ぶ。202応答のジョブIDを使い、GET /api/tasks/generate-jobs/{job_id}で進捗を取得する。

## 変更履歴

- 2026-11-10: 初回登録
