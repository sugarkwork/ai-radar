---
type: "repo"
name: "umlx5h/LLPlayer"
genre: "tts-audio"
url: "https://github.com/umlx5h/LLPlayer"
author: "umlx5h"
source_post: "https://x.com/awe0_io/status/2118667207597322379"
sources: ["https://x.com/awe0_io/status/2118667207597322379?a=xWZXv2zM0qxlAXVijYU&s=46", "https://x.com/awe0_io/status/2118667207597322379", "https://github.com/umlx5h/LLPlayer", "https://api.github.com/repos/umlx5h/LLPlayer", "https://raw.githubusercontent.com/umlx5h/LLPlayer/main/README.md", "https://api.github.com/repos/umlx5h/LLPlayer/releases/latest"]
first_seen: "2026-11-06"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "Beta版で設定互換性が変わる可能性。ASR/OCRはローカルだが翻訳はエンジンによってクラウド送信・API費用が生じる。 当方でインストール・推論・生成・ベンチ再現はしていない。"
repo: "umlx5h/LLPlayer"
license: "GPL-3.0"
language: "C#"
created: "2025-01-31"
updated: "2026-11-05"
stars: 4620
forks: 290
open_issues: 61
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
size_kb: 158932
archived: false
fetched_at: "2026-11-09T21:43:44Z"
last_release: "v0.3.0"
last_release_at: "2026-04-19"
---

# umlx5h/LLPlayer

## 出来ること

二重字幕、Whisper ASR、自動翻訳、ビットマップ字幕のOCR、単語検索を統合した語学学習向け動画プレイヤー。

## 目的・背景

紹介対象は `umlx5h/LLPlayer`。対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:24.526230+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

## 依存関係

Windows 10 x64 1903以降またはWindows 11 x64、.NET Desktop Runtime 10、Visual C++ 2022以降。whisper.cpp/faster-whisper、Tesseract/Microsoft OCR、翻訳エンジンを選択。

## 実行条件

Beta版で設定互換性が変わる可能性。ASR/OCRはローカルだが翻訳はエンジンによってクラウド送信・API費用が生じる。

コード本体の許諾と、基底モデル・同梱素材・外部API・音声/人物等の利用条件は別に確認する。

## 最短手順

1. [公式README](https://github.com/umlx5h/LLPlayer#readme)で対応版と依存を確認する。
2. 上記の対象固有条件を満たす環境を用意し、配布元の手順を選ぶ。
3. 外部サービスの料金・認証・データ送信とライセンスを確認してから導入する。

本調査では導入・ビルド・起動をしていないため、成功済みのコマンドとしては掲載しない。

## 出典

- @awe0_io: https://x.com/awe0_io/status/2118667207597322379
- 対象資料: https://github.com/umlx5h/LLPlayer
- 参照: https://api.github.com/repos/umlx5h/LLPlayer
- 参照: https://raw.githubusercontent.com/umlx5h/LLPlayer/main/README.md
- 参照: https://api.github.com/repos/umlx5h/LLPlayer/releases/latest

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
