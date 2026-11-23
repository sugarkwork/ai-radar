---
name: "自媒体工作台 (DSH Media Desk)"
genre: "other"
url: "https://github.com/woniuniuniu/dsh-media-desk"
repo: "woniuniuniu/dsh-media-desk"
flags: ["unverified"]
risk_notes: "日本語での生成対応はREADMEで確認できないため不明。作者の説明に基づく機能紹介で、独立した実機検証はしていない。"
stars: 1637
forks: 192
open_issues: 7
size_kb: 8561
language: "JavaScript"
created: "2026-11-02"
updated: "2026-11-18"
archived: false
license: "MIT"
commits_30d: 43
commits_90d: 43
commit_cadence: "daily"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/NFT_Chen/status/2119436949002109200"]
fetched_at: "2026-11-22T13:14:38.117173+00:00"
---

# 自媒体工作台 (DSH Media Desk)

## 出来ること

- DeepSeek Harnessのサイドバーで使うコンテンツ制作ワークスペース。アイデアから口播スクリプト、タイトル、動画カバー、挿絵、6コマ分镜を作成し、会話で編集できます。コンテンツの予定管理、投稿後のデータ振り返り、スタイル設定にも対応するとREADMEは説明しています。画像生成には対応する画像APIまたはDeepSeek Harnessに登録された画像生成ツールが必要です。

## 目的・背景

- 作者が日々のコンテンツ制作で、アイデアの記録、原稿作成、投稿後の振り返りに使うために作った実験的なプラグインとREADMEに記載されています。

## 依存関係

- DeepSeek Harnessのプラグインとして動作します。README記載の要求バージョンは0.2.1-rc.5以上の0.2.xです。文章生成にはHarnessで設定したモデル、画像生成には画像APIキーまたは対応するHarness画像生成ツールを利用できます。自分のアカウント情報を取り込む機能は任意で、Monidとそのデータサービスを利用します。

## 実行条件

- READMEではDeepSeek Harness 0.2.xを要求し、0.2.2-rc.1のデスクトップ版とWeb版でテストしたと説明しています。デスクトップ版・Web版のプラグイン導入手順があり、Web版はスマートフォンのブラウザーからも開けるとの記載です。生成モデルや画像生成APIの利用条件・費用は、接続するサービスやアカウントに依存します。

対応言語: READMEはUIの中文・英文対応と、英語に切り替えるとスクリプト、タイトル、分镜も英語になると説明。日本語対応は記載がなく不明。（出典: https://github.com/woniuniuniu/dsh-media-desk）
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- Harnessのプラグイン画面で実験的なカスタムプラグイン索引を有効にし、README記載の索引 `https://raw.githubusercontent.com/woniuniuniu/dsh-media-desk/main/index.json` を追加して「自媒体工作台」をインストールします。索引を使わない場合はプラグイン追加画面に `dsh-media-desk` を入力するか、デスクトップ版では `dsh plugin --profile desktop add dsh-media-desk`、Web版では `dsh plugin --profile web add dsh-media-desk` を実行します。初回表示のサンプルデータは、右上の「示例数据 · 清空」から消去できます。

## 変更履歴

- 2026-11-23: 初回登録
