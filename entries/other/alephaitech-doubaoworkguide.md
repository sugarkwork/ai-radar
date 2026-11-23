---
name: "豆包工作蓝皮书（DoubaoWork Guide）"
genre: "other"
url: "https://github.com/AlephAITech/DoubaoWorkGuide"
flags: ["unverified"]
risk_notes: "製品の機能・画面・価格・権限・利用範囲は変更される可能性があり、READMEも具体的な操作では製品の現行版と公式説明を参照するよう案内している。"
repo: "AlephAITech/DoubaoWorkGuide"
stars: 257
forks: 31
open_issues: 1
size_kb: 413268
language: "JavaScript"
created: "2026-08-31"
updated: "2026-11-15"
archived: false
license: "MIT"
commits_30d: 1
commits_90d: 30
commit_cadence: "monthly"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/Ryrenz/status/2119370604662968543"]
fetched_at: "2026-11-19T19:12:57.114647+00:00"
---

# 豆包工作蓝皮书（DoubaoWork Guide）

## 出来ること

- READMEによると、豆包工作の導入から最初のタスク完了までの手順に加え、接続器、Skill、API、定時タスク、複数Agentを扱う。個人の生産性、自媒体、知識管理、電商、金融研究の5分野に31件の実務タスク例を収録。オンライン版では全文検索、章ナビゲーション、画像・動画表示、読書進捗記録などを提供すると説明されている。

## 目的・背景

- 豆包工作を初めて使う人や、実務タスクを再利用できる方法として整理したい人向けの、コミュニティ作者による非公式の中国語実践ガイド。READMEでは49本のガイドと事例を収録していると説明されている。

## 依存関係

- READMEによると、サイトは純静的構成で、フロントエンド依存関係をインストールせずローカル閲覧できる。内容は構造化JSONとローカルメディアで管理する。索引を再生成する場合はNode.jsのnpmスクリプトを使う。

## 実行条件

- ローカル閲覧にはPython 3が必要。開発依存関係のインストールとブラウザー自動化によるテスト・監査にはnpm installが案内されている。公開先はsiteディレクトリで、READMEでは追加のビルド手順は不要と説明されている。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- リポジトリのREADMEが案内するオンライン版 doubaowork.homes を開き、「从第一篇开始」または「查看阅读指南」から読み始める。ローカルではリポジトリのルートで `python3 -m http.server 4173 --bind 127.0.0.1 --directory site` を実行し、ブラウザーからローカルサーバーを開く。ポート4173が使用中なら別の空きポートを指定する。

## 変更履歴

- 2026-11-23: 初回登録
