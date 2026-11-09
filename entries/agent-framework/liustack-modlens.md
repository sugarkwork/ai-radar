---
type: "repo"
name: "liustack/modlens"
genre: "agent-framework"
url: "https://github.com/liustack/modlens"
author: "liustack"
source_post: "https://x.com/Cryptoxorz/status/2118870302096785649"
sources: ["https://x.com/cryptoxorz/status/2118870302096785649?a=KyMILm1-ZMVp-DB0WPg&s=46", "https://x.com/Cryptoxorz/status/2118870302096785649", "https://x.com/Cryptoxorz/status/2118870307998245282", "https://github.com/dsh-market/dsh-market", "https://github.com/zhu1090093659/dsh-web", "https://github.com/ccch1mneyyy/dsh-TUI", "https://github.com/omdsh-dev/DSH-better-sidebar", "https://github.com/liustack/modlens", "https://github.com/bowenliang123/dsh-context", "https://github.com/zilliztech/memsearch", "https://github.com/NanmiCoder/dsh-agent-teams", "https://github.com/ysr666/dsh-vision-router", "https://github.com/omdsh-dev/dsh-browser"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "DSH必須プラグイン一覧に載ることとDSH専用実装であることは別。対応エージェント・権限・画面送信の扱いは未検証。 当方でインストール・推論・生成・ベンチ再現はしていない。"
repo: "liustack/modlens"
license: "MIT"
language: "TypeScript"
created: "2026-02-22"
updated: "2026-11-07"
stars: 4859
forks: 152
open_issues: 2
commits_30d: 13
commits_90d: 100
commit_cadence: "weekly"
size_kb: 12514
archived: false
fetched_at: "2026-11-09T00:30:41.228226+00:00"
---

# liustack/modlens

## 出来ること

テキスト主体のコーディングエージェントに視覚情報を渡す補助として紹介されたmodlens。

2026-11-09確認のREADMEもtext-onlyモデルへ視覚処理を足すプラグインと説明し、GLM-5.3とGLM-5.3-Flashの入力能力を区別する。画像を見たことにして文章モデルへ直接渡す仕組みではなく、視覚エンジンとの連携である。

## 目的・背景

紹介対象は `liustack/modlens`。対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:41.228226+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

## 依存関係

原チェックのREADMEではDSH専用ではなくtext-only coding agent全般向けと説明。

## 実行条件

DSH必須プラグイン一覧に載ることとDSH専用実装であることは別。対応エージェント・権限・画面送信の扱いは未検証。

コード本体の許諾と、基底モデル・同梱素材・外部API・音声/人物等の利用条件は別に確認する。

## 最短手順

1. [公式README](https://github.com/liustack/modlens#readme)で対応版と依存を確認する。
2. 上記の対象固有条件を満たす環境を用意し、配布元の手順を選ぶ。
3. 外部サービスの料金・認証・データ送信とライセンスを確認してから導入する。

本調査では導入・ビルド・起動をしていないため、成功済みのコマンドとしては掲載しない。

## 出典

- @Cryptoxorz: https://x.com/Cryptoxorz/status/2118870302096785649
- 対象資料: https://github.com/liustack/modlens
- 参照: https://x.com/Cryptoxorz/status/2118870307998245282
- 参照: https://github.com/dsh-market/dsh-market
- 参照: https://github.com/zhu1090093659/dsh-web
- 参照: https://github.com/ccch1mneyyy/dsh-TUI
- 参照: https://github.com/omdsh-dev/DSH-better-sidebar
- 参照: https://github.com/bowenliang123/dsh-context
- 参照: https://github.com/zilliztech/memsearch
- 参照: https://github.com/NanmiCoder/dsh-agent-teams
- 参照: https://github.com/ysr666/dsh-vision-router
- 参照: https://github.com/omdsh-dev/dsh-browser

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
