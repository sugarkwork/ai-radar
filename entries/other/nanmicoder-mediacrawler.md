---
repo: NanmiCoder/MediaCrawler
name: MediaCrawler
genre: other
url: https://github.com/NanmiCoder/MediaCrawler
license: 未確認（API は NOASSERTION、標準ライセンスファイル無し）
language: Python
created: 2023-06-09
updated: 2026-11-06
added: 2026-11-04
first_seen: 2026-11-04
sources:
  - https://x.com/leo_xiaolei/status/2117517260470485470
flags: []
risk_notes: "各プラットフォームの利用規約と著作権に抵触しうる。収集した投稿・動画の再配布は権利者の許諾が必要。規約違反・アカウント停止のリスクは利用者側。"
stars: 70399
forks: 13343
open_issues: 220
commits_30d: 17
commits_90d: 39
commit_cadence: weekly
size_kb: 30690
archived: false
fetched_at: "2026-11-06T22:52:46Z"
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
