---
name: "Introducing Loom: agent memory that keeps up with your code"
genre: "article"
url: "https://clickhouse.com/blog/introducing-loom-agent-memory-that-keeps-up-with-your-code"
published: "2026-11-13"
flags: ["unverified"]
risk_notes: "ベンチマークはClickHouseによる自社評価であり、記事は独立した再現結果を示していない。記載された改善値は評価条件に基づく著者報告として扱う。"
type: "article"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/legoboku/status/2121527246062236042"]
fetched_at: "2026-11-14T09:09:18.732975+00:00"
---

# Introducing Loom: agent memory that keeps up with your code

## テーマ

- ClickHouse上にエージェントの記憶とコード索引を統合するオープンソースツール Loom の紹介。記事は、記憶の保存・検索・共有と、記憶を現在のコードに照らして扱う設計を説明している。

## 著者の主張

- 著者らによると、Loomは記憶とコード索引を同じClickHouseデータベースに置き、MCP・HTTP API・Python/TypeScript SDK経由で保存や検索を行う。検索ではベクトル検索、BM25、長文の逐語チャンク、エンティティグラフを併用し、記憶には出典やバージョンを保持する。コード変更で記憶が古くなった場合はレビュー対象として示すという。記事記載の自社ベンチマークでは、コード質問の平均回答品質スコアが0.78から0.84へ、ファイル特定精度が91.4%から96.4%へ変化した。

## 裏取り・注意点

- 記事には導入要件としてClickHouse 26.5以降、ベクトル検索の高速経路には26.8以降を推奨と記載。ベンチマークは記事著者による自社評価で、コード質問24問・各3回などの条件が示されている。LongMemEval-Sの100問比較については著者自身が統計的有意差を主張するには不十分としている。これらの数値は独立実測ではなく、掲載された評価条件下での著者報告。

## 出典

- ClickHouse公式ブログ「Introducing Loom: agent memory that keeps up with your code」（2026-11-13）。https://clickhouse.com/blog/introducing-loom-agent-memory-that-keeps-up-with-your-code

## 変更履歴

- 2026-11-14: 初回登録
