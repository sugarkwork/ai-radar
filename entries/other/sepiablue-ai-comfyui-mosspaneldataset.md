---
repo: "sepiablue-ai/ComfyUI-MossPanelDataset"
name: "ComfyUI-MossPanelDataset"
genre: other
url: "https://github.com/sepiablue-ai/ComfyUI-MossPanelDataset"
license: "MIT"
stars: 39
language: "Python"
created: "2026-11-02"
updated: 2026-11-06
added: "2026-11-03"
first_seen: "2026-11-03"
sources: []
flags: []
risk_notes: ""
forks: 5
open_issues: 0
commits_30d: 18
commits_90d: 18
commit_cadence: weekly
size_kb: 47794
archived: false
fetched_at: "2026-11-06T22:52:14Z"
---

# ComfyUI-MossPanelDataset

## 出来ること

- ComfyUI のカスタムノード。196枚の見本から漫画のコマ割り（2〜6コマ）を画像で選び、人物・場面・セリフを専用欄に入力して MOSS-Image に渡す。配置ごとのワークフローを探したり、JSON や座標を手書きしたりする必要がない。
- コマ数・種類・名前で絞り込み、お気に入り登録ができる。配置を選ぶとコマ入力ノードと接続が自動で増減し、コマを減らしたときの入力は退避されて、戻すと復元される（人物・セリフ・モデル・サンプラー・シードの設定を維持）。
- 人物の外見と場面は英語で、セリフは描かせたい言語のまま渡す。翻訳も追加の LLM も使わない。
- 「空のコマ枠」モードで、人物・場面・セリフを除いた枠だけを生成できる。プロンプトを確認・編集するノードも同梱。
- 見本画像と配置情報を同梱しているため、導入後のカタログ閲覧に外部サービスへの接続は不要。デモ動画（30秒）付き。
- **構図テンプレート120種**: 1人40・2人40・3人40の構図見本から、コマごとにカメラ構図を選べる。見本画像を参照入力に渡すのではなく、英語プロンプトと人物領域の比率指定で誘導する（接続しなければ従来の処理）。
- **3人までの人物指定**: 共通の人物設定に人物3を足せる。各コマで1〜3人の任意の組み合わせと最大3発言を指定でき、話す順番を変えても人物の位置は入れ替わらない。
- **人物画像から外見を抽出**: 人物画像を MOSS と共用のテキストエンコーダー（Qwen）で英語の外見文へ変換して外見欄へ渡せる。年代・顔立ち・体格・髪型・服装などを拾い、追加モデルは要らない。UI は ComfyUI の表示言語に追随する（日本語／英語）。

## 目的・背景

漫画生成では「コマ割り」の指定が最大の摩擦で、配置ごとに配布ワークフローを探して座標を直す必要があった。それを画像から選ぶ UI に置き換え、MOSS-Image のプロンプト組み立て（コマごとの人物・場面・セリフ）までをノード内で完結させる。データセットの元生成は Windows + RTX 3060 12GB で行ったと README にある。

## 依存関係

- Python 3.10 以上と、MOSS-Image のネイティブ対応を含む ComfyUI（動作確認は ComfyUI v0.42.0 / Python 3.13）。`CLIPLoader` に `moss_image`、`EmptyFlux2LatentImage` ノードが必要で、古い ComfyUI では動かない。
- モデル重みは非同梱。手動で配置する: `diffusion_models/moss_image_sft_int8_convrot.safetensors`、`text_encoders/qwen3.5_9b_int8_convrot.safetensors`、`vae/flux2-vae.safetensors`。

## 実行条件

- 同梱ワークフローの設定は 1024×1536、25ステップ、CFG 2.5、`er_sde` / `simple`、DMD LoRA なし。
- 実生成が確認されているのは作者の環境（Windows / RTX 3060 12GB）のみ。他の GPU・OS での生成は未確認と明記されている。
- 旧試作版が入っている場合はフォルダを重複させない。配布版の DB は同梱196種のみで、除外された配置を使うワークフローは選び直しが必要。
- Comfy Registry には未登録。`custom_nodes` へ git clone して配置する。

## 最短手順

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/sepiablue-ai/ComfyUI-MossPanelDataset.git
# ComfyUI を再起動し、example_workflows/make_manga.json を開いて保存
```

## 変更履歴

- 2026-11-03: 初回登録（star 32 / pushed 2026-11-02 / MIT）
- 2026-11-06: 構図テンプレート120種・3人指定・人物画像からの外見抽出・日英UIを追記（ab51665 / 70636b6）
