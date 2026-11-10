---
type: "repo"
name: "social-media-research-skills"
genre: "agent-framework"
url: "https://github.com/ScrapeCreators/social-media-research-skills"
repo: "ScrapeCreators/social-media-research-skills"
license: "MIT"
stars: 6082
language: "Python"
created: "2026-06-06"
updated: "2026-08-26"
added: "2026-11-07"
first_seen: "2026-11-07"
sources: ["https://x.com/abir35627/status/2118648224202551573"]
flags: []
risk_notes: "① 実体は Markdown のスキル13本＋検証スクリプト1本で、Python 表記は scripts/validate-skills.py のみ。テストも CI も無い（.github 無し）。② 最終 push は 2026-08-26、直近30日のコミット0。issue #11 / #12 が「スキル内のエンドポイントパスが現行APIと不一致で404」を指摘したまま未修正（/v1/twitter/user/tweets → 正は /v1/twitter/user-tweets、/v1/tiktok/hashtags/popular は廃止、#9 は /v1/credit/balance → /v1/credit-balance）。スキル間でも表記が割れている（scrapecreators-api は user/tweets、outlier-post-finder は user-tweets）。③ データ取得は ScrapeCreators の有料APIが必須。キー無しでは1件も返らない。無料枠は100クレジット＋最大1,200の追加分のみで、1回のアウトライア分析が数十クレジットを消費する。④ 回収できるのは公開データだけで、ログイン必須・非公開・DM等は対象外。⑤ 各プラットフォームのToSとスクレイピング可否の判断は利用者側。⑥ MIT は明記されているが、実質はベンダーのAPI導線（キー取得→課金）であり、独立検証ではなくベンダー自身の主張が根拠。"
forks: 167
open_issues: 9
commits_30d: 0
commit_cadence: "stale"
size_kb: 41
archived: false
last_push: "2026-08-26"
commits_90d: 2
fetched_at: "2026-11-09T21:34:50Z"
last_release: ""
last_release_at: ""
---

# social-media-research-skills — SNSリサーチの13工程をエージェントに配るスキル集

## 出来ること

- 13本のスキルで構成: `outlier-post-finder` / `transcript-intelligence` / `comment-mining` / `competitor-social-research` / `ad-library-teardown` / `trend-discovery` / `influencer-prospecting` / `audience-research` / `social-listening-brief` / `product-demand-research` / `creator-profile-teardown` / `content-repurposing` / `scrapecreators-api`
- `outlier-post-finder` は投稿を20件以上集め、中央値ベースラインに対する倍率で Huge（5x以上）/ Strong（2〜5x）/ Mild（1.5〜2x）に分類。サンプル10件未満なら confidence low と明示させる
- `transcript-intelligence` は TikTok・Instagram・YouTube・Facebook・X・LinkedIn・Rumble・Reddit の動画文字起こしから、要約・フック・主張・引用・再利用可能な素材を抽出
- `comment-mining` はコメントから質問・反論・ペインポイント・購買意図・顧客の生の言い回しを集める（VOCレポート）
- `ad-library-teardown` は Meta / Google / LinkedIn の配信中広告を、訴求角度・フック・CTA・オファー・次のテスト案に分解
- `influencer-prospecting` は公開プロフィールから候補リストをCSV/表で出力、`audience-research` はフォロワーの国・属性シグナルから相性を confidence 付きで評価
- `scrapecreators-api` が全スキルのデータ層。27+プラットフォーム・110エンドポイントの意図別ルーティング表を持ち、呼ぶ前に per-endpoint の OpenAPI 仕様を取得するよう指示している
- 出力はJSONではなく成果物（レポート・表・CSV・スワイプファイル）で、投稿URLの出典を付ける方針を README で明記

## 目的・背景

- ScrapeCreators 社自身が公開している公式スキル集。APIラッパーではなく「ワークフロー第一、API第二」を掲げ、ユーザーの依頼（例: 「この競合の外れ値投稿を探す」）を業務成果物まで通す手順書として書かれている
- 設計原則として、公開データのみ・出典明記・クリエイター自身の平常値と比較・言い回しを原文のまま残す・最後に次のアクションを置く、の6点を README に列挙
- 同社の配布形態は MCP・CLI・スキルの3種で、本リポジトリはスキル版。マーケティング色は強いが、手順の中身（中央値比較、confidence ラベル、サンプル数不足の明示）は実務的

## 依存関係

- `SCRAPECREATORS_API_KEY`（`x-api-key` ヘッダで送る）。取得は scrapecreators.com
- Node.js / npx（`npx skills add` で導入）。ホストは Agent Skills 仕様対応のもの（Claude Code、Cursor、Codex、GitHub Copilot、Gemini CLI、Windsurf、VS Code 等）
- スキルの `allowed-tools` は Bash / Read / Write / WebFetch を想定
- 実行時に `https://api.scrapecreators.com` と `https://docs.scrapecreators.com/{path}/openapi.json` へ到達できること
- リポジトリ内のコードは `scripts/validate-skills.py`（frontmatter 検証用）のみで、Python 実行環境はこの検証にしか要らない
- `.claude-plugin/marketplace.json` と `plugin.json` を同梱（Claude Code のプラグイン経路でも配布）

## 実行条件

- APIキー必須。無い場合 Authorization エラーで何も返らない
- 従量クレジット制: 無料100クレジット（クレカ不要）、紹介・GitHub スター・G2レビューで最大1,200追加。以降は $47 / 25,000、$497 / 500,000（2026年10月時点の表示）
- 大半のエンドポイントは1リクエスト=1クレジット。ただし一部は複数消費し、AI文字起こしは「開始1分あたり10クレジット」の従量（ネイティブ字幕は返った時のみ1クレジット）。キャッシュヒットは0クレジット、レート制限なし
- 1回のアウトライア分析でも「20件以上のフィード＋勝ち投稿の詳細＋文字起こし＋コメント」で数十クレジット規模になるため、無料枠は動作確認と数回の試行で尽きる
- 対象は公開データのみ。ログイン後・非公開・DM・フォロワー限定は取得できない（README が明記）
- 鮮度に注意: 最終 push 2026-08-26、以降コミットなし。issue #11・#12 が指す通り `scrapecreators-api` 内の一部パスは現行APIで404（`/v1/twitter/user/tweets` → `user-tweets`、`/v1/tiktok/hashtags/popular` は廃止）。404 が出たら docs の per-endpoint 仕様で現行パスを引き直す前提で使う
- 各プラットフォームの利用規約、スクレイピングの可否、収集データの扱いは利用者の責任

## 最短手順

- `export SCRAPECREATORS_API_KEY=sk_...` をシェルのプロファイルに置く
- `npx skills add ScrapeCreators/social-media-research-skills` でスキルを導入し、エージェントを再起動
- 残クレジットを確認: `curl -s https://api.scrapecreators.com/v1/credit-balance -H "x-api-key: $SCRAPECREATORS_API_KEY"`（スキル内の `/v1/credit/balance` 表記は404）
- 単発疎通: `curl -s "https://api.scrapecreators.com/v1/tiktok/profile?handle=charlidamelio" -H "x-api-key: $SCRAPECREATORS_API_KEY"`
- エージェントに「@アカウントの YouTube Shorts の外れ値投稿を直近1ページから探して」と依頼 → レポート形式で返るか確認
- パスが404になったら `https://docs.scrapecreators.com/{path}/openapi.json` を取得して正しいパスとパラメータを確認し、その後 API を叩く
- 大量収集の前に、対象件数×クレジット単価を見積もってから実行する

## 変更履歴

- 2026-11-07: 初回登録
