---
name: "RelayVSR: Large–Small Model Collaboration for Efficient Real-World Video Super-Resolution"
genre: "article"
url: "https://kopperx.github.io/RelayVSR/"
published: "2026-09-29"
flags: ["unverified"]
risk_notes: "FPS・GPUメモリ・品質評価は論文著者による実験報告。単一のNVIDIA A100 80GBでのモデル推論結果であり、ComfyUI版の動作や投稿にある14 GB VRAMでの30 FPSを裏付けるものではない。双方向参照では入力30 FPS時に最大0.5秒の先読み待ちがあると論文に記載。"
type: "article"
added: "2026-11-12"
first_seen: "2026-11-12"
sources: ["https://x.com/wildmindai/status/2118493695100289374"]
fetched_at: "2026-11-12T06:20:38Z"
---

# RelayVSR: Large–Small Model Collaboration for Efficient Real-World Video Super-Resolution

## テーマ

- 疎なキーフレームを大規模生成モデルで補強し、その参照情報を軽量な動画超解像ネットワークが各フレームに利用するストリーミング方式 RelayVSR。

## 著者の主張

- 公式プロジェクトページと論文は、双方向参照モードについて1080p、単一NVIDIA A100 80GBで29.29 FPS、ピークGPUメモリ13.82 GB、初回出力まで0.327秒と報告している。これは論文著者による評価結果であり、独立実測ではない。

## 裏取り・注意点

- 公式ページから対応する論文とコードへのリンクを確認。論文は201フレームのモデル推論比較を記載し、双方向参照モードでは30 FPS入力時に将来のキーフレームを待つため最大0.5秒の遅延が生じうるとしている。評価条件はA100 80GBであり、ComfyUI上の動作や投稿で触れられた14 GB VRAM・30 FPSはこの資料から確認できない。

## 出典

- 公式プロジェクトページ https://kopperx.github.io/RelayVSR/ — 方式、著者、性能報告への案内。対応する論文 https://arxiv.org/abs/2609.37850 — 公開日、評価条件、性能値、先読み遅延の根拠。

## 変更履歴

- 2026-11-12: 初回登録
