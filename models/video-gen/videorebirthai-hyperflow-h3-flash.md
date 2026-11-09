---
type: "model"
name: "VideoRebirthAI/hyperflow-h3-flash"
genre: "video-gen"
url: "https://huggingface.co/VideoRebirthAI/hyperflow-h3-flash"
author: "VideoRebirthAI"
source_post: "https://x.com/DeepForest_Inc/status/2118808820013244894"
sources: ["https://x.com/deepforest_inc/status/2118808820013244894?a=wknqtPTRg80skozUea8&s=46", "https://x.com/DeepForest_Inc/status/2118808820013244894", "https://x.com/video_rebirth/status/2118729708988969078", "https://x.com/airi_ai_navi/status/2119236435752689904", "https://huggingface.co/VideoRebirthAI/hyperflow-h3-flash", "https://huggingface.co/VideoRebirthAI/hyperflow-h3-flash/raw/main/README.md", "https://x.com/mapte_fireball/status/2118878741321687447?a=l2Xb1ZRD5GQIW06ngUQ&s=46", "https://x.com/mapte_fireball/status/2118878741321687447", "https://x.com/mapte_fireball/status/2118879117982695630", "https://huggingface.co/api/models/VideoRebirthAI/hyperflow-h3-flash", "https://github.com/Video-Rebirth/hyperflow-h3-flash", "https://github.com/Video-Rebirth/ComfyUI-HyperFlow-Flash", "https://x.com/aiaicreate/status/2119010112551747700?a=W_zQBEbI1_IK40umZyI&s=46", "https://x.com/aiaicreate/status/2119010112551747700", "https://x.com/aiaicreate/status/2119010129429594396", "https://x.com/video_rebirth/status/2119081595592458245"]
first_seen: "2026-11-06"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "公式の24/32GB GPU実測に対し16GBは未計測。重みはMiniMax H3 Community Licenseで地域・売上規模・表示・出力学習利用に条件。コードのApacheとは別。 当方でインストール・推論・生成・ベンチ再現はしていない。"
model: "VideoRebirthAI/hyperflow-h3-flash"
license: "other"
base_model: ["MiniMaxAI/MiniMax-H3"]
downloads: 40788
likes: 102
format: "safetensors / gguf"
size: "配布中の重みファイル 19本・合計155,350,498,824 bytes（複数形式・量子化・派生を含む。必要メモリではない）"
created: "2026-11-04"
updated: "2026-11-06"
fetched_at: "2026-11-09T00:30:31.820815+00:00"
pricing: "free"
pricing_detail: "重みのダウンロードに利用料金の表示なし。ライセンス・用途・地域・商用許諾と実行費用は別途確認。"
signup_required: false
license_name: "minimax-h3-community-license-agreement"
---

# VideoRebirthAI/hyperflow-h3-flash

## 出来ること

MiniMax H3を約13.7B/13.9Bへ圧縮したHyperFlow H3 Flash。4/6/8ステップで5.2〜15秒の24fps映像と32kHzステレオ音声を同時生成すると説明。

## 目的・背景

対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:31.820815+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

## 収録ファイル

公式APIの現行一覧（2026-11-09T00:30:31.820815+00:00）。重み 19本。

- `fl2va_gguf/minimax_h3_fl2va_hyperflow_flash_14b-Q3_K_M.gguf` — 7,215,807,072 bytes
- `fl2va_gguf/minimax_h3_fl2va_hyperflow_flash_14b-Q4_K_M.gguf` — 9,053,456,480 bytes
- `fl2va_gguf/minimax_h3_fl2va_hyperflow_flash_14b-Q4_K_S.gguf` — 8,011,480,160 bytes
- `fl2va_gguf/minimax_h3_fl2va_hyperflow_flash_14b-Q5_K_M.gguf` — 10,277,808,224 bytes
- `fl2va_gguf/minimax_h3_fl2va_hyperflow_flash_14b-Q6_K.gguf` — 11,578,681,952 bytes
- `fl2va_gguf/minimax_h3_fl2va_hyperflow_flash_14b-Q8_0.gguf` — 14,929,689,696 bytes
- `fl2va_int8_convrot/diffusion_pytorch_model-00001-of-00003.safetensors` — 5,331,906,296 bytes
- `fl2va_int8_convrot/diffusion_pytorch_model-00002-of-00003.safetensors` — 5,290,477,648 bytes
- ほか11本。複数形式・量子化・分割を含むため全量ダウンロードを推奨する意味ではない。

[ファイル一覧](https://huggingface.co/VideoRebirthAI/hyperflow-h3-flash/tree/main)。配布容量とロード後の必要メモリ、TE/VAE等の外部依存は区別する。

## 実行条件

fl2va/ref2vaのGGUFとINT8を配布。Q4_K_M約9.1GB、Q8_0約14.9GB。ComfyUIは専用Flashノード・GGUFノード・テキストエンコーダ等が別途必要。

公式の24/32GB GPU実測に対し16GBは未計測。重みはMiniMax H3 Community Licenseで地域・売上規模・表示・出力学習利用に条件。コードのApacheとは別。

## 使い方

[公式モデルカード](https://huggingface.co/VideoRebirthAI/hyperflow-h3-flash)から対応する実装・形式と必要な基底モデルを選ぶ。ファイル一覧は取得したが、重みのダウンロード・ロード・推論は実施していない。

## 出典

- @DeepForest_Inc: https://x.com/DeepForest_Inc/status/2118808820013244894
- @mapte_fireball: https://x.com/mapte_fireball/status/2118878741321687447
- @aiaicreate: https://x.com/aiaicreate/status/2119010112551747700
- @video_rebirth: https://x.com/video_rebirth/status/2119081595592458245
- 対象資料: https://huggingface.co/VideoRebirthAI/hyperflow-h3-flash
- 参照: https://x.com/video_rebirth/status/2118729708988969078
- 参照: https://x.com/airi_ai_navi/status/2119236435752689904
- 参照: https://huggingface.co/VideoRebirthAI/hyperflow-h3-flash/raw/main/README.md
- 参照: https://x.com/mapte_fireball/status/2118878741321687447
- 参照: https://x.com/mapte_fireball/status/2118879117982695630
- 参照: https://huggingface.co/api/models/VideoRebirthAI/hyperflow-h3-flash
- 参照: https://github.com/Video-Rebirth/hyperflow-h3-flash
- 参照: https://github.com/Video-Rebirth/ComfyUI-HyperFlow-Flash
- 参照: https://x.com/aiaicreate/status/2119010112551747700
- 参照: https://x.com/aiaicreate/status/2119010129429594396
- 参照: https://x.com/video_rebirth/status/2119081595592458245

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
