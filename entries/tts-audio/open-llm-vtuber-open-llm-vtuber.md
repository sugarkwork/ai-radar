---
repo: "Open-LLM-VTuber/Open-LLM-VTuber"
name: "Open-LLM-VTuber"
genre: "tts-audio"
url: "https://github.com/Open-LLM-VTuber/Open-LLM-VTuber"
flags: ["unverified"]
risk_notes: "オフライン動作、応答遅延、各OSでのデスクトップ機能、MCP呼び出しは未実測。GitHubの公開一覧では v1.2.1 に Latest 表示があるが、リリース日時は未確定。APIのライセンス値は unknown。フロントエンドと各素材・モデルの利用条件は個別確認が必要。 GitHub APIでライセンスを確認できていません。"
stars: 14666
forks: 1761
open_issues: 161
size_kb: 46740
language: "Python"
created: "2023-11-24"
updated: "2026-05-15"
archived: false
license: "unknown"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/0xGky/status/2119310447514194104"]
fetched_at: "2026-11-10T12:19:04+00:00"
---

# Open-LLM-VTuberで組むLive2D音声対話環境

## 出来ること

- マイクで話しかけ、Live2Dキャラクターの音声応答を途中で遮って会話を続けられるとREADMEは説明する。カメラや画面の入力、クリックやドラッグへの反応も記載されている。

## 目的・背景

- 当初はオフラインかつWindows以外でも動かせるAI VTuberを目指したプロジェクト。LLM、音声認識（ASR）、音声合成（TTS）を構成に応じて選べる。

## 依存関係

- 公式手順では uv でPython依存関係を導入する。Gitで取得する場合はフロントエンドのサブモジュールも取得する。持ち込みのLive2Dモデルは live2d-models に配置し、model_dict.json とキャラクター設定に登録する。対応範囲は公式ガイドでCubism 3〜5。
- 公式のv1.2.0告知ではフロントエンドに独自ライセンスを適用している。配信や再配布では、フロントエンド、Live2D素材、音声・推論モデルそれぞれの条件を確認する。外部APIの料金とデータの取り扱いは選択したサービスに依存する。

## 実行条件

- READMEはWindows、macOS、Linux対応を掲げる。ブラウザー版はローカルのバックエンドで起動し、デスクトップ表示には別途Electronクライアントを使う。
- オフライン利用にはLLM、ASR、TTSをローカルで動く構成にそろえ、依存パッケージやモデルを先に取得する。公式クイックスタートの既定TTSはedgeTTSのため、オフライン用には変更する。カメラ画像を会話に使う場合は画像を扱える構成を選ぶ。

## 最短手順

- 公式リリースの配布ZIPを使うか、git clone https://github.com/Open-LLM-VTuber/Open-LLM-VTuber --recursive で取得する。プロジェクト直下で uv sync を実行する。
- conf.yaml で利用するLLM・ASR・TTSを設定し、uv run run_server.py で起動する。設定ファイルがなければ初回起動で生成できる。起動後に http://localhost:12393 を開いて対話する。
- AIからMCPツールを呼ぶ場合は、公式MCPガイドに沿って mcp_servers.json の time を使い、conf.yaml の basic_memory_agent で use_mcpp を有効にして mcp_enabled_servers に time を指定する。起動後、会話画面で現在時刻を尋ねてツール呼び出しを試せる。

## 変更履歴

- 2026-11-10: 初回登録
