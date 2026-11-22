---
name: "Aliens Eye"
genre: "other"
url: "https://github.com/arxhr007/Aliens_eye"
repo: "arxhr007/Aliens_eye"
license: "MIT"
stars: 4836
language: "Python"
created: "2021-09-22"
updated: "2026-11-15"
forks: 573
open_issues: 0
commits_30d: 19
commit_cadence: "weekly"
commits_90d: 53
size_kb: 24095
archived: false
flags: []
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
risk_notes: ""
sources: ["https://x.com/bkdgiffug/status/2119212049398210763"]
fetched_at: "2026-11-17T13:11:58.567951+00:00"
---

# Aliens Eye

## 出来ること

- READMEでは、ユーザー名を7,700以上のプラットフォームで非同期に検索し、見つかったプロフィールの表示名・自己紹介・アバターを抽出する機能を説明しています。アバターや自己紹介などによるプロフィールの相関分析、リンク先ユーザー名の再帰検索、ドメイン確認、定期再スキャン、途中再開、JSON・CSV・HTML・Markdown・PDF・グラフ形式でのレポート出力にも対応するとしています。検出結果の精度評価や、保存したレスポンスコーパスを使った再現可能な評価機能も記載されています。これらはREADME上の説明で、独立した性能検証ではありません。

## 目的・背景

- READMEは本ツールを「AI-OSINT Username Scanner」と説明し、複数サイトにまたがるユーザー名検索と検出結果の分析を用途として挙げています。

## 依存関係

- READMEに記載された任意機能の追加依存は、browser が Playwright、train が scikit-learn、correlate が Pillow、pdf が reportlab、tui が textual、serve が mcp です。基本機能の依存関係一覧は提示されたREADME本文では確認できません。

## 実行条件

- READMEは `pip install aliens-eye` によるインストールを案内しています。ブラウザー機能を使う場合は `pip install "aliens-eye[browser]"` と `python -m playwright install chromium`、Tor利用時はローカルのTorデーモンが必要と記載されています。実際の動作環境での確認は行っていません。

## 最短手順

- README記載の手順は、`pip install aliens-eye` でインストールし、`aliens_eye username` を実行する方法です。Docker利用時は `docker build -t aliens-eye .` の後に `docker run --rm -it aliens-eye username` を実行します。

## 変更履歴

- 2026-11-22: 初回登録
