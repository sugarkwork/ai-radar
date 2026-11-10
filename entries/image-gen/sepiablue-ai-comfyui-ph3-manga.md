---
type: "repo"
name: "sepiablue-ai/ComfyUI-PH3-Manga"
genre: "image-gen"
url: "https://github.com/sepiablue-ai/ComfyUI-PH3-Manga"
author: "sepiablue-ai"
source_post: "https://x.com/OnwUh12/status/2118891000089411602"
sources: ["https://x.com/onwuh12/status/2118891000089411602?a=M4gUQoIGnxJPahOWFqE&s=46", "https://x.com/OnwUh12/status/2118891000089411602", "https://x.com/sep_is_heim/status/2118873007854944386", "https://github.com/sepiablue-ai/ComfyUI-PH3-Manga", "https://api.github.com/repos/sepiablue-ai/ComfyUI-PH3-Manga", "https://raw.githubusercontent.com/sepiablue-ai/ComfyUI-PH3-Manga/main/README.md", "https://github.com/sepiablue-ai/ComfyUI-MossPanelDataset", "https://x.com/phantom_202601/status/2119190903135047886?a=9jZsYicg21hDtdsoKh0&s=46", "https://x.com/Phantom_202601/status/2119190903135047886", "https://x.com/phantom_202601/status/2119190903135047886", "https://make-profit.net/2026/11/06/genai-lab-55-p-h3-image-lora-16gb-character-sheet-twelve-edits-christmas-outfit/"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "RTX4070で1ページ90秒はREADMEに根拠が見つからない投稿者申告。ノードMITとP-H3重みの独自条件は別。生成・写植は未試験。 当方でインストール・推論・生成・ベンチ再現はしていない。"
repo: "sepiablue-ai/ComfyUI-PH3-Manga"
license: "MIT"
language: "Python"
created: "2026-11-06"
updated: "2026-11-07"
stars: 8
forks: 0
open_issues: 0
commits_30d: 10
commits_90d: 10
commit_cadence: "weekly"
size_kb: 3236
archived: false
fetched_at: "2026-11-09T21:38:39Z"
last_release: ""
last_release_at: ""
---

# sepiablue-ai/ComfyUI-PH3-Manga

## 出来ること

P-H3で漫画の各コマの指示文を組み立てるComfyUIノード。2〜6コマ196種、人物最大3人、吹き出し編集、日本語縦書き・ルビ等を案内。

## 目的・背景

紹介対象は `sepiablue-ai/ComfyUI-PH3-Manga`。対象固有の機能・制約の説明は2026-11-07, 2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:48.947345+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

## 依存関係

P-H3対応ComfyUI、PrunaAI/P-H3-Image-Comfyのint8三点、BudouX、日本語フォントが必要。MossPanelDatasetの導入は不要。

## 実行条件

RTX4070で1ページ90秒はREADMEに根拠が見つからない投稿者申告。ノードMITとP-H3重みの独自条件は別。生成・写植は未試験。

コード本体の許諾と、基底モデル・同梱素材・外部API・音声/人物等の利用条件は別に確認する。

## 最短手順

1. [公式README](https://github.com/sepiablue-ai/ComfyUI-PH3-Manga#readme)で対応版と依存を確認する。
2. 上記の対象固有条件を満たす環境を用意し、配布元の手順を選ぶ。
3. 外部サービスの料金・認証・データ送信とライセンスを確認してから導入する。

本調査では導入・ビルド・起動をしていないため、成功済みのコマンドとしては掲載しない。

## 出典

- @OnwUh12: https://x.com/OnwUh12/status/2118891000089411602
- @Phantom_202601: https://x.com/Phantom_202601/status/2119190903135047886
- 対象資料: https://github.com/sepiablue-ai/ComfyUI-PH3-Manga
- 参照: https://x.com/sep_is_heim/status/2118873007854944386
- 参照: https://api.github.com/repos/sepiablue-ai/ComfyUI-PH3-Manga
- 参照: https://raw.githubusercontent.com/sepiablue-ai/ComfyUI-PH3-Manga/main/README.md
- 参照: https://github.com/sepiablue-ai/ComfyUI-MossPanelDataset
- 参照: https://x.com/Phantom_202601/status/2119190903135047886
- 参照: https://x.com/phantom_202601/status/2119190903135047886
- 参照: https://make-profit.net/2026/11/06/genai-lab-55-p-h3-image-lora-16gb-character-sheet-twelve-edits-christmas-outfit/

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
