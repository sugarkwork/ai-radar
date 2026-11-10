---
repo: "andyhuo520/vibe-knowledge"
name: "vibe-knowledge"
genre: "video-gen"
url: "https://github.com/andyhuo520/vibe-knowledge"
license: "MIT"
stars: 613
forks: 92
open_issues: 0
size_kb: 50510
language: "JavaScript"
created: "2026-10-28"
updated: "2026-10-28"
archived: false
commits_30d: 3
commits_90d: 3
commit_cadence: "monthly"
last_release: "v1.0.0"
flags: ["unverified"]
risk_notes: "READMEと公開リリースの記載を確認。コードの実行、サンプルの視聴、出典の正確性、画質、処理時間、質検の検出精度、OS別の動作、外部サービスの現行料金は未検証。公開リリースの一覧で最新版タグを確認し、正確な公開日時は未確認。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/ganfanren_ai/status/2117893354654769438"]
fetched_at: "2026-11-10T10:56:31+00:00"
---

# vibe-knowledge — 出典付き解説動画を制作するClaude Codeスキル

## 出来ること

- 題材の調査、出典表と台本の作成、ナレーション、コードによる1080p60の逐次フレーム描画、品質チェック、公開用素材の準備を対話で進める。READMEはOCRによる照合、音量、フレームの静止、BGMの検査を記載している。

## 目的・背景

- 数字や人名などの出典をfacts.mdにまとめ、台本と絵コンテを生成前に確認する構成。GitHub Releasesでは同じ題材の基本版・拡張版・比較用動画が配布されている。

## 依存関係

- Claude Codeにvibe-knowledgeとai-teardownの両スキルを導入する。描画用のPython環境にnumpy、scipy、Pillow、PlaywrightとChromium Headless Shellを入れ、FFmpegを用意する。音声はXiaomi MiMoを使い、OCR工程はmacOS Visionとswiftcを使う構成。

## 実行条件

- 基本版はRenoiseのクレジット消費が0。拡張版はRenoise MCPで一部の素材を生成し、README上は見積もり提示と利用者の承認を経て実行する。MiMoの利用にはAPIキーが必要。
- NOTICEによるとMITの対象はコードと文書。サンプルはデモ用で、同梱BGMは本ツールで制作した動画に使えるが単体での再配布・販売は不可。既定音声はMiMoで作成した合成音声で、音声クローンには本人の音声か明示的に許可された音声を使う。

## 最短手順

- READMEの導入手順に沿って両スキルを ~/.claude/skills/ に配置し、CINE_PYとMiMoの認証を設定する。Claude Codeで『基本版で、ベンフォードの法則を解説する知識短編を作って』と依頼し、出典表、台本、絵コンテを確認してから生成を承認する。

## 変更履歴

- 2026-11-10: 初回登録
