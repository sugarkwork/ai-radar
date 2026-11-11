---
name: "Crawl4AI"
genre: "agent-framework"
url: "https://github.com/unclecode/crawl4ai"
repo: "unclecode/crawl4ai"
license: "Apache-2.0"
stars: 87228
language: "Python"
created: "2024-05-09"
updated: "2026-11-10"
forks: 9090
open_issues: 331
commits_30d: 30
commit_cadence: "daily"
commits_90d: 100
size_kb: 151881
archived: false
flags: ["unverified"]
risk_notes: "Cloud APIは従量課金で、READMEに記載の価格はプランや利用量により異なる。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/thegreatest_sv/status/2118325722850697573"]
fetched_at: "2026-11-11T19:07:11.004659+00:00"
---

# Crawl4AI

## 出来ること

- WebページをLLM向けのMarkdownに変換し、CSS・XPath・正規表現・LLMを使った構造化データ抽出ができる。ブラウザー制御、ページ巡回、URL探索、チャンク分割もREADMEに記載されている。

## 目的・背景

- Webページからの情報抽出やWeb-to-Markdownを目的とする。READMEでは、ライブラリがCrawl4AI Cloudを支えるクローラーとして説明されている。

## 依存関係

- Pythonライブラリはブラウザーのインストールが必要で、初回に `crawl4ai-setup` を実行する手順が記載されている。Dockerでの実行方法も案内されている。

## 実行条件

- ローカル利用はPython環境とブラウザーが必要。Cloud APIを使う場合はAPIキーが必要で、READMEには月1,000無料クレジットと有料プランの案内がある。

## 最短手順

- ローカルでは `pip install -U crawl4ai`、続けて `crawl4ai-setup` を実行し、`AsyncWebCrawler` でURLを巡回する例がある。CloudではAPIキーを `CRAWL4AI_KEY` に設定し、`https://api.crawl4ai.com/scrape` にリクエストしてMarkdownを取得する。

## 変更履歴

- 2026-11-11: 初回登録
