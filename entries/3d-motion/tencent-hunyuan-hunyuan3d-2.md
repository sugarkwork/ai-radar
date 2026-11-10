---
repo: "Tencent-Hunyuan/Hunyuan3D-2"
name: "Hunyuan3D-2"
genre: "3d-motion"
url: "https://github.com/Tencent-Hunyuan/Hunyuan3D-2"
license: "unknown"
stars: 15376
forks: 1594
open_issues: 254
size_kb: 83148
language: "Python"
created: "2025-01-21"
updated: "2025-10-28"
archived: false
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
flags: ["unverified"]
risk_notes: "GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/Y0urDumble/status/2117739253748937033"]
fetched_at: "2026-11-10T10:28:18+00:00"
---

# Hunyuan3D-2で単一画像から3Dメッシュを生成

## 出来ること

- 画像から形状メッシュを生成し、GLBやOBJに書き出せる。生成したメッシュや手持ちのメッシュには、別段階でテクスチャを合成できる。

## 目的・背景

- Hunyuan3D-DiTで形状を生成し、Hunyuan3D-Paintでテクスチャを合成する。開発元のREADME掲載表では、CMMD・FID_CLIP・FID・CLIP-scoreの4指標で掲載された比較対象を上回った。

## 依存関係

- PyTorchとrequirements.txtの依存パッケージ、モデル重みが必要。テクスチャ生成のセットアップにはcustom_rasterizerとdifferentiable_rendererのビルドが含まれる。

## 実行条件

- READMEの公称VRAMは形状生成で6 GB、形状とテクスチャの生成で合計16 GB。
- リポジトリのLICENSEはTencent独自のCommunity License。EU・英国・韓国は適用地域から除外される。利用・配布には同ライセンスの条件が適用される。料金と運用コストは未確認。

## 最短手順

- PyTorchを用意し、READMEの手順で依存パッケージとリポジトリ本体をインストールする。形状生成だけならテクスチャ用拡張のビルドを省ける。
- AIエージェントから呼ぶには、同一マシンで python api_server.py --host 127.0.0.1 --port 8080 を起動し、HTTPツールから /generate にPOSTする。入力画像のBase64文字列をJSONのimageフィールドに入れ、応答をGLBとして保存する。READMEの例はテクスチャなしの形状生成。

## 変更履歴

- 2026-11-10: 初回登録
