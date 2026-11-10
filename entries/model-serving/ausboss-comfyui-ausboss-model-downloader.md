---
type: "repo"
name: "ausboss/ComfyUI-AusBoss-Model-Downloader"
genre: "model-serving"
url: "https://github.com/ausboss/ComfyUI-AusBoss-Model-Downloader"
author: "ausboss"
source_post: "https://x.com/aiaicreate/status/2118893732330455218"
sources: ["https://x.com/aiaicreate/status/2118893732330455218?a=4VGJVgaixBlyKGRU-KE&s=46", "https://x.com/aiaicreate/status/2118893732330455218", "https://github.com/ausboss/ComfyUI-AusBoss-Model-Downloader", "https://api.github.com/repos/ausboss/ComfyUI-AusBoss-Model-Downloader"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "既存ファイルは上書きせず再ハッシュもしないため完全性の証明にはならない。取得したモデルは実行しない設計だが配布元・トークン・重みの権利確認は必要。 当方でインストール・推論・生成・ベンチ再現はしていない。"
repo: "ausboss/ComfyUI-AusBoss-Model-Downloader"
license: "MIT"
language: "Python"
created: "2026-11-06"
updated: "2026-11-09"
stars: 9
forks: 1
open_issues: 1
commits_30d: 5
commits_90d: 5
commit_cadence: "weekly"
size_kb: 152
archived: false
fetched_at: "2026-11-09T21:39:27Z"
last_release: ""
last_release_at: ""
---

# ausboss/ComfyUI-AusBoss-Model-Downloader

## 出来ること

Hugging Face/CivitaiのURLからComfyUIのモデルフォルダへ重みを取得するノード。

## 目的・背景

紹介対象は `ausboss/ComfyUI-AusBoss-Model-Downloader`。対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:50.313886+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

## 依存関係

対応拡張子を限定し保存先は登録モデルフォルダのみ。Installed表示とDownload missing、ワークフローへのリンク保存を案内。

## 実行条件

既存ファイルは上書きせず再ハッシュもしないため完全性の証明にはならない。取得したモデルは実行しない設計だが配布元・トークン・重みの権利確認は必要。

コード本体の許諾と、基底モデル・同梱素材・外部API・音声/人物等の利用条件は別に確認する。

## 最短手順

1. [公式README](https://github.com/ausboss/ComfyUI-AusBoss-Model-Downloader#readme)で対応版と依存を確認する。
2. 上記の対象固有条件を満たす環境を用意し、配布元の手順を選ぶ。
3. 外部サービスの料金・認証・データ送信とライセンスを確認してから導入する。

本調査では導入・ビルド・起動をしていないため、成功済みのコマンドとしては掲載しない。

## 出典

- @aiaicreate: https://x.com/aiaicreate/status/2118893732330455218
- 対象資料: https://github.com/ausboss/ComfyUI-AusBoss-Model-Downloader
- 参照: https://api.github.com/repos/ausboss/ComfyUI-AusBoss-Model-Downloader

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
