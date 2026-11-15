---
name: "ComfyUI Omnichar"
genre: "video-gen"
url: "https://github.com/omnichar/ComfyUI-Omnichar"
flags: ["unverified"]
risk_notes: "Omnichar Cloudのライセンス付きキャラクターでは、実行ごとのプロバイダーへの報告と、画像・動画の出力許可条件がある。"
repo: "omnichar/ComfyUI-Omnichar"
stars: 139
forks: 22
open_issues: 0
size_kb: 9683
language: "Python"
created: "2026-10-02"
updated: "2026-11-15"
archived: false
license: "GPL-3.0"
commits_30d: 3
commits_90d: 29
commit_cadence: "monthly"
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/dextune/status/2118984300498677835"]
fetched_at: "2026-11-15T15:28:57.905932+00:00"
---

# ComfyUI Omnichar

## 出来ること

- ComfyUI上で`.char`形式のキャラクターを読み込み、顔・体・衣装の参照画像、説明文、任意のLoRAをノードに接続できる。Encode Characterでキャラクターを作成し、Save Characterで保存できる。READMEはFLUX.2、MiniMax H3、Krea 2などの対応を掲げ、MiniMax H3向けの音声入力方法も説明している。

## 目的・背景

- READMEによると、`.char`に参照画像、固定した説明文、任意の学習済みLoRAをまとめ、対応モデル間でキャラクター情報を使うためのComfyUI統合。参照画像の順序は保持され、プロンプト中の番号指定と対応する。

## 依存関係

- README記載の要件はComfyUI、Python 3.10以上、`requirements.txt`から導入する`omnichar-sdk`。

## 実行条件

- キャラクターファイルは既定で`ComfyUI/models/characters/`に置く。READMEは、Omnichar Cloudのライセンス付きキャラクターを使う場合、ライセンス確認のためオンライン接続とライセンスシークレットが必要と説明している。ライセンス確認が通った時点で、実行が後で失敗してもキュー投入ごとに1回の生成としてプロバイダーへ報告される。

## 最短手順

- README記載の手順：ComfyUIの`custom_nodes`へ移動し、`https://github.com/omnichar/ComfyUI-Omnichar`をcloneする。リポジトリ内で`pip install -r requirements.txt`を実行してComfyUIを再起動する。`.char`を`ComfyUI/models/characters/`に置き、Load CharacterとDecode Characterをワークフローに接続する。

## 変更履歴

- 2026-11-15: 初回登録
