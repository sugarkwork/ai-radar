---
repo: "0x0funky/agent-sprite-forge"
name: "Agent Sprite Forge"
genre: image-gen
url: "https://github.com/0x0funky/agent-sprite-forge"
license: "MIT"
stars: 5316
language: "Python"
created: "2026-04-23"
updated: 2026-11-06
added: "2026-11-03"
flags: [unverified]
risk_notes: "元ポストは「ゲームエンジンへの取り込みは未確認」と留保するが、README は Godot/Aseprite/Tiled/LDtk 書き出しを検証済みと明記。実機検証は未実施。"
source_post: "https://x.com/AiAircle34052/status/2117493224118047187"
sources:
  - "https://x.com/AiAircle34052/status/2117493224118047187"
  - "https://x.com/Mnilax/status/2116583914684702837"
forks: 517
open_issues: 14
commits_30d: 3
commits_90d: 100
commit_cadence: monthly
size_kb: 99664
archived: false
fetched_at: "2026-11-06T22:52:10Z"
last_release: v0.4.0
last_release_at: 2026-10-06
---

# Agent Sprite Forge

## 出来ること

- 承認した1枚のマスター画像から、キャラクターの全アクション（idle / walk / run / attack / jump / hurt）をゲーム投入可能な形で作る。アクションごとに画像→動画のクリップを1本生成し、決定論的な Python ツールでキーイング・位置合わせ・ループ判定・リタイム・仕上げ・パッケージまで通す。
- 書き出し: PNG アトラス、アルファ付き VP9 WebM、packed alpha MP4、Godot の SpriteFrames / Sprite3D、Aseprite JSON。`generate2dmap` でタイルとマップ（Tiled / Godot / LDtk 向け）も作る。
- ピクセル仕上げモード: 最大32色パレット、二値アルファ、選択的アウトライン。マスター画像の色を OKLab で固定するカラーロック付き（速い手足で色が転ぶ問題への対策）。
- 各アクションの採用判定（面積・足元・同一性・ズーム・背景・端・モーション・終端ポーズ・色にじみ・タイミング）を数値で行い、落ちたものは修正句付きで再生成する。
- すべての生成呼び出しをコスト付きでログし、予算上限を設定できる。
- **hibit 仕上げ**（v0.5.0）: 画像モデルには「ピクセルアート」ではなく平坦なセル画（輪郭線なし・素材ごとに最大3階調）を描かせ、その後に画素化する。キャラクターごとに元画像から色を学び（既定16色）、多数決のダウンサンプルとヒステリシスでちらつきを抑える。`master_still.py` / `finish_frames.py` / `sprite_set.py` / `generate2dmap` が `--finish hibit` に対応する。
- **エフェクトの2経路**: コード駆動の pixelfx を使う経路と画像経路を `fx_pixelfx.py check` で選べる。hibit 用の 480×270 背景（14色パレット）も生成できる。

## 目的・背景

Claude Code プラグイン／Codex／Grok 向けのスキル群として 2026-04 公開。0.4 系で「1枚の絵から全アクション」に作り替えられた。README には実測のビフォーアフター（例: キーイング 271秒→44秒、フリンジ 0.704→0、攻撃 4.1秒→0.7秒）が表で載っている。

参照ポスト（@AiAircle34052）は「書き出したものをゲーム制作ソフトの編集画面に読み込めるかは未確認」と留保しているが、**README は Godot / Aseprite / Tiled / LDtk 向けの書き出しを明記し、書き出したファイルをデコードして検証するとしている**。留保は投稿者側の未確認であり、リポジトリ側の主張とは食い違う。

## 依存関係

- Python + `numpy>=1.26` / `Pillow>=10.1` / `scipy>=1.11`（Claude Code プラグイン導入時は手動で入れる）。
- ffmpeg 5.1 以上（PATH 上）。
- 画像・動画の生成経路: 自分の API キー（OpenAI / Google Gemini / xAI / BytePlus / fal.ai）、無ければサインイン済みの Codex CLI か Grok CLI、最後の手段としてコード生成アート。

## 実行条件

- 画像生成・動画生成のいずれも外部サービス依存。キーかログインが無いと実用的な出力は得られない。
- 1キャラクター＝1マスター画像＋6クリップ。クリップ生成とキーイングに相応の時間とAPI課金がかかる（README は1セットの実測時間を記載）。
- Windows 対応（Codex のサンドボックス、cp1252/cp950 コンソール、ロックファイル削除への対処が README にある）。
- 生成した絵の権利・利用条件は各生成サービスの規約に従う。

## 最短手順

```bash
# Claude Code（プラグイン）
claude plugin marketplace add 0x0funky/agent-sprite-forge --sparse .claude-plugin skills
claude plugin install agent-sprite-forge@agent-sprite-forge
python -m pip install "numpy>=1.26" "Pillow>=10.1" "scipy>=1.11"

# Codex
git clone https://github.com/0x0funky/agent-sprite-forge.git
cd agent-sprite-forge
python -m pip install -r requirements.txt
python tools/install_skills.py --apply --host codex
```

```
Use $generate2dsprite to make a master still of Aria, a young swordswoman hero: side view, facing right, HD.
Use $video2dsprite to animate the approved Aria master: idle, walk, run, attack, jump and hurt. Package them for Godot and the web.
```

## 変更履歴

- 2026-11-03: 初回登録（star 4,920 / pushed 2026-10-06 / MIT / 0.4 系）
- 2026-11-06: hibit 仕上げ（平坦なセル画→画素化、16色パレット・ヒステリシス）とエフェクト2経路を追加（v0.5.0 / 6b3da5c）
