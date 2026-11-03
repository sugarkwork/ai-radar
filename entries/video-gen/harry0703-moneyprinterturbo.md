---
repo: "harry0703/MoneyPrinterTurbo"
name: "MoneyPrinterTurbo"
genre: video-gen
url: "https://github.com/harry0703/MoneyPrinterTurbo"
license: "MIT"
stars: 138303
language: "Python"
created: "2024-03-11"
updated: 2026-11-02
added: "2026-11-03"
first_seen: "2026-11-03"
sources: []
flags: []
risk_notes: ""
forks: 22075
open_issues: 82
commits_30d: 100
commits_90d: 100
commit_cadence: daily
size_kb: 541281
archived: false
fetched_at: "2026-11-03T22:57:53Z"
last_release: v1.3.9
last_release_at: 2026-10-21
---

# MoneyPrinterTurbo

## 出来ること

- テーマやキーワードを1つ入れると、脚本 → 音声 → 素材（ストック映像/画像）→ 字幕 → BGM → 合成まで自動で進み、縦型・横型のショート動画を書き出す。
- 入口が4つある: AI エージェント（Skill 経由）、WebUI、REST API、CLI。バッチで複数本の生成、タスク履歴、設定とAPIキーのエクスポート/インポートに対応。
- 脚本は AI 生成のほか自作も可。LLM は Kimi / OpenAI / Claude / Gemini / DeepSeek / 通義千問 / Azure OpenAI / 火山引擎方舟 / xAI Grok / MiniMax / 小米 MiMo などに対応。
- 配布形態が多い: Windows 一键启动包（.7z）、PyPI 公式パッケージ `mpt`、Docker（`ghcr.io/harry0703/moneyprinterturbo:latest`）、Google Colab。

## 目的・背景

2024-03 公開の中国製ショート動画自動生成ツール。素材検索・TTS・字幕焼き込み・BGM までを1本のパイプラインにまとめ、動画編集の手作業をなくすことを狙う。README にスポンサー枠が多く、LLM/素材/音声は外部 API 前提の構成。

## 依存関係

- Python 3.11 以上（推奨 3.11）。`uv` での環境構築を推奨。
- `ffmpeg` が PATH 上に必要（一键启动包と Docker には同梱）。
- クラウド LLM・オンライン素材・クラウド TTS を使う場合はそれぞれの API キー。`config.example.toml` を `config.toml` にコピーして設定する。

## 実行条件

- README の最低要件は CPU 4コア / RAM 4GB。推奨 6〜8コア / 8GB、理想 8コア以上 / 16GB。
- GPU は必須ではない（推奨 4GB 以上、理想 8GB 以上）。`faster-whisper` やバッチ生成を回すなら GPU の効果が大きい。
- Windows の一键启动包は展開先パスに中文・特殊文字・空白を含めないこと。

## 最短手順

```bash
git clone https://github.com/harry0703/MoneyPrinterTurbo.git
cd MoneyPrinterTurbo
cp config.example.toml config.toml
docker compose -f docker-compose.release.yml up
# WebUI: http://127.0.0.1:8501   API: http://127.0.0.1:8080/docs
```

## 変更履歴

- 2026-11-03: 初回登録（star 138,300 / pushed 2026-11-02 / MIT）
