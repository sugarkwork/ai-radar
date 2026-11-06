---
repo: CurioCrafter/CurioMesh
name: CurioMesh
genre: 3d-motion
url: https://github.com/CurioCrafter/CurioMesh
license: GPL-3.0
stars: 42
language: Python
created: 2025-08-11
updated: 2026-11-05
added: 2026-11-05
first_seen: 2026-11-05
source_post: https://x.com/happy_modeling/status/2118466746629976101
sources:
  - https://modelinghappy.com/archives/71416
flags: []
risk_notes: ""
forks: 2
open_issues: 1
commits_30d: 100
commits_90d: 100
commit_cadence: daily
size_kb: 48901
archived: false
fetched_at: "2026-11-06T03:32:57Z"
last_release: v0.9.7
last_release_at: 2026-11-05
---

# CurioMesh

## 出来ること

- Blender の**自動リトポロジー**アドオン。高密度メッシュやフォトグラメトリのスキャンを、**オールクワッド**のメッシュに変換する。
- メッシュ全体を一度に処理するほか、**パーツごとに処理して、気になる部分だけ再計算**できる。スライダーでポリゴンサイズを変え、マスクで密度を増減できる。
- 3種類の生成スタイル: 元形状を保つ **Keep Detail**、バランス型 **Balanced**、均一で整ったクワッドを作る **Uniform**（サブディビジョン向き）。
- ガイドカーブでポリゴンの流れを指定できる。
- **ノーマルマップ／カラーテクスチャのベイク**（高密度→ローポリへのディテール転写）と、3段階のLOD生成。
- ゲームエンジン向けの書き出し（Unreal Engine / Unity）。ライブプレビュー付き。

## 目的・背景

生成AIで作った3Dモデルやフォトグラメトリのスキャンは、そのままではポリゴンが多すぎてゲーム・リアルタイム用途に使えない。リトポロジーは手作業だと時間がかかる工程で、それを Blender 内で自動化する。公式サンプルでは 17,456ポリゴンの胸像を、Keep Detail で2,508クワッド、Balanced で3,920クワッドに削減している。

## 依存関係

- Blender（アドオンとしてインストール）。
- 外部Python依存はアドオンに同梱。GPUは必須ではないが、高密度メッシュではCPU時間を使う。

## 実行条件

- GPL-3.0（アドオン）。Blender 本体のバージョン要件は README を確認する。
- 入力は**四角形化できるサーフェス**が前提。穴・非多様体・重なったジオメトリは前処理が必要。
- 生成AIのメッシュ（特にスカルプト系）は形が滑らかすぎる／ノイズが多い場合があり、ガイドカーブとマスクで調整する。
- ★42（2026-11 時点）と小さいが、v0.9.7・直近30日で100+コミットと開発は活発。**AI による Blender 操作の後工程**（生成→リトポ→ベイク→LOD）に組み込みやすい。

## 最短手順

```text
1. GitHub からリポジトリを取得し、Blender の Preferences → Add-ons → Install で zip を入れる
2. 対象メッシュを選択し、CurioMesh パネルを開く
3. スタイル（Keep Detail / Balanced / Uniform）とポリゴン数を指定
4. 必要ならパーツ分割 → 問題箇所だけ再計算
5. ベイク（Normal / Color）→ LOD 作成 → UE / Unity 向けに書き出し
```

## 変更履歴

- 2026-11-05: 初回登録（★42 / pushed 2026-11-05 / GPL-3.0 / v0.9.7）
