---
repo: wheresryan22/anatomy
name: Anatomy
genre: 3d-motion
url: https://github.com/wheresryan22/anatomy
author: wheresryan22
license: MIT
stars: 24536
language: JavaScript
created: 2026-10-08
updated: 2026-10-18
added: 2026-11-04
first_seen: 2026-11-03
source_post: https://x.com/Fluyeporlaweb/status/2117544561861972226
sources:
  - https://skills.wheresryan.sh/anatomy
forks: 2044
open_issues: 71
commits_30d: 100
commits_90d: 100
commit_cadence: daily
size_kb: 12817
archived: false
fetched_at: "2026-11-04T04:47:05Z"
last_release: v1.1.0
last_release_at: 2026-10-12
---

# Anatomy

## 出来ること

- アイソメトリック（等角投影）の**分解図・断面図**で仕組みを説明する Claude スキル。「トークンバケット型レートリミッタはどう動くか」のように頼むと、実在の機械・計器・道具・家具を部品から組み上げ、動く図として出力する。
- 出力は3種。**SVG**（四階調シェーディングのソリッド部品を奥から手前へ描く。単体 HTML / スタイル埋め込みの `.svg` / React・Next.js コンポーネント）、**SVG + WebGL**（炎・排気・水・コースティクス・ランプ光・グロー・蒸気など線で描けないものを、図と同じアイソメカメラのシェーダで描く。WebGL 無しでも SVG は読める）、**3D**（ベータ。ダイヤルやターンテーブルの回転、指の屈曲、破片の落下など可動部だけを毎フレーム再投影・再シェーディング）。
- ライト／ダークの2テーマ。ライトが設計の基準。
- 図には実数値のライブ読み取りが付き、部品の実寸・個数も正しく持つ。動きはイージング付きで、`prefers-reduced-motion` では静止する。
- 検証ツールを同梱: `kit/audit.mjs` が干渉・接地・重なりの描画順を検査し、ヘッドレス Chrome の `capture.mjs` / `drive.mjs` がスクリーンショット・接写・スロー再生のコンタクトシートを撮り、`lines.mjs` が宙に浮いた線を不合格にし、`turn-check.mjs` が 3D を検査する。スキルは生成した PNG をすべて読むよう指示される。

## 目的・背景

「アイソメ図の生成」を、見た目のそれらしさではなく**機構として成立しているか**で担保する方向のスキル。ジオメトリを一度だけ組み、奥から手前へ塗り、クリティックのように自己検証するワークフローを `SKILL.md` に固定している。`kit/` が等角カメラ・立体・部品ライブラリ・旋盤・チューブ・WebGL・3D ランタイム・React コンポーネントを持ち、React 以外の依存は無い。2026-10-08 作成、10-18 時点で 2.4 万 star。

## 依存関係

- Agent Skills 対応ホスト: Claude Code、Antigravity、OpenCode、Codex、MiniMax Code
- Node.js **20.10 以上**（組み込みモジュールのみ。`npm install` 不要）
- 検証時の Chrome / Chromium（`capture.mjs` / `drive.mjs` / `lines.mjs` / `turn-check.mjs`）。Codex ではブラウザ検査が Chrome を起動するため、サンドボックスで許可が必要な場合がある

## 実行条件

- 図の生成に API キーは不要。モデルはホスト側のエージェントが使う。
- **遅いのは仕様**。部品表・ジオメトリ・監査・両テーマでの接写まで含むため、1枚に長いセッションを要する。30部品の 3D 全周監査は15〜20分。
- 描けるのは機械・計器・道具・家具。人物や正確な地図は不得意で、機構を持たない概念は弱い。グラフ・軸・系列を持つチャートライブラリではない。
- WebGL が無い環境では SVG のみ。3D モードはベータで、小さな図は 60fps、380部品の負荷試験では 1440px 幅で約20fps（13… は README で途切れているため未確認）。

## 最短手順

```bash
npx skills add wheresryan22/anatomy -g -a claude-code
# 以後 Claude Code で:
#   /anatomy explain how a token bucket rate limiter works, interactive
# Codex では $anatomy、他のホストは -a antigravity / opencode / minimax-code
```

## 変更履歴

- 2026-11-04: 初回登録
