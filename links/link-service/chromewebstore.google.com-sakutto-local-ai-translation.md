---
name: "Sakutto - Local AI translation"
genre: "link-service"
url: "https://chromewebstore.google.com/detail/sakutto-local-ai-translat/mhlbjjijfkoghmcjndgdimhdlfkhadfl"
pricing: "free"
pricing_detail: "Chrome ウェブストアと作者のREADMEは無料、広告なし、課金機能なしと説明。初回にPLaMoモデルのダウンロードとライセンス同意が必要。"
signup_required: false
flags: ["unverified"]
risk_notes: "ページ本文や選択範囲は既定で端末内処理と作者は説明しているが、モデル取得時は Hugging Face への通信が発生する。設定で任意のローカルサーバーを指定した場合、翻訳文はそのURLへ送信される。これらは掲載元の説明であり、独立した実機検証ではない。"
type: "link"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/RoundtableSpace/status/2119274964054639103"]
fetched_at: "2026-11-18T15:37:13Z"
---

# Sakutto - Local AI translation

## 目的

- Chrome上でWebページを読みながら翻訳する拡張機能。作者の説明では、既定の翻訳処理は端末内で行われる。

## 何ができるか

- 作者のREADMEによると、ページ全体、選択範囲、入力文、PDF、動画字幕を翻訳できる。ページ翻訳は原文置換と原文・訳文の併記を選べ、GPUが使える環境ではWebGPUを利用し、使えない場合はCPUに切り替える。PLaMo 3 Translateの53言語に対応し、日本語を含む。ChromeではPLaMoが扱わない追加11言語にChrome内蔵翻訳を使う。初回にモデルをダウンロードしてライセンスに同意すると、以後はオフラインでも翻訳できるとのこと。作者は翻訳精度や実機での独立検証結果を示していない。

対応言語: PLaMo 3 Translateの53言語を双方向に利用可能。ChromeではPLaMo非対応の追加11言語をChrome内蔵翻訳で処理。日本語を含む。（出典: https://github.com/jammaru/sakutto/blob/main/README.md）
日本語対応: 日本語はPLaMo 3 Translateの対応言語。通常の日本語からやさしい日本語への変換もPLaMoのみで提供。Chromeの追加11言語による拡張機能ではない。（出典: https://github.com/jammaru/sakutto/blob/main/README.md）

## 料金

- Chrome ウェブストアと作者のREADMEでは無料、広告なし、課金機能なしと案内されている。

## 登録の要否

- アカウント登録は不要と掲載されている。利用時にはPLaMoライセンスへの同意とモデルの初回ダウンロードが必要。

## 変更履歴

- 2026-11-23: 初回登録
