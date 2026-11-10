---
repo: NVlabs/SoL-Pi
name: SoL-Pi
genre: agent-framework
url: https://github.com/NVlabs/SoL-Pi
author: NVIDIA / NTU / MIT（NVlabs）
license: MIT
stars: 3657
language: TypeScript
created: 2026-09-02
updated: "2026-11-09"
added: 2026-11-04
first_seen: 2026-11-03
source_post: https://x.com/AnnatarXBT/status/2117516376201998782
sources:
  - https://nvlabs.github.io/SoL-Pi/
  - https://arxiv.org/abs/2609.20519
forks: 299
open_issues: 90
commits_30d: 32
commits_90d: 73
commit_cadence: "daily"
size_kb: 30171
archived: false
fetched_at: "2026-11-09T21:34:03Z"
last_release: ""
last_release_at: ""
---

# SoL-Pi

## 出来ること

- **長時間動くコーディングエージェントのトークン消費を、作業量を減らさずに下げる** Pi 向けの拡張。Pi 本体は無改変のまま、公開拡張 API で4つの機構を載せる。すべて opt-in で既定は無効。
- **Action Fusion**（ツール）: ファイル編集・書き込みと、その直後に走る検証コマンドを1回のツール呼び出しにまとめる。編集内容を見てから決めるコマンドは従来どおり分離。
- **ObservationPack**（観測）: 大きなツール出力をハンドル化し、必要なときに正確にページ単位で読み戻せるようにする。最初の数リクエストは全文、その後はハンドル＋サイズ＋先頭・末尾の抜粋に置き換える。
- **Evidence-Preserving Reducer**（委譲）: 4KiB 以上のビルド・テストログを安価なモデルに渡して「根拠の要約」を作らせ、書式・原文ハッシュ・終了ステータス・サイズ・引用の一字一句一致を素のコードで検証する。検証に落ちるか認証情報らしき文字列があれば、元のログをそのまま返す。判断はあくまで主モデル。
- **Online Context Compact**（文脈）: 完了したステップの境目でのみ圧縮し、プロンプトキャッシュの書き直しコストと比較して得なときだけ実行する。
- 追加の使い方: `examples/sol-pi-skill` で Claude Code の `/sol-pi`、Codex の `$sol-pi` から、ホスト会話を文脈としてバックグラウンド実行させられる。`examples/solpi-visual` は Blender の3Dシーン再構成向けで、Codex 比でシーンあたりコスト37%減・モデル呼び出し13%減（作者例）。

## 目的・背景

NVIDIA・NTU・MIT の研究（arXiv:2609.20519、*SoL-Pi: Recursively Scaling Auto-Research Loops for Efficient Agent Harness*）の公開実装。エージェントの実行トレースから「繰り返し行動・膨らみ続ける文脈・巨大な出力・情報量の少ないログ」を見つけ、Karpathy 流の autoresearch ループ（提案→実装→レビュー→実験→採用/破棄）をハーネス自体に回して、効率と能力のゲートを先に固定したうえで生き残った機構だけを採用している。論文の 51 タスク EdgeBench では、トークン流量 44.7〜49.0% 減、API コストは Pi 比で約3分の1減、ネイティブの Codex / Claude Code 比で 50.0% / 54.3% 減、スコアは Pi の約94%を維持。2026-09-02 作成、11-04 時点で 3,638 star。

## 依存関係

- Node.js **22.19 以上**、npm
- `@earendil-works/pi-coding-agent` **0.84.2 以上**（0.84.2 / 1.0.4 / 1.3.0 で検証済み。1.0.x と 1.1.0 は内部パッケージを固定しておらず新規インストールが起動しない）
- Pi 本体（SoL-Pi は Pi の公式配布物ではない）
- Reducer を使う場合、安価なモデルへのルート設定（`sol-pi.json`）

## 実行条件

- 設定は単一の実効ファイル: プロジェクトの `.pi/sol-pi.json`（信頼済みプロジェクトのみ）→ 無ければ `~/.pi/agent/sol-pi.json`。両方はマージされず、プロジェクト側が優先。
- 既定は全機構オフ。まず `actionFusion` と `observationPack` だけ有効化する控えめな設定が README に例示されている（追加のモデル呼び出しが無く、実行を止めないため）。
- ログを安価なモデルに渡す Reducer は、内容によっては機密情報の扱いに注意が必要（README にセキュリティ節あり）。
- 論文の数値は 2026-08-17 時点の API 価格・51タスクの公開 EdgeBench によるもので、独立再現は未確認。
- 開発中で pi-v1 と最新モデルに対応中。バージョン互換の警告は `scripts/check-pi-compat.mjs` が出す。

## 最短手順

```bash
npm install --global @earendil-works/pi-coding-agent@1.3.0
pi install git:github.com/NVlabs/SoL-Pi
# プロジェクト限定なら
pi install git:github.com/NVlabs/SoL-Pi --local --approve
# 設定例（控えめ: モデル呼び出しを増やさない2機構だけ）
cat > .pi/sol-pi.json <<'JSON'
{ "version": 1, "actionFusion": true, "observationPack": true,
  "evidencePreservingReducer": false, "onlineContextCompact": false,
  "cacheWriteReadRatio": 12.5 }
JSON
```

## 変更履歴

- 2026-11-04: 初回登録
