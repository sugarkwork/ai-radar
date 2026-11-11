---
name: "Sverchok"
genre: "3d-motion"
url: "https://github.com/nortikin/sverchok"
repo: "nortikin/sverchok"
license: "GPL-3.0"
stars: 2557
language: "Python"
created: "2013-10-26"
updated: "2026-11-10"
forks: 247
open_issues: 212
commits_30d: 24
commit_cadence: "daily"
commits_90d: 28
size_kb: 732639
archived: false
flags: ["unverified"]
risk_notes: "Blender 5.1、4.5、3.6、2.8対応との記載。追加ライブラリは一部ノードで必要。個別機能の依存条件はREADME記載のDependencies資料を参照。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/RealMarvelX/status/2118330503040221345"]
fetched_at: "2026-11-11T20:09:27.753551+00:00"
---

# Sverchok

## 出来ること

- Blender上でノードを組み合わせ、メッシュ、曲線、サーフェス、ソリッドなどの幾何を作成・編集するアドオン。READMEには600超のノード、パラメトリック構成、断面・押し出し等の加工、面積・体積計算、CSV等の入出力、ベクトル・スカラー場、SVG/DXF出力、BREP/NURBS/IFCデータ交換などが記載されている。出典: https://github.com/nortikin/sverchok

## 目的・背景

- 建築家やデザイナー向けに、ノードを用いた幾何のビジュアルプログラミングを提供する。座標・辺・面のリスト、変換行列、曲線、サーフェス、場、ソリッドなどを扱う。出典: https://github.com/nortikin/sverchok

## 依存関係

- README記載の前提Blenderバージョンは5.1、4.5、3.6、2.8。一部の追加ノードやスクリプトはscipy、marching cubes、geomdl、scikit-image、shapely、circlify、freecadpython3libなどを利用する。個別の依存条件はREADMEからリンクされたDependencies資料に記載。出典: https://github.com/nortikin/sverchok

## 実行条件

- Blenderアドオンとして使用する。追加ライブラリを必要とするノードもある。READMEはPython Scripted nodeやBlender Python API（bpy）を利用する機能も挙げている。出典: https://github.com/nortikin/sverchok

## 最短手順

- READMEの手順では、GitHubのmaster ZIPをダウンロードし、展開せずにBlenderのEdit > Preferences > Add-onsからInstall...で選択してインストールし、「Node: Sverchok」を有効化する。出典: https://github.com/nortikin/sverchok

## 変更履歴

- 2026-11-11: 初回登録
