---
repo: calesthio/OpenMontage
name: OpenMontage
genre: video-gen
url: https://github.com/calesthio/OpenMontage
license: AGPL-3.0
stars: 75779
language: Python
created: 2026-03-29
updated: 2026-10-28
added: 2026-11-03
sources:
  - https://x.com/its_ronc/status/2117523925618041112
forks: 10024
open_issues: 437
commits_30d: 45
commits_90d: 100
commit_cadence: daily
size_kb: 77481
archived: false
fetched_at: "2026-11-03T15:43:07Z"
---

# OpenMontage

## 出来ること

- コーディングエージェント（Claude Code / Cursor / Copilot / Windsurf / Codex）を動画制作スタジオ化する。企画・リサーチ・台本・素材生成・編集・書き出しまでをエージェントが回す。
- パイプライン表には 11 種: Animated Explainer / Animation / Avatar Spokesperson / Cinematic / Clip Factory / Documentary Montage / Hybrid / Localization & Dub / Podcast Repurpose / Screen Demo / Talking Head（リポジトリ説明文は「12 pipelines」と記載）。
- 「静止画を動かして動画と呼ぶ」のではなく、**実写素材ベースの Documentary Montage** を持つ。Pexels / Archive.org / NASA / Wikimedia / Unsplash を CLIP で索引化したコーパスから実際の動画クリップを引いて編集する。
- 制作ツール 100 種以上、プロバイダ統合 60 種以上、エージェント向けスキル／制作知識ファイル 700 以上を同梱。
- パイプラインは YAML マニフェスト、各工程の進め方は Markdown スキルとして書かれており、オーケストレータのコードは存在しない（エージェント自身がオーケストレータ）。
- 事前に 15〜25 件の Web 検索を回して台本の根拠を取る、コスト見積もりと上限設定、pre-compose 検証ゲート、ffprobe＋フレーム抽出によるレンダ後セルフレビューまで含む。

## 目的・背景

calesthio（@calesthioailabs）による agentic 動画制作システム。2026-03-29 作成、約 76MB、Python、AGPL-3.0。GitHub Trending 1 位を取ったと README に記載。README には実際にこのパイプラインで作った短編が並び、概算コストも書かれている（例: 60 秒アニメで $1.33、50 秒縦型で約 $4、7 ワールドのショーケースで約 $5）。

## 依存関係

- Python 3.10+、FFmpeg、Node.js 18+。
- 何らかの AI コーディングアシスタント（Claude Code / Cursor / Copilot / Windsurf / Codex のいずれか）。
- API キーは**すべて任意**。`FAL_KEY`（FLUX 画像 + Veo / Kling / MiniMax 動画）、`ATLASCLOUD_API_KEY`（Seedream / Kling / Seedance / Hailuo）ほか、`.env` に足した分だけツールが増える。
- キーゼロでも動く範囲: ナレーションは Piper TTS（オフライン）、素材は Archive.org / NASA / Wikimedia / Pexels / Unsplash / Pixabay、合成は Remotion（React）と HyperFrames（HTML/CSS/GSAP）。
- クラウド動画生成モデルを使う場合は各プロバイダのアカウントと課金が別途必要。

## 実行条件

- OS は README に限定記載なし（Python / FFmpeg / Node が動けばよい）。GPU は任意のクラウド生成を使う場合は不要、ローカルモデルを使う場合は別途必要。
- ディスク: リポジトリは約 76MB。生成素材とレンダ中間ファイルが別途積み上がる。
- クラウド生成を使う場合、生成時間と従量課金はプロバイダ次第。README はコスト上限・承認しきい値を設定できるとしている。
- `make setup` が前提とするシェル環境（Windows での動作可否）は未確認。

## 最短手順

```bash
git clone https://github.com/calesthio/OpenMontage.git
cd OpenMontage
make setup                    # 依存インストール
cp .env.example .env          # 任意: FAL_KEY などを追記（無くても動く）
# コーディングエージェントをこのディレクトリで開き、作りたい動画を自然言語で指示
```

## 変更履歴

- 2026-11-03: 初回登録（star 75,755 / pushed 2026-10-28）
