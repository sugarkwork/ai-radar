---
repo: "deepbeepmeep/WanGP"
name: "WanGP"
genre: video-gen
url: "https://github.com/deepbeepmeep/WanGP"
license: "WanGP Community License 2.0"
stars: 11441
language: "Python"
created: "2025-02-27"
updated: 2026-11-06
added: "2026-11-03"
first_seen: "2026-11-03"
sources: []
flags: []
risk_notes: ""
forks: 1855
open_issues: 1379
commits_30d: 63
commit_cadence: daily
size_kb: 108084
archived: false
commits_90d: 100
fetched_at: "2026-11-06T22:52:24Z"
last_release: manager-v0.1.14
last_release_at: 2026-11-03
---

# WanGP

## 出来ること

- 動画・画像・音声/音声合成・3D 生成を1つの Web UI にまとめた実行環境。1モデル1アプリを入れ分けずに済む。
- 対応モデルが広い: 動画は Wan 2.1/2.2、MiniMax H3、LTX-2/2.3/2.5、HunyuanVideo 1/1.5、LongCat、Kandinsky など。画像は Flux 1/2、Qwen Image、Qwen Image Edit、Krea 2、Z-Image など。音声は IndexTTS2、Fish Audio、MOSS-TTS、ACE-Step、Stable Audio など。3D は Hunyuan3D 2.1、TRELLIS.2、TripoSG、TripoSplat など。
- **Viggle Remake**（v19.20）: 元動画のモーション・カメラ・タイミング・音声を保ったまま、人物の入れ替え（Swap）やオブジェクト・背景・天候・照明の変更（Edit）ができる。Showrunner に任せると、ショット分割・参照フレームの作成と編集・検証まで自動で進む。
- **Showrunner Draft / Final**: 480p の下書きで画・構図・尺を確かめ、選んだテイクのプロンプト・シード・参照画像を最終解像度へ引き継げる。
- **アップスケーラの追加**: RelayVSR（実写・生成物向けの高速アップスケーラ。x4 モデルと LightX2V の x2、既定は x2 まで）、高速化した FlashVSR、顔の仕上げ TaoMate-FVSR（最大5人）を選べる。
- 「Deepy Prime」というエージェント機能があり、アイデアから生成までを対話で進められる。**Showrunner** はブリーフからショット割り・キャスティング・撮影・検品・編集まで進め、最長10分の完成尺（ミュージックビデオ、短編、広告、予告、絵本）にまとめる。声を動画モデル（MiniMax H3）自身に喋らせる設定、8〜15秒などのショット長指定、言語モデルなしで1ショットを描画する Render now を持つ。
- ギャラリー閲覧、モーションデザイナー、モデル管理、CivitAI ブラウザなどのプラグインを同梱。
- ハードウェアを見て適切なモデルファイルを自動判別してダウンロードする（`--offline` で全ダウンロードを止め、不足ファイルを報告するモードもある）。
- 省メモリ設計を明示: 一部モデルは 4GB VRAM から、テキスト生成系は RAM 32GB 級の Q4 Experts 版を推奨、と README に記載。

## 目的・背景

「GPU が小さい環境でもオープンソース生成モデルを使えるようにする」ことを掲げる統合アプリ。旧名 Wan2GP。モデルごとに環境を作り直す代わりに、量子化・オフロード・カーネル切替をアプリ側で吸収する構成。

## 依存関係

- Python と PyTorch。README の手動手順は GPU 世代で分岐する（RTX 20xx〜50xx: Python 3.11.14 + torch 2.10 cu130 / GTX 10xx: Python 3.10.9 + torch 2.7.1 cu128）。
- Windows は Triton のバージョンを GPU と PyTorch に合わせて個別に導入する。
- `scripts/install.sh` / `install.bat` がインストーラ、`scripts/run.sh` / `run.bat` が起動。Pinokio、サードパーティ製デスクトップランチャー、公式の WanGP Manager（Windows、実験的）も選べる。
- AMD は RDNA 2〜4 向けの手順を docs に分けて用意。

## 実行条件

- NVIDIA（GTX 10xx〜RTX 50xx）または AMD（ROCm）の GPU が前提。CPU 実行の記述はない。
- モデルごとの必要 VRAM・ディスク量は docs/MODELS.md を参照。リポジトリサイズは約 106MB だが、モデル weights は別途ダウンロードされる。
- **ライセンスは OSI 認証のオープンソースライセンスではない**（`WanGP Community License 2.0`、GitHub API 上も NOASSERTION）。商用利用や再配布の条件は LICENSE 本文の確認が必要。各モデルにも固有ライセンスがある。
- Issue が 1,369 件開いており、トラブル時は既存 Issue の検索が前提。

## 最短手順

```bash
git clone https://github.com/deepbeepmeep/WanGP.git
cd WanGP
# Windows: scripts\install.bat → scripts\run.bat
bash scripts/install.sh
bash scripts/run.sh
```

## 変更履歴

- 2026-11-03: 初回登録（★11,362 / pushed 2026-11-03 / WanGP Community License 2.0）
- 2026-11-04: Showrunner の音声・ショット長・手動描画の設定を追記（bd1ff59）
- 2026-11-06: Viggle Remake と Showrunner Draft/Final、RelayVSR・TaoMate-FVSR・NitroFusion2 Z-Image Turbo を追記（v19.20）
