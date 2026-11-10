---
repo: "citrolabs/ego-lite"
name: "ego lite"
genre: "other"
url: "https://github.com/citrolabs/ego-lite"
stars: 22387
forks: 1269
open_issues: 271
size_kb: 9054
language: "JavaScript"
created: "2026-04-16"
updated: "2026-11-10"
archived: false
license: "MIT"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
last_release: "v2.1.0"
flags: ["unverified"]
risk_notes: "公式リリース一覧ではv2.1.0がLatestと表示された。最新リリースへの直接アクセスはタイムアウトし、公開日時は未確認。作者ベンチマークの再現性、ブラウザデータの取り扱い、Spaces間の分離の実効性は未検証。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/opensourcelab9/status/2117504564941508613"]
fetched_at: "2026-11-10T09:19:17Z"
---

# ego lite — AIエージェントと並行作業できるブラウザ

## 出来ること

- CodexやClaude Codeが専用のSpaceでページを開き、構造化テキストとして内容を読み取ったり、フォームに入力したりできる。利用者は自分のSpaceで閲覧を続けられる。

## 目的・背景

- 利用者とエージェントが同じブラウザ内の別々の作業領域で並行して作業する設計。ego-browserは、エージェントがページ操作をJavaScript関数として組み合わせるための接続層を提供する。
- 開発元は実サイト上の31タスクで他の4ツールと比較し、速度、成功率、費用で優位だったと報告している。独立した再測定は行っていない。

## 依存関係

- ego-browserスキルには、ego-browserコマンドを提供するego liteブラウザ本体と、スキルを呼び出すエージェントCLIが必要。

## 実行条件

- README記載の対応OSはmacOSとWindows。リポジトリの内容はMITライセンスで、ブラウザ本体は別途無料で配布される。
- 初回起動時にChromeデータの移行を選ぶと、既存のログイン状態やCookieをエージェントから利用できるとREADMEに記載されている。

## 最短手順

- 公式READMEから対応OS向けのアプリを導入する。
- 対応するエージェントCLIで `/ego-browser` に続けて、公開ページを開いて見出しを読み取るなどの依頼を入力する。

## 変更履歴

- 2026-11-10: 初回登録
