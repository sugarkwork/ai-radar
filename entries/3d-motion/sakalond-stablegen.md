---
repo: "sakalond/StableGen"
name: "StableGen"
genre: 3d-motion
url: "https://github.com/sakalond/StableGen"
license: "GPL-3.0"
stars: 1632
language: "Python"
created: "2025-05-15"
updated: "2026-11-04"
added: "2026-11-03"
first_seen: "2026-11-03"
sources: []
flags: []
risk_notes: ""
forks: 163
open_issues: 7
commits_30d: 100
commit_cadence: "daily"
size_kb: 491148
archived: false
commits_90d: 100
fetched_at: "2026-11-09T21:31:38Z"
last_release: "v0.5.0"
last_release_at: "2026-11-04"
---

# StableGen

## 出来ること

- Blender のアドオンとして、メッシュやシーン全体に Diffusion モデルでテクスチャを貼る。UV を切って手で描く工程を置き換える。
- シーン内のカメラからガイド画像をレンダリングし、同一 PC またはネットワーク上の ComfyUI サーバーに投げて、投影（projection）でテクスチャに戻す。
- テクスチャの一部分だけを指示して描き直せる。PBR マテリアル（法線・ラフネス等）の生成にも対応。
- プロンプトまたは画像から新しいメッシュを生成し、自動リギングまで通せる（パッケージ 8 と 14）。
- 生成したメッシュを LATO.2 でローポリのトポロジに作り直せる（パッケージ 18）。TRELLIS.2 のメッシュが内側に残す閉じた殻を取り除く Make Solid も使える。
- ゲームエンジン向けの書き出し。

## 目的・背景

「1プロンプトからリグ付きアセットまで」を Blender 内で完結させるアドオン。生成そのものは ComfyUI 側のモデル（SDXL、Qwen Image 2.1 など）に任せ、Blender 側はガイド画像の作成と投影を担当する分担設計。

## 依存関係

- Blender 4.2〜4.5、または 5.1 以降（**Blender 5.0 は非対応**と明記）。
- ComfyUI サーバー。v0.5.0 からは StableGen のパネル（ComfyUI setup 画面）から導入・起動できる。同梱の `installer.py` も引き続き使え、カスタムノードとモデルを入れる（パッケージ 3: SDXL、13: Qwen Image 2.1、8: メッシュ生成、14: 自動リギング、15〜17: 実験的アーキテクチャ、18: LATO.2 のローポリ化）。TRELLIS.2 は ComfyUI 0.42 以降のネイティブノードで動き、旧 `ComfyUI-TRELLIS2` ノードは不要になった。
- Windows / Linux / macOS（Apple Silicon）。アドオンの ZIP は Releases から。

## 実行条件

- NVIDIA GPU 推奨。SDXL で約 8GB、Qwen Image で 16GB 以上の VRAM が必要と README に記載。
- モデル用に 10GB〜50GB 超のディスク。StableGen 自身の ComfyUI を入れる場合は別に約5GB。
- オブジェクト相対の投影を使う場合は Blender 5.1 以降。
- Blender 側で Output Directory と Server Address（既定 `127.0.0.1:8188`）を設定し、Preferences → System → Network の「Allow Online Access」を有効にする必要がある。
- GPL-3.0。アドオンを改変して配布する場合は同一ライセンスが及ぶ。

## 最短手順

```bash
# 1) ComfyUI を用意。v0.5.0 からはパネルの「ComfyUI setup」から導入・起動できる
#    （既存の ComfyUI を指定するか、別マシンのサーバーに接続する選択肢もある）
# 2) モデルを導入（パネルから、またはリモート側で installer.py を実行）
python installer.py /path/to/ComfyUI
# 3) Releases からアドオン ZIP を取得 → Blender: Edit > Preferences > Get Extensions > Install from Disk
# 4) アドオン設定で Output Directory と Server Address を指定
```

## 変更履歴

- 2026-11-03: 初回登録（★1,426 / pushed 2026-11-02 / GPL-3.0 / v0.4.0）
- 2026-11-04: パネルからの ComfyUI 導入と LATO.2 によるローポリ化・Make Solid を追記（v0.5.0）
