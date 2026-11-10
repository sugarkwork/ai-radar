---
repo: "stretchcloud/deepscrape"
name: "DeepScrape"
genre: "mcp-server"
url: "https://github.com/stretchcloud/deepscrape"
flags: ["unverified"]
risk_notes: "READMEに記載された機能と手順を確認した。実行時の動作、サイト変更後の復旧率、破損PDFの解析精度、モデル利用料の具体額は未確認。GitHubの最新版リンクはリリース一覧に遷移し、取得した一覧にはリリースが表示されていなかったため、最新リリースのタグと公開日時は未確認。"
stars: 337
forks: 28
open_issues: 0
size_kb: 9132
language: "TypeScript"
created: "2025-06-05"
updated: "2026-08-21"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 5
commit_cadence: "monthly"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/stretchcloud/status/2119222115862040970"]
fetched_at: "2026-11-10T11:29:46+00:00"
---

# DeepScrapeでWebページの抽出ルールを再利用し、MCPから呼び出す

## 出来ること

- WebページをMarkdownやHTMLなどに変換できる。Site → MCPは保存した抽出設定をサイト別のMCPツールとして公開する。

## 目的・背景

- READMEによると、`/api/extract-auto` はLLMでCSSセレクターを生成し、以降は保存したセレクターで抽出する。抽出ルールが機能しなくなると再生成する。ページ内容をLLMで処理する別経路 `/api/extract` もある。

## 依存関係

- ブラウザー描画にはPlaywright、バックグラウンドジョブにはBullMQとRedisを使う。LLM機能にはOpenAIまたはOpenAI互換エンドポイントを設定できる。

## 実行条件

- READMEのローカル構成はnpmで依存関係を入れ、`.env` にAPIキーとRedisの接続先を設定する。LLMを使う場合はモデルの接続情報も設定する。本体はMITライセンスで、外部モデルの利用料は接続先の条件による。

## 最短手順

- READMEのQuick Startに沿って依存関係と `.env` を準備し、`npm run dev` で起動して `http://localhost:3000/health` を確認する。
- `mcp/` で `npm install` と `npm run build` を実行する。Claude DesktopのMCP設定で `node` と `mcp/dist/server.js` の絶対パスを指定し、`DEEPSCRAPE_API_URL` にローカルAPIのURL、`DEEPSCRAPE_API_KEY` に `.env` で設定したAPIキーを指定する。
- Claudeに `deepscrape_scrape` を使って `https://example.com` をMarkdownで取得するよう依頼する。

## 変更履歴

- 2026-11-10: 初回登録
