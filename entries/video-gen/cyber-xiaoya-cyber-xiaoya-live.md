---
repo: cyber-xiaoya/cyber-xiaoya-live
name: 赛博小雅直播版（Cyber Xiaoya Live）
genre: video-gen
url: https://github.com/cyber-xiaoya/cyber-xiaoya-live
license: AGPL-3.0（コードのみ。素材・ブランドは NOTICE で別扱い）
stars: 815
language: Python
created: 2026-10-24
updated: "2026-11-09"
added: 2026-11-05
first_seen: 2026-11-05
source_post: ""
sources:
  - https://www.19980303.xyz/
  - https://github.com/cyber-xiaoya/cyber-xiaoya-danmaku
flags: []
risk_notes: "AGPL-3.0。改変版をネットワーク経由で提供するとソース公開義務が生じる。人物画像・音声などの素材とブランドは NOTICE によりライセンス対象外。第三者製の弾幕収集ツールは各プラットフォームの規約に従う必要があり、AI配信の表示義務を定める平台もある。"
forks: 350
open_issues: 1
commits_30d: 18
commits_90d: 18
commit_cadence: "weekly"
size_kb: 5616
archived: false
fetched_at: "2026-11-09T21:44:28Z"
last_release: "v1.0.0"
last_release_at: "2026-10-24"
---

# 赛博小雅直播版（Cyber Xiaoya Live）

## 出来ること

- **Vidu のクラウドレンダリングで動く「组件版」デジタルヒューマン**を、自分の配信に組み込むための一式。口パク・表情・動作のレンダリングと配信は Vidu 側、思考・発声・弾幕処理・点播・録画はすべてローカル。
- 構成は「ブラウザの舞台ページ（`http://127.0.0.1:8795/stage`）→ ローカル橋（FastAPI :8795）→ Vidu 雲 → WebRTC でブラウザが購読」。
  - LLM のストリームを文単位に切り、ローカル TTS で PCM にして Vidu に渡す
  - Vidu は「文字／音声を映像にする」係だけ。ASR・LLM・TTS のクラウド套餐は不要
- 観客の弾幕がそのまま**動作コマンド**になる（「墨鏡を出す」など）。舞台ページから手打ち・直発・点播・中断もできる。
- 歌のリクエスト、録画のダウンロード、記憶の残りターン数、Token 使用量と Vidu クレジット消費の統計パネル（画面上をドラッグ可）。
- 2026-11-02 の更新で、複数動作の**固定編成**（組内2秒／組間15秒、順序はランダムか順番）、99鑽以上のギフトで「贈り物を顔の前に出す」演出、会員の入場挨拶、発話側のNGワードフィルタが入った。
- 弾幕収集は別リポジトリ（`cyber-xiaoya/cyber-xiaoya-danmaku`、★64・AGPL-3.0）が担当。抖音／B站／YouTube／動画号に対応し、`tts.output` を `dh` にすると本リポジトリの橋へ流し込める。

## 目的・背景

「完成品を配る」のではなく、**配信の骨組みを配る**という設計。作者（天工开帧）は README で「ダウンロードしてダブルクリックで配信できるものではない」と明言しており、人物形象・克隆音色・人設・動作庫・歌庫・API Key は一切同梱していない。理由は、それらが各配信者の資産であり、二次販売を防ぐ境界でもあるため。コードは完全で、足りないのは「自分のコンテンツ」だけ、という立場。

## 依存関係

- **Windows 10/11 + NVIDIA GPU（8GB以上のVRAM）**。アプリ本体はPowerShellスクリプトで起動する。
- **Vidu アカウントと API Key**（`vda_...`）。デジタルヒューマンのレンダリングと配信に必須で、**1秒1クレジット**の従量課金。残高が45クレジット未満だと開場できない。
- **LLM の API Key**（既定は DeepSeek `deepseek-flash`、OpenAI互換なら何でも可）。
- **TTS は OmniVoice のみ対応**。WSL2 + Ubuntu 22.04 + CUDA が必要で、作者の実測で約11GBのVRAMを使用。RTX 50系（Blackwell）は cu130 系のPyTorchが要る。`tools/omnivoice/` のラッパー2ファイルを上流リポジトリへコピーする手順が必須。
- ffmpeg（音声デコード）。

## 実行条件

- **約1時間のセットアップ**が前提（作者の見積り）。Vidu で形象（`avatar_id`）を作り、任意で動作庫（`library_id`）を用意する。
- 同梱されていないもの: 人物形象、克隆音色、人設プロンプト、文案、歌単、動作庫の中身、API Key、OmniVoice の重み（数GB）、依存環境（2GB+）。
- TTS を差し替える場合は `src/tts/` にアダプタを自分で書く（Edge-TTS や GPT-SoVITS は未実装）。
- **ライセンスはコードが AGPL-3.0**。改変してネットワーク越しに提供する場合はソース公開義務が生じる。素材・ブランドは NOTICE により対象外。作者は「有料販売・代部署は非公認」と明記している。
- プラットフォーム側の規約と、AI生成であることの表示義務は利用者側の責任。第三者製の弾幕収集ツールの合规リスクも同様。
- ★706 / fork 310 / open issue 1。初版 v1.0.0 は 2026-10-24。

## 最短手順

```powershell
# 1) Python 3.12 + uv
winget install --id Python.Python.3.12
pip install uv

# 2) 依存導入
uv venv .venv --python 3.12
uv pip install -r requirements.txt

# 3) config.json に Vidu の api_key / avatar_id、LLM の key_file を設定
# 4) OmniVoice（WSL2）を起動し、tts.omnivoice_base を合わせる
bash ~/omnivoice-wsl/start_server.sh

# 5) アプリ起動（PowerShell スクリプト）
./start-component-stack.ps1
# ブラウザで http://127.0.0.1:8795/stage を開く
```

## 変更履歴

- 2026-11-05: 初回登録（★706 / pushed 2026-11-02 / AGPL-3.0 / v1.0.0）
