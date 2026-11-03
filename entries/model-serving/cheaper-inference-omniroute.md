---
repo: "cheaper-inference/OmniRoute"
name: "OmniRoute"
genre: model-serving
url: "https://github.com/cheaper-inference/OmniRoute"
license: "MIT"
stars: 84278
language: "TypeScript"
created: "2026-02-13"
updated: 2026-11-03
added: "2026-11-03"
first_seen: "2026-11-03"
sources: []
flags: []
risk_notes: ""
forks: 12649
open_issues: 564
commits_30d: 100
commits_90d: 100
commit_cadence: daily
size_kb: 2502883
archived: false
fetched_at: "2026-11-03T22:58:33Z"
last_release: v3.8.52
last_release_at: 2026-10-19
---

# OmniRoute

## 出来ること

- 1つのエンドポイント（既定 `http://localhost:20128/v1`）で多数のプロバイダとモデルに接続するゲートウェイ。README の見出しは「380プロバイダ・1400+モデル」で、Anthropic / OpenAI / Gemini / Kimi / GLM / DeepSeek / MiniMax などを OpenAI 互換 API として束ねる。
- クォータを認識した自動フォールバックと20種類のルーティング戦略。`model: auto` で、利用可能かつ上限に達していない接続へ振り分ける。
- Claude Code / Codex / Cursor / OpenCode / Cline / Copilot などのクライアントをそのまま向けられる。MCP・A2A 対応、CLI、デスクトップアプリ（Electron）と PWA。
- 「RTK + Caveman」のプロンプト圧縮でトークン消費を15〜95%削減（作者記載、平均約89%）。
- 無料枠の台帳をダッシュボード（`/dashboard/free-tiers`）で見える化し、プールの重複を排除して月あたりの残量を計算する。

## 目的・背景

複数の無料枠を手で積むと SDK とレート制限の管理が破綻する。そこで「どのプロバイダにどれだけ残っているか」を1か所で把握し、上限に当たったら自動で次へ送る層を作る、という発想。README 自身が「無料枠の合計は OmniRoute からの付与ではなく、それぞれ別に取得できる第三者枠の推定合計」と明記している。

## 依存関係

- Node.js / npm、または Docker（`diegosouzapw/omniroute`）。

## 実行条件

- 使うプロバイダのアカウントと認証情報は自分で用意する（BYO）。プロバイダごとに上限・可用性・規約が異なる。
- `tos: avoid` と分類されたプロバイダ（Kiro など）は既定で自動ルーティングから除外される。アカウントを接続しても解除されない。
- プロバイダ数・無料枠トークン数（約16.2億/月）は作者のカタログ集計で、第三者の検証はない。数字は2週間ごとに再監査され上下する。
- 無料枠の利用が各プロバイダの規約に適合するかは利用者の責任。規約違反になり得る構成を自動で止める仕組みはない。

## 最短手順

```bash
docker run -p 20128:20128 diegosouzapw/omniroute
# ダッシュボードでプロバイダを接続し、Endpoints から OmniRoute のキーを取得
curl http://localhost:20128/v1/chat/completions \
  -H "Authorization: Bearer YOUR_OMNIROUTE_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"auto","messages":[{"role":"user","content":"Hello!"}]}'
```

## 変更履歴

- 2026-11-03: 初回登録（star 84,274 / pushed 2026-11-03 / MIT）
