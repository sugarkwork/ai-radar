---
type: "repo"
name: "lowkeytea/scyllasband"
genre: "tts-audio"
url: "https://github.com/lowkeytea/scyllasband"
author: "lowkeytea"
source_post: "https://x.com/mapte_fireball/status/2118974266784018721"
sources: ["https://x.com/mapte_fireball/status/2118974266784018721?a=7bYEtVD_cM2eDkGAIBM&s=46", "https://x.com/mapte_fireball/status/2118974266784018721", "https://www.reddit.com/r/LocalLLaMA/comments/1xpq3l0/scyllas_band_v4_open_source_tts_with_code_to_run/", "https://huggingface.co/spybyscript/scyllasband", "https://github.com/lowkeytea/scyllasband", "https://api.github.com/repos/lowkeytea/scyllasband"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "ランタイムApache-2.0と各構成要素の条件を確認する。モデルの70ms等を全デバイスでの実測保証にしない。 当方でインストール・推論・生成・ベンチ再現はしていない。"
repo: "lowkeytea/scyllasband"
license: "Apache-2.0"
language: "C++"
created: "2026-07-19"
updated: "2026-11-07"
stars: 27
forks: 2
open_issues: 2
commits_30d: 12
commits_90d: 24
commit_cadence: "weekly"
size_kb: 260394
archived: false
fetched_at: "2026-11-09T00:31:01.127323+00:00"
---

# lowkeytea/scyllasband

## 出来ること

Scylla's Bandの音声・歌唱モデルをC API、Python、iPhone/Android等から利用するランタイム。

## 目的・背景

紹介対象は `lowkeytea/scyllasband`。対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:31:01.127323+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

## 依存関係

選択端末ごとのモデルバンドル/バックエンドが必要。発話の強度・速度・ピッチと歌唱JSONを扱う。

## 実行条件

ランタイムApache-2.0と各構成要素の条件を確認する。モデルの70ms等を全デバイスでの実測保証にしない。

コード本体の許諾と、基底モデル・同梱素材・外部API・音声/人物等の利用条件は別に確認する。

## 最短手順

1. [公式README](https://github.com/lowkeytea/scyllasband#readme)で対応版と依存を確認する。
2. 上記の対象固有条件を満たす環境を用意し、配布元の手順を選ぶ。
3. 外部サービスの料金・認証・データ送信とライセンスを確認してから導入する。

本調査では導入・ビルド・起動をしていないため、成功済みのコマンドとしては掲載しない。

## 出典

- @mapte_fireball: https://x.com/mapte_fireball/status/2118974266784018721
- 対象資料: https://github.com/lowkeytea/scyllasband
- 参照: https://www.reddit.com/r/LocalLLaMA/comments/1xpq3l0/scyllas_band_v4_open_source_tts_with_code_to_run/
- 参照: https://huggingface.co/spybyscript/scyllasband
- 参照: https://api.github.com/repos/lowkeytea/scyllasband

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
