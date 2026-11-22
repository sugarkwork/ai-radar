---
name: "yuwen-publish-precheck｜发布前审"
genre: "coding-agent"
url: "https://github.com/yuwen-cool/yuwen-publish-precheck"
repo: "yuwen-cool/yuwen-publish-precheck"
license: "MIT"
stars: 816
language: "Python"
created: "2026-07-15"
updated: "2026-10-08"
forks: 78
open_issues: 0
commits_30d: 0
commit_cadence: "monthly"
commits_90d: 4
size_kb: 130
archived: false
flags: ["unverified"]
risk_notes: "検出精度やプラットフォームでの審査結果に関する説明はREADME内の作者の記述・例であり、独立した検証結果ではない。README自身も審査通過を保証せず、最終判断はプラットフォーム側に依存するとしている。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/ruyi3699/status/2118862747832025357"]
fetched_at: "2026-11-16T21:48:35Z"
last_release: "v1.0.6"
last_release_at: "2026-09-16"
---

# yuwen-publish-precheck｜发布前审

## 出来ること

- READMEによると、抖音・小红书・微信视频号向けに投稿文を確認し、問題箇所の指摘、修正文の提案、修正後の再確認を行う。利用者のルールや事例をローカルの data/ に蓄積する機能も説明されている。

## 目的・背景

- 作者は、投稿前に表現上の懸念を見つけて修正を支援することを目的として説明している。READMEでは「可以发」は今回の確認範囲で阻断問題が見つからなかったという意味で、審査通過を保証しないとしている。

## 依存関係

- README記載ではPython 3.10以上が必要で、第三者Python依存はない。Agent Skillsに対応するツールでの利用を案内している。

## 実行条件

- README記載ではローカル実行で、原稿と個人データは第三者へアップロードしない。初回利用時に、常用プラットフォーム、業種、商業モデルなどの利用者プロフィールを作成する案内がある。

## 最短手順

- README記載の手順は、Agent Skills対応ツールに「请安装这个 skill：https://github.com/yuwen-cool/yuwen-publish-precheck.git」と依頼する方法、または案内されたスキルディレクトリへgit cloneする方法。インストール後、対象の投稿文を添えて確認を依頼する。

## 変更履歴

- 2026-11-14: 初回登録
