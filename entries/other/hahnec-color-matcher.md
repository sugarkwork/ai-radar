---
repo: "hahnec/color-matcher"
name: "color-matcher"
genre: "other"
url: "https://github.com/hahnec/color-matcher"
stars: 706
forks: 50
open_issues: 7
size_kb: 124542
language: "Python"
created: "2020-02-29"
updated: "2026-02-24"
archived: false
license: "GPL-3.0"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
last_release: "v0.5.0"
last_release_at: ""
flags: ["unverified"]
risk_notes: "著者による手法比較の独立再現、映像の時間方向の一貫性、現行環境での動作は未検証。GitHub は v0.5.0 を Latest と表示し、PyPI は 0.6.0 を掲載している。GitHub リリースの年を含む公開日は未確認。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/RealMarvelX/status/2117612832019689696"]
fetched_at: "2026-11-10T09:50:44+00:00"
---

# color-matcher — 参照画像を使った色合わせ

## 出来ること

- 参照画像の色分布を入力画像に転写する。CLI では単一画像のほか、入力ディレクトリを指定した一括処理もできる。

## 目的・背景

- 学習画像のデータ拡張や写真・映像フレームの色調補正に使える。README は Reinhard 法、Monge–Kantorovich Linearization（MKL）、多変量ガウス分布に基づく色転写（MVGD）、ヒストグラムマッチングを説明している。
- 著者はライトフィールドの色の一貫性を Wasserstein 距離とヒストグラム距離で評価し、HM-MVGD-HM の優位性を報告している。比較の独立再現や映像のフレーム間の一貫性は確認していない。

## 依存関係

- リポジトリの requirements.txt には NumPy 1.21 以上、imageio、docutils、ddt、matplotlib、packaging 24.2 以上が記載されている。

## 実行条件

- PyPI の公開メタデータでは Python 3 以上。README に Unix と Windows のローカル CLI 使用例がある。コードは GPL-3.0 で、PyPI から配布されている。

## 最短手順

- `pip3 install color-matcher` で導入し、`color-matcher -h` で引数を確認する。
- 入力画像と参照画像を用意し、`color-matcher -s input.png -r reference.png` を実行する。
- AI エージェントからは、ローカルのシェル実行機能で入力画像と参照画像のパスを引数として渡す。Python ワークフローでは画像を読み込み、`ColorMatcher().transfer(src=img_src, ref=img_ref, method='mkl')` の結果を正規化して保存する。

## 変更履歴

- 2026-11-10: 初回登録
