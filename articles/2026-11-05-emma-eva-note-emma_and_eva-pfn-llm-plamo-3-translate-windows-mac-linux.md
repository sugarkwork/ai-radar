---
type: "article"
name: "PFNの翻訳特化LLM「PLaMo 3 Translate」をスマホ・Windows・Mac・Linuxに入れる方法"
genre: "article"
url: "https://note.com/emma_and_eva/n/n47bfc2009891"
author: "Emma先生 & Eva先生（note: emma_and_eva）"
published: "2026-11-05"
added: "2026-11-06"
first_seen: "2026-11-07"
sources: ["https://www.preferred.jp/ja/news/pr20261105", "https://huggingface.co/pfnet/plamo-3-translate-8b", "https://github.com/pfnet/plamo-translate-cli", "https://x.com/preferred_jp/status/2118134261912092801"]
flags: ["unverified"]
risk_notes: "PFN 公式ブログではなく第三者アカウントのまとめ記事。ベンチマーク優位は PFN 自身の評価の引用、iPhone の 0.515 秒は GIGAZINE の 1 回計測の引用で独立検証なし。winget での llama.cpp 導入、PocketPal AI での 0.8B 読み込み手順、llama.app のインストールスクリプト（取得したスクリプトをシェルに渡す方式）は本文の記述のみで未検証。記事末尾は著者の有料講義の宣伝。"
fetched_at: "2026-11-06T18:28:40Z"
source_post: "https://x.com/preferred_jp/status/2118134261912092801"
---

# PFNの翻訳特化LLM「PLaMo 3 Translate」をスマホ・Windows・Mac・Linuxに入れる方法

## テーマ

- PFN が 2026-11-05 に重みを公開した翻訳特化 LLM「PLaMo 3 Translate」（0.8B / 2B / 8B / 31B）を、iPhone・Android・Windows・Mac・Linux の各環境でローカルに動かすための導入手順を OS 別に整理した記事。
- 著者は PFN ではなく、note で AI 活用講義を販売するアカウント「Emma先生 & Eva先生」。公式ドキュメントの代替ではなく、複数系統の導入路を 1 本にまとめた二次資料として読む位置づけ。

## 著者の主張

- 導入は 3 系統。モバイルは PocketPal AI + GGUF（Q4_K_M、Snapdragon 端末は Q4_0 も可）、デスクトップは llama.cpp の llama-server、Apple Silicon の Mac は PFN 公式 CLI plamo-translate（MLX バックエンド）。
- サイズ選択は「スマホは 0.8B、PC は 2B から始め、品質が足りなければ 8B」。31B は NVIDIA GPU + vLLM 向け。
- 量子化は Q4_K_M を推奨。Q2_K は一部指標で低下が目立つとモデルカードにあるとしている。
- llama-server では --chat-template-file chat_template.jinja の指定が必須（GGUF 埋め込みの旧テンプレートは訳文履歴を扱えない）。
- 用語集（glossary）・文脈（context）・文体（form: polite / plain）は chat_template_kwargs で渡し、システムプロンプトや原文に指示を混ぜない。
- ライセンスは非商用が無償・登録不要、商用は売上 10 億円で条件が分岐するため業務利用前に全文確認が必要。
- 「外部に送信されない」はローカル実行時のみで、クラウド版の「PLaMo翻訳」とは別物だと明記している。

## 裏取り・注意点

- GGUF の Q4_K_M ファイルサイズ（0.57 / 1.81 / 5.28 / 19.53 GB）は Hugging Face API の blob サイズ（573,123,200 / 1,807,199,392 / 5,280,442,080 / 19,526,590,304 bytes）と一致した。
- 公式 CLI の記述（pip install plamo-translate、Python 3.10〜3.14、MLX で初回 5.76 GB を取得し読み込み時に 4bit 量子化、既定は 2B）は pfnet/plamo-translate-cli の README と一致。リポジトリは ★358・最終 push 2026-11-06 で現役。
- CLI は Windows 非対応（WSL 利用）と README に明記されており、記事が Windows を llama.cpp 手順にしていることと矛盾しない。
- 未検証: winget での llama.cpp 導入、PocketPal AI での plamo-3-translate-0.8b 読み込み手順、llama.app のインストールスクリプト（URL は 200 を返すが中身は未確認。取得したスクリプトは実行前に内容確認が必要）。
- 未検証: iPhone 17 Pro で約 280 語を 0.515 秒という数値は GIGAZINE の 1 回計測の引用。TranslateGemma や Hy-MT2 を上回るという主張は PFN 自身の評価で第三者の再現は出ていない（記事も「参考程度に」と留保）。
- 記事は著者の有料講義（AI 講義シリーズ）の宣伝を末尾に含む。手順部分は具体的だが、数値・優位性の主張は出典元の性格を踏まえて扱う必要がある。
- モデル本体は models/other/pfnet-plamo-3-translate-8b.md に既存。本記事はモデル解説ではなく OS 別導入手順（CLI・llama.cpp・モバイル）に価値があり、モデル項目とは内容が重ならない。

## 出典

- 記事: https://note.com/emma_and_eva/n/n47bfc2009891 （2026-11-05 15:10 公開、Emma先生 & Eva先生）
- PFN ニュースリリース: https://www.preferred.jp/ja/news/pr20261105
- モデルカード: https://huggingface.co/pfnet/plamo-3-translate-8b / https://huggingface.co/pfnet/plamo-3-translate-2b-GGUF
- 公式 CLI: https://github.com/pfnet/plamo-translate-cli
- 記事が引用する検証: GIGAZINE https://gigazine.net/news/20261105-plamo-3-translate-open-weight/ 、PC Watch https://pc.watch.impress.co.jp/docs/news/2153784.html

## 変更履歴

- 2026-11-07: 初回登録
