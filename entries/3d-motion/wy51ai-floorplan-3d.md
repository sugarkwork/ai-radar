---
repo: "wy51ai/floorplan-3d"
name: "floorplan-3d"
genre: 3d-motion
url: "https://github.com/wy51ai/floorplan-3d"
license: "MIT"
stars: 3393
language: "HTML"
created: "2026-09-29"
updated: 2026-10-02
added: "2026-11-03"
first_seen: "2026-11-03"
sources: []
flags: []
risk_notes: ""
forks: 707
open_issues: 10
commits_30d: 0
commits_90d: 9
commit_cadence: monthly
size_kb: 18
archived: false
fetched_at: "2026-11-03T22:59:07Z"
---

# floorplan-3d

## 出来ること

- ブラウザだけで動く間取り・リフォーム設計ツール。2D 平面図に家具を置き、壁を撤去し、寸法を測り、そのまま Three.js の3Dシーンに切り替えて確認できる。アプリ全体が `index.html` 1枚で、ビルド不要。
- 2D: 原図の 1:60 / 1:100 表示（単位 mm）、60種以上の家具・家電をドラッグ配置、Shift で自由角度の回転、サイズ変更、壁への自動スナップ。寸法測定（壁際スナップ、Shift で水平/垂直固定）。非耐力壁の撤去と耐力壁の表示。レイヤ切替（寸法・部屋名・家具・グリッド・耐力壁）。
- 3D: 鳥瞰・斜視・俯視の切替、部屋リストから該当室へカメラ移動、WASD＋マウス（タッチは仮想スティック）での漫游、ドアの開閉、壁の全高/断面切替、日照時間スライダー、夜景照明。3D上でも家具を選択・移動でき、2D と同期する。
- 集計と出力: 部屋面積と内法面積の自動計算、部屋ごとの床材変更（フローリング・タイル・大理石・テラゾ・カーペット）と面積＋5%ロスでの概算、Undo/Redo、localStorage への自動保存、PNG 書き出し、プラン JSON の入出力、中文/English 切替。

## 目的・背景

リフォーム検討時に、平面図と3Dを行き来しながら家具配置と壁の撤去可否を確認したい、という用途に絞ったツール。フレームワークもビルド工程も使わず、SVG で2D、Three.js r160 で3Dを描く構成にして、ファイル1つで配布できるようにしている。

## 依存関係

- モダンブラウザのみ。Three.js は jsDelivr の CDN から読み込む。
- ローカルサーバを立てる場合は Python 3（`python3 -m http.server`）。

## 実行条件

- 初回の3D表示にはネット接続が必要（CDN 依存）。オフライン運用するなら Three.js をローカルに落として参照先を変える。
- 户型データは `index.html` 内の定数（`ROOMS` / `WALLS` / `WINS` / `MATS` / `LIB`）で定義されている。自分の間取りに変えるにはここを編集する。
- 面積・概算はブラウザ内の計算で、法規や実測の代替にはならない。

## 最短手順

```bash
git clone https://github.com/wy51ai/floorplan-3d.git
cd floorplan-3d
python3 -m http.server 8000
# http://localhost:8000
```

## 変更履歴

- 2026-11-03: 初回登録（star 3,393 / pushed 2026-10-02 / MIT）
