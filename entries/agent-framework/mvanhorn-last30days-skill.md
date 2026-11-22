---
name: "last30days-skill"
genre: "agent-framework"
url: "https://github.com/mvanhorn/last30days-skill"
repo: "mvanhorn/last30days-skill"
language: "Python"
archived: false
flags: ["unverified"]
risk_notes: "READMEは現行のコマンドやセットアップ動作の正本を別ファイルのSKILL.mdとして案内していますが、その内容は今回の資料に含まれていません。READMEに記載された追加ソースや効果の範囲は独立確認していません。"
stars: 69049
forks: 6145
open_issues: 21
size_kb: 58496
created: "2026-01-23"
updated: "2026-11-17"
license: "MIT"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/suraj_sharma14/status/2122585528906518837"]
fetched_at: "2026-11-18T00:41:25.925263+00:00"
---

# last30days-skill

## 出来ること

- READMEの説明では、Reddit、Hacker News、GitHubなど複数の情報源を検索し、エンゲージメント指標を使って結果を評価し、AIエージェントが要約します。利用できる情報源や認証条件はソースごとに異なります。

## 目的・背景

- 作者は、AI分野の変化やコミュニティの新しい情報を追うために作り、営業前の企業調査や会議前の人物調査などにも使うようになったと説明しています。これはREADMEにある作者の説明です。

## 依存関係

- READMEには、Claude Codeのマーケットプレイス経由、またはAgent Skills対応ホスト向けのnpx skills addコマンドによる導入方法が記載されています。一部の情報源には追加CLI、APIキー、ログイン済みセッションなどが必要とされています。個別の必須依存関係の全容は、添付READMEだけでは確認できません。

## 実行条件

- README記載の導入例は、Claude Codeでは「/plugin marketplace add mvanhorn/last30days-skill」「/plugin install last30days」、その他の対応ホストでは「npx skills add mvanhorn/last30days-skill -g」です。情報源によって追加設定や認証が必要です。現行の詳細な動作条件はREADMEが案内するSKILL.mdを確認してください。

## 最短手順

- 対応するエージェント環境で「npx skills add mvanhorn/last30days-skill -g」を実行して導入し、READMEの例にある「/last30days Peter Steinberger」のように調査対象を指定します。コマンドと利用例はREADME記載のものです。

## 変更履歴

- 2026-11-22: 初回登録
