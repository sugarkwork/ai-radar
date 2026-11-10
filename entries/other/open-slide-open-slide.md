---
repo: "open-slide/open-slide"
name: "open-slide"
genre: "other"
url: "https://github.com/open-slide/open-slide"
license: "MIT"
stars: 9729
language: "TypeScript"
created: "2026-04-26"
updated: "2026-11-09"
forks: 716
open_issues: 146
commits_30d: 33
commit_cadence: "daily"
commits_90d: 100
size_kb: 61930
archived: false
flags: ["unverified"]
risk_notes: "公開リリース一覧では @open-slide/core@2.3.2 が Latest と表示された一方、取得した /releases/latest はキャッシュから @open-slide/core@2.0.1 に転送されたため、最新タグと公開日時は未確定。CLIやエージェントは実行しておらず、制作時間の短縮、PPTXの再現性・編集互換性、エージェント側の契約・料金は未検証。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/opensourcelab9/status/2115571817826103426"]
fetched_at: "2026-11-10T12:26:43+00:00"
---

# open-slideでReactスライドを作り、画面上のコメントで修正する

## 出来ること

- コーディングエージェントでスライドを下書きし、ブラウザーで確認できる。公式READMEには静的HTML・PDF・編集可能なPPTXへの書き出しと、発表者ノート・タイマー付きの発表モードが記載されている。

## 目的・背景

- 各ページをReactコンポーネントとして記述し、固定の1920×1080キャンバスの拡大縮小やページ送りはフレームワークが担当する。画面上で付けた修正コメントはソース内のマーカーとして保存され、エージェントがまとめて処理する。

## 依存関係

- 初期化には npx と @open-slide/cli、開発サーバーの起動には pnpm を使う。描画はReact、開発基盤はVite。公式のcore 2.0.0リリースノートではNode.js 20.19以上が必要とされている。

## 実行条件

- ローカルの開発サーバーとブラウザーを使う。AIによる作成・修正にはClaude Codeなどのコーディングエージェントを用意する。公式リリースノートでは、アプリ内パネルからローカルに導入済みのClaude CodeまたはCodexを使う機能も案内されている。リポジトリのライセンスはMIT。

## 最短手順

- `npx @open-slide/cli init my-slide` で初期化し、`cd my-slide` に続けて `pnpm dev` で起動する。
- 生成された作業ディレクトリでClaude Codeを開き、`/create-slide` を呼ぶ。題材と見た目、枚数、文字量、動きの有無を伝える。
- ブラウザーで対象要素に修正コメントを付け、Claude Codeで `/apply-comments` を呼んで反映する。

## 変更履歴

- 2026-11-10: 初回登録
