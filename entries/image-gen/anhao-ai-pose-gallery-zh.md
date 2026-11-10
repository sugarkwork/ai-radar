---
repo: "anhao/ai-pose-gallery-zh"
name: "AI 角色参考与合成工作台 · 中文版（3合1）"
genre: "image-gen"
url: "https://github.com/anhao/ai-pose-gallery-zh"
flags: ["unverified"]
risk_notes: "README に基づく。デモと各生成連携の動作、生成品質、クラウド API の料金、素材ごとの許諾、最新リリースは未確認。 GitHub APIでライセンスを確認できていません。"
stars: 6608
forks: 1670
open_issues: 14
size_kb: 1170001
language: "TypeScript"
created: "2026-10-27"
updated: "2026-11-04"
archived: false
license: "unknown"
commits_30d: 82
commits_90d: 82
commit_cadence: "daily"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/ganfanren_ai/status/2118493023164334541"]
fetched_at: "2026-11-10T10:04:41Z"
---

# ポーズ・衣装・人物の参照画像を組み合わせる中国語ワークベンチ

## 出来ること

- 中国語でポーズ・衣装・人物を検索し、白い素体画像と深度マップを切り替えながら、参照画像とプロンプトを組み合わせられる。ComfyUI のカスタムノードからは個別の参照画像や合成画像を出力できる。

## 目的・背景

- 日本語メタデータで別々に公開されていた参照ギャラリーを中国語で横断利用できるようにしたプロジェクト。ポーズの深度マップは ControlNet Depth の入力に使えると README に記載されている。生成品質の比較や改善幅は未確認。

## 依存関係

- Web 版をローカルで開発・ビルドするには Node.js 20 以上と pnpm が必要。カスタムノードは既存の ComfyUI 環境の torch、NumPy、Pillow、aiohttp を再利用する。

## 実行条件

- 生成には利用者が設定する Gemini、GPT Image、Qwen、Doubao のクラウド API、またはローカル ComfyUI のワークフローが必要。クラウド API の料金は接続先の条件を確認する。
- README ではフロントエンド、プラグイン、処理スクリプトを MIT とし、画像と原データを適用範囲から除外している。収録画像の商業転売と有償配布を禁じており、CharaDB の参照画像には再配布禁止など別の条件がある。成人向け素材は README によると既定の SFW モードで非表示になる。

## 最短手順

- README が案内するデモ https://ai-pose-gallery.anhao.app/ を開き、SFW モードのままポーズ・衣装・人物を各一つ選んで合成レシピに追加する。
- Claude Code から検索する場合は、リポジトリを手元に置き、`skills/pose-reference-standard` を `~/.claude/skills/` にシンボリックリンクする。Claude Code に『pose-reference-standard を使い、立ち姿の参照画像を探して』と依頼する。画像を指す相対パスが解決できるよう、リポジトリの構成を保つ。

## 変更履歴

- 2026-11-10: 初回登録
