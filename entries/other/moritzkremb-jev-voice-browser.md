---
repo: "moritzkremb/jev-voice-browser"
name: "jev-voice-browser"
genre: "other"
url: "https://github.com/moritzkremb/jev-voice-browser"
stars: 431
forks: 71
open_issues: 8
size_kb: 83
language: "JavaScript"
created: "2026-09-17"
updated: "2026-09-21"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 2
commit_cadence: "stale"
flags: ["unverified"]
risk_notes: "性能と費用はREADMEに記載された作者環境での報告で、独立再現、現行のAPI料金・利用条件、確認機構の実効性は未検証。GitHubの公開リリース一覧にはリリースが表示されていない。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/thegreatest_sv/status/2115779290033803462"]
fetched_at: "2026-11-10T12:33:06Z"
---

# jev-voice-browser — 発話の途中結果からChromiumを操作する実装例

## 出来ること

- 音声やテキストでページ移動、検索、クリック、入力、スクロール、タブ切り替えを指示できる。READMEによると、対象要素の候補は最大100件で、iframe内の要素は対象外。

## 目的・背景

- Node.jsサーバーが認識途中の文字列とページ要素の候補をJevに渡し、意図・対象・発話の完了などを判定する。返された確率をルールで評価し、実行・待機・確認・無視を切り替える。検索語や入力文字列は、発話からコードが抽出した候補を使う。
- 作者が2026年9月に報告したフィクスチャ上の実API統合テストは34件中34件成功。Jev応答時間の中央値は約300 msで、作者環境の値。

## 依存関係

- Node.js 20以上、npm、PlaywrightとChromium、TypeSafe SDKおよびJev APIキーが必要。マイク入力にはChromeまたはEdgeのWeb Speech APIを使う。

## 実行条件

- 標準構成ではローカルの制御ページと、操作対象の別Chromiumウィンドウを使う。READMEによると音声はGoogleに送られる。コードはMITライセンスで、README記載のAPI呼び出し費用は1回あたり約0.0002米ドル。現行料金は未確認。

## 最短手順

- READMEに従ってリポジトリを取得し、npm install と npx playwright install chromium を実行する。TypeSafe APIキーを .env に設定して ./run.sh で起動する。
- Chromeで http://localhost:8787 を開き、Start mic を押してマイクを許可し、go to wikipedia などを話す。テキスト欄でも試せる。AI判定の呼び出しはアプリ内の src/jev.js が担当し、入力の更新に応じてTypeSafe SDK経由でJevに判定を求める。

## 変更履歴

- 2026-11-11: 初回登録
