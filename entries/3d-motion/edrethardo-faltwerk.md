---
type: "repo"
name: "Faltwerk"
genre: "3d-motion"
url: "https://github.com/edrethardo/Faltwerk"
author: "Aaron Nowak (@edrethardo) / James Kane (@jameskane05) — co-developer, testing, feedback"
repo: "edrethardo/Faltwerk"
license: "MIT"
stars: 36
language: "Python"
created: "2026-10-27"
updated: "2026-11-04"
added: "2026-11-07"
first_seen: "2026-11-05"
sources: ["https://x.com/tokufxug/status/2118171681437175920", "https://jameskane05.github.io/faltwerk-demo/", "https://github.com/edrethardo/Faltwerk"]
flags: []
risk_notes: "研究コード（作成 2026-10-27、コミット3件、リリース・PyPI 無し、README に Research code, moving quickly）。画像ソースの学習は PyTorch + gsplat 1.5 + CUDA GPU（24GB 推奨）と外部データセットが必要。MCP サーバ・REST API・Agent Skill は無く、呼び出し口は CLI と Python API のみ。GitHub API の license 判定は NOASSERTION だが LICENSE 本文は MIT。 投稿の「1.4GB→5〜7MB」「Quest 3 で 25〜40Mbps」は投稿者の比較値で、本項目では採用していない。"
forks: 3
open_issues: 0
commits_30d: 3
commit_cadence: "sporadic（作成 2026-10-27 から3日で3コミット、以降 2026-11-04 の最終 push まで停止）"
size_kb: 1429
archived: false
fetched_at: "2026-11-07T11:44:12Z"
source_post: "https://www.linkedin.com/posts/james-c-kane_can-i-interest-anyone-in-a-tiny-angry-james-ugcPost-7523402576223203328-Bdc8/"
---

# Faltwerk — 4D Gaussian Splatting を曲線で圧縮し WebGPU で配信する codec

## 出来ること

- .falt ビットストリームの Python リファレンス実装（encoder / decoder、rANS・曲線・コードブック・予測）を同梱。python -m codec.measure で、同じシンボルに対するエンコード・復号・サイズと所要時間の測定ができる。
- 標準レシピ tools/faltwerk_recipe.py が scene.json（データのみ）から recipe.sh を組み立て、前処理・学習・エンコード・復号評価までを通す。--rate-target <Mbit/s> を付けると、その配信レートに収まるよう splat を間引いて再微調整する。
- 入力は3系統: 順視カメラ画像（LLFF / N3DV 形式）、マット付きマルチカメラリグ（フレームごとの教師モデルあり）、3D ソフトのアニメーションメッシュ。メッシュは train/mesh/mesh2gs.py がジオメトリから直接 splat を作るため学習が不要で、CPU だけで完走する。
- WebGPU のデコーダ兼プレイヤー（TypeScript、Python リファレンスと bit-exact）と、並べて比較するビューア、WebXR モード。セクション単位のプログレッシブ配信に対応し、カメラは自由に動かせる。
- 実測（この検証時、CPU のみ）: 合成メッシュシーンで .falt を4本（前景・背景 × 2セクション）生成。前景 shaded_p0_fg は 1.58 Mbit/s、背景 shaded_p0_bd は 0.09 Mbit/s（いずれも 30.0 fps）、往復一致（roundtrip True）。
- AI から使える形は CLI 2本（tools/faltwerk_recipe.py、python -m codec.measure）と Python API。MCP サーバ・REST API・Agent Skill は提供されていない。

## 目的・背景

- 動的な 4D Gaussian Splatting の再構成を、ブラウザやヘッドセットでストリーミング再生できる小さなビットストリーム（.falt）に変換する codec。フレームごとの .ply を並べる代わりに、splat ごとの時変属性（位置・回転・スケール・不透明度・基本色）を 32 フレーム区間あたり数ノットの曲線に畳み、時間方向の冗長性を落とす。
- 残りの冗長性は、SH 高次バンドの区間ごとベクトル量子化（カラーのコードブック）、newborn splat の Morton 順、ノット差分の時間 / k-NN 予測で削る。区間ごとにキーを持てるのでランダムアクセスは保たれる。
- 量子化ステップ・splat 予算・near plane・サンプル間隔を手で調整せず、カメラのフットプリントや教師統計、メッシュ形状から規則で導く方式（1ソースにつき定数セット1つ）。
- 発見源は LinkedIn の投稿（James C. Kane が Aaron Nowak との共同公開を告知し、コメントでリポジトリ URL を提示）。投稿の「1.4GB→5〜7MB」「Quest 3 で 25〜40Mbps」は投稿者による比較値で、本項目の数値としては採用していない。
- コードは MIT（Copyright (c) 2026 Aaron Nowak and Faltwerk contributors）で無料。アカウント・API キー・課金は不要。同梱しない第三者データセットとモデルは MIT の対象外（THIRD_PARTY.md）。

## 依存関係

- codec とテスト: Python 3.10 以上 + numpy + zstandard のみ（CPU）。requirements.txt は numpy / zstandard / pytest の3行。
- 画像ソースの学習: PyTorch + gsplat 1.5 + CUDA GPU（24GB 推奨）。requirements-train.txt。N3DV などのデータセットはリポジトリに同梱されず別途入手。
- ビューア: Node.js 23 以上と WebGPU 対応ブラウザ。GPU が無くても SwiftShader で合成デモを出せる（web/make_scene.py）。
- メッシュ経路（mesh2gs.py）は GPU も学習も不要で、Python + numpy だけで動く。

## 実行条件

- tools/faltwerk_recipe.py の --py は既定が python3。numpy 等を入れたインタプリタを明示しないと rules 段で ModuleNotFoundError: No module named 'numpy' になる（今回実際に踏んだ）。
- リポジトリサイズは 1,429 KB、既定ブランチ main、リリース・タグは 0 件、PyPI パッケージも無い。取得は git clone か tarball。
- 研究コードで、README に Research code, moving quickly と明記。作成 2026-10-27、コミットは3件のみ、最終 push 2026-11-04。
- ビットストリーム仕様 docs/format-falt.md はドイツ語で、v1〜v6 のフラグ（SN_VQ / pred / FOLLOW / RESCALE / BSPLINE）で拡張。旧 .csgs（magic CSGS）も引き続き読める。
- GitHub API の license 判定は NOASSERTION だが、LICENSE 本文は MIT。ライセンス判断は API のフィールドではなく LICENSE 実体で行うこと。

## 最短手順

- git clone https://github.com/edrethardo/Faltwerk && cd Faltwerk
- python3 -m venv .venv && .venv/bin/pip install numpy zstandard pytest（= requirements.txt の中身）
- python3 tools/make_synthetic_mesh.py work/synthetic → シーン定義 work/synthetic/scene.json ができる（GPU 不要）
- .venv/bin/python tools/faltwerk_recipe.py --source mesh --scene work/synthetic/scene.json --out work/runs/synthetic --py "$PWD/.venv/bin/python" --run
- work/runs/synthetic/<look>_p<i>_<part>/enc/falt/*.falt と measure.json を確認。ログに roundtrip True と Mbit/s が出れば配信ストリームまで通っている
- 画像入力に進む場合: python3 tools/faltwerk_recipe.py --source images --scene train/recipe/scenes/n3dv_flame_steak.json --out work/runs/flame で recipe.sh を生成し、bash work/runs/flame/recipe.sh（CUDA GPU・gsplat・N3DV の入手が前提）

## 変更履歴

- 2026-11-07: 初回登録
