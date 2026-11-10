---
repo: "Leonxlnx/earshot"
name: "earshot"
genre: "tts-audio"
url: "https://github.com/Leonxlnx/earshot"
license: "MIT"
stars: 4406
forks: 283
open_issues: 4
size_kb: 3489
language: "Python"
created: "2026-10-15"
updated: "2026-11-06"
archived: false
commits_30d: 51
commits_90d: 51
commit_cadence: "daily"
last_release: "v0.4.1"
flags: ["unverified"]
risk_notes: "実行と独立評価は未実施。作者評価の結果が他の素材や編集工程に一般化するか、発見投稿の動画で効果音のタイミングが改善したか、最新版の正確な公開時刻は未確認。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/Y0urDumble/status/2115193601458151552"]
fetched_at: "2026-11-10T11:59:42+00:00"
---

# earshot — AIエージェント向けのローカル音声レビューと効果音合成

## 出来ること

- 音声の特徴をタグと測定値で記述し、文章との一致度を評価する。長い録音から条件に合う区間を探し、動画の音響タイムラインや改善候補も出力できる。
- forge はコードから効果音候補を合成・評価する。fit は録音に近い音を生成するパラメータ付きの合成コードを書き出す。

## 目的・背景

- コーディングエージェントが音声や映像を制作した後、タグ、音響指標、タイムラインを使って修正箇所を判断するためのツール。
- 作者は v0.4.1 のリリースノートで、実録の効果音195件のうち168件が各素材のタイトルを用いた判定に合格したと報告している。演出上の役割を示す抽象的な表現では判定が難しいとも記している。

## 依存関係

- READMEのuv導入手順では、uvとPATH上のffmpeg・ffprobeが必要。クローンからの導入はPython 3.10以上で、CPU版PyTorchを使う。
- コードはMIT。README記載の既定モデルはCLAPがApache-2.0、ASTがBSD-3-Clause。録音をfitで加工する場合は元録音の利用条件も確認する。

## 実行条件

- ローカルCPUで動作する。初回のモデル利用時に合計約1.1 GBの重みを取得し、以後はキャッシュから読み込む。
- 任意のGeminiレビュー機能には別途APIキーが必要。

## 最短手順

- `uv tool install "earshot[mcp] @ git+https://github.com/Leonxlnx/earshot"` で導入し、`earshot doctor --fetch` でモデルを取得する。
- Claude Codeに `claude mcp add earshot --scope user -- earshot mcp` で登録する。AIにearshotで対象のWAVを記述するよう依頼するか、対象動画のカットと効果音のタイミングをレビューするよう依頼する。CLIからは `earshot describe enter.ogg` で音声の記述を試せる。

## 変更履歴

- 2026-11-10: 初回登録
