---
repo: "mromidev/claude-animated-shorts"
name: "Claude Animated Shorts"
genre: 3d-motion
url: "https://github.com/mromidev/claude-animated-shorts"
license: "MIT"
stars: 1195
language: "TypeScript"
created: "2026-11-01"
updated: 2026-11-01
added: "2026-11-03"
first_seen: "2026-11-03"
sources: []
flags: []
risk_notes: ""
forks: 270
open_issues: 3
commits_30d: 2
commits_90d: 2
commit_cadence: monthly
size_kb: 17948
archived: false
fetched_at: "2026-11-03T22:58:04Z"
---

# Claude Animated Shorts

## 出来ること

- Claude Code 用のスキル一式。55〜70秒の縦型アニメ短編（3D世界の中の2Dキャラクター、インク輪郭、塗り絵のような街、レンズブラー、滑走するカメラ、行進曲と効果音）を、three.js + Remotion でローカルにレンダリングして作る。**AI 動画生成モデルは使わない**。
- `SKILL.md` にパイプライン全体と全ルール・修正手順・最終的な見た目のパラメータを記載。題材決め → 脚本 → 声 → `story.ts` のショット計画 → スチル確認 → 本番レンダリング、の順でエージェントが進める。
- 参考実装として67秒の短編「The Bridge That Fell for a Song」のソース（世界・キャラ・インク・レンズブラー・グレーディング・脚本・カメラ）と、合成音（効果音・行進曲・ダッキングとラウドネス調整済みのミックス）を同梱。
- 20本の参照作から測定した `STYLE_BIBLE.md`、7本の計測レポート（モーション/奥行き/テクスチャ/キャラ/ライティング/輪郭/グレーディング）、参照フレーム38枚、コンタクトシート20枚（計1,200フレーム）を同梱し、自分のフレームと比較しながら寄せる。

## 目的・背景

動画「How to Make Viral Animated Shorts Using Claude (Full Workflow)」の配布物。生成AIで絵を作るのではなく、参照作を計測して数値化した見た目を three.js のコードで再現するアプローチを取る。事実確認（題材の調査）から脚本・音まで含むため、出力は「AI slop」ではなく作り込んだ短編になる。

## 依存関係

- Node.js、Remotion と `@remotion/three`、Python 3、`ffmpeg`。
- スキルは `~/.claude/skills/cartoon-3d-short/` にフォルダごとコピーして使う（clone か ZIP）。

## 実行条件

- `REMOTION_TMP` を容量の大きいドライブに設定する。Remotion のバンドルは毎回 `public/`（約1.3GB）を一時フォルダへコピーするため。
- 参照フレームはスタイル研究用。脚本・キャラクター・声は自作する前提（README が明記）。
- コードとドキュメントは MIT。参照フレームの扱いは同梱の LICENSE に従う。

## 最短手順

```bash
git clone https://github.com/mromidev/claude-animated-shorts.git \
  ~/.claude/skills/cartoon-3d-short
# Claude Code で:
# 「Use the cartoon short skill and make a short about …」
```

## 変更履歴

- 2026-11-03: 初回登録（star 1,192 / pushed 2026-11-01 / MIT）
