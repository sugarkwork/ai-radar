---
type: "repo"
repo: "7err4/fumika"
name: "Fumika — ローカル漫画・画像・LoRA学習スタジオ"
genre: "image-generation"
url: "https://github.com/7err4/fumika"
author: "7err4"
license: "NOASSERTION"
language: "Python"
stars: 6
forks: 3
open_issues: 1
created: "2026-10-21"
updated: "2026-10-25"
commits_30d: 2
commits_90d: 2
commit_cadence: "monthly"
size_kb: 10228
archived: false
risk_notes: "コードはApache-2.0だがCommons Clause付き（ソフトウェア自体の販売・ホスト有償サービスを制限）。OSIオープンソースではなくソース公開。ComfyUIノードパックはGPL-3.0。モデルは各配布元のライセンスに従う。出力物（ページ/漫画/アセット/LoRA）はFumikaのライセンス対象外。名称・ロゴ・キャラクターはAll rights reserved。当方未インストール。 当方でインストール・動作・性能の実行検証はしていない。"
sources: ["https://x.com/dextune/status/2119301388857745593", "https://github.com/7err4/fumika", "https://github.com/7err4/fumika/blob/master/README.md", "https://github.com/7err4/fumika/blob/master/LICENSE"]
added: "2026-11-09"
first_seen: "2026-11-09"
source_post: "https://x.com/dextune/status/2119301388857745593"
fetched_at: "2026-11-09T21:38:45Z"
flags: ["unverified"]
last_release: "v0.1.1"
last_release_at: "2026-10-25"
---

# Fumika — ローカル漫画・画像・LoRA学習スタジオ

## 出来ること

短編を漫画ページ（吹き出し付き）に変換、画像生成、LoRA学習を1つのGUIで行う。バンドルされたComfyUI（独自Python、システムPythonに干渉しない）をエンジンとし、MCPサーバーでAIエージェントから操作可能。

## 目的・背景

Windows/Linux（NVIDIA）向けのローカル制作環境。プラグイン形式で機能を選択し、必要なモデルのみダウンロードする。

## プラグイン一覧

- MOSS Doujin: 物語→漫画ページ（3案から最も読みやすい1案を採用）
- MOSS LoRA Trainer: キャラクター/スタイルLoRA学習
- Slider Trainer: Anima用スライダーLoRA（-2〜+2）
- SDXL LoRA Trainer: SDXL/Illustrious/Pony用LoRA・LyCORIS・embedding
- Anima LoRA Trainer: Anima 1.0/2.9B/3.8B用LoRA学習
- Image Studio: 単体画像生成（txt2img/img2img/inpaint/upscale）
- Asset Studio: 表情セット/衣装/ターンテーブル/プロフィール/アイテム/ちび/ピクセルスプライト

## 依存関係

ComfyUI Windows portable（Windows）またはuvで構築したComfyUI+Python 3.13+PyTorch CUDA 13（Linux）。Git必須。各トレーナーは必要ツールをcloneする。

## 実行条件

Windows 10/11 64bit または Linux x86-64。NVIDIA GPU必須。macOS非対応。VRAM 24GB推奨、int8モデルで smaller cards も可。

## 最短手順

Windows: setup.exe（管理者権限不要）。Linux: AppImageまたは.deb。初回起動でプラグインとモデルを選択・ダウンロード。

## 注意点

コードはApache-2.0だがCommons Clause付き（ソフトウェア自体の販売・ホスト有償サービスを制限）。OSIオープンソースではなくソース公開。ComfyUIノードパックはGPL-3.0。モデルは各配布元のライセンスに従う。出力物（ページ/漫画/アセット/LoRA）はFumikaのライセンス対象外。名称・ロゴ・キャラクターはAll rights reserved。当方未インストール。

## 変更履歴

- 2026-11-09: 初回収録。公式資料を確認し、未実行の範囲を明記。
