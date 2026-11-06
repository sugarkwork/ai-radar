---
repo: Renz1998/ComfyUI-Prompt-Atelier
name: ComfyUI Prompt Atelier
genre: other
url: https://github.com/Renz1998/ComfyUI-Prompt-Atelier
license: GPL-3.0
stars: 0
language: Python
created: 2026-11-04
updated: 2026-11-05
added: 2026-11-05
first_seen: 2026-11-05
source_post: https://x.com/aiaicreate/status/2118345509077401991
sources: []
flags: []
risk_notes: ""
forks: 0
open_issues: 1
commits_30d: 25
commits_90d: 25
commit_cadence: daily
size_kb: 5670
archived: false
fetched_at: "2026-11-06T03:38:14Z"
---

# ComfyUI Prompt Atelier

## 出来ること

- ローカルモデルで**生成用プロンプトを作る／広げる** ComfyUI ノード集。画像キャプション生成、キャラクター指示、DART タグ拡張、MOSS 用レイアウトJSON出力をまとめて扱う。
- `nkchocoai/ComfyUI-Dart` の拡張フォーク。**旧ノードIDを維持**しているため、既存ワークフローを差し替えずに使える。
- ローカルの Qwen / DART モデルを使い、単語からのタグ展開や画像からの詳細プロンプト生成ができる。
- 詳細度を4段階で指定でき、最大トークン数を制御できる。
- MOSS 向けの**レイアウトJSON**を直接出力できる（配置指定プロンプトの生成）。

## 目的・背景

画像生成のプロンプト作成は、参照画像を見ながら語彙を足していく作業で、外部のLLMサービスに投げることが多い。それを ComfyUI 内のローカルモデルで完結させ、ワークフローの一部として扱えるようにする。2026-11-04 公開の新しいプロジェクト。

## 依存関係

- ComfyUI。
- ローカルの Qwen 系モデル、DART モデル（タグ拡張用）。モデルは別途取得する。
- リポジトリサイズは約5.7MB（コードのみ）。

## 実行条件

- ★0・作成から1日（2026-11 時点）。**実績はまだない**ため、既存の ComfyUI-Dart ワークフローの互換性を自分で確認する。
- GPL-3.0（フォーク元のライセンスを継承）。
- MOSS 用JSONは MOSS 側のスキーマに依存する。バージョン差異で読めないことがある。
- 画像キャプション生成はビジョンモデルの性能に依存する。日本語の語彙はモデル次第。

## 最短手順

```text
1. ComfyUI/custom_nodes にリポジトリを配置
2. ComfyUI を再起動し、Prompt Atelier のノードを追加
3. Qwen / DART のモデルパスを設定
4. 画像 or 単語を入力 → 詳細度（4段階）と最大トークンを指定 → プロンプト生成
5. 必要なら MOSS レイアウトJSONを出力して下流ノードへ
```

## 変更履歴

- 2026-11-05: 初回登録（★0 / pushed 2026-11-05 / GPL-3.0 / 公開翌日）
