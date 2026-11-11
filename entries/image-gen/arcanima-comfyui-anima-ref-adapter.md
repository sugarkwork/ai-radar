---
name: "Anima Reference Adapter for ComfyUI"
genre: "image-gen"
url: "https://github.com/ArcAnima/ComfyUI-Anima-Ref-Adapter"
flags: ["unverified"]
risk_notes: "アダプターの重みはCircleStone Non-Commercialライセンス。READMEではコードのライセンスをApache-2.0としている。"
repo: "ArcAnima/ComfyUI-Anima-Ref-Adapter"
stars: 234
forks: 14
open_issues: 4
size_kb: 13749
language: "Python"
created: "2026-10-27"
updated: "2026-10-31"
archived: false
license: "Apache-2.0"
commits_30d: 12
commits_90d: 12
commit_cadence: "weekly"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/malariadx/status/2120128085374951521"]
fetched_at: "2026-11-11T06:16:24.804050+00:00"
---

# Anima Reference Adapter for ComfyUI

## 出来ること

- Animaに参照画像を与え、プロンプトで指定した場面に合わせてキャラクターの外見や画風を保つことを目指す。参照画像2枚を並べて、1枚の画像に2キャラクターを出す手順もREADMEに記載されている。これらは作者の説明であり、独立した実測結果ではない。

## 目的・背景

- キャラクター名や作者タグ、服装タグに頼らず、参照画像と場面のプロンプトでオリジナルキャラクターを生成する用途として説明されている。READMEによると開発は資金不足で一時停止しており、別々のキャラクター参照と画風参照の機能は公開されていない。

## 依存関係

- ComfyUI、Anima base v1.0、Qwen3-0.6B text encoder、Qwen-Image VAEが必要。READMEでは追加のカスタムノードは不要としている。初回利用時に183 MBのアダプター重みをHugging Faceからダウンロードする。コードはApache-2.0、重みはCircleStone Non-Commercialライセンスと記載されている。

## 実行条件

- READMEの推奨設定はAnima base v1.0。標準のAnimaワークフローに「Anima Ref Adapter」ノードを追加し、モデル、VAE、参照画像を接続してサンプラーへ渡す。参照画像はref_megapixels（既定値1.0）に合わせてアスペクト比を保ってリサイズされる。

## 最短手順

- 1. ComfyUI/custom_nodesで `git clone https://github.com/ArcAnima/ComfyUI-Anima-Ref-Adapter.git` を実行する。2. Anima base v1.0、Qwen3-0.6B text encoder、Qwen-Image VAEを用意する。3. ComfyUIを再起動し、リポジトリ内の `workflows/anima_ref_adapter.json` を開く。4. 参照画像と場面を説明するプロンプトを設定して実行する。初回実行時に重みが取得される。

## 変更履歴

- 2026-11-11: 初回登録
