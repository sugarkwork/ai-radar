---
repo: "OpenMontageInc/OpenMontage"
name: "OpenMontage"
genre: "video-gen"
url: "https://github.com/OpenMontageInc/OpenMontage"
license: "AGPL-3.0"
stars: 79249
language: "Python"
created: "2026-03-29"
updated: "2026-11-09"
forks: 10586
open_issues: 333
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 78414
archived: false
flags: ["unverified"]
risk_notes: "最新リリースのタグと公開日時は未確認。制作パイプラインの動作、作例の映像品質・費用の再現性、素材ごとの利用条件は独立に検証していない。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/0xGky/status/2119585510008213749"]
fetched_at: "2026-11-10T08:43:53+00:00"
---

# OpenMontage — コーディングエージェントで台本から動画を制作

## 出来ること

- 自然言語の指示から、台本、素材調達、音声、字幕、合成を段階的に進める。参考動画を渡すと、文字起こし、テンポ、場面、キーフレーム、スタイルを分析して制作案を提示する流れがREADMEに記載されている。

## 目的・背景

- パイプライン定義、工程別スキル、ツールレジストリを使い、コーディングエージェントが複数の制作ツールを扱えるようにする。開発元は、Kling v3の映像、Google Chirp3-HDのナレーション、ロイヤリティフリーのピアノ曲、Remotionによる合成を使った60秒の作例について、総費用1.33米ドルと記載している。

## 依存関係

- Python 3.10以上、FFmpeg、README指定の修正済みNode.js、およびClaude CodeやCursorなどのコーディングエージェント。音声にはPiper TTS、合成にはRemotionまたはHyperFramesを利用できる。

## 実行条件

- READMEには有料の生成APIキーを使わず、Piper TTSや公開アーカイブ素材で制作する経路がある。外部サービスを使う構成では、選んだサービスのAPIキーと料金が適用される。リポジトリのライセンスはAGPL-3.0で、取り込む素材の利用条件は配布元ごとに異なる。

## 最短手順

- 公式リポジトリを取得し、前提ソフトをそろえてプロジェクト直下で `make setup` を実行する。Windows PowerShell向けの手順もREADMEにある。
- Claude CodeやCursorでプロジェクトを開き、『ニューラルネットワークが学習する仕組みを60秒のアニメーションで説明して』のように制作を依頼する。

## 変更履歴

- 2026-11-10: 初回登録
