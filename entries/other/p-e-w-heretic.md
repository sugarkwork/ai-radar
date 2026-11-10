---
repo: "p-e-w/heretic"
name: "Heretic"
genre: other
url: "https://github.com/p-e-w/heretic"
license: "AGPL-3.0"
stars: 40132
language: "Python"
created: "2025-09-21"
updated: "2026-11-08"
added: "2026-11-03"
first_seen: "2026-11-03"
sources: []
flags: []
risk_notes: ""
forks: 4590
open_issues: 65
commits_30d: 29
commits_90d: 46
commit_cadence: "daily"
size_kb: 2036
archived: false
fetched_at: "2026-11-09T21:41:26Z"
last_release: "v2.1.0"
last_release_at: "2026-11-08"
---

# Heretic

## 出来ること

- 追加学習なしで LLM の振る舞いを書き換えるツール。対照的なプロンプト例とスコアラの組で方向を決め、モデルの重みを数学的に操作する（ablation 系）。
- 既定の動作は拒否の抑制（検閲除去）。設定ファイルを切り替えると、slop の抑制、ユーモアの抑制、お世辞（sycophancy）の低減、感情的な整合性の変更などができる。
- 対象モデルが手元のハードで動けば改変できる。bitsandbytes による on-the-fly 4bit 量子化（`quantization = "bnb_4bit"`）で VRAM 要件を下げられる。
- 密なモデルのほか、マルチモーダルモデルや複数の MoE アーキテクチャ、ハイブリッド構成にも対応。
- 改変手順を共有する「Heretic Grimoire」と、`heretic` タグ付きで公開された数千の派生モデル（Hugging Face）。

## 目的・背景

モデルの「実行」ではなく「改変」を、大規模計算資源を持つ企業だけのものから個人の PC に下ろすことを狙う。学習を伴わないため数時間で1モデルを処理できる。コミュニティによる MMLU / GSM8K の比較では、競合の abliteration ツールより良い傾向と README は主張している（一次データは外部の投稿）。

## 依存関係

- Python 3.10 以上、PyTorch 2.6 以上。
- `pip install -U heretic-llm`。

## 実行条件

- 対象モデルが動くだけの VRAM が必要（4bit 量子化で大幅に下がる）。
- 設定は作業ディレクトリの `config.toml`、または `HERETIC_CONFIG_FILE` で指定。
- **Heretic 1.x 用の設定ファイルは 2.x と非互換**。移行ガイド（`docs/migration_v1_to_v2.md`）を参照。
- ライセンスは AGPL-3.0。改変・再配布の条件は本家と各モデルのライセンスに従う。検閲除去は各モデルの利用規約と法域のルールの範囲で使う。

## 最短手順

```bash
pip install -U heretic-llm
heretic Qwen/Qwen3-4B-Instruct-2507
```

## 変更履歴

- 2026-11-03: 初回登録（star 38,738 / pushed 2026-11-03 / AGPL-3.0）
