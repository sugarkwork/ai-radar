---
name: "speech.cpp"
genre: "tts-audio"
url: "https://github.com/nyosegawa/speech.cpp"
repo: "nyosegawa/speech.cpp"
stars: 406
forks: 28
open_issues: 12
size_kb: 5864
language: "C++"
created: "2026-09-29"
updated: "2026-11-14"
archived: false
license: "MIT"
commits_30d: 52
commits_90d: 100
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/gyakuse/status/2116928286286901601"]
fetched_at: "2026-11-14T02:08:51.337043+00:00"
---

# speech.cpp

## 出来ること

- 音声合成、録音音声の文字起こし、発話区間検出、話者ダイアライゼーション、ノイズ除去、マイクのライブ文字起こしを提供する。HTTP経由でOpenAIの音声APIおよびRealtime文字起こしを提供する機能もREADMEに記載されている。出典: https://github.com/nyosegawa/speech.cpp

## 目的・背景

- 音声関連の機能を、ggmlを使うC++の単一コマンド `speech` と共有ライブラリ `libspeech`、共通C APIで提供する。READMEではCPU、Metal、Vulkanでの実行を説明している。出典: https://github.com/nyosegawa/speech.cpp

## 依存関係

- READMEに記載の基盤はggml。初回利用時にモデルを名前で指定してHugging Faceから取得する。モデルごとの追加依存関係はREADMEの提示範囲では確認できない。出典: https://github.com/nyosegawa/speech.cpp

## 実行条件

- README記載の対象は、Apple Silicon搭載macOS、x64 Windows、x64 Linux。macOSはMetal、WindowsはVulkan、LinuxはVulkanまたはCPUに対応するとされる。Linuxビルドにはglibc 2.34以降が必要。モデルは初回に取得する。出典: https://github.com/nyosegawa/speech.cpp

## 最短手順

- READMEのQuick startでは、`speech tts qwen3-tts-0.6b --voice ryan -o hello.wav "Hello. It will be sunny in Tokyo tomorrow."` で音声を生成し、`speech asr qwen3-asr-0.6b hello.wav` で文字起こしする手順を示す。モデルは初回に取得される。出典: https://github.com/nyosegawa/speech.cpp

## 変更履歴

- 2026-11-14: 初回登録
