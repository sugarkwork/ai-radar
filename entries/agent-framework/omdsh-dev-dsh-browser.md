---
type: "repo"
name: "omdsh-dev/dsh-browser"
genre: "agent-framework"
url: "https://github.com/omdsh-dev/dsh-browser"
author: "omdsh-dev"
source_post: "https://x.com/Cryptoxorz/status/2118870302096785649"
sources: ["https://x.com/cryptoxorz/status/2118870302096785649?a=KyMILm1-ZMVp-DB0WPg&s=46", "https://x.com/Cryptoxorz/status/2118870302096785649", "https://x.com/Cryptoxorz/status/2118870307998245282", "https://github.com/dsh-market/dsh-market", "https://github.com/zhu1090093659/dsh-web", "https://github.com/ccch1mneyyy/dsh-TUI", "https://github.com/omdsh-dev/DSH-better-sidebar", "https://github.com/liustack/modlens", "https://github.com/bowenliang123/dsh-context", "https://github.com/zilliztech/memsearch", "https://github.com/NanmiCoder/dsh-agent-teams", "https://github.com/ysr666/dsh-vision-router", "https://github.com/omdsh-dev/dsh-browser"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "20%高速という値は投稿/READMEの主張で比較条件・独立追試なし。ログイン済みブラウザの操作を無制限に許可しない。 当方でインストール・推論・生成・ベンチ再現はしていない。"
repo: "omdsh-dev/dsh-browser"
license: "MIT"
language: "TypeScript"
created: "2026-08-06"
updated: "2026-11-08"
stars: 1025
forks: 83
open_issues: 37
commits_30d: 21
commits_90d: 100
commit_cadence: "daily"
size_kb: 1811
archived: false
fetched_at: "2026-11-09T21:34:12Z"
last_release: "v0.1.4"
last_release_at: "2026-11-08"
---

# omdsh-dev/dsh-browser

## 出来ること

DSHのブラウザ操作を補助するdsh-browser。10選ではPlaywrightより高速と紹介。

2026-11-09確認のREADMEではDSH bridgeとChrome/Firefox MV3拡張の両方が必要で、通常のdsh pluginコマンドだけでは導入できない。既存ログイン・cookieを保持してページを操作する。対象DSHは0.2.1-rc.5固定で旧版非対応という案内。

## 目的・背景

紹介対象は `omdsh-dev/dsh-browser`。対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:43.876166+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

## 依存関係

TypeScript実装。ブラウザ環境とDSHの対応、権限・認証の設定を要確認。

## 実行条件

20%高速という値は投稿/READMEの主張で比較条件・独立追試なし。ログイン済みブラウザの操作を無制限に許可しない。

コード本体の許諾と、基底モデル・同梱素材・外部API・音声/人物等の利用条件は別に確認する。

## 最短手順

1. [公式README](https://github.com/omdsh-dev/dsh-browser#readme)で対応版と依存を確認する。
2. 上記の対象固有条件を満たす環境を用意し、配布元の手順を選ぶ。
3. 外部サービスの料金・認証・データ送信とライセンスを確認してから導入する。

本調査では導入・ビルド・起動をしていないため、成功済みのコマンドとしては掲載しない。

## 出典

- @Cryptoxorz: https://x.com/Cryptoxorz/status/2118870302096785649
- 対象資料: https://github.com/omdsh-dev/dsh-browser
- 参照: https://x.com/Cryptoxorz/status/2118870307998245282
- 参照: https://github.com/dsh-market/dsh-market
- 参照: https://github.com/zhu1090093659/dsh-web
- 参照: https://github.com/ccch1mneyyy/dsh-TUI
- 参照: https://github.com/omdsh-dev/DSH-better-sidebar
- 参照: https://github.com/liustack/modlens
- 参照: https://github.com/bowenliang123/dsh-context
- 参照: https://github.com/zilliztech/memsearch
- 参照: https://github.com/NanmiCoder/dsh-agent-teams
- 参照: https://github.com/ysr666/dsh-vision-router

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
