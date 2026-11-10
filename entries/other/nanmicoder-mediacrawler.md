---
repo: NanmiCoder/MediaCrawler
name: MediaCrawler
genre: other
url: https://github.com/NanmiCoder/MediaCrawler
license: 未確認（API は NOASSERTION、標準ライセンスファイル無し）
language: Python
created: 2023-06-09
updated: "2026-11-09"
added: 2026-11-04
first_seen: 2026-11-04
sources: ["https://x.com/leo_xiaolei/status/2117517260470485470", "https://x.com/chenfacai0/status/2118922893933350978?a=468vYYORc7R_7p9Dtsg&s=46", "https://x.com/chenfacai0/status/2118922893933350978", "https://github.com/NanmiCoder/MediaCrawler", "https://api.github.com/repos/NanmiCoder/MediaCrawler", "https://raw.githubusercontent.com/NanmiCoder/MediaCrawler/main/LICENSE"]
flags: ["unverified"]
risk_notes: "各プラットフォームの利用規約と著作権に抵触しうる。収集した投稿・動画の再配布は権利者の許諾が必要。規約違反・アカウント停止のリスクは利用者側。"
stars: 70741
forks: 13389
open_issues: 217
commits_30d: 21
commits_90d: 43
commit_cadence: "daily"
size_kb: 30756
archived: false
fetched_at: "2026-11-09T21:41:17Z"
license_detail: "原チェックのLICENSE/README解釈: NON-COMMERCIAL LEARNING LICENSE 1.1。APIのSPDX判定とは別。利用前に現行本文を確認。"
type: "repo"
author: "NanmiCoder"
source_post: "https://x.com/chenfacai0/status/2118922893933350978"
amplifiers: []
last_release: ""
last_release_at: ""
---

# MediaCrawler

## 出来ること

- 中国系プラットフォーム横断のデータ収集ツール。小红书（RED）・抖音・快手・B站・微博・百度貼吧・知乎の**投稿とコメント**を取得する。
- ブラウザのログイン状態（Playwright）と JS 署名を使い、暗号アルゴリズムのリバースエンジニアリングをせずに各サイトの API を叩く方式。1回の設定で複数プラットフォームを回せる。
- キーワード検索・指定投稿の取得・コメント収集などのモードを持つ。
- **実況写真（Live Photo）**: 抖音と小红书の投稿で、実況動画の付属クリップを検出して一緒に保存できる。

## 目的・背景

NanmiCoder による 2023-06 公開のプロジェクト。中国の主要プラットフォームがそれぞれ独自の署名方式を持つため、その都度リバースエンジニアリングが必要だった収集作業を、ログイン状態の流用で共通化した点が普及の理由。★7万・fork 1.3万と、この分野では最大規模。

## 依存関係

- Python 3.9 以上
- Playwright（ブラウザドライバ）と Chromium
- 各プラットフォームのアカウント（ログイン状態を保存して使う）

## 実行条件

- ログイン状態の保存が必要。アカウント停止リスクを伴う。
- Playwright が動くデスクトップ環境（ヘッドレス可）。
- **利用規約・著作権の確認が前提**。収集物の再配布は権利者許諾が必要。学術・個人分析の範囲でも各サイトの規約に従う必要がある。

## 最短手順

```bash
git clone https://github.com/NanmiCoder/MediaCrawler
# README の手順で Playwright を導入し、対象プラットフォームにログインして設定を保存
```

## 変更履歴

- 2026-11-04: 初回登録（★70,094 / pushed 2026-11-03 / ライセンス表記なし・利用条件は要確認）
- 2026-11-06: 抖音・小红书の実況写真（付属動画）取得と、B站の wbi キー取得の耐障害化を追記（ade7a23 / 0be1882）

## 追加出典・確認範囲（2026-11-09）

中国系複数プラットフォームの投稿・コメントを収集するMediaCrawler。

ブラウザログイン状態を使う。個人情報・著作権・サイト規約に沿う範囲に限定する。

原チェックでNON-COMMERCIAL LEARNING LICENSE1.1を確認。既存の「標準ライセンス無し」表記は最新の利用条件説明としては不十分で非商用学習研究限定・大規模収集禁止。

対象固有の機能・制約の説明は2026-11-07のチェック記録を基にしている。メタ情報は2026-11-09T00:30:51.927285+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

### 今回取得した公式メタ情報

既存フロントマターの過去値は維持し、今回の取得値を下に併記する。どちらも実行・性能の追試ではない。

| 項目 | 値 |
|---|---|
| repo | NanmiCoder/MediaCrawler |
| url | https://github.com/NanmiCoder/MediaCrawler |
| license | NOASSERTION |
| language | Python |
| created | 2023-06-09 |
| updated | 2026-11-08 |
| stars | 70663 |
| forks | 13380 |
| open_issues | 219 |
| commits_30d | 21 |
| commits_90d | 47 |
| commit_cadence | daily |
| size_kb | 30756 |
| archived | False |
| fetched_at | 2026-11-09T00:30:51.927285+00:00 |
| license_detail | 原チェックのLICENSE/README解釈: NON-COMMERCIAL LEARNING LICENSE 1.1。APIのSPDX判定とは別。利用前に現行本文を確認。 |


- @Chenfacai0: https://x.com/Chenfacai0/status/2118922893933350978
- 対象資料: https://github.com/NanmiCoder/MediaCrawler
- 参照: https://api.github.com/repos/NanmiCoder/MediaCrawler
- 参照: https://raw.githubusercontent.com/NanmiCoder/MediaCrawler/main/LICENSE

- 2026-11-09: 関連出典と確認範囲を追記。既存の記述・過去の数値・原文プロンプトは維持。今回の実行確認なし。
