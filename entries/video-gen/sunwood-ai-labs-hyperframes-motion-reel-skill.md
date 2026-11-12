---
name: "HyperFrames Motion Reel Skill"
genre: "video-gen"
url: "https://github.com/Sunwood-ai-labs/hyperframes-motion-reel-skill"
repo: "Sunwood-ai-labs/hyperframes-motion-reel-skill"
stars: 185
forks: 26
open_issues: 0
size_kb: 54
language: "unknown"
created: "2026-09-29"
updated: "2026-09-29"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 6
commit_cadence: "monthly"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-12"
first_seen: "2026-11-12"
sources: ["https://x.com/PromptLabCN/status/2120750742785171596"]
fetched_at: "2026-11-12T06:13:06.021483+00:00"
---

# HyperFrames Motion Reel Skill

## 出来ること

- 短いテーマと任意の画像・音声から、デザインシステム、ビートごとのタイムライン、コード生成音声を含むHyperFrames動画を制作するClaude Codeスキル。READMEは、GSAPとCanvas/SVGを使ったアニメーション構成、決定的レンダリング、MP4出力までを機能として説明している。出典: https://github.com/Sunwood-ai-labs/hyperframes-motion-reel-skill

## 目的・背景

- READMEによると、Remotion版のモーションリール制作をHyperFramesへ移植し、Apache-2.0および無料ツールを使う構成としている。商用利用に関する記述はREADME上の説明であり、独立したライセンス調査結果ではない。出典: https://github.com/Sunwood-ai-labs/hyperframes-motion-reel-skill

## 依存関係

- README記載の要件は、Node.js（現行LTS）とnpx、HyperFramesレンダラー用のGoogle Chrome、最終確認用のffmpegおよびffprobe。ビルド時にHyperFramesの複数のドメインスキルを併せてインストールする手順も記載されている。出典: https://github.com/Sunwood-ai-labs/hyperframes-motion-reel-skill

## 実行条件

- READMEの既定値は15秒、60 FPS、120 BPM、1920×1080、MP4/H.264。プロンプトで指定した尺、BPM、解像度、アスペクト比、素材は既定値を上書きする。WindowsではPowerShell向けのインストール例が掲載されている。出典: https://github.com/Sunwood-ai-labs/hyperframes-motion-reel-skill

## 最短手順

- READMEのQuick Startに従い、リポジトリをClaude Codeのskillsディレクトリへ配置し、必要要件とHyperFramesドメインスキルを用意する。続いて「/hyperframes-motion-reel <テーマ>」形式でテーマを指定する。README記載の制作フローは、コンセプト、デザインとタイムライン作成、実装、lint/check、スナップショット確認、レンダリング、ffprobe/ffmpegによるスポットチェック。出典: https://github.com/Sunwood-ai-labs/hyperframes-motion-reel-skill

## 変更履歴

- 2026-11-12: 初回登録
