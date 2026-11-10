---
repo: "suno-ai/bark"
name: "Bark"
genre: "tts-audio"
url: "https://github.com/suno-ai/bark"
license: "MIT"
stars: 39332
language: "Jupyter Notebook"
created: "2023-04-07"
updated: "2024-08-19"
added: "2026-11-03"
sources:
  - "https://x.com/RoundtableSpace/status/2117357328152350832"
flags: []
risk_notes: ""
forks: 4659
open_issues: 269
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
size_kb: 2641
archived: false
fetched_at: "2026-11-09T21:43:40Z"
last_release: ""
last_release_at: ""
---

# Bark

## 出来ること

- テキストから音声を生成する Transformer ベースの TTS。話し言葉に加えて笑い声・ため息・泣き声・「音楽」的な非言語音も生成する。
- 多言語対応。日本語を含む複数言語のテキストを読ませられる（話者プリセットは英語話者中心）。
- 出力は 24kHz の WAV。長文は自動で分割される。

## 目的・背景

Suno による 2023-04 公開の TTS モデル。リポジトリは 2024-08 を最後に更新が止まっており、事実上メンテナンス終了状態（archived ではない）。後発の音声生成モデルと比べると品質・速度で見劣りするが、非言語音まで含めて生成できる点と MIT ライセンスで今も参照実装として使われる。

## 依存関係

- PyTorch 2.0 以上。README は CUDA 11.7 / 12.0 で検証と記載。
- `pip install git+https://github.com/suno-ai/bark.git` で導入する。**`pip install bark` は別パッケージ**なので使わない（README が明示的に警告）。
- 追加で HuggingFace transformers の最新版が必要になる場合がある（README に手順あり）。

## 実行条件

- フルモデルを GPU に載せる場合、約 12GB の VRAM を要する（README 記載）。設定を変えれば 2GB 程度の GPU でも動くが低速。
- CPU でも動作するが、生成時間は大幅に伸びる。
- モデル重みは初回に自動ダウンロード。

## 最短手順

```bash
pip install git+https://github.com/suno-ai/bark.git
```

```python
from bark import generate_audio, SAVE_PATH, preload_models
preload_models()
audio = generate_audio("こんにちは、テストです。[laughs]")
```

## 変更履歴

- 2026-11-03: 初回登録（star 39,290 / pushed 2024-08-19 / MIT・更新停止）
