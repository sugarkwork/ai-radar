---
name: "pump.fun"
genre: "link-service"
url: "https://pump.fun/"
author: "Baton Corporation, Ltd.（Pump Entities）"
flags: ["unverified"]
risk_notes: "【元ポストの主張と実測の区別】ポストはAI生成の「emo kid」インフルエンサーの顔を使い第三者がコインを3件ローンチしたと述べ、$45Kピーク・$161K出来高・クリエイター手数料0.30%・本人の取り分ゼロ等の数字を挙げる。実測できたのはプラットフォーム側の仕様のみ：(1) ボンディングカーブのクリエイター手数料は公式料金ページで0.300%と確認でき、ポストの0.30%と一致。(2) コイン作成にプラットフォーム手数料はなく、誰でも画像・名前・シンボルを入れて発行できる（作成ページで画像15MB/動画30MB、名前・シンボル・画像は作成後に変更不可と明記）ため、第三者が他人の顔写真でコインを作ることに同意確認の仕組みはない。(3) 一方、$12K収益・297Kフォロワー・52.3M再生・$45Kピーク・$161K出来高・保有者8人等は投稿者の推計／個別コインの値で、こちらでは一次確認していない（unverified）。【未確認】Terms Section 32 の Prohibited Jurisdiction の国別リストは本文が取得上限で切れ、具体的な国名を確認できていない（英国でブロックとの外部報道はあるが一次情報では未確認）。米国等での提供可否、創業者・運営会社の詳細、公式の書き込み系API／オンチェーンSDKの有無も未確認（Developer APIは明示的に読み取り専用で、取引・署名は不可）。https://pump.fun/ 本体はCloudflareのbotチェレンジで平文HTTPには403を返す（ヘッドレスでは描画成功）。【リスク】ミームコインは内在価値がなく投機的で全額損失があり得る（TermsのRISK WARNING、Tokenized Agent Disclaimer）。手数料は予告なく改定されうる。18歳以上・Prohibited Jurisdiction除外・制裁/AMLスクリーニングあり。第三者による肖像・商標の無断利用と、それに対するDMCA/商標ガイドライン上の削除対応が主な法的論点。"
pricing: "free"
pricing_detail: "利用は無料でサブスクリプション型のプランはない。コイン作成はプラットフォーム手数料0（Solanaのネットワーク手数料とオンチェーンアカウント作成用の少額SOLのみ）。ボンディングカーブの取引は合計1.25%（クリエイター0.300% / プロトコル0.95% / LP 0%）。PumpSwapへの卒業時に0.015 SOL。卒業後のcanonical poolは時価総額による段階制で合計0.300%〜1.250%（〜420 SOL帯1.250%、98,240 SOL以上0.300%）、非canonicalプールは0.30%。Custom Pairはボンディングカーブ1.25%／PumpSwap 0.30%。料金ページ最終更新2026-10-17、改定はページ更新のみで行われうる。Developer APIとMCPサーバーは「currently provided without charge」で、将来の有料化は留保されている。"
signup_required: true
type: "link"
added: "2026-11-08"
first_seen: "2026-11-08"
sources: ["https://x.com/Y0urDumble/status/2110811759670181977"]
fetched_at: "2026-11-08T06:48:00+00:00"
---

# pump.fun — コードなしでSolanaのミームコインを発行・売買できるローンチパッド

## 目的

- Solana上のミームコインを、コードを書かずに誰でも短時間で発行し、その場で売買できるローンチパッド。公式ドキュメントは「Pump.fun is a memecoin launchpad on Solana. Anyone can launch a coin in under a minute. There's no liquidity to seed, no presale, and no team allocation.」と説明している。
- 流動性の初期提供もマーケットメイカーも不要で、発行した瞬間からボンディングカーブ上で取引が成立する。AI生成キャラクターの顔を使った第三者のコイン乱発が話題になった現場がこのサイトで、読む側には「誰でも無審査・低コストでトークンを発行できる場所」として理解するのが実態に近い。

## 何ができるか

- コイン作成: 名前・シンボル・説明・画像（任意でSNSリンク）を入れてウォレットで署名するだけ。作成ページの指定は画像15MBまで（jpg/gif/png推奨、1000x1000px以上）、動画30MBまで。公式ガイドは「Name, symbol, and image are immutable.」として作成後の変更不可を明記している。
- 価格形成: ボンディングカーブは「a constant-product AMM」で、買いで価格が上がり売りで下がる。板・マーケットメイカーなし。既定のしきい値に達するとPumpSwapへ流動性が自動移行し、「Graduation is automatic and irreversible.」とされる。
- 売買・保有の可視化: フィード、Explore、Leaderboard、Live、保有者向けHolder Rewards、$PUMP、Perps（Hyperliquid経由のレバレッジ）などの画面がある。
- AI・エージェントから使える形（一次情報で確認できた範囲）: 公式の読み取り専用Developer API（https://api.pump.fun/v1、Bearerキー、67ルート／6スコープ）と、ホスト型MCPサーバー（https://mcp.pump.fun/mcp、28ツール、すべて readOnlyHint: true）が提供されている。MCPはClaude Code / Claude Desktop / Cursor等から同じキーで接続でき、プロフィール・フォローグラフ・コールアウト・リーダーボード・公開ウォレットのポジションを読める。ユーザー生成テキストは untrusted としてラップされ、エージェントが本文中の指示に従わないよう明示される。
- AIから使えない部分: コインの作成・売買・署名はブラウザ（または公式モバイルアプリ）でのウォレット操作のみ。Developer APIの規約は「an API Key cannot create, post, follow, trade, transfer, sign or otherwise take any action on the Pump Platform」と明記しており、公式の書き込み系APIや公式CLIは確認できていない（サードパーティ製の取引ボットやSDKは多数あるが一次情報ではない）。
- 制限: Developer APIは申請・承認制（即時発行なし、組織あたりキー5本まで）。既定レートは2 req/s・50,000リクエスト/UTC日。ブラウザのOriginヘッダ付きリクエストは失効扱い。

## 料金

- 閲覧・利用そのものは無料。月額プランやサブスクリプションは設定されていない（「Pump Entities and affiliates do not charge any fee for accessing the Pump Platform itself.」）。
- コイン作成: プラットフォーム手数料0。「No platform fee, for any pairing. You pay only the Solana network transaction fee and the small SOL deposit the network requires to create the token's on-chain accounts.」
- ボンディングカーブの取引: 合計1.25%（クリエイター0.300% / プロトコル0.95% / LP 0%）。クリエイター取り分は取引のたびに発生し、慈善団体への寄付に切り替えることもできる。
- PumpSwapへの卒業: 0.015 SOL（全コイン共通）。卒業後のcanonical poolは時価総額の段階制で合計0.300%〜1.250%（0–420 SOL帯が1.250%、98,240 SOL以上が0.300%）。非canonicalプールは合計0.30%、Custom Pairはボンディングカーブ1.25%／PumpSwap 0.30%。
- 料金ページの最終更新は2026-10-17。改定は「may change these fees from time to time by updating this page」とされており、事前通知なく変わりうる。Developer APIとMCPは現時点で無料（「currently provided without charge」）だが、将来の有料化は明示的に留保されている。

## 登録の要否

- 発行・売買にはウォレット接続が必須。Phantom / Solflare / Backpack などSolana対応ウォレット、またはPrivy経由のメールサインイン（埋め込みウォレットを自動生成）のいずれか。
- 18歳以上であることの認定と利用規約・プライバシーポリシーへの同意が初回に求められる（クリックラップに「certify that you are over 18 years old」と表示）。Prohibited Jurisdiction に所在・居住する者は利用不可と規約に明記され、地理位置・IP・デバイス・ウォレット等のシグナルで制限するとされている（国別リストの具体名は未確認）。
- Developer APIを使う場合はpump.funアカウントで開発者コンソール（developers.pump.fun）に申請し、pump.funチームの承認後にキーを発行する。キーの全文は一度しか表示されない。MCPサーバーも同じキーが必要。

## 変更履歴

- 2026-11-08: 初回登録
