---
name: "treg REA growth"
genre: "link-service"
url: "https://treg.to/rea-growth"
author: "superdesigndev（Superdesign Dev Pty Ltd）"
pricing: "freemium"
pricing_detail: "$1.00 の初回無料クレジット後は前払い残高からの従量課金。プロバイダ実費でマークアップ0%、サブスク・席課金なし。例: Douyin 286 tools が $0.001/call から、People & contact 284 tools が $0.0001/success から、TikTok 192 tools が $0.00035/success から。自前キー・自チームのツール・接続アカウントは課金なし（2026-11-07 時点）"
signup_required: true
flags: ["unverified"]
risk_notes: "未確認: 無料クレジット取得にカード登録や本人確認が必要か、verified account の条件、表示価格の税・通貨換算。料金はプロバイダのレート次第で変動し、$0.58 や各レートは 2026-11 時点の掲載値。ショーケース（Lovable の被リンク数・流入推定など）はベンダー自身の実行記録で、第三者の追試はない。当方ではスキルを実行しておらず出力品質は未検証。X 連携は treg の X アプリ経由だと自前キーでも従量課金。GitHub API の license は NOASSERTION だが LICENSE 本文は Apache-2.0。"
type: "link"
added: "2026-11-07"
first_seen: "2026-11-07"
sources: ["https://x.com/MengTo/status/2118384737626857724"]
fetched_at: "2026-11-07T15:47:12Z"
---

# treg / REA growth — 競合企業の「いつ・何で増えたか」を逆算するエージェントスキル

## 目的

- treg.to は「エージェント向けツールの OpenRouter」を名乗る従量課金の API ゲートウェイ。1 つのトークンで 126 プロバイダ・4,100+ のツール（SEO/SERP、被リンク、SNS 投稿、人物・企業情報、広告ライブラリ、スクレイピング、画像/動画/音声生成）を、プロバイダごとの契約なしで呼べる。
- /rea-growth はその上で動く公開スキル。企業ドメインを渡すと、いつ成長が加速したか、どのチャネルのどの施策がそれを動かしたかを公開データから並べ、真似できるプレイを 10 個（各プロンプト付き）返す。投稿の「studying brands」はこれを指す。

## 何ができるか

- スキル本体は https://treg.to/skills/rea-growth/SKILL.md（17,788 bytes）で誰でも読める。mode=full は Step 0-12: サイトの URL 構造 → 技術スタック・提携・資金/ニュース → 検索流入の変曲点 → 検索/AI 回答 → 広告 → 言及・UGC → 自社コンテンツ → プロダクトのループ（"Made with" バッジ等）→ 次の拡大先 → 各施策と成長速度の対応 → カスタマージャーニー → プレイ化。成果物は playbook.md / playbook.html / CSV。mode=content は YouTube・TikTok・Instagram・X・LinkedIn・Reddit のタイトル・サムネ・コピーの分析だけを Step 0/1/7/13 で行い content.md / content.html / CSV を出す。
- 出力の規律が明文化されている: 所見はすべて SEEN（呼び出し結果か画像で確認、リンク付き）か INFERRED（見えたものからの推論、根拠を明示）に分類し、見えなければ not seen と書く。公開情報のみ・アカウント作成やフォーム入力や接触は禁止。数値は Python で計算し日付を付す。既定の予算上限は $3 で、エンドポイント初回呼び出し前に catalog_get で価格を確認させる。
- AI からの呼び方: クラウド型（ChatGPT / claude.ai）は https://treg.to/mcp/ をカスタムコネクタに追加して OAuth 同意（どのチームが支払うかを選ぶ）。MCP のツールは catalog_search / catalog_get / call / call_media / resources_list / balance / my_tools / catalog_request / feedback / review。
- ローカルのコーディングエージェントは `curl -fsSL https://treg.to/install.sh | sh` で CLI とスキルを入れ、`treg login`（ブラウザ）→ `treg catalog search` → `treg catalog get <id>` → `treg call <id> --query key=value` の順で使う。素の HTTP なら GET https://treg.to/call/<id>?key=value に X-Treg-Token、自チームのツールは https://treg.to/call/<tool-name>/<path>。
- 実走例: lovable.dev を 2026-10-23 に分析し、データ費用 $0.58。レポートは https://treg.to/rea-growth.md に全文公開（推定 US 検索流入の月次表、変曲点 2025-01〜06 の約11倍、"Edit with Lovable" バッジが 20,132 参照ドメイン / 255,420 被リンクで初出 2025-02-09 等、すべて日付付き）。
- 限界: 一部データはチーム自前のキーが必要（例: 流入元別の Akta）。検索流入は推定値。結果は実行日時点のスナップショットで、数値は変わる。

## 料金

- サブスクなし。前払い残高から呼び出しごとにプロバイダ自身のレートで課金され、マークアップ 0%（terms に明記）、席課金・月額最低なし。新規チームは $1.00 の無料クレジット（llms.txt は once per new verified account と記載）。
- 掲載レートの例（/pricing、プラットフォーム別の下限）: Douyin 286 tools が $0.001/call から、People & contact 284 tools が $0.0001/success から、Company data 261 tools が $0.0001/result 未満から、Open web & SEO 243 tools が $0.0001/result 未満から、TikTok 192 tools が $0.00035/success から、Instagram 188 tools が $0.0007/success から、YouTube 168 tools が $0.0009/success から、Google Keyword Data 167 tools が $0.00012/call から。個別ツールの実価格はツールページと catalog_get に出る。
- 自前キー（BYOK）を登録したプロバイダ、自チームが登録したツール、接続済みの自アカウント（GA4 / Search Console / Google Ads 等）は課金されない。例外として treg の X アプリ経由の X 連携は自前キーでも従量課金。
- 残高が尽きるとメーター制の呼び出しは明確なエラーで止まり、自前キーの呼び出しは動き続ける。
- 実費の目安: Lovable の REA 実行 1 本が $0.58（2026-10-23）、20 件の Meta 広告 + 17 件の Google 広告取得が $0.015（共有キー）、キーワード 50 件の需要調査が $0.11。

## 登録の要否

- 呼び出しには要。未認証で https://treg.to/mcp/ を叩くと HTTP 401（Bearer を要求）、/call/<id> も 401 not authenticated。
- サインインは GitHub / Google の OAuth、またはメールに届くコード。CLI は treg login（ブラウザ）または --token <token>、招待は treg accept。MCP コネクタでは OAuth 同意の際に支払うチームを選ぶ。
- 登録なしで読めるもの: トップ・カタログ・料金・ドキュメント・llms.txt・/rea-growth のページ・SKILL.md・レポートの .md。カタログの検索と価格確認は CLI/HTTP だとトークンが要る。
- カード登録や本人確認が無料クレジットの条件かは未確認。

## 変更履歴

- 2026-11-07: 初回登録
