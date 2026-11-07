---
type: "link"
name: "Gracia (Gracia AI)"
genre: "3d-motion"
url: "https://gracia.ai/"
author: "Gracia AI, Inc."
pricing: "paid"
pricing_detail: "処理は分単位の従量課金。Streaming/VR ティア $800/分（セグメント最低課金あり）、VFX ティア $2,500/分、40〜50分/年以上でボリューム割引。キャプチャは別途でパートナー経由 概ね $15,000〜20,000/日。初回は1〜2分の無料処理テストあり。Web/Python/C++/Apple SDK とデモ用 .mint は無償。独立した料金ページはなく、金額はトップページ F.A.Q. の記載（2026-11 時点）"
signup_required: true
added: "2026-11-07"
first_seen: "2026-11-07"
sources: ["https://docs.gracia.ai/", "https://docs.gracia.ai/streaming-usage", "https://docs.gracia.ai/streaming-view-token-openapi", "https://docs.gracia.ai/sdks/python", "https://docs.gracia.ai/sdks/web", "https://github.com/gracia-labs/web-sdk", "https://github.com/gracia-labs/python-sdk", "https://demo.gracia.ai/", "https://x.com/tokufxug/status/2118171681437175920"]
flags: []
risk_notes: "金額は独立した料金ページではなくトップページ F.A.Q.（クライアント描画 / assets/landing-9a750015.js 内）の記載で、2026-11 時点のベンダー公表値。配信 API キーは Settings → Api Settings でパートナーアカウント限定、取得は support@gracia.ai への連絡が必要でセルフサーブ不可。SDK のライセンスは GitHub 上 'Other'（NOASSERTION）で再配布条件は未確認。デモ .mint の配信元 gstatic.gracia.ai は Cloudflare チャレンジを返し curl では 403（ブラウザでは取得可）。元ポストは別プロジェクト「Faltwerk」（edrethardo/Faltwerk、カーブ圧縮の 4DGS ストリーミングコーデック）の宣伝で gracia.ai に言及がなく、投稿の数値（32フレーム、1.4GB→5〜7MB、25〜40Mbps）は本件の根拠にしていない。"
fetched_at: "2026-11-07T12:01:41Z"
source_post: "https://x.com/tokufxug/status/2118171681437175920"
---

# Gracia — 実写マルチカメラから4DGSを再構成し、SDKと配信APIで再生する

## 目的

- 同期済みのマルチカメラ実写素材から、自由視点で見られる4D（3DGS＋時間軸）表現を作り、Web・VR・エンジン上で再生するための商用プラットフォーム。
- 「プロンプトで作った映像ではなく、実測のシーン」をロボティクス・ライブスポーツ・映像制作に渡すことを掲げており、ジオメトリ保持と時間方向の安定性（フレーム間でスプラットがちらつかないこと）を売りにしている。
- AI 側からは、配信トークン発行の HTTP API と、ローカルGPUで描画する Python/C++ SDK の2経路で扱える。処理そのもの（撮影素材→.mint）はパートナー契約ベースのクラウド工程。

## 何ができるか

- 処理: ゲンロック／シャッター同期したマルチカメラ素材を .mint（時間安定性を持たせた独自フォーマット）または .PLY 連番に変換。スプラット数は Streaming 100〜125K、VR 200〜300K、VFX 最大1M の3ティア。納品は通常3〜5日。
- 配信 API: ベース URL https://streaming.gracia.ai。POST /api/v1/streaming/view-token/issue、POST /api/v1/streaming/view-token/revoke、PUT /api/v1/streaming/view-token/update の3本で視聴トークンを発行・失効・更新する。OpenAPI 3.0.3 の YAML が公開され、認証は X-API-KEY ヘッダ。エージェントからは通常の HTTP 呼び出しで叩ける。
- Web SDK: npm install github:gracia-labs/web-sdk。WebGPU＋WASM の再生ランタイムで、vanilla JS / React hooks / Three.js / PlayCanvas に対応。Quest 3・Pico 4 Ultra・Vision Pro 向けの XR（ハンドトラッキング、グラブ移動、空間オーディオ、環境リライティング）込み。demo.gracia.ai に複数のライブデモ。
- Python SDK: パッケージ名は graciasdk。prebuilt wheel を pip で入れるだけで、GPU 上で 3DGS（静的）/4DGS（動画）を描画し、RGBA・depth・mesh_color を NumPy 配列で受け取る。Vulkan（Windows/Linux）または Metal（Apple Silicon）、CPython 3.12 以上、free-threaded ビルド非対応。
- その他: C/C++ SDK（Vulkan、C ABI + ヘッダオンリー C++ ラッパー）、Apple SDK（Swift/Metal）、Unity・Unreal プラグイン。Gracia Studio というデスクトップ運用ツールもある。
- データ側: /data で「Custom 4D Data」の受託キャプチャを提供。POVステレオ＋多視点ドーム、深度・4Dハンドトラック・セマンティックスプラット・リライティングを付与し、撮影拠点は日本・US・カナダ・欧州・UK・自社リグから選べる。

## 料金

- 処理は分単位の従量課金。Streaming/VR ティア $800/分（セグメント単位の最低課金あり）、VFX ティア $2,500/分（放送・映画品質）。40〜50分/年以上の年間量でボリューム割引。
- キャプチャ（撮影）は処理と別料金で、パートナー経由 概ね $15,000〜20,000/日。
- 初回は1〜2分の無料処理テストがあり、リグとワークフローの検証に使える。
- SDK（Web/Python/C++/Apple）とデモ用 .mint は無償。ただし https://gracia.ai/pricing という独立した料金ページは存在せず（アプリのシェルが返る）、上記金額はトップページの F.A.Q. の記載（2026-11 時点）。

## 登録の要否

- 必要。処理の投入・配信トークンの発行・API キーの確認は Gracia アカウント（クラウドプラットフォーム）前提で、まずサインインしてプロジェクトを作る。
- API キーは Settings → Api Settings で発行するが、この画面はパートナーアカウント限定。パートナー契約は support@gracia.ai への連絡で、セルフサーブの登録フローはない。
- アカウントなしで試せる範囲: Python SDK を pip で入れてローカルの .mint/.ply を描画する、Web SDK を npm で入れてデモを動かす、demo.gracia.ai のプレイヤーを見る、までは登録不要（GPU は必要）。

## 変更履歴

- 2026-11-07: 初回登録
