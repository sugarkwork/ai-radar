---
name: "Dreaming with a dynamic workflow"
genre: "article"
url: "https://platform.claude.com/cookbook/managed-agents-cma-dreaming-with-a-dynamic-workflow"
published: "2026-11-02"
flags: ["unverified"]
risk_notes: "記事の費用・所要時間は著者が示した条件での報告で、一般的な性能保証ではない。また、記事は未信頼の記録がメモリ内容を変えうると説明している。夜間の既存ストア更新には変更の事前レビューが既定でないため、運用前に保存内容を確認する必要がある。"
type: "article"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/lucas_flatwhite/status/2118883529253941380"]
fetched_at: "2026-11-14T10:09:59.398597+00:00"
---

# Dreaming with a dynamic workflow

## テーマ

- Managed Agentsのdynamic workflowを使い、完了済みセッションの記録をwiki形式のメモリにまとめ、後続セッションが読み取り専用で利用する「dreaming」の実装例。

## 著者の主張

- 著者は、リードエージェントがワークフローを作成し、各記録を分析するエージェント群がメモリを作成・更新した後、整理エージェントが重複や索引を整える構成を示す。記事内の報告では、約12 MB・50超の長い記録を使ったdreamは、既定設定で約8ドル・約10分、比較設定では約10ドル・約9分だった。これは記事記載の実行条件における著者の報告である。

## 裏取り・注意点

- 公式手順では、分析エージェントは記録を未信頼データとして扱い、メモリストアを読み書きする。利用する側のセッションにはストアを読み取り専用でマウントする。記事は、悪意ある記録がストアの内容を変えたり予算を消費したりしうると説明し、夜間更新は既存ストアへ反映される前に既定のレビューがないため、保存内容の監査を勧めている。費用と時間の数値は特定条件での著者報告であり、一般化できる性能保証ではない。

## 出典

- Anthropic, “Dreaming with a dynamic workflow,” 公開日 2026-11-02. https://platform.claude.com/cookbook/managed-agents-cma-dreaming-with-a-dynamic-workflow

## 変更履歴

- 2026-11-14: 初回登録
