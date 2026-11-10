---
type: "repo"
name: "ACE-Step（v1 / 3.5B）"
genre: "tts-audio"
url: "https://github.com/ace-step/ACE-Step"
repo: "ace-step/ACE-Step"
license: "Apache-2.0"
stars: 5044
language: "Python"
created: "2025-04-28"
updated: "2026-02-15"
added: "2026-11-07"
first_seen: "2026-11-07"
sources: ["https://x.com/abir35627/status/2118648224202551573"]
flags: []
risk_notes: "① 発見元ポストは「ACE-Step 1.5」とセクション再生成を挙げているが、本リポジトリは v1（重みは ACE-Step-v1-3.5B）で、v1.5 は別リポジトリ ace-step/ACE-Step-1.5。ロードマップの「Train and Release ACE-Step V1.5」も未チェックのままで、v1.5 の告知は外部ページへのリンクのみ。本エントリの対象は v1 であり、新規プロジェクトとして読むべきではない。② 最終 push は 2026-02-15 で約9か月停止（30日コミット0）、タグ・GitHub Releases はゼロ。open issues 155 件が未処理のまま。③ setup.py の version は 0.2.0、classifier は Development Status :: 3 - Alpha。④ Dockerfile はビルド時に HEAD を clone するため再現性がなく、イメージを固定できない。⑤ README の「8GB VRAM」は cpu_offload 併用時の値で、素の推論要件ではない。⑥ HF の重みは 2025-05-22 以降更新なし。⑦ Features 節は RapMachine を「Coming Soon」に残したまま、News では 2025-05-12 にリリース済みと書いており記述が古い。⑧ README が ac**p.com 等を偽サイトと明記しており、公式は GitHub Pages のみ。"
forks: 662
open_issues: 155
commits_30d: 0
size_kb: 14337
archived: false
fetched_at: "2026-11-09T21:42:51Z"
commits_90d: 0
commit_cadence: "stale"
last_release: ""
last_release_at: ""
---

# ACE-Step（v1 / 3.5B） — 歌詞付きの楽曲をGPUで数十秒に生成する音楽生成基盤モデル

## 出来ること

- Text2Music: タグ（ジャンル・楽器・雰囲気）＋構造タグ付き歌詞（[verse] / [chorus] / [bridge]）＋長さを渡して楽曲を生成する。抽象では「A100 で4分の楽曲を20秒」と記載。
- 歌詞は19言語に対応し、性能が良い上位10言語として英語・中国語・ロシア語・スペイン語・日本語・ドイツ語・フランス語・ポルトガル語・イタリア語・韓国語を挙げる。データ量の偏りから少数言語は劣ると明記。
- Retake: seed と分散度を変えて、元の生成物から少しだけ違うテイクを作る。
- Repainting: 開始・終了時刻を指定して、楽曲の一部区間だけを再生成する（入力は text2music の出力／直前の repaint／アップロードから選ぶ）。発見元ポストの「セクション再生成」に対応する機能で、v1 にも存在する。
- Edit: タグや歌詞を差し替えて既存曲を編集する。only_lyrics モード（旋律を保持）と remix モード（旋律も変える）の2択。flow-edit による歌詞の局所修正は、歪みを避けるため一度に小さい区間のみ、逐次適用。
- Extend: 曲の前後に音を足して延長する（左右の長さを個別指定）。
- LoRA: 歌詞からボーカルだけを出す Lyric2Vocal、テキストから楽器ループ／サンプルを出す Text2Samples、中国語ラップの RapMachine（ACE-Step-v1-chinese-rap-LoRA）。学習コードとLoRA学習手順も同梱。
- Gradio の Web UI（7865番）と Python API の両方。ComfyUI ノードは別リポジトリ（ACE-Step-ComfyUI）。

## 目的・背景

- ACE Studio と StepFun の共同プロジェクト。技術レポートは arXiv 2506.00045（2025-06）。
- 構成は diffusion 系の生成に Sana の Deep Compression AutoEncoder（DCAE）と軽量 linear transformer を組み合わせ、学習時に MERT / m-hubert で意味表現を揃える（REPA）。LLM 系の歌詞整合と diffusion 系の速度の折衷を狙う。
- 単発の text-to-music パイプラインではなく「音楽版 Stable Diffusion」＝サブタスクを載せられる基盤モデル、というのが README の主張。Lyric2Vocal などの LoRA はその実例。
- バージョンの関係（重要）: 本リポジトリは v1 で、重みは Hugging Face の ACE-Step/ACE-Step-v1-3.5B。**v1.5 はこのリポジトリの後継タグではなく、別リポジトリ ace-step/ACE-Step-1.5**（2025-09-04 作成、HF は ACE-Step/Ace-Step1.5、2026-01-28 公開、XL 4B 系は 2026-04-02）。本リポジトリの README は v1.5 を外部ページへのリンクと News 項目として紹介するだけで、コードも重みも含まない。ロードマップの該当項目も未完了のまま。v1.5 の機能（4GB未満での動作、10分までの生成、ステム分離など）を使いたい場合の移行先は ACE-Step-1.5。

## 依存関係

- Python 3.10 以上（README の推奨。Dockerfile も 3.10）。venv か Conda。
- PyTorch（README の例は CUDA 12.6 版）。requirements.txt は diffusers>=0.33.0、transformers==4.50.0、pytorch_lightning==2.5.1、librosa==0.11.0、spacy==3.8.4、accelerate==1.6.0、gradio、soundfile==0.13.1、peft、numpy などをピン留め。
- 歌詞の前処理: 日本語は cutlet + fugashi[unidic-lite]、言語判定に py3langid、韓国語は hangul-romanize、中国語は pypinyin。日本語歌詞を使うならこの一式が必須。
- Windows で `--torch_compile` を使う場合は triton-windows。
- 重みは初回起動時に Hugging Face から自動取得（既定 `~/.cache/ace-step/checkpoints`）。内訳は transformer 6.61GB、umt5-base 1.13GB、DCAE 0.31GB、vocoder 0.21GB で合計約8.3GB。
- Docker は nvidia/cuda:12.6.0-runtime-ubuntu22.04 ベース。`/app/checkpoints` `/app/outputs` `/app/logs` をボリューム化。

## 実行条件

- プロジェクト自身の記載: 2025-05-10 のメモリ最適化で「Max VRAM を 8GB に削減、コンシューマ機器との互換性を向上」。推奨起動は `acestep --torch_compile true --cpu_offload true --overlapped_decode true`。つまりこの 8GB は CPU オフロード併用時の値。
- 速度は README の実測表（batch 1、単一GPU）: RTF は 27 steps で RTX 4090 34.48x / A100 27.27x / RTX 3090 12.76x / MacBook M2 Max 2.27x。1分の音声を描画する時間はそれぞれ 1.74s / 2.20s / 4.70s / 26.43s。60 steps では M2 Max が RTF 1.03（ほぼ実時間）まで落ちる。
- macOS では `--bf16 false` を指定する（README の明記）。
- 生成物の権利・著作権リスクは README の disclaimer 側の話で、Apache-2.0 はコードに対するライセンス。商用利用の可否はモデルカードと自国の法域で別途確認が要る。
- README は「公式サイトは GitHub Pages のみ、ac**p.com 等は偽サイト」と警告している。課金を伴う類似ドメインは踏まない。

## 最短手順

```bash
git clone https://github.com/ace-step/ACE-Step.git
cd ACE-Step
python -m venv .venv && source .venv/bin/activate
pip install -e .
acestep --port 7865
```

省メモリ構成（README の推奨）:

```bash
acestep --torch_compile true --cpu_offload true --overlapped_decode true
```

- 重みの置き場所を固定するなら `acestep --checkpoint_path /path/to/checkpoint --port 7865 --device_id 0 --bf16 true`。指定先にモデルが無ければ自動でそこへ落ちる。
- ライブラリとして使うなら `pip install git+https://github.com/ace-step/ACE-Step.git`。
- Docker なら `docker compose up`（compose はビルド時に GitHub の HEAD を clone するため、版は固定されない）。
- UI のタブは Text2Music → Retake → Repainting → Edit → Extend の順。部分的な作り直しは Repainting で開始・終了秒を指定する。

## 変更履歴

- 2026-11-07: 初回登録
