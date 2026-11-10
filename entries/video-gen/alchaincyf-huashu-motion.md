---
repo: "alchaincyf/huashu-motion"
name: "huashu-motion（花叔）"
genre: "video-gen"
url: "https://github.com/alchaincyf/huashu-motion"
license: "MIT"
stars: 2567
language: "JavaScript"
created: "2026-10-18"
updated: "2026-10-22"
added: "2026-11-03"
sources:
  - "https://x.com/daaihq/status/2117446567284367459"
flags: []
risk_notes: ""
forks: 257
open_issues: 4
commits_30d: 15
commits_90d: 15
commit_cadence: "weekly"
size_kb: 43226
archived: false
fetched_at: "2026-11-09T21:43:56Z"
last_release: "v0.3.1"
last_release_at: "2026-10-22"
---

# huashu-motion（花叔）

## 出来ること

- 製品発表映像（ローンチフィルム）をエージェントが作るスキル。製品情報を読ませると方向性を3案提示し、選ぶと本編を書き、自分で譜面を書いて音楽を付け、ブラウザのエディタを開く。
- 修正は「画面上の該当箇所をクリックして、そこだけ直す指示を書く」方式。クリック位置は時間と要素情報を伴ってエージェントに渡る。タイトル・色・数字・滞在時間もエディタで調整できる。
- 制作の根拠として、Apple / Nothing / GoPro / Google / Vercel / Linear / Anthropic など実在の発表映像21本を FFmpeg で計測し、カット点・ビート・ラウドネス・エネルギー曲線を参照している。

## 目的・背景

中国語圏で「花叔」として知られる開発者（alchaincyf）による 2026-10 公開。README は中国語（英語版は README.en.md）。Claude Code / Codex / WorkBuddy / Grok Bot / Muse / Dots 上で動くと記載。関連スキルとして `/huashu-video-pipeline`（構成）と `/huashu-art-motion`（作画）も案内されている。

## 依存関係

- Node 22 以上。
- FFmpeg（書き出し・音楽合成）。
- Chrome（プレビュー／レンダリング）。コマンドを実行できる環境が前提。
- ナレーション（任意）: macOS 標準音声は導入不要。Kokoro で中国語を読ませる場合は uv + Python 3.12 と約325MB のモデル、字単位の同期には whisper-cli（`brew install whisper-cpp`）。

## 実行条件

- レンダリングはローカル実行。GPU は不要（コード描画＋ブラウザ）。
- 中国語前提のチュートリアル・音声まわりが多く、日本語運用は README の範囲外＝未確認。
- 生成物の利用条件はリポジトリの MIT に従う（同梱アセットは個別確認）。

## 最短手順

```bash
npx skills add alchaincyf/huashu-motion
# エージェントに「製品Xの30秒の発表映像を作って」と依頼
```

## 変更履歴

- 2026-11-03: 初回登録（star 2,205 / pushed 2026-10-22 / MIT / Node 22+）
