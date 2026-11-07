---
type: "link"
name: "ArtCraft Craft Apps"
genre: "mcp-server"
url: "https://getartcraft.com/apps"
author: "ArtCraft (GitHub: storytold)"
pricing: "free"
pricing_detail: "Craft Apps 自体は無料・Apache-2.0。/pricing の有料プラン（Basic 8 / Pro 28 / Max 48 USD/月、年払い20%off）は別製品の ArtCraft Studio（AI画像・動画、クレジット制）向けで、Craft Apps の利用には課金がない。"
signup_required: false
added: "2026-11-07"
first_seen: "2026-11-07"
sources: ["https://x.com/awe0_io/status/2117816163598287229"]
flags: []
risk_notes: "ベンダー自身が多くのアプリを 'Early alpha' / 'In development' と表記しており機能は未完成。MCPサーバは既定では起動せず、利用者が明示的にクライアントへ登録する必要がある。--automation-read-root / --automation-write-root で与えた範囲のファイル読み書き権限をエージェントに渡すため、書き込みルートは専用フォルダに限定する旨がドキュメントに明記されている。PhotoCraft の日本語UIフォントは別リポジトリ（craft-fonts）依存。"
fetched_at: "2026-11-06T21:06:07Z"
---

# ArtCraft Craft Apps — CLI と MCP サーバを備えた無料・オープンソースのクリエイティブアプリ16本

## 目的

- 画像編集・ベクター・動画・PDF・DTP・3Dテクスチャ・DAW・CAD・表計算など、商用クリエイティブソフト相当の機能をRust製ネイティブアプリとして無料・オープンソースで提供するスイート。
- UIだけでなくCLI・JSON制御チャネル・MCPサーバを同じコマンド基盤の上に置き、AIエージェントが人の操作と同じ粒度でアプリを駆動できることを設計目標にしている。

## 何ができるか

- 16アプリ: PhotoCraft（画像編集）/ VectorCraft（ベクター）/ FilmCraft（動画編集）/ LightCraft（RAW現像・フォトライブラリ）/ PdfCraft（PDF）/ EffectCraft（モーショングラフィックス）/ DesignCraft（ページレイアウト）/ FigCraft（UIデザイン）/ TextureCraft（3Dテクスチャ）/ MaterialCraft（プロシージャルマテリアル）/ WordCraft / SoundCraft（DAW）/ DeckCraft / CADCraft / GridCraft（表計算）/ Craft Anything。
- MCP: 各アプリのCLIから stdio の MCP サーバを起動できる（photocraft-cli mcp、pdfcraft-cli mcp、vectorcraft-cli mcp、filmcraft-cli mcp、gridcraft-cli mcp を実ドキュメントで確認）。クライアント設定は JSON の mcpServers に command=photocraft-cli, args=[mcp, --automation-read-root, ...] を書く形式。
- MCPツール: command_list（コマンド一覧・パラメータ仕様・有効状態の取得）、command_run（単発実行）、command_batch（順次実行、stop_on_error 指定可）。PhotoCraft は500以上のコマンドをUIと共用。
- CLI: photocraft-cli run / batch でヘッドレスにファイル変換・一括処理が可能。Linux の .deb/.rpm は /usr/bin/photocraft-cli を同梱、macOS は署名・公証済みの CLI バイナリを別途配布。
- 制御チャネル: デスクトップアプリは loopback 限定・認証付きの JSON 制御チャネル（--control）を持ち、UI状態の取得やポインタ操作、オフスクリーン撮影ができる。
- 実行環境: macOS / Windows / Linux（AppImage・deb・rpm・Flatpak・Arch）と FreeBSD、さらに WebAssembly 版をブラウザで実行可能。ファイル処理はローカル完結でクラウド往復なし。
- エージェント側の安全設計: MCP起動時に --automation-read-root / --automation-write-root で読み書き範囲を限定でき、書き込みは画像・ドキュメント拡張子か画像バイト列のみ許可、それ以外（.rs や .env など）は拒否される。

## 料金

- Craft Apps は無料。公式ページに 'Free · Open source'、各アプリページに 'Free and open source' と明記。ライセンスは Apache-2.0（GitHub API で確認）。
- 同じサイトの /pricing は別製品 ArtCraft Studio（AI画像・動画生成アプリ）のサブスクで、Basic 8 USD/月（通常10、年払い20%off時・1,000クレジット）、Pro 28 USD/月（通常35・3,750クレジット）、Max 48 USD/月（通常60・6,600クレジット）、Enterprise は個別見積。年払いは 96 / 336 / 576 USD。
- Craft Apps の利用自体にサブスクやクレジット消費はなく、費用が発生するのは Studio の生成クレジットと任意の買い切りクレジットパック。

## 登録の要否

- 不要。ランチャー（craft-launcher v0.14.1）と各アプリのインストーラは GitHub Releases への直リンクで、アカウント作成やログインの導線は確認できなかった。
- MCP を使う場合はアカウントではなく、CLI をインストールして利用中のMCPクライアント（Claude など）に手動で登録する作業が必要（'Installing the CLI does not start or register an MCP server automatically'）。
- ブラウザ版（app.getartcraft.com）と Studio の有料プラン・クレジット購入時のサインイン要否は今回の取得では確認できず未確認。

## 変更履歴

- 2026-11-07: 初回登録
