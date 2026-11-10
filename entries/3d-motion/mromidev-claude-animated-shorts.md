---
repo: "mromidev/claude-animated-shorts"
name: "Claude Animated Shorts"
genre: 3d-motion
url: "https://github.com/mromidev/claude-animated-shorts"
license: "MIT"
stars: 2591
language: "TypeScript"
created: "2026-11-01"
updated: "2026-11-01"
added: "2026-11-03"
first_seen: "2026-11-03"
sources: ["https://x.com/Manojkumar2257/status/2119258187920777253"]
flags: ["unverified"]
risk_notes: "今回の紹介はREADMEと一致したが、新たな実行検証ではない。 今回の動作・推論・生成・性能は未検証。"
forks: 564
open_issues: 11
commits_30d: 2
commits_90d: 2
commit_cadence: "monthly"
size_kb: 17948
archived: false
fetched_at: "2026-11-09T21:31:26Z"
type: "repo"
author: "mromidev"
source_post: "https://x.com/Manojkumar2257/status/2119258187920777253"
amplifiers: []
last_release: ""
last_release_at: ""
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

## 追加出典・確認範囲（2026-11-09）

Claude Code向けの短編制作キットを再紹介した投稿。

Three.js/Remotion等を使うコード描画で、動画生成モデルではない。

今回の紹介はREADMEと一致したが、新たな実行検証ではない。

対象固有の機能・制約の説明は2026-11-08（原記録）のチェック記録を基にしている。メタ情報は2026-11-09T00:31:33.451107+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

### 今回取得した公式メタ情報

既存フロントマターの過去値は維持し、今回の取得値を下に併記する。どちらも実行・性能の追試ではない。

| 項目 | 値 |
|---|---|
| repo | mromidev/claude-animated-shorts |
| url | https://github.com/mromidev/claude-animated-shorts |
| license | MIT |
| language | TypeScript |
| created | 2026-11-01 |
| updated | 2026-11-01 |
| stars | 2422 |
| forks | 525 |
| open_issues | 10 |
| commits_30d | 2 |
| commits_90d | 2 |
| commit_cadence | monthly |
| size_kb | 17948 |
| archived | False |
| fetched_at | 2026-11-09T00:31:33.451107+00:00 |


- @Manojkumar2257: https://x.com/Manojkumar2257/status/2119258187920777253
- 対象資料: https://github.com/mromidev/claude-animated-shorts

- 2026-11-09: 関連出典と確認範囲を追記。既存の記述・過去の数値・原文プロンプトは維持。今回の実行確認なし。
