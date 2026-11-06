---
type: "repo"
name: "treg（REA growth スキル同梱のエージェント用ツールレジストリ）"
genre: "mcp-server"
url: "https://github.com/superdesigndev/treg"
repo: "superdesigndev/treg"
license: "Apache-2.0 + 追加条項（GitHub API は NOASSERTION）"
stars: 7255
language: "Python"
created: "2026-07-15"
updated: "2026-11-06"
added: "2026-11-06"
first_seen: "2026-11-06"
sources: ["https://x.com/MengTo/status/2118384737626857724"]
flags: []
risk_notes: "ライセンスは API 上 NOASSERTION で、実体は Apache-2.0＋追加条項：自社利用・セルフホストは自由だが、競合するホスティング型レジストリとして第三者に再配布するには書面許可が要る（treg.to の API を自社製品から課金パススルーで呼ぶのは許可）。実運用は有料：新規アカウントの $1.00 を使い切るとプリペイド残高へのチャージが必須（データ元の原価でマークアップなし、というのはベンダーの主張で独立検証はしていない）。CLI は `curl -fsSL https://treg.to/install.sh | sh` で入れる形式なので中身を確認してから実行したい。CLI は匿名の利用ログを PostHog に送る（既定オン、TREG_TELEMETRY=0 で停止）。README の『4,100+ tools / 126 providers』『no markup』はベンダー公表値。rea-growth が出す数値は第三者のデータ販売API由来で、Growth の因果はスキル自身も INFERRED と明記しており断定材料にはならない。投稿の返信欄にある Cloudflare の security-audit スキルや /untangle-codebase は無関係なリンク塊で、主題は treg。"
forks: 654
open_issues: 263
commits_30d: 100
commit_cadence: "daily"
size_kb: 133449
archived: false
fetched_at: "2026-11-06T08:38:30Z"
last_release: "v0.30.0"
last_release_at: "2026-11-05"
---

# treg — エージェント用ツールの OpenRouter。1トークンで 4,100+ API を従量課金で呼び、rea-growth スキルで競合の成長を分解する

## 出来ること

- 1つのベースURL＋1つのトークン（`X-Treg-Token`）で、カタログ上の外部APIを呼ぶ。実リクエストのURLの頭に `https://treg.to/call/` を付けるだけで、treg がホスト名からツールを解決し、認証情報をサーバ側で注入して中身はそのまま中継する（呼び出し側は鍵を持たない）
- ベンダー名ではなく『やりたいこと』で探す：`treg catalog search "backlinks for a domain"` / `treg catalog search --new`。`treg catalog get <id>` でパラメータ・**価格**・レスポンス例まで見てから `treg call <id>` で実行
- カタログはSEO・被リンク、SNS・トレンド、人物・企業エンリッチ、広告、スクレイピング、画像/動画/音声生成まで。README 表記で 4,100+ エンドポイント・126 プロバイダ、1コール1セント以下から
- 自分のチームの鍵・ツール・スキルを持ち寄れる：`treg scan`（読み取りのみの下見）→ `treg upload`（`.env`・スキルディレクトリ・導入済みCLIを一括登録、暗号化して保存）。自分の鍵は treg の鍵より常に優先され、その呼び出しは課金されない
- CLI も同じ資格情報で動かせる：`treg run stripe -- get /v1/balance`、`treg shell start` で subshell 内の CLI に自動注入。実行履歴は `treg calls` / `treg runs`
- マルチ資格情報のツール（例：Google Ads の OAuth bearer ＋ developer-token ヘッダ）を `--bind` で複数注入。OAuth は `treg oauth connect` で初回トークンを取り、以後は自動更新。`treg health` で資格情報の生死を確認
- スキルを1つの配布物として登録・配布：`SKILL.md` ＋ 秘密 ＋ ツールを束ね（bundle）、`treg skill install <name>` で各自のエージェントに配る。鍵はサーバ側に残る
- 同梱ワークフロースキル：`treg`（カタログ探索と実行）／`web-access`（自前のWebツールで足りないときの読み取り）／`lead-signals`（購買シグナルの発見）／`recruit`（求人票から候補者ランキング）／`make-ugc`（UGC動画）／`jev-memory`（Claude Code 用の記憶）／`rea-growth`
- **rea-growth（投稿の主題）**：対象企業を入れると、サイト構成・導入技術と提携/資金調達・検索とAI回答での言及・広告出稿・話題にした人・自社コンテンツ（タイトル/サムネ/カバー/キャプション）・被リンクとプロダクトループ・採用を、設定を除く13ステップ（1〜11で収集、12で playbook、13が content モードの結び）で集め、`playbook.md` ＋ 1ファイルの `playbook.html`（チャネル別の Contact Sheet、成長曲線に各施策をピン留め）＋ CSV を出す。各施策にはそのまま貼れる実践プロンプトが付く。`content` モードはコンテンツだけを短縮版で出力。なお opt-in 扱いで、`--skills all` には含まれない（`sh -s -- --skills rea-growth` と明示する）
- rea-growth の規律：すべての記述を **SEEN**（取得結果か画像で確認、リンク付き）か **INFERRED**（何から推論したかを明記）に分ける。公開情報のみ・アカウント作成もフォーム入力も接触もしない。各ステップ後に「3行の所見＋次に確認すること＋概算コスト」を出して続行/中断を選ばせる
- チーム運用：org（最大10）単位でスコープ、role は owner/admin/member/viewer、メンバーごとのツールアクセス制御、WorkOS 経由のエンタープライズ SSO、`treg calls` の監査ログ
- MCP サーバとして繋げる：Claude コネクタ用は `https://treg.to/mcp/v2/`（カタログの厳選分のみ、読み取りと書き込みを分離）。Claude Code は `/plugin marketplace add superdesigndev/treg` → `/plugin install treg@treg`、他のエージェントは `npx skills add superdesigndev/treg -s treg`
- セルフホスト可：`scripts/dev-local.sh up` で localhost:18790 に起動（sqlite・メールOTPはdevモード）。本番は `pip install "tools-registry[server]"`

## 目的・背景

- エージェントが実務で使うデータは、Semrush $139/月、Moz $99/月、Crunchbase $99/月、Apollo $59/席のようなサブスクの向こう側、あるいはサインアップの壁・招待制・パートナー限定でAPIすら無いところにある。1回の実行のために契約する人はいない — その口座を treg 側が持ち、1コール数分の1セントで切り売りする、というのが建前
- 設計の中心は `proxy.py` の `relay()` 1関数：上流を『模倣せず中継する』。書き換えるのは hop-by-hop ヘッダ、treg 自身の制御ヘッダとセッションCookie（上流に漏らさない）、注入する資格情報の3つだけ。だから上流APIの仕様変更に追随でき、呼び出し側は鍵を持たない
- 提供元は Superdesign チーム（Jason Zhou 氏ら）。treg.to でホストしつつ、リポジトリ自体がセルフホスト可能な実装として公開されている
- 投稿との関係：MengTo の投稿は『ブランド研究のスキルが凄い』として **スキル側のページ（treg.to/rea-growth）**とリポジトリを並べている。主題は rea-growth スキルで、このリポジトリはそれが走る土台（課金・資格情報・カタログ）ごと公開されている、という構図。同じ投稿の返信欄に混ざる Cloudflare の security-audit スキルや `/untangle-codebase` は無関係なリンク塊
- rea-growth の出自も README の位置づけ通り『レシピ（SKILL.md）＋秘密＋ツールを1つに束ねる』の実例で、成長調査の手順そのものはプロンプトとして読めるが、実行は treg のカタログAPI（DataForSEO、Predictleads、ScrapeCreators、SerpApi、AnyAPI 等）に依存する

## 依存関係

- CLI：Python 3.12 または 3.13 ＋ uv（推奨）/ pipx / pip3 のいずれか。install.sh がこの範囲を明示的に指定して入れる
- サーバを自分で立てる場合：`tools-registry[server]`（FastAPI・DBドライバ・暗号化が追加される。素の `tools-registry` は CLI のみ）、ダッシュボードのビルドに Node 22.12+ と npm、`dev-local.sh` に tmux と uv。DB は SQLite（開発）または Postgres（本番）
- `TREG_SECRET_KEY`（Fernet 鍵）と DB のバックアップが必須。鍵を失うと保存済みの秘密は復号不能
- エージェント側：MCP クライアント（Claude Code / Claude.ai コネクタ等）、または `npx skills add`。treg のトークン以外の設定は不要
- rea-growth の場合：`treg.web.search` / `treg.web.extract`（無料枠、`X-Treg-Route-Prefer: tinyfish`）から始まり、DataForSEO（検索・被リンク）、Predictleads（技術検出・提携・資金調達）、ScrapeCreators / AnyAPI / HarvestAPI / Crawl4AI / Adyntel / SerpApi（各SNS・広告ライブラリ）を順に呼ぶ。チャネル別トラフィックだけは自前の Akta キーが必要で、無ければ『unavailable』として有機/paid の内訳で代替する
- すべて treg のカタログ経由なので、各プロバイダの口座は不要（BYOK も可）。Python が計算を担い、表示する数値はコードの出力に限定する指示が入っている

## 実行条件

- ホスト版：サインイン（GitHub / Google / メールのワンタイムコード）→ 新規の確認済みアカウントに **$1.00 の無料クレジット**（1回限り）。以降はプリペイド残高へのチャージ。カタログ呼び出しはデータ元の原価でメータリング（マークアップ無し＝ベンダー主張）
- 自分の鍵・自分のツール・接続済みアカウントの呼び出しは課金されない。逆に言えば、無料クレジットだけで回せるのはカタログの一部（公開ルートのあるエンドポイントとWeb読み取り）に限られる
- 残高切れは HTTP **402** `insufficient_balance` で、`balance_micro` / `estimated_cost_micro` / `topup_url` を返す（エージェントが文言を読まずに対応できる形）
- rea-growth の実費：サイトの公開例（lovable.dev、2026-10-23 時点の数値）でフル実行 **$0.58**、内訳はサイト$0.001／技術・ニュース$0.16／成長曲線$0.151／検索1,000キーワード$0.132／AI回答3件$0.008／広告4網$0.031／SNS$0.004／被リンク$0.05／求人$0.04。既定の予算上限は **$3**、ステップごとに確認が入る
- 地域既定は米国（`location_code` 2840 / `language_code` en）。日本企業を調べるなら国コードと言語の差し替えが要る（スキルに JP 用の指定は無い）
- データの限界：公開情報のみ・アカウント作成/フォーム入力/接触は禁止なので、ログインの内側・招待制・非公開の数字は取れない。ブロックされたページは迂回せず『blocked』として記録し次へ進む。因果（この施策が成長を生んだ）は常に INFERRED 扱い
- セルフホストは無料だが、ライセンスの追加条項により『競合するホスティング型レジストリ』としての再配布は不可。CLI のインストールは `curl | sh` 形式、CLI は匿名利用ログを PostHog に送る（既定オン）
- MCP 経由の場合、Claude コネクタ面（`/mcp/v2/`）は画像・動画・音声生成を出さず、読み取り/書き込みを分けて公開している。フル機能は `/mcp/` 側

## 最短手順

```bash
# 1) CLI（Python 3.12/3.13 + uv 推奨）— 中身を確認してから実行するなら先に install.sh を読む
curl -fsSL https://treg.to/install.sh | sh

# 2) サインイン（GitHub 既定 / --email はワンタイムコード / --token はエージェント・CI 用）
treg login

# 3) 鍵も登録もなしで、まず1回動かす
treg catalog search "backlinks for a domain"
treg call tikhub.tiktok.user.profile --query uniqueId=tiktok
treg balance

# 4) 使うツールのパラメータと価格を確認してから呼ぶ
treg catalog get hunter.people.email.find
treg call hunter.people.email.find --query domain=reddit.com

# 5) エージェントに繋ぐ（Claude Code の場合）
#    /plugin marketplace add superdesigndev/treg
#    /plugin install treg@treg        → /mcp で treg を選んでサインイン
#    もしくは: npx skills add superdesigndev/treg -s treg

# 6) rea-growth（ブランド・成長の分解）を走らせる
#    エージェントに: https://treg.to/llms.txt を読ませ、続けて
#    「https://treg.to/skills/rea-growth/SKILL.md に従って競合の成長を逆算して」
#    予算上限（既定 $3）と対象ドメイン・自社ステージを先に伝える

# 7) 自分の鍵・CLI を共有する場合
treg scan            # 読み取りのみの下見
treg upload          # 暗号化して登録

# 8) セルフホスト（tmux + uv、sqlite、dev OTP）
git clone https://github.com/superdesigndev/treg && cd treg
scripts/dev-local.sh up      # http://localhost:18790
```


## 変更履歴

- 2026-11-06: 初回登録
