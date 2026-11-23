---
name: "Parametric Topdown Pixel Architecture"
genre: "other"
url: "https://github.com/Zengkailin/parametric-topdown-pixel-architecture"
license: "unknown"
flags: ["unverified"]
risk_notes: "Repository license is reported as unknown. The README says third-party atlas materials may require separate permission; their licensing is not established here. GitHub APIでライセンスを確認できていません。"
repo: "Zengkailin/parametric-topdown-pixel-architecture"
stars: 234
forks: 36
open_issues: 0
size_kb: 13880
language: "JavaScript"
created: "2026-10-26"
updated: "2026-10-31"
archived: false
commits_30d: 5
commits_90d: 5
commit_cadence: "weekly"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/dextune/status/2119399537060270430"]
fetched_at: "2026-11-20T03:23:09.213341+00:00"
---

# Parametric Topdown Pixel Architecture

## 出来ること

- パラメータで作成した建物を、俯瞰のピクセルアート画像にレンダリングするツール。READMEでは、10種類の建築スタイルと46種類の建物タイプ、正交／透視投影、複数方向の画像やスプライトシートの出力、PNG・ZIP・配方JSONの書き出しを案内しています。ブラウザー版と、同じレンダリング機能を使うNode.jsコマンドライン版があります。

## 目的・背景

- READMEによると、Godotプラグイン `hd2d_scene_tools` の幾何とパラメータを参照したウェブ移植版です。Godot向けには、CLIまたはウェブ版から裁剪PNGと`.tscn`のプリセットを出力する機能も説明されています。

## 依存関係

- 通常のブラウザー利用ではREADME記載のとおり、インストール不要で、`index.html`を開いて使用できます。CLIはNode.js 18以上が必要で、npm installは不要とされています。開発スクリプトにはPython 3.10以上とPillowが必要なものがあります。

## 実行条件

- READMEはChromeまたはEdgeを推奨しています。`file://`で空白ページになるなどの問題がある場合は、プロジェクトのディレクトリで`python -m http.server 8000`を起動してローカルサーバー経由で開く手順を示しています。CLIは`node cli/tb.js ...`で実行します。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- ブラウザー版はプロジェクトをダウンロードして展開し、`index.html`または`启动工具.bat`を開きます。スタイルと建物タイプ、形状パラメータや視点を選び、現在方向のPNG、全方向のZIP、またはスプライトシートを出力します。CLIの例は`node cli/tb.js render forest inn -o out/inn.png`です。

## 変更履歴

- 2026-11-23: 初回登録
