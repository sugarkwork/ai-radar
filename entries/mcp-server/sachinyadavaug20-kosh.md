---
repo: "SachinyadavAug20/kosh"
name: "Kosh"
genre: "mcp-server"
url: "https://github.com/SachinyadavAug20/kosh"
license: "Apache-2.0"
stars: 4
forks: 0
open_issues: 0
size_kb: 26429
language: "TypeScript"
created: "2026-10-30"
updated: "2026-11-10"
archived: false
commits_30d: 61
commits_90d: 61
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: ["実機での起動、クライアントとの接続、GLBの生成品質や処理時間、最新リリース、M8ven評価は未確認。README内でBlenderの対応版とツール数の記述に幅があり、実際の対応範囲は未確認。Gemini APIの利用料金は未確認。"]
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/samtagon38824/status/2118037888986460441"]
fetched_at: "2026-11-10T11:43:29+00:00"
---

# Kosh — AIクライアントからBlenderを操作する3D制作向けMCPサーバー

## 出来ること

- READMEでは、パラメトリックCAD、スカルプト、アニメーションを扱い、生成したメッシュをGLBとして取り出せるとしている。

## 目的・背景

- Spring BootのMCPサーバーがAIクライアントからJSON-RPCを受け取り、Blenderをヘッドレスで実行する。Web StudioはNext.jsとThree.jsを使う構成。

## 依存関係

- READMEの前提条件はOpenJDK 21以上、Maven 3.9以上、Node.js 20以上、npm 10以上、Blender 4.xまたは5.x LTS。stdioブリッジを使う場合はPython 3も必要。

## 実行条件

- READMEのローカル構成ではMCPサーバーが8080、Web Studioが3000で待ち受ける。Geminiを使う生成例では利用者のAPIキーをX-Google-Keyヘッダーで渡す。リポジトリのライセンスはApache-2.0。

## 最短手順

- READMEの手順では、依存関係をPATHに通し、リポジトリのルートでBashからrun.shを起動する。
- SSE対応のMCPクライアントにhttp://localhost:8080/mcp/sseを登録する。stdioを使う場合はpython3とscripts/kosh_mcp_stdio.pyの絶対パスを登録する。
- 接続後にtools/listで公開ツールを確認し、AIクライアントから簡単な形状の作成を依頼する。READMEの生成例はcad_modelにpromptとformat=glbを渡す。

## 変更履歴

- 2026-11-10: 初回登録
