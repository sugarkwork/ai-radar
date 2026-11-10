---
type: "repo"
name: "livliv-dev/player"
genre: "3d-motion"
url: "https://github.com/livliv-dev/player"
author: "livliv-dev"
source_post: "https://x.com/DDJCXX/status/2118931450812568006"
sources: ["https://x.com/ddjcxx/status/2118931450812568006?a=SawzNevfpN4j-N92Rn4&s=46", "https://x.com/DDJCXX/status/2118931450812568006", "https://github.com/livliv-dev/player", "https://api.github.com/repos/livliv-dev/player", "https://raw.githubusercontent.com/livliv-dev/player/main/README.md", "https://registry.npmjs.org/@livliv-dev/player", "https://livliv-dev.github.io/player/"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "Apache-2.0はプレイヤーのみ。同梱21キャラは個人非商用・クレジット等の別条件で一部さらに例外。公開直後でmodel.json v4等の形式は流動的。 当方でインストール・推論・生成・ベンチ再現はしていない。"
repo: "livliv-dev/player"
license: "Apache-2.0"
language: "TypeScript"
created: "2026-11-04"
updated: "2026-11-09"
stars: 1395
forks: 146
open_issues: 1
commits_30d: 40
commits_90d: 40
commit_cadence: "daily"
size_kb: 23816
archived: false
fetched_at: "2026-11-09T21:31:19Z"
last_release: "v0.3.0"
last_release_at: "2026-11-06"
---

# livliv-dev/player

## 出来ること

WebGL2でLivLiv/VRM/PNGtuberを共通APIで再生し、音声リップシンクやMediaPipe顔追従、OBS向けiframeを案内するプレイヤー。

## 目的・背景

紹介対象は `livliv-dev/player`。対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:55.872140+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

## 依存関係

TypeScript/npm環境。コア約30KB gzip、顔追従等は必要時の遅延読込み。音声・カメラへの許可が必要。

## 実行条件

Apache-2.0はプレイヤーのみ。同梱21キャラは個人非商用・クレジット等の別条件で一部さらに例外。公開直後でmodel.json v4等の形式は流動的。

コード本体の許諾と、基底モデル・同梱素材・外部API・音声/人物等の利用条件は別に確認する。

## 最短手順

1. [公式README](https://github.com/livliv-dev/player#readme)で対応版と依存を確認する。
2. 上記の対象固有条件を満たす環境を用意し、配布元の手順を選ぶ。
3. 外部サービスの料金・認証・データ送信とライセンスを確認してから導入する。

本調査では導入・ビルド・起動をしていないため、成功済みのコマンドとしては掲載しない。

## 出典

- @DDJCXX: https://x.com/DDJCXX/status/2118931450812568006
- 対象資料: https://github.com/livliv-dev/player
- 参照: https://api.github.com/repos/livliv-dev/player
- 参照: https://raw.githubusercontent.com/livliv-dev/player/main/README.md
- 参照: https://registry.npmjs.org/@livliv-dev/player
- 参照: https://livliv-dev.github.io/player/

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
