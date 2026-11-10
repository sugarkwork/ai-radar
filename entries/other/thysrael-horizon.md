---
repo: "Thysrael/Horizon"
name: "Horizon"
genre: other
url: "https://github.com/Thysrael/Horizon"
license: "MIT"
stars: 13147
language: "Python"
created: "2026-02-20"
updated: "2026-11-09"
added: "2026-11-03"
first_seen: "2026-11-03"
sources: []
flags: []
risk_notes: ""
forks: 1876
open_issues: 5
commits_30d: 80
commit_cadence: "daily"
size_kb: 16443
archived: false
commits_90d: 95
fetched_at: "2026-11-09T21:41:32Z"
last_release: ""
last_release_at: ""
---

# Horizon

## 出来ること

- RSS、Hacker News、Reddit、Telegram、X、GitHub、金融ニュースなどを1つの巡回にまとめ、AI で選別して日次ブリーフィングを作る。
- プロファイル（編集方針のセット）ごとに「何を載せるか・何を残すか・何を書くか」を定義できる。同梱例は `tech-news`（出来事と背景）、`tech-blog`（技術的な深掘り）、`ai-creator`（コンテンツ素材向け）。
- スコアリング規約としきい値で取捨選択し、同一ストーリーの重複を統合する。要約・背景・解決策・持ち帰り、といった出力の型をプロンプトで切り替える。
- Web 調査で背景情報を補い、コミュニティの議論を添える。
- カテゴリごとの分量上限を設定でき、1トピックが briefing を占領しないようにできる。
- 英語・中国語のブリーフィングを Markdown で生成し、GitHub Pages 公開、メール、webhook（Feishu ボット等）で配信。MCP 連携も持つ。

## 目的・背景

「ニュースを読む時間を減らす」のではなく「読む価値のあるものだけを自分用の編集方針で残す」ための個人用ニュースレーダー。設定は JSON とプロンプトで、Python を書かずに調整できることを売りにしている。

## 依存関係

- Python と `uv`（推奨）。`pip install -e .` も可。
- LLM の API キー: OpenAI / Gemini / Claude / DeepSeek / MiniMax / 豆包 / Ollama など。
- 任意: OpenBB の金融ニュースを使う場合は専用 extra。Feishu 通知を使う場合はボット設定。

## 実行条件

- 既定は API キー必須。ただし ChatGPT 有料プラン保持者は「Sign in with ChatGPT」でキーなし運用が選べる（README に記載）。
- `data/config.json` の `api_key_env` は「環境変数の名前」を書く欄で、キー本体を書く欄ではない（README が明示）。実値は `.env` に置く。
- 対話式の設定ウィザード（`uv run horizon-wizard`）があり、興味分野を答えると config が生成される。

## 最短手順

```bash
git clone https://github.com/Thysrael/Horizon.git
cd Horizon
uv sync
uv run horizon-wizard        # 興味分野を答えて data/config.json を生成
```

## 変更履歴

- 2026-11-03: 初回登録（★12,260 / pushed 2026-11-03 / MIT）
