---
repo: "dreammis/social-auto-upload"
name: "social-auto-upload"
genre: "other"
url: "https://github.com/dreammis/social-auto-upload"
license: "MIT"
stars: 16378
forks: 2777
open_issues: 87
size_kb: 24752
language: "Python"
created: "2023-12-04"
updated: "2026-10-22"
archived: false
commits_30d: 16
commits_90d: 43
commit_cadence: "weekly"
last_release: "v1.0.0-skills.2"
flags: ["unverified"]
risk_notes: "対応表は開発元の記載。実アカウントでのログイン、投稿成功率、定時公開、処理時間、各サービスの規約適合性は未検証。最新リリースのタグは確認済みだが、公開年とタイムゾーンを含む日時は未確認。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/ganfanren_ai/status/2117237474493968435"]
fetched_at: "2026-11-10T08:28:22Z"
---

# social-auto-upload｜動画・画像付き投稿・記事を配信するCLIとAgent Skill

## 出来ること

- READMEの対応表では、抖音・快手・小紅書は動画と画像付き投稿、Bilibiliは動画、大魚号と知乎は動画と記事に対応する。YouTubeの定時投稿は開発中、知乎の定時投稿は実験的とされている。

## 目的・背景

- 投稿先ごとに異なる入力と公開操作を、共通の `sau` コマンド体系にまとめる。エージェントは共通または投稿先別のSkillから、対象サービスの手順を参照できる。

## 依存関係

- パッケージ定義はPython 3.10以上3.13未満を指定する。導入ガイドはuvを推奨し、ブラウザー操作にPatchrightとChromiumを使う。READMEによるとBilibiliの初回実行時にはbiliupを自動取得する。

## 実行条件

- 投稿先ごとのアカウントと有効なログインセッションが必要。`--account` はローカルのセッション識別名。コードのライセンスはMIT。投稿先サービスの利用条件は個別に確認する。

## 最短手順

- [導入ガイド](https://github.com/dreammis/social-auto-upload/blob/main/docs/install.md)に沿ってCLIとChromiumを準備し、`sau douyin --help` で入口を確認する。
- 対応エージェントに `npx skills add dreammis/social-auto-upload --skill douyin-upload` で抖音用Skillを追加する。利用者が `sau douyin login --account creator` でログインし、エージェントに `sau douyin check --account creator` で状態を確認させる。
- 投稿内容とアカウントを確認してから、エージェントに `sau douyin upload-video --account creator --file videos/demo.mp4 --title タイトル` を実行させる。このコマンドは実際の投稿操作を行う。

## 変更履歴

- 2026-11-10: 初回登録
