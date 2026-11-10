---
repo: "patch-gg/pixelfx"
name: "pixelfx"
genre: image-gen
url: "https://github.com/patch-gg/pixelfx"
license: "MIT"
stars: 6308
language: "JavaScript"
created: "2026-10-30"
updated: "2026-11-09"
added: "2026-11-03"
sources:
  - "https://x.com/daaihq/status/2117446567284367459"
flags: []
risk_notes: ""
forks: 830
open_issues: 11
commits_30d: 9
commits_90d: 9
commit_cadence: "weekly"
size_kb: 25357
archived: false
fetched_at: "2026-11-09T21:38:24Z"
last_release: ""
last_release_at: ""
---

# pixelfx

## 出来ること

- 244 種のピクセルアート・エフェクト集。火・爆発・魔法・天気・UI・拾い物・生物など。すべて「小さなコード」として実装されている。
- キャラクターが絡むエフェクトは「振りかぶる→放つ→接触で停止→回復」という演技（acting）として作られており、12 種のモーションが攻撃の連鎖になる。
- ギャラリーでその場再生、色替え、左右反転、スプライトシート書き出し（任意エンジン向け）。
- Claude Code スキル同梱: 新規エフェクトを「下書き→描画→観察→修正」のループで作る。

## 目的・背景

2026-10-30 作成、2日で約4,000 star。手法は Hugo Duprez の「How to make (good) pixel art effects with Claude」（コードを粘土として扱い、目で判断し、参照を食わせる）に依拠しており、README がその旨と元実装（Sprite Fusion の OSS）を明記している。

## 依存関係

- Node.js（`tools/*.mjs` を実行するため）。`npm i github:patch-gg/pixelfx` または `src/core` と必要なエフェクトだけコピー。
- Claude Code のプラグインとしてスキルを入れる場合は `/plugin install pixelfx@pixelfx`。

## 実行条件

- 描画はブラウザ／Node 上の Canvas。GPU・API キー不要。
- 出力は PNG スプライトシート、またはブラウザで動く JS。ゲームエンジン側の取り込み手順はエンジン毎のドキュメントに従う。
- `node tools/check.mjs` が色のにじみ・継ぎ目・乱数の再現性・重いフレームを検査する。

## 最短手順

```bash
npm i github:patch-gg/pixelfx
node tools/render.mjs fire/torch --gif
node tools/render.mjs ice/frost-nova --sheet
node tools/serve.mjs   # ギャラリーをローカルで開く
```

## 変更履歴

- 2026-11-03: 初回登録（star 3,961 / pushed 2026-10-31 / MIT / 244エフェクト）
