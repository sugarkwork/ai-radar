---
repo: "anishfn/shapeshift"
name: "Shapeshift"
genre: "other"
url: "https://github.com/anishfn/shapeshift"
stars: 1066
forks: 106
open_issues: 6
size_kb: 12116
language: "TypeScript"
created: "2026-09-22"
updated: "2026-09-23"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 18
commit_cadence: "monthly"
last_release: ""
last_release_at: ""
flags: ["unverified"]
risk_notes: ["READMEと公開ソースを確認。コードは実行しておらず、分類精度、曖昧な入力での挙動、実応答時間、オンライン障害時のフォールバックは未実測。TypeSafe APIの現行料金と利用条件は未確認。"]
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/thegreatest_sv/status/2115779290033803462"]
fetched_at: "2026-11-10T12:34:19+00:00"
---

# Shapeshift — 自然文から用途に合うUIカードを選ぶ

## 出来ること

- 1つの入力欄から予定、チェックリスト、タイマー、割り勘などの既定カードを選ぶ。作者の例では `split 2400 between 3` で1人あたり₹800を表示する。保存したカードはブラウザーの localStorage に残る。

## 目的・背景

- オンラインではTypeSafe Jevへの1回の呼び出しで、カード種別や緊急度など14問を並列評価する。日付・金額・単位の抽出や計算はTypeScriptのパーサーが担当する。作者によると、状態機械は別の候補が連続して優勢になるか十分に確信度が高い場合にカードを切り替え、入力途中の表示の揺れを抑える。

## 依存関係

- Bun 1.2以上。Next.js App Router、React 19、TypeScript、Tailwind CSS v4、shadcn/ui、Motion、chrono-node、zodを使用する。リポジトリはMIT。

## 実行条件

- 既定は組み込みのキーワード分類で、起動後は外部の分類サービスやアカウントが不要。オンラインモードではサーバー側にTypeSafe APIキーを設定し、入力文を外部サービスへ送る。公開ルートのコードでは、オンライン分類成功時に正規化した入力の先頭40文字をサーバーログに出力する。
- GitHubの公開Releasesページではリリースなしと表示された。

## 最短手順

- リポジトリを取得し、`bun install`、`bun dev` の順に実行する。`http://localhost:3000` を開き、`split 2400 between 3` を入力する。`/` キーでカードの種類を一覧できる。
- AIから呼ぶ場合は、起動したローカルアプリの `/api/intent` に `POST` で `Content-Type: application/json` と `text` フィールドを含むJSONを送る。返るのは意図分類の結果。Jevを使う場合は `.env.example` を `.env.local` にコピーし、サーバー側の `TYPESAFE_API_KEY` を設定して再起動する。

## 変更履歴

- 2026-11-11: 初回登録
