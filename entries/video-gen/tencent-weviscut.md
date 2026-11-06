---
type: "repo"
name: "WeVisCut（記事を数分の編集済み動画に変える9Bツールエージェント）"
genre: "video-gen"
url: "https://github.com/Tencent/WeVisCut"
repo: "Tencent/WeVisCut"
license: "Apache-2.0（GitHub API は NOASSERTION）"
stars: 79
language: "Python"
created: "2026-09-09"
updated: 2026-10-30
added: "2026-11-06"
first_seen: "2026-10-31"
sources: ["https://x.com/Machinedelusion/status/2116668287656333409", "https://tencent.github.io/WeVisCut/", "https://huggingface.co/tencent/WeVisCut"]
flags: []
risk_notes: "README の『Claude Opus 5 と同等を約33分の1のトークンで』は技術レポート側の主張で、第三者の独立再現は確認していない。配布物はコードと学習用パイプラインまでで、既定の素材検索は公開Web検索に依存するため、そのままでは素材の権利確認は利用者側の責任。bf16 の9Bを動かすには約24GBのNVIDIA GPUが要る（UIだけならGPU不要）。学習済みポリシーの重みは HF の tencent/WeVisCut。"
forks: 11
open_issues: 1
commits_30d: 10
commit_cadence: weekly
size_kb: 733802
archived: false
fetched_at: "2026-11-06T09:14:02Z"
last_release: ""
last_release_at: ""
commits_90d: 29
---

# WeVisCut — 知識記事やナレーション原稿を、数分の編集済み動画に組み上げる9Bツールエージェント

## 出来ること

- 長文の知識記事／ナレーション原稿を渡すと、章分割・ショット設計・ナレーション合成・素材検索・テンプレート装飾・BGM選曲・品質判定・自己修復・結合までを、1回あたり**約12回のツール呼び出し**で通しで行う
- 行動空間は**12個の編集ツール**：`Tool_SegmentArticle`（章分割）、`Tool_PlanShots`（ショット設計）、`Tool_GenerateAudio`（ナレーション合成、ここで尺が確定する）、`Tool_RetrieveVisual`（素材検索）、`Tool_DecorateShot`（アニメーションテンプレートの穴埋め）、`Tool_TimelineCompose`（1ショットのレンダリング）、`Tool_MusicSearch`（BGMプレイリスト）、`Tool_TextQuickJudge` / `Tool_VLMRenderJudge`（文章／書き出し後の動画の品質ゲート）、`Tool_SelfReflect`（次に直す場所の決定）、`Tool_ModalProbe`（外部サービスの事前確認）、`Tool_StitchVideo`（最終結合）
- **段階をハードコードしない**：各ステップで9Bのポリシーが現在の編集状態を読み、ツール呼び出しを**1つだけ**出す。ガードレールは不正な呼び出しを拒否するだけで、代わりの判断はしない
- **Studio（`studio/`）**：章・ショット・ナレーション・字幕・素材・テンプレート・BGM・レンダリングの8トラックが同期した編集タイムライン。一時停止／再開、手動編集、チャットでの修正指示（「冒頭の一文を変えて」「0:15の映像を差し替えて」）、変更したショットだけの再レンダリング、バージョンのロールバックができる
- **学習時と同一の実行環境**：推論時も学習時と同じ12ツール・同じ状態JSONを渡す（プロンプト内に出てくる `AICutPipeline` は学習時の識別子で、意図的に残されている）
- **データ生成パイプライン（`data_construct_pipeline/`）**：orchestrator / generator / critic の3ロールで長距離トラジェクトリを収集する仕組みを同梱。Studio が学習済みポリシーを**提供する**側、こちらは学習データを**記録する**側
- 素材とBGMの既定取得先は公開Web検索（`asset_retrieval_tool`）。`studio_config.yaml` で自前のHTTP API・ローカルフォルダ・Pythonプラグインに差し替えられる（通常いじるのはこのファイルだけ）

## 目的・背景

- 動画編集を「ツール列をエージェントが自分で選ぶ問題」として解いた研究色の強いリリース。従来の自動編集は工程を固定したパイプラインになりがちで、素材が取れない・尺が合わないといった失敗に弱い。WeVisCut は失敗を検出して自分で直す経路（judge → reflect → repair）をツール呼び出しの中に置いている
- Tencent の公開リポジトリで、技術レポート・9Bポリシーの重み・Studio ランタイム・軌跡構築パイプラインの4点セットが同時に出ている
- 投稿は英語圏のアカウントによる紹介で、tencent.github.io のプロジェクトページと HF のモデルページ、GitHub の3リンクを並べている

## 依存関係

- Python 3.11 以上。`requirements.txt` と（GPU環境では）`requirements-gpu.txt`。CUDAに合った torch を先に入れる
- `scripts/setup_external_tools.sh` が ffmpeg・Node・レンダラ（約1.1GB）を取得する
- `huggingface_hub[cli]` で `tencent/WeVisCut` を取得。重みの読み込みには `qwen3_5` を登録した `ms-swift` が必要（自前の環境を使う場合は `AICUT_MS_SWIFT_PATH`）
- github.com に到達できない環境向けに、`requirements.txt` の git 固定を `deepagents==0.7.7` に置き換える案内がある

## 実行条件

- bf16 の9Bポリシーを動かすには **約24GBのNVIDIA GPU**。`run_studio.sh --no-model` なら重みを読まずにUIだけ起動できる
- 起動は `http://<host>:8081/`。重みはバックグラウンドで30〜60秒かけて読み込まれ、その間もUIは操作できる
- 既定の素材検索は公開Web検索なので、オフライン環境では `studio_config.yaml` の差し替えが前提
- 素材・BGMの権利はツール側では担保されない。公開Web検索の結果をそのまま書き出せるため、公開用途では取得元の確認が要る
- 直近30日のコミットは 0 で、最終pushは 2026-10-30。研究リリース直後の状態で、活発に開発中というわけではない

## 最短手順

```bash
git clone https://github.com/Tencent/WeVisCut.git && cd WeVisCut

pip install -r requirements.txt
pip install -r requirements-gpu.txt          # CUDA に合う torch を先に入れておく

bash scripts/setup_external_tools.sh         # ffmpeg / Node / レンダラ（約1.1GB）

pip install -U "huggingface_hub[cli]"
hf download tencent/WeVisCut --local-dir checkpoints/weviscut-9b

bash run_studio.sh --check                   # パス確認のみ（GPU不要）
bash run_studio.sh                           # http://<host>:8081/
# 重みを読まずにUIだけ見る場合: bash run_studio.sh --no-model

# 素材・BGMの取得先を変える
python3 -m studio.config --summary
# → studio_config.yaml を編集（HTTP API / ローカルフォルダ / Python プラグイン）
```

## 変更履歴

- 2026-11-06: 初回登録
