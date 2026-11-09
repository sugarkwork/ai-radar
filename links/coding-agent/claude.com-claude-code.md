---
name: "Claude Code"
genre: "coding-agent"
url: "https://claude.com/product/claude-code"
author: "Anthropic"
pricing: "paid"
pricing_detail: "Free では利用不可。Pro $20/月（年払い $17/月、$200 一括）、Max $100/月（Pro の5倍）、Ultra $200/月（週10倍、verified は5時間制限なし）。Team は席単位で公開ページに単価表示なし、Enterprise は $20/席/月 + API 従量（年払い）。Console はトークン従量で Opus 5.5 が $4/$20 per MTok、fast mode は $8/$40。税別・2026-11-09 時点。"
signup_required: true
flags: ["unverified"]
risk_notes: "Claude Code は汎用コーディングエージェントで、CGI/動画専用の機能はない。投稿のスタックではブリーフ→ショットリスト/カメラワークの文章生成と、MCP 経由の Blender 操作指示を担うが、モデリング・ライティング・レンダーは Blender、編集は HyperFrames/FFmpeg 側。『全部 Claude Code がやる』は不正確。投稿の15秒動画は 1440x1800（4:5）・30fps・15.03秒の1フォーマットで、画面内に『INVOICE · EXAMPLE』『ILLUSTRATIVE BUILD LOG』『FICTIONAL BRAND · RENDERED IN BLENDER』と明記された UI モックアップ。請求例はアニメーションで増える『EXAMPLE』で、終盤は $300 + $600 + $400 + $400 + $300 = $2,000。実在の請求ではなく、$1,500–5,000 の市場価格は未検証。DELIVERY GATE は 0/6 から終盤 6/6 になるが、それは UI のチェックで、実ファイルは 4:5 の1フォーマットのみ。16:9/9:16/1:1 の実ファイルは確認できない。『4 shots』は UI のショットリスト、『3 formats』は UI 表示で、納品物の実体は未確認。`/cgi-ad-studio` の配布物（skill/リポジトリ/プロンプト）へのリンクは投稿になく、.blend も生成スクリプトも公開されていない。引用 X 記事はログイン要求で本文未確認。15秒・4カメラ・3フォーマットの納品実績は未検証。『no 3D artist / no studio』は投稿の主張、『one operator』は UI のコピーで、実際の制作体制は確認できない。返信の supervoid_si も『ブランドはレンダーではなく光・カメラ・ビートの判断に払う』と指摘している。"
type: "link"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/Y0urDumble/status/2114084322227503206"]
fetched_at: "2026-11-09T13:18:50Z"
---

# Claude Code — ターミナルで動くコーディングエージェント、CGI スタックでは工程の指示役

## 目的

- 投稿の CGI 広告スタックで、クライアントブリーフをショットリストとカメラワークに落とす『DIRECT』工程を担うコーディングエージェント。ただし CGI 専用ツールではなく、汎用のコード/ツール実行エージェントをプロンプトとスキルで CGI 制作向けに使う位置づけ。
- ターミナル・IDE・デスクトップ・Web で同じエンジンを使い、リポジトリの CLAUDE.md、skills、MCP サーバーを共有する。

## 何ができるか

- コードベースを読み、計画し、複数ファイルを編集、テスト実行、git の commit/PR 作成まで行う。`claude "..."` の対話モードと `claude -p "..."` の非対話モードがある。
- MCP クライアントとして外部ツールを接続できる。Blender MCP を `claude mcp add blender uvx mcp-for-blender` で追加すると、Blender のシーン操作・Python 実行・レンダー確認をツールとして呼べる。3D のレンダー自体は Blender が行う。
- `CLAUDE.md`、skills、hooks、subagents、Agent SDK、GitHub Actions/GitLab CI でワークフローを固定化できる。CGI 用の専用ショットリスト機能はなく、投稿の `/cgi-ad-studio` のようなプロンプト/スキル側の設計に依存する。
- 画像・動画の生成モデルは Claude Code 自体には含まれない。画像/動画は Blender、HyperFrames、FFmpeg など外部ツールに渡す。

## 料金

- Free は Claude Code 非対応。Pro $20/月（年払い $17/月、$200 一括）で使える。Max $100/月は Pro の5倍、Ultra $200/月は週10倍で verified アカウントは5時間制限なし。
- Team は席単位（公開ページに単価表示なし）、Enterprise は $20/席/月 + API 従量の年払い。いずれも税別。
- Console（API）はトークン従量。Opus 5.5 は入力 $4/MTok・出力 $20/MTok、fast mode は $8/$40。プロンプトキャッシュのヒットは $0.20/MTok。
- 料金は 2026-11-09 時点の公式表示。プラン改定で変わる。

## 登録の要否

- 必要。初回起動で Claude アカウント（Pro 以上）または Console アカウントのログインが要る。`ANTHROPIC_API_KEY` を承認すれば API キーでも起動できる。
- インストール: macOS/Linux/WSL は公式の `https://claude.ai/install.sh`、Windows は `https://claude.ai/install.ps1` を実行。`claude --version` で確認。
- Blender とつなぐ場合は、別途 Blender MCP のアドオンと uv を入れる。Claude Code 単体では Blender を操作できない。

## 変更履歴

- 2026-11-09: 初回登録
