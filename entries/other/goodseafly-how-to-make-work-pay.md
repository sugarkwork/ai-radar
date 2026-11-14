---
name: "高性价比职场指南"
genre: "other"
url: "https://github.com/goodseafly/how-to-make-work-pay"
repo: "goodseafly/how-to-make-work-pay"
license: "unknown"
stars: 489
forks: 43
open_issues: 1
size_kb: 53935
language: "HTML"
created: "2026-10-06"
updated: "2026-10-26"
archived: false
commits_30d: 12
commits_90d: 32
commit_cadence: "weekly"
flags: ["unverified"]
risk_notes: "GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/bkdgiffug/status/2118700427801919767"]
fetched_at: "2026-11-13T19:08:05.018658+00:00"
---

# 高性价比职场指南

## 出来ること

- READMEによると、職場の採用、契約、賃金、休暇、社会保険、労災、退職、解雇などについて、576件の提案を検索・閲覧できます。オンライン検索ページにはキーワード、章、証拠レベル、コストによる絞り込みがあり、オフライン版も案内されています。

## 目的・背景

- 中国大陸の現行制度をもとに、仕事に関する判断材料を提供するガイドです。各提案にはコスト、見込む利益、証拠レベル、出典が記載されるとREADMEにあります。

## 依存関係

- READMEでは、オンライン検索ページは静的ページで、バックエンドやデータベース、依存パッケージは不要と説明されています。PDF生成にはpandoc 3.1以上とtypst 0.13以上が必要です。チェック用スクリプトは標準ライブラリのみで動作すると記載されています。

## 実行条件

- オンライン検索ページはHTTP経由で開く必要があります。READMEにある最短のローカル起動例は `python -m http.server 8000` です。オフライン単一HTML版はブラウザーで直接開けると説明されています。

## 最短手順

- 読むだけならREADME記載のオンライン検索ページを開き、キーワードや章などで絞り込みます。ローカルでオンラインページを確認する場合は、リポジトリ内で `python -m http.server 8000` を実行し、ブラウザーでローカルサーバーを開きます。生成物の再構築には用途別の `tools/build-*.py` スクリプトが案内されています。

## 変更履歴

- 2026-11-14: 初回登録
