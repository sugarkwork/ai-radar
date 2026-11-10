---
repo: elder-plinius/OBLITERATUS
name: OBLITERATUS
genre: other
url: https://github.com/elder-plinius/OBLITERATUS
license: AGPL-3.0
stars: 9407
language: Python
created: 2026-03-03
updated: "2026-11-05"
added: 2026-11-05
first_seen: 2026-11-05
source_post: https://x.com/Forhanvv/status/2118463967412854938
sources:
  - https://huggingface.co/spaces/pliny-the-prompter/obliteratus
flags: []
risk_notes: "モデルの拒否挙動を除去する（abliteration）ツール。各モデルのライセンスと利用規約、および出力の責任は利用者側。本エントリは手順を記載せず、存在と構成のみを記録する。"
forks: 1706
open_issues: 9
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
size_kb: 40637
archived: false
fetched_at: "2026-11-09T21:41:00Z"
last_release: "v0.1.4"
last_release_at: "2026-10-15"
---

# OBLITERATUS

## 出来ること

- 公開モデルの**拒否（refusal）挙動を除去**するためのツール。モデル重みの方向を推定して編集する abliteration を、CLI とノートブックの両方から実行する。
- 配布形態が3つある: CLI（`obliteratus obliterate <model> --method advanced`）、Google Colab ノートブック（Run all で完結）、Hugging Face Space（ZeroGPU、HF Pro の日次クォータ内で無料）。
- 量子化・LoRA など複数の手法を切り替えられる。出力は HF 形式のモデルとして保存され、そのまま推論に使える。

## 目的・背景

モデルの安全側の挙動（拒否）を、プロンプトではなく**重み側で外す**手法の実装。作者は elder-plinius。投稿では「DeepSeek V4.1 Flash の uncensored 版を作るのに使われた」と紹介されているが、これは投稿者の説明で、一次情報での裏取りはしていない。

## 依存関係

- Python（CLI 実行時）。GPU は HF Space の ZeroGPU または Colab のランタイムを利用できる。
- HF のアカウント（Space / モデル取得）。HF Pro は Space の日次クォータに影響する。
- 対象モデルのライセンスに従う（多くは独自ライセンスで、改変・再配布に条件がある）。

## 実行条件

- **AGPL-3.0**。改変版をネットワークサービスとして提供する場合はソース公開義務。
- モデルによっては abliteration 後の再配布がライセンス違反になる。**元モデルのライセンス確認が前提**。
- 除去できるのは「拒否の傾向」であり、能力の保証はない。安全性の評価は別途必要。
- ★9,189 / fork 1,625 / 直近30日で100+コミット（v0.1.4）。活発だが、内容の性質上、業務利用は規約確認が必須。

## 最短手順

```bash
# CLI（詳細な手順は本エントリには記載しない。README を参照）
pip install obliteratus
obliteratus obliterate <org/model> --method advanced

# ノートブック / Space
# https://huggingface.co/spaces/pliny-the-prompter/obliteratus
# https://colab.research.google.com/github/elder-plinius/OBLITERATUS/blob/main/notebooks/abliterate.ipynb
```

## 変更履歴

- 2026-11-05: 初回登録（★9,189 / pushed 2026-11-05 / AGPL-3.0 / v0.1.4）
