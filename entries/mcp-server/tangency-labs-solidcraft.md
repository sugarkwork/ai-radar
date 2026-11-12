---
name: "SolidCraft"
genre: "mcp-server"
url: "https://github.com/tangency-labs/solidcraft"
repo: "tangency-labs/solidcraft"
flags: ["unverified"]
risk_notes: "ライセンス表記に差異があります。READMEは「MIT OR Apache-2.0」と記載していますが、提供された測定値ではApache-2.0です。採用前にライセンスファイルを確認してください。"
stars: 15931
forks: 2181
open_issues: 6652
size_kb: 531665
language: "Rust"
created: "2026-10-07"
updated: "2026-11-12"
archived: false
license: "Apache-2.0"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-12"
first_seen: "2026-11-12"
sources: ["https://x.com/Leviwoyun/status/2118546148860526934"]
fetched_at: "2026-11-12T15:11:02.435866+00:00"
---

# SolidCraft

## 出来ること

- パラメトリックな3D CADアプリ。スケッチ、拘束、フィーチャーのタイムライン、パラメーター、アセンブリ、板金機能を備えるとREADMEに記載。STEP、IGES、3MF、STL、OBJ、glTFの入出力（対応範囲内）とURDF出力、デスクトップ・ブラウザー・ヘッドレスCLI・MCPサーバーの提供も記載されている。

## 目的・背景

- READMEでは、簡単な部品向けに「Early but usable」と説明し、公開参照部品76件中75件で解析値またはFreeCAD計算値と一致したと作者が報告している。これはREADME上の作者報告であり、独立した実測ではない。

## 依存関係

- READMEには依存関係の一覧は記載されていない。

## 実行条件

- READMEにはWindows、macOS、Linux向け配布物とブラウザー版が案内されている。ソースからの実行例にはRustのCargoコマンドが示されている。

## 最短手順

- デスクトップアプリは `cargo run --release -p solidcraft -- --sample`。MCPサーバーは `solidcraft-cli mcp` で起動でき、Claude Codeへの登録例として `claude mcp add solidcraft -- solidcraft-cli mcp` がREADMEに記載されている。

## 変更履歴

- 2026-11-12: 初回登録
