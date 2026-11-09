---
repo: "FareedKhan-dev/kimi-k3-in-c"
name: "kimi-k3-in-c"
genre: model-serving
url: "https://github.com/FareedKhan-dev/kimi-k3-in-c"
license: "Apache-2.0"
stars: 10251
language: "C"
created: "2026-08-01"
updated: 2026-10-02
added: "2026-11-03"
first_seen: "2026-11-03"
sources: ["https://x.com/mdaman010/status/2118684826203021621?a=6mS302Az7kjEB2eI8D0&s=46", "https://x.com/mdaman010/status/2118684826203021621", "https://api.github.com/repos/FareedKhan-dev/kimi-k3-in-c", "https://raw.githubusercontent.com/FareedKhan-dev/kimi-k3-in-c/main/README.md", "https://github.com/FareedKhan-dev/kimi-k3-in-c"]
flags: ["unverified"]
risk_notes: "1.56TBのチェックポイントを8.24GBのRAMで動かすという主張。数値は作者の docs/data のみで、独立した再現・検証はない。"
forks: 1625
open_issues: 26
commits_30d: 0
commits_90d: 48
commit_cadence: monthly
size_kb: 31708
archived: false
fetched_at: "2026-11-04T22:50:44Z"
last_release: v1.1.0
last_release_at: 2026-10-02
type: "repo"
author: "FareedKhan-dev"
source_post: "https://x.com/mdaman010/status/2118684826203021621"
amplifiers: []
---

# kimi-k3-in-c

## 出来ること

- Kimi K3（2.78兆パラメータ）の推論を C99 だけで実装したエンジン。BLAS・推論フレームワーク・GPU を一切使わない。エンジン本体は 176KB。
- 1.56TB のチェックポイントをディスクから逐次ストリームし、ピーク RSS 8.24GB で動かす（作者計測）。RAM が増えるとモデルの一部がメモリに載り、トークンあたりの時間だけが短くなる。
- 作者の計測表（同一マシン・124コア・NVMe）: 8GB で26.5秒/トークン、32GB で24.2秒、64GB で19.8秒、128GB 以上で5.6秒。出力はどの構成でもバイト単位で同一と主張。
- MoE、linear attention、MXFP4 量子化、AVX2 の SIMD カーネルを自前実装。Linux / macOS / Windows でビルド可能。
- `--chat` で端末内の対話モードに入れる。公式の XTML チャット形式に従い、履歴は JSONL、思考の長さは `--no-think` / `--thinking-effort` で切り替え、既定は貪欲法で `--temperature` 等を指定したときだけサンプリングする。

## 目的・背景

「巨大モデルは巨大な GPU がないと動かない」という前提を、メモリ階層とディスク帯域の使い方で崩す実験。速度を捨ててでも、同じ重み・同じ出力を手元のマシンで再現することを目的にしている。v1.0.0 でトークンあたりの計算を約8倍軽くし、追撃質問を3.9倍速くしたと CHANGELOG にある。

## 依存関係

- C99 コンパイラ（`make`）。BLAS も Python も不要。
- 1.56TB のチェックポイントを置ける空きディスク（NVMe 推奨）。
- 重みの取得手順は README の Requirements 節を参照。

## 実行条件

- **主張の検証状況**: ピーク RSS 8.24GB、26.5秒/トークンなどの数値は作者の `docs/data/` にある自己計測のみ。第三者の再現報告は確認できていない。1.56TB のディスクを用意する必要があるため、試すハードルは高い。
- 8GB 構成では毎ステップ全重みをディスクから読むため、ストレージ速度がそのまま速度になる。
- ライセンスは Apache-2.0。モデル重み側のライセンスは別途確認が必要。

## 最短手順

```bash
git clone https://github.com/FareedKhan-dev/kimi-k3-in-c.git
cd kimi-k3-in-c
make
./kimi-k3 --help   # 重みのパスなどは README の Requirements / Usage を参照
```

## 変更履歴

- 2026-11-03: 初回登録（star 9,857 / pushed 2026-10-02 / Apache-2.0）
- 2026-11-04: --chat 対話モードを追記（v1.1.0）

## 追加出典・確認範囲（2026-11-09）

Kimi K3の巨大チェックポイントをディスクから読みながらC99で推論する実装。

1.56TBの重みとNVMe容量が前提。8.24GBはチェックポイント容量ではなく生成中のピークRSS。

8GB RAM時の26.5秒/トークン等は開発者測定。小容量RAMで実用的な速度になることを示していない。

対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:25.104085+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

### 今回取得した公式メタ情報

既存フロントマターの過去値は維持し、今回の取得値を下に併記する。どちらも実行・性能の追試ではない。

| 項目 | 値 |
|---|---|
| repo | FareedKhan-dev/kimi-k3-in-c |
| url | https://github.com/FareedKhan-dev/kimi-k3-in-c |
| license | Apache-2.0 |
| language | C |
| created | 2026-08-01 |
| updated | 2026-10-02 |
| stars | 11331 |
| forks | 1770 |
| open_issues | 28 |
| commits_30d | 0 |
| commits_90d | 47 |
| commit_cadence | monthly |
| size_kb | 31708 |
| archived | False |
| fetched_at | 2026-11-09T00:30:25.104085+00:00 |


- @mdaman010: https://x.com/mdaman010/status/2118684826203021621
- 対象資料: https://github.com/FareedKhan-dev/kimi-k3-in-c
- 参照: https://api.github.com/repos/FareedKhan-dev/kimi-k3-in-c
- 参照: https://raw.githubusercontent.com/FareedKhan-dev/kimi-k3-in-c/main/README.md

- 2026-11-09: 関連出典と確認範囲を追記。既存の記述・過去の数値・原文プロンプトは維持。今回の実行確認なし。
