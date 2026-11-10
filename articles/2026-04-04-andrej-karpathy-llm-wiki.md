---
name: "LLM Wiki"
genre: "article"
url: "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
author: "Andrej Karpathy"
published: "2026-04-04"
flags: ["unverified"]
risk_notes: "導入時間、任意のPDFの取り込み、回答精度、規模拡大時の性能は未検証。Gist本文では再配布ライセンスと実装時の費用を確認できなかった。"
type: "article"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/Bober_smart/status/2116526023256723618"]
fetched_at: "2026-11-10T06:14:16Z"
---

# LLM Wiki：原資料から更新し続けるMarkdown知識ベース

## テーマ

- 原資料を保存し、LLMエージェントが相互リンク付きのMarkdown Wikiを更新する設計。原資料、生成Wiki、運用ルール文書の三層を分ける。

## 著者の主張

- 取り込み時に要約や関連ページを更新しておくと、質問のたびに原資料から知識を組み立て直す手間を減らせるという提案。索引と更新ログを設け、定期点検で矛盾や古い記述、リンク漏れを探す。

## 裏取り・注意点

- 原文ではClaude CodeのCLAUDE.mdやCodexのAGENTS.mdを運用ルール文書の例に挙げ、Obsidianを閲覧に使う著者の運用を紹介している。具体的なフォルダ構成やツール選択は利用者に委ねている。
- 候補投稿の閲覧数や5分での導入、任意のPDFを処理できるという記述は原文で裏付けられなかった。回答精度や規模拡大時の性能は実測していない。

## 出典

- [Andrej Karpathyの公開Gist『LLM Wiki』](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)。候補投稿やその返信とは区別し、登録対象はこの設計解説とした。

## 変更履歴

- 2026-11-10: 初回登録
