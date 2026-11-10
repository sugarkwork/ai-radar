---
repo: chatfire-AI/huobao-drama
name: Huobao Drama（火宝短剧）
genre: video-gen
url: https://github.com/chatfire-AI/huobao-drama
license: CC BY-NC-SA 4.0（README のバッジ。GitHub API は NOASSERTION）
language: TypeScript
created: 2026-01-05
updated: "2026-11-05"
added: 2026-11-04
first_seen: 2026-11-04
sources:
  - https://x.com/Manorgw/status/2117522416167759906
flags: []
risk_notes: "CC BY-NC-SA 4.0。商用利用は不可で、改変物も同じライセンスが必要。生成物の権利・商用利用は別途確認。"
stars: 17181
forks: 3198
open_issues: 46
commits_30d: 8
commits_90d: 100
commit_cadence: "weekly"
size_kb: 48185
archived: false
fetched_at: "2026-11-09T21:44:20Z"
last_release: "v4.0.11"
last_release_at: "2026-11-05"
---

# Huobao Drama（火宝短剧）

## 出来ること

- 「一言で短劇を1本作る」を掲げる、脚本から成片までの自動パイプライン。LLM が脚本を解析して人物・場景・分镜（絵コンテ）を抽出し、画像生成でキャラクターと背景を作り、動画生成モデルで各ショットを映像化する。
- 工程ごとの機能: キャラクター管理（AI生成・一括生成・アップロード）／分镜から動画タスクの自動生成（場面記述とプロンプト生成、タスク単位の一括生成）／Text-to-Video と Image-to-Video／FFmpeg によるショット単位の合成と字幕／全編の連結と書き出し。
- 素材は統一アセットライブラリで管理し、ローカル保存にも対応。
- キャラクターごとに音色サンプルをアップロード・試聴・差し替え・削除できる。分镜の動画プロンプトに `#キャラクター名` と書くと、動画生成時にその音色が渡される（ローカル音声の検証と形式変換も行う）。初回の分镜分解とプロンプト生成も、キャラクターの割り当てと使える音色を踏まえて参照を入れる。
- **Electron のデスクトップアプリ**があり、フロント（Nuxt 3 + Vue 3）とバックエンド（Hono + Drizzle ORM + Mastra AI Agents + SQLite）が同梱。
- エージェントのスキル定義（`backend/workspace/skills/` の `SKILL.md`）を UI から編集でき、制作フローを自分向けに変えられる。

## 目的・背景

中国語圏の AI 短劇（縦型の連続ドラマ）ブームに合わせて 2026-01 に公開された。投稿者が指摘しているとおり「数分で確実に納品」ではなく、所要時間と品質はモデル・ハードウェア・素材に強く依存する。★16,970 / fork 3,160 と、この分野では大きい。

## 依存関係

- Node.js 20 以上
- LLM・画像生成・動画生成の各 API キー（「Huobao Quick Setup」で3種の推奨構成を一括設定できる）
- FFmpeg（合成・字幕・書き出し）
- デスクトップ版を使う場合は Electron（配布バイナリあり）

## 実行条件

- 生成は基本クラウドAPI。ローカルGPUで回す構成ではない（モデルは同梱されない）。
- ディスク: 生成素材とSQLiteのデータが積み上がる。
- **ライセンスは CC BY-NC-SA 4.0**。商用利用不可、改変物も同一ライセンス。業務利用は不可なので注意。

## 最短手順

```bash
git clone https://github.com/chatfire-AI/huobao-drama
# デスクトップ版（Releases）か、README の手順で frontend/backend を起動
# 設定 → Huobao Quick Setup に API キーを貼る
```

## 変更履歴

- 2026-11-04: 初回登録（★16,970 / v4.0.10 / TypeScript / CC BY-NC-SA 4.0）、キャラクターの音色サンプルと `#名前` 参照を追記（v4.0.10）
