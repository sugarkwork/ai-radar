---
repo: kanaworksai-hue/effekseer-vfx-skill
name: effekseer-vfx-skill
genre: 3d-motion
url: https://github.com/kanaworksai-hue/effekseer-vfx-skill
author: KanaWorks_AI（@dextune）
license: MIT
stars: 79
language: Python
created: 2026-10-10
updated: 2026-10-29
added: 2026-11-04
first_seen: 2026-11-04
source_post: https://x.com/dextune/status/2117798991438192931
sources: []
forks: 6
open_issues: 0
commits_30d: 11
commits_90d: 11
commit_cadence: weekly
size_kb: 6458
archived: false
fetched_at: "2026-11-04T04:47:01Z"
---

# effekseer-vfx-skill

## 出来ること

- コーディングエージェント（Claude Code / Codex / Cursor / Gemini CLI / Copilot / OpenCode など Agent Skills 対応ホスト）に、ゲーム用のリアルタイム VFX を作らせるスキル2本組。
- `effekseer-vfx`（制作側）: ブリーフ → テクスチャ → Python レシピ → 公式 EffekseerCore でビルド → Godot でフィルムストリップ撮影 → 1点だけ直す → 繰り返し。約30個の合成可能なレイヤープリミティブ、静的リンタ、保存/再オープンの読み戻し検証、Godot Lab（2体のダミー間のエフェクトとして演出）、ピクセルフラグ付き撮影、反復履歴、レビュー対象ビルドを固定する改ざん検知つき証跡を含む。
- `vfx-review`（レビュー側）: レシピを見ずに、固定ルーブリックでフィルムストリップだけを別エージェントが採点する。作者が自分の作品を採点しない構成。
- 完成例16種（ブリーフ・テクスチャ付き）を同梱。遠距離攻撃4組（火/氷/毒/…）など。
- 0.3 で効果の作り方が3通りに: **手続き型**（プリミティブ＋テクスチャ）／**ビデオフリップブック**（image-to-video モデルに黒背景で動きを描かせ、`vfx video-flipbook` でキー・クロップ・マスク・パック）／**併用**（シートを本体レイヤーにし、プリミティブで着弾閃光・火花・亀裂・熱ゆらぎを足す）。Seedance 2.5 で検証済み、前後フレームを扱えるモデルなら可。
- Unity 対応: `vfx unity-install` で URP ランタイムパッケージ（ElementProfile、飛翔物・即着弾・地面噴出、ヒットストップ、シェイク、対象持ち上げ）を導入し、`vfx unity-export` でシートを再生可能なスキルとデモシーンに変換。
- クリップのプロンプトとシートのパラメータは `vfx/video_prompts.json` に記録され、同じシートを再生成・差分生成できる。

## 目的・背景

KanaWorks_AI による、VFX アーティストの反復作業をコード側のループとして再現する試み。プリミティブの拡大・フェード・スクロール・侵食では「炎が同じシルエットのまま煙に変わる」ような連続的な形状変化を作れないため、その部分だけ動画生成モデルに任せ、輪郭・着弾・破片はプリミティブで制御する分担になっている。2026-10-10 作成、10-29 時点で 79 star。

## 依存関係

- 制作（authoring）: Python 3.11+ または `uv`（macOS / Linux / Windows。macOS 標準の 3.9 では動かない）
- ビルド: **macOS Apple Silicon** または **Windows x64** のみ。初回セットアップで約250MBを `~/.cache/effekseer-vfx` に取得（ネットワーク必要）
- レンダリング/レビュー: 上記＋ Godot 4（Forward+、`PATH` か `GODOT` で指定）＋ `ffmpeg`
- ビデオフリップブック: authoring 環境＋`ffmpeg`
- Unity: Unity 6（6000.0+）＋ URP 17（6000.5 で検証）
- エージェント側: Agent Skills 対応ホスト。Claude Code はプラグイン、Codex は `$skill-installer`、その他は `npx skills add`

## 実行条件

- ビルドとレンダリングの検証済み環境は macOS ARM64（Effekseer Core 1.80.7 / EffekseerForGodot4 1.80.5.1 / Godot 4.7 / .NET 9）と Windows 11 x64（Godot 4.7.2）。
- **Linux は authoring のみ**。ビルド経路は未検証。ヘッドレス Linux でのキャプチャは未対応で、レビューにはウィンドウ付き Godot が必要。
- Windows の cmd / PowerShell では `vfx.cmd` / `setup.ps1` を使う（Git Bash なら `sh` のままで可）。
- レビュー指標は実ビューポートのピクセルヒューリスティックで、GPU 時間やオーバードロー値ではない。同梱例のスコアも作者自身のキャプチャに対する独立レビューで、16件中2件は `iterate` 判定。
- `soft` パーティクルは Forward+ 専用（Compatibility レンダラには深度テクスチャが無い）。

## 最短手順

```bash
# 1) スキルを導入（Claude Code）
#    /plugin marketplace add kanaworksai-hue/effekseer-vfx-skill
#    /plugin install effekseer-vfx@effekseer-vfx
# 2) それ以外のホスト
npx skills add kanaworksai-hue/effekseer-vfx-skill
# 3) ゲームプロジェクト側で環境診断 → ツールチェーン導入
sh <skill>/scripts/vfx doctor
sh <skill>/scripts/setup.sh          # Windows は setup.ps1
# 4) エフェクト生成（例）
#    「Make a water-column skill from a video flipbook and set it up in my Unity project.」
```

## 変更履歴

- 2026-11-04: 初回登録（0.3 の3方式・Unity 対応時点）
