---
type: prompt
name: "CLAUDE.md に足す「コンテキスト節約」6行（Ahorro de contexto）"
genre: prompt-other
url: ""
author: "@maarcoofdezz"
source_post: "https://x.com/maarcoofdezz/status/2117744331515666475"
sources: []
added: "2026-11-05"
flags: []
risk_notes: ""
target: "Claude Code"
transcribed_from: text
prompt_sha1: "4d505a0e0e944a175f67d250a7ae92c4bf03b74c"
---

# CLAUDE.md に足す「コンテキスト節約」6行

## 目的

Claude Code のトークン消費は、コードを書く量より「不要なファイルを丸ごと読む」「既に決めたことを繰り返す」「役目を終えた文脈を引きずる」ことに消える、という前提に立つ。CLAUDE.md の末尾に6行追記して、読み込み方と応答の仕方を変える。

投稿者が挙げている変化:

- ファイルを丸ごと読む前に検索する
- 探索はサブエージェントに任せ、要約だけ受け取る
- ファイル全文ではなく diff を見せる
- 既に決めたことを繰り返さない
- 圧縮（`/compact`）や新規セッションのタイミングを教える
- 既定で短く答える

## 前提

- Claude Code（または CLAUDE.md を読むエージェント）。
- 既存の CLAUDE.md の**末尾に追記**する。投稿者の想定所要時間は1分。
- 原文はスペイン語。プロンプト本文は一字一句そのまま収録している。

## プロンプト本文

```text
## Ahorro de contexto
- Antes de leer un archivo entero, busca con grep y lee solo lo que necesites.
- Para explorar el proyecto, usa un subagente y tráeme solo el resumen.
- Muéstrame el diff, no el archivo completo.
- No repitas lo que ya hemos decidido en esta sesión.
- Si cambiamos de tarea, propón /compact o una sesión nueva.
- Respuestas cortas por defecto.
```

日本語の意味（参考・本文は上記のまま使う）:

1. ファイルを丸ごと読む前に、grepで探して必要な分だけ読む
2. プロジェクトの探索はサブエージェントに任せ、要約だけ持ってくる
3. ファイル全体ではなく diff を見せる
4. このセッションで既に決めたことを繰り返さない
5. タスクが変わったら `/compact` か新規セッションを提案する
6. 既定では短く答える

## 使い方

- `CLAUDE.md` の末尾に上記ブロックを貼る。
- 効き方を確認するときは、同じタスクを追記前後で走らせ、`/cost` と `/context` の数値、読み込まれたファイル数を比べる。
- サブエージェント（Task）や `/compact` はバージョンによって挙動が変わる。手元のClaude Codeで使えるか先に確認する。

## 注意点

- **効果は投稿者の主張で、計測値の提示はない。**「トークンが減る」は動作の変化（読む量・出す量を減らす指示）からの推定であって、ベンチマークではない。
- 6行はいずれも「振る舞いの指示」であり、強制力はない。モデルやバージョンによっては無視されることがある。
- リプライ欄には追加案として「計算はすべてローカルのPythonで実行させる」という1行が挙がっている（手計算のトークン消費を避ける意図）。原文には含まれていない。
- 同じ内容を英語で使いたい場合は自分で訳す必要がある。機械翻訳だと「diffを見せる」などの指示が曖昧になりやすい。

## 変更履歴

- 2026-11-05: 初回登録（投稿のリプライ欄にあった6行を原文のまま収録。投稿は2,195 likes / 469,447 views 時点）
