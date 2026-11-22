---
name: "Humanizer"
genre: "coding-agent"
url: "https://github.com/blader/humanizer"
repo: "blader/humanizer"
license: "MIT"
stars: 70372
language: "Python"
created: "2026-01-18"
updated: "2026-11-10"
forks: 5526
open_issues: 5
commits_30d: 20
commit_cadence: "daily"
commits_90d: 68
size_kb: 351
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 依存関係。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/suraj_sharma14/status/2122585528906518837"]
fetched_at: "2026-11-18T00:42:02.087265+00:00"
---

# Humanizer

## 出来ること

- READMEによると、文章の主張を保ちながらAI生成文に見られる26種類のパターンを確認し、文章を書き換える。貼り付けた文章では書き換え案と短い批評、最終版を示す。ファイルを指定した場合、コード、データ、frontmatter、リンク先は変更せず、文章表現を編集すると説明されている。個人的な文章では書き手の意見や癖を保ち、技術・参照文書では中立で簡潔な文体にするとしている。

## 目的・背景

- Wikipediaの「Signs of AI writing」を基に、文章中の定型的な表現や構成を見つけて書き換えるスキルとしてREADMEで紹介されている。作者はAI検出器の回避を目的としておらず、出力の多くは検出器に判定されると説明している。README記載のブラインドテストでは16回すべてでHumanizerの書き換えが元のAI文より好まれたとしているが、これはREADME上の作者側の報告であり、独立検証ではない。

## 依存関係

- READMEに明記された依存関係は確認できない。

## 実行条件

- READMEによると、Claude CodeプラグインにはClaude Code 2.1.142以降が必要。CodexではSkills CLIを使って導入できる。

## 最短手順

- Codexでは `npx skills add blader/humanizer --global --agent codex` で全体にインストールし、`/humanizer` の後に文章を貼り付けるか、「Please humanize this text: [your text]」のように依頼する。特定のファイルを編集する場合は、そのパスを指定する。

## 変更履歴

- 2026-11-22: 初回登録
