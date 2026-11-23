---
name: "three-bmfont-text"
genre: "3d-motion"
url: "https://github.com/Experience-Monks/three-bmfont-text"
repo: "Experience-Monks/three-bmfont-text"
license: "MIT"
stars: 803
language: "JavaScript"
created: "2015-03-12"
updated: "2022-03-22"
forks: 173
open_issues: 33
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 703
archived: false
flags: ["unverified"]
risk_notes: "READMEでは安定性バッジが「unstable」とされ、README記載の最新3.xはThree.js r109以降向け。リポジトリ情報では最終更新が2022-03-22のため、現在のThree.jsとの互換性は未確認。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/0xclayo/status/2123016316353155192"]
fetched_at: "2026-11-18T14:13:10.730582+00:00"
---

# three-bmfont-text

## 出来ること

- Three.jsでビットマップフォントを描画するためのBufferGeometryを生成します。READMEによると、グリフを単一のBufferGeometryにまとめ、単語の折り返し、文字間隔、カーニング、SDF/MSDF、複数テクスチャのフォントに対応します。生成したgeometryはupdate()でテキストやレイアウトを更新できます。

## 目的・背景

- BMFontの文字定義とテクスチャを使ったテキスト描画をThree.jsで扱うためのライブラリです。READMEでは、minify後のサイズを約12kbと説明しています。

## 依存関係

- READMEの使用例では、BMFont定義の読み込みにload-bmfontを使い、レイアウト処理はlayout-bmfont-textを基盤としています。

## 実行条件

- README記載の3.x系はThree.js r109以降向けです。旧版Three.jsでは、r69–73およびr79–108向けとしてthree-bmfont-text@2.3.0が案内されています。

## 最短手順

- npmからthree-bmfont-textを導入し、BMFont定義を用意します。READMEの例ではload-bmfontで定義を読み込み、createText({ font, text, width, align })でgeometryを生成し、テクスチャを読み込んでThree.Meshに渡します。実際の描画コードやオプションはREADMEのUsageを参照してください。

## 変更履歴

- 2026-11-23: 初回登録
