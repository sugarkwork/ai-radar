---
repo: "diffusionstudio/lottie"
name: "Text-to-Lottie"
genre: "3d-motion"
url: "https://github.com/diffusionstudio/lottie"
last_release: "v1.0.0"
last_release_at: "2026-06-15"
flags: ["unverified"]
risk_notes: "導入・生成・プレビューは未実行。出力品質、複雑なシーンや各再生環境での互換性、参照動画からの再現、対応ランタイムの最低バージョン、エージェント側の料金は未検証。"
stars: 5716
forks: 302
open_issues: 2
size_kb: 5000
language: "TypeScript"
created: "2026-06-04"
updated: "2026-07-25"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/CryptooGG_/status/2119312343892976064"]
fetched_at: "2026-11-10T12:08:08+00:00"
---

# Text-to-Lottie — コーディングエージェントで Lottie JSON を作成・編集

## 出来ること

- 文章や SVG をもとに Lottie JSON を作成する。付属プレイヤーでエージェントの変更を確認し、再生位置を動かしながら調整できる。 [README](https://raw.githubusercontent.com/diffusionstudio/lottie/main/README.md)

## 目的・背景

- エージェントがレイヤー、図形、キーフレーム、イージングを JSON に直接記述する。作者は短い単一シーンやモーショングラフィックスを得意と説明している。 [開発元の解説](https://diffusion.studio/changelog/text-to-lottie)

## 依存関係

- 生成にはスキル対応のコーディングエージェントが必要。付属プレイヤーのパッケージ定義には SolidJS、CanvasKit WASM、Vite が含まれる。 [README](https://raw.githubusercontent.com/diffusionstudio/lottie/main/README.md) [package.json](https://raw.githubusercontent.com/diffusionstudio/lottie/main/package.json)

## 実行条件

- 公式導入手順は npx を使う。プレビューはブラウザで行い、Web に組み込む場合は README に lottie-web の例がある。リポジトリは MIT ライセンスで、持ち込む SVG やフォントの利用条件は素材ごとに確認する。 [README](https://raw.githubusercontent.com/diffusionstudio/lottie/main/README.md) [ライセンス表示](https://github.com/diffusionstudio/lottie)

## 最短手順

- `npx skills add diffusionstudio/lottie` でスキルを追加する。
- Claude Code または Codex に『text-to-lottie を使い、この SVG の輪郭を元の形状のまま、透明背景で、2 秒かけて描画して』のように依頼する。
- `public/projects/<project>/<scene>/lottie.json` を付属プレイヤーで確認し、必要に応じてタイミングやイージングの調整を依頼する。 [README](https://raw.githubusercontent.com/diffusionstudio/lottie/main/README.md)

## 変更履歴

- 2026-11-10: 初回登録
