---
name: "Speakr"
genre: "agent-framework"
url: "https://github.com/murtaza-nasir/speakr"
repo: "murtaza-nasir/speakr"
license: "AGPL-3.0"
stars: 4172
language: "Python"
created: "2025-05-05"
updated: "2026-11-13"
forks: 359
open_issues: 7
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 131489
archived: false
flags: ["unverified"]
risk_notes: "料金はREADMEで確認できない。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/ruyi3699/status/2118768879308505192"]
fetched_at: "2026-11-14T04:11:35.668455+00:00"
---

# Speakr

## 出来ること

- 音声を録音またはファイルから取り込み、文字起こし、要約、アクション項目や予定の抽出、録音単位のチャット、録音ライブラリ横断の意味検索・チャットを行う。フォルダー、タグ、保持ポリシー、共有、ユーザー・グループ管理、REST API、署名付きWebhook、テンプレート出力を備えるとREADMEに記載。WhisperX、OpenAI、Mistral / Voxtral、AssemblyAI、Tencent Cloud ASR、OpenASR、Alibaba FunASR、カスタムASR Webサービスに対応すると説明されている。

## 目的・背景

- プライバシーを重視する個人やグループ向けに、自身のインフラ上で音声記録を整理された検索可能なノートへ変換するセルフホスト型プラットフォームとして紹介されている。

## 依存関係

- 文字起こしには利用者が選ぶASRエンジンを接続する。WhisperXはセルフホスト型の推奨エンジンで、話者機能の利用に必要とREADMEに記載。OpenAI等の外部サービス利用条件や各エンジンの追加依存関係は、添付READMEでは特定されていない。

## 実行条件

- READMEは自前のインフラで動作するセルフホスト型として説明し、Docker Hubへの案内を掲載している。具体的な最小システム要件、各バックエンドの設定条件、料金は添付READMEの範囲では確認できない。

## 最短手順

- READMEが案内する Quick Start（https://murtaza-nasir.github.io/speakr/getting-started）を参照し、自身のインフラにSpeakrを構成して利用するASRエンジンを設定する。録音はアプリ内、対応入力デバイス、または既存音声ファイルから取り込める。

## 変更履歴

- 2026-11-14: 初回登録
