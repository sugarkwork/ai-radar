---
name: "Awesome Chinese Secondhand Slang（中国二手暗语全书与避坑合规指南）"
genre: "other"
url: "https://github.com/Domainsun/awesome-chinese-secondhand-slang"
repo: "Domainsun/awesome-chinese-secondhand-slang"
flags: ["malicious", "low-quality", "unverified"]
risk_notes: "READMEは、平台の敏感語検出を避けるための代替語・暗語や、文案の排雷・転译を売り手向け用途として記載している。これは規制・モデレーション回避を助けうる。収録件数と分類数にもREADME内の不一致がある。 README内で収録規模が一致しない（本文は4,569+変異形・114分類、バッジは5,082,569+変異形・149分類）。記載された語句の意味や存活状態、平台ルールへの適合性は独立確認されていない。"
stars: 777
forks: 51
open_issues: 1
size_kb: 217
language: "unknown"
created: "2026-10-17"
updated: "2026-10-19"
archived: false
license: "MIT"
commits_30d: 8
commits_90d: 8
commit_cadence: "weekly"
type: "repo"
added: "2026-11-13"
first_seen: "2026-11-13"
sources: ["https://x.com/bkdgiffug/status/2118668719169626547"]
fetched_at: "2026-11-13T13:09:39.845807+00:00"
---

# Awesome Chinese Secondhand Slang（中国二手暗语全书与避坑合规指南）

## 出来ること

- READMEによると、二手取引の用語・変異形・分類・存活状態・解説をJSON形式で提供する。買い手向けの取引語句の説明と注意点も掲載している。データの取得例として、READMEはdata/slang-dictionary.jsonのraw URLをcurlで取得する手順を示している。

## 目的・背景

- READMEは、買い手が商品説明の含意やリスクを理解すること、合法的な売り手が平台の風控に対応することを目的として掲げている。READMEには検出回避を意図した代替語の利用例も含まれる。

## 依存関係

- READMEに記載されたデータ取得例はcurlを使用する。リポジトリ内JSONデータの利用に必要な追加依存関係はREADMEでは確認できない。

## 実行条件

- READMEに記載された取得先はGitHub上のdata/slang-dictionary.json。アクセス権、必要環境、APIの稼働条件についてREADMEに記載はない。

## 最短手順

- README記載の例：`curl -O https://raw.githubusercontent.com/Domainsun/awesome-chinese-secondhand-slang/main/data/slang-dictionary.json`。

## 変更履歴

- 2026-11-13: 初回登録
