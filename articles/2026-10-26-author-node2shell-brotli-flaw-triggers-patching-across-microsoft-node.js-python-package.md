---
name: "Node2Shell: Brotli Flaw Triggers Patching Across Microsoft, Node.js, Python Packages"
genre: "article"
url: "https://www.securityweek.com/node2shell-brotli-flaw-triggers-patching-across-microsoft-node-js-python-packages/"
published: "2026-10-26"
flags: []
type: "article"
added: "2026-11-16"
first_seen: "2026-11-16"
risk_notes: ""
sources: ["https://x.com/ueo0j/status/2122146243509973404"]
fetched_at: "2026-11-16T08:23:16.579534+00:00"
---

# Node2Shell: Brotli Flaw Triggers Patching Across Microsoft, Node.js, Python Packages

## テーマ

- Google Brotliデコーダーの境界外書き込み脆弱性（CVE-2026-111497、Node2Shell）と、Node.js、Microsoft製品、Pythonパッケージなどにおける修正状況を扱う。

## 著者の主張

- 記事は、細工したBrotli入力が脆弱なデコーダーに渡ると、プロセスのクラッシュやメモリ内容の漏えい、コード実行につながる可能性があると説明する。修正版への更新に加え、実行中プロセスの再起動や修正済みベースイメージでのコンテナ再構築が必要としている。

## 裏取り・注意点

- Node.js公式の2026年10月21日セキュリティリリースは、脆弱性がNode.js 22.x、24.x、26.xに影響し、細工された入力をnode:zlibで展開する場合にプロセスメモリの破損が起こり得ると説明している。公式修正版はそれぞれ22.23.4、24.22.1、26.12.1。記事が紹介するImpervaのコード実行実演は研究者による報告であり、この記事の独立実測ではない。影響には、攻撃者制御データが脆弱なデコーダーに到達する経路が関係する。

## 出典

- SecurityWeek記事（公開日と記事内容）: https://www.securityweek.com/node2shell-brotli-flaw-triggers-patching-across-microsoft-node-js-python-packages/
Node.js公式セキュリティリリース: https://nodejs.org/en/blog/vulnerability/october-2026-security-releases
Node.js 22.23.4リリース: https://nodejs.org/en/blog/release/v22.23.4/
Node.js 24.22.1リリース: https://nodejs.org/en/blog/release/v24.22.1/
Node.js 26.12.1リリース: https://nodejs.org/en/blog/release/v26.12.1/

## 変更履歴

- 2026-11-16: 初回登録
