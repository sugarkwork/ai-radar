---
repo: "rany2/edge-tts"
name: "edge-tts"
genre: "tts-audio"
url: "https://github.com/rany2/edge-tts"
last_release: "7.3.1"
flags: ["unverified"]
risk_notes: "音声合成は実行しておらず、現時点での接続可否、音声品質、字幕の同期精度と単語単位での出力条件は未検証。サービスの料金・利用上限・生成音声の商用利用条件、最新リリースの公開年を含む正確な日時は未確認。 GitHub APIでライセンスを確認できていません。"
stars: 12499
forks: 1179
open_issues: 9
size_kb: 2197
language: "Python"
created: "2021-05-10"
updated: "2026-10-14"
archived: false
license: "unknown"
commits_30d: 8
commits_90d: 8
commit_cadence: "weekly"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/Y0urDumble/status/2117396633889427646"]
fetched_at: "2026-11-10T08:50:46+00:00"
---

# edge-ttsでナレーションとSRT字幕をまとめて生成する

## 出来ること

- テキストからMP3音声とタイムコード付きSRT字幕を生成する。音声の種類、読み上げ速度、音量、ピッチを指定できる。

## 目的・背景

- Microsoft Edgeのオンライン音声合成サービスをPythonやCLIから呼び出すクライアント。CLIの実装は、受信した音声データを保存し、単語または文の境界イベントをSRTに変換する。

## 依存関係

- 公式のパッケージ設定ではPython 3.7以上と、aiohttp、certifi、tabulate、typing-extensionsが必要。READMEによると、Windows以外でedge-playbackを使う場合はmpvが必要。

## 実行条件

- 入力テキストはオンラインサービスへ送られるため、ネットワーク接続が必要。パッケージ設定ではコードのライセンスをLGPLv3と分類している。サービスの料金・利用上限や生成音声の商用利用条件は未確認。

## 最短手順

- `pip install edge-tts` でインストールし、`edge-tts --list-voices` で使用する音声名を確認する。
- `edge-tts --text "こんにちは" --voice <音声名> --write-media narration.mp3 --write-subtitles narration.srt` の `<音声名>` を一覧から選んだ値に置き換えて実行する。
- シェル実行権限のあるAIエージェントから呼ぶ場合は、台本をUTF-8で `script.txt` に保存し、`edge-tts --file script.txt --voice <音声名> --write-media narration.mp3 --write-subtitles narration.srt` を呼ぶ。生成したMP3とSRTを動画編集工程に渡す。

## 変更履歴

- 2026-11-10: 初回登録
