---
name: "MarkItDown"
genre: "other"
url: "https://github.com/microsoft/markitdown"
flags: ["unverified"]
risk_notes: "プロセスの権限でリソースへアクセスするため、READMEは信頼できない環境で入力をサニタイズし、用途に必要な範囲のconvert関数を使うよう注意しています。画像のキャプションと音声の文字起こしはWebホスト型サービスに依存します。変換の精度やサービス料金はREADMEから確認できません。"
repo: "microsoft/markitdown"
stars: 194754
forks: 14682
open_issues: 816
size_kb: 6015
language: "Python"
created: "2024-11-13"
updated: "2026-11-07"
archived: false
license: "MIT"
commits_30d: 9
commits_90d: 100
commit_cadence: "weekly"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/thegreatest_sv/status/2118043980420030914"]
fetched_at: "2026-11-10T16:22:18.748508+00:00"
---

# MarkItDown

## 出来ること

- PDF、PowerPoint、Word、Excel、画像、音声、HTML、CSV・JSON・XML、ZIP、YouTube URL、EPUBなどをMarkdownへ変換します。READMEでは、見出し・リスト・表・リンクなどの文書構造をMarkdownとして保持することを重視すると説明しています。

## 目的・背景

- LLMや関連するテキスト分析パイプラインで利用するため、さまざまなファイルをMarkdownに変換する軽量なPythonユーティリティです。人が読むための高忠実度な文書変換より、テキスト分析ツールでの利用を想定しています。

## 依存関係

- Python 3.10〜3.14が必要です。形式別の追加依存関係は任意で、READMEにはPDF、DOCX、PPTXなどの個別インストール例があります。画像キャプションと音声文字起こしはWebホスト型サービスに依存します。

## 実行条件

- READMEは依存関係の競合を避けるため仮想環境を推奨しています。入力へのアクセスは実行プロセスの権限で行われます。

## 最短手順

- 仮想環境を用意し、`pip install 'markitdown[all]'`でインストールしてから、`markitdown path-to-file.pdf > document.md`を実行します。出力先は`-o document.md`でも指定できます。

## 変更履歴

- 2026-11-11: 初回登録
