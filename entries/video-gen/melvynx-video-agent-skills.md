---
name: "video-agent-skills"
genre: "video-gen"
url: "https://github.com/Melvynx/video-agent-skills"
repo: "Melvynx/video-agent-skills"
license: "MIT"
stars: 158
language: "JavaScript"
created: "2026-10-09"
updated: "2026-11-06"
forks: 39
open_issues: 1
commits_30d: 13
commit_cadence: "weekly"
commits_90d: 26
size_kb: 9366
archived: false
flags: ["unverified"]
risk_notes: "Tregによる一部機能は有料と記載されていますが、料金はREADMEに明記された範囲に限られます。"
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/eva_love_1999/status/2119028590423802349"]
fetched_at: "2026-11-15T14:13:11.551620+00:00"
---

# video-agent-skills

## 出来ること

- Claude Code向けの動画制作スキル群。READMEでは、動画の編集、スクリプト作成、競合動画の分析、翻訳、画像生成、YouTube・Instagram・TikTokへの公開などを説明しています。`short-editing`は素材から字幕付き動画、字幕ファイル、投稿文を作成すると記載されています。

## 目的・背景

- 短尺動画やYouTube動画の制作工程を、スキルを通じて支援するリポジトリです。READMEによると、スキルはClaudeに作業方法を指示し、`short-editing`にはレンダーエンジンが含まれます。

## 依存関係

- README記載の編集エンジンはNode、Chrome、ffmpegを使用し、音声認識にwhisper.cppを使用します。ElevenLabsキーは翻訳に、Codexは画像生成に任意で接続できます。TregはInstagram分析や各プラットフォームへの公開に任意で利用されます。

## 実行条件

- Claude Codeをプロジェクトフォルダーで利用する手順が記載されています。編集エンジンはmacOS、Windows、Linuxで動作するとREADMEにあります。`/studio-setup`でツール確認と編集環境の準備を行う手順が案内されています。

## 最短手順

- プロジェクトフォルダーで `npx skills add Melvynx/video-agent-skills -a claude-code` を実行し、Claude Codeで `/studio-setup` を実行します。動画素材を `video-agent/takes/` に置いて `/short-editing` を実行する手順がREADMEに記載されています。

## 変更履歴

- 2026-11-15: 初回登録
