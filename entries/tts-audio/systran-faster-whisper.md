---
repo: "SYSTRAN/faster-whisper"
name: "faster-whisper"
genre: "tts-audio"
url: "https://github.com/SYSTRAN/faster-whisper"
last_release: "v1.2.1"
flags: ["unverified"]
risk_notes: ["最新リリースのタグは確認済み。公開日の年とタイムゾーンを含む公開日時は未確認。", "性能値は開発元のベンチマーク。今回の精査では実行せず、別の音源や環境での処理速度・認識精度は未検証。"]
stars: 26637
forks: 2228
open_issues: 20
size_kb: 40527
language: "Python"
created: "2023-02-11"
updated: "2026-11-06"
archived: false
license: "MIT"
commits_30d: 6
commits_90d: 13
commit_cadence: "weekly"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/nuannuan_share/status/2119640438135242817"]
fetched_at: "2026-11-10T09:29:45+00:00"
---

# faster-whisper — 音声をタイムスタンプ付きで文字起こしするPythonライブラリ

## 出来ること

- 音声ファイルを文字起こしし、区間ごとの開始・終了時刻とテキストを取得できる。単語単位の時刻も取得でき、区間の時刻とテキストを字幕データに整形できる。 [公式README](https://github.com/SYSTRAN/faster-whisper#usage)

## 目的・背景

- Whisperの推論をCTranslate2で再実装し、CPUとGPUで8ビット量子化を利用できる。開発元の13分音声の比較では、RTX 3070 Ti 8GBでlarge-v2をFP16、ビーム幅5で実行した場合、faster-whisper v1.1.0は1分03秒・4525 MB、openai/whisperは2分23秒・4708 MBだった。処理時間とメモリ使用量は精度設定やバッチサイズでも変わる。 [開発元ベンチマーク](https://github.com/SYSTRAN/faster-whisper#benchmark)

## 依存関係

- 推論にCTranslate2、音声のデコードにFFmpegライブラリを同梱するPyAVを使う。システムへのFFmpegの別途導入は不要。 [公式README](https://github.com/SYSTRAN/faster-whisper#requirements)

## 実行条件

- Python 3.9以上。CPUではINT8で実行できる。READMEが案内するGPU構成にはCUDA 12向けcuBLASとcuDNN 9が必要。モデルをサイズ名で指定するとHugging Face Hubから対応するモデルを取得する。変換済みのローカルモデルも指定できる。 [公式README](https://github.com/SYSTRAN/faster-whisper)
- リポジトリのコードはMITライセンス。 [公式ライセンス](https://github.com/SYSTRAN/faster-whisper/blob/master/LICENSE)

## 最短手順

- `pip install faster-whisper` で導入する。Pythonで `from faster_whisper import WhisperModel` を実行し、`WhisperModel('small', device='cpu', compute_type='int8')` でモデルを用意する。
- `segments, info = model.transcribe('audio.mp3')` を呼び、`segments` を反復して `start`、`end`、`text` を取り出す。AIエージェントから使う場合は、このPython処理を音声パスを受け取るローカルツールに包み、区間の配列を返す。 [Python APIの公式使用例](https://github.com/SYSTRAN/faster-whisper#usage)

## 変更履歴

- 2026-11-10: 初回登録
