---
repo: "warpdotdev/common-skills"
name: "Common Skills"
genre: "coding-agent"
url: "https://github.com/warpdotdev/common-skills"
license: "MIT"
stars: 686
language: "Python"
created: "2026-04-30"
updated: "2026-10-28"
forks: 44
open_issues: 45
commits_30d: 2
commit_cadence: "monthly"
commits_90d: 20
size_kb: 1022
archived: false
flags: ["unverified"]
risk_notes: "評価精度、レビュー時間の短縮効果、導入コマンドの実動作、ホスト環境ごとの互換性、最新リリースは未確認。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/sumika45379/status/2115643537048154583"]
fetched_at: "2026-11-10T12:28:27+00:00"
---

# Warp Common Skills — /merge-risk でPRのマージリスクを5観点から確認

## 出来ること

- PRの目的との整合性、影響範囲、検証の証拠、ロールバックの負担、障害検知のしやすさを評価し、総合リスクを低・中・高で返す。各観点ではリスクを高める不足点を挙げる。
- 定義では影響範囲と検証を各2倍、ロールバックを1.5倍で重み付けする。ユーザー体験が変わる場合はスクリーンショットや録画によるE2Eの証拠を求める。

## 目的・背景

- Warp が複数のリポジトリで再利用できるエージェント向け手順を共有するコレクション。merge-risk はレビュー時に、追加で読む箇所や不足している検証を絞るために使える。評価精度やレビュー時間の短縮は未検証。

## 依存関係

- 共有スキルの導入には README 記載の skills CLI（npx 経由）を使うか、対象ディレクトリをプロジェクトの .agents/skills/ に配置する。リポジトリのライセンスは MIT。

## 実行条件

- スキルを読み込めるエージェントに、対象のPR差分、PR説明、関連チケットや検証結果を参照できる状態で渡す。利用できる証拠に応じて、評価で指摘される不足点が変わる。

## 最短手順

- README の単体導入例のスキル名を置き換え、Warp 向けに `npx skills@latest add warpdotdev/common-skills --skill merge-risk --agent warp --global` で導入する。
- 対象PRを参照できる状態で Warp エージェントに `/merge-risk` を使って評価するよう依頼し、総合リスクと観点ごとの不足点を確認する。

## 変更履歴

- 2026-11-10: 初回登録
