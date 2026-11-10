---
repo: "Donchitos/Claude-Code-Game-Studios"
name: "Claude Code Game Studios"
genre: "coding-agent"
url: "https://github.com/Donchitos/Claude-Code-Game-Studios"
flags: ["unverified"]
risk_notes: "ブラウザ試作とフックは独立実行していない。作者が報告した比較は3企画に限られ、完成した試作品の評価は同等だった。Godot・Unity・Unreal経路と設計文書による掘り下げは、作者の同等の比較評価が未実施。最新リリースのタグと日時は未確認。Claude Codeの利用料金は未確認。"
stars: 37789
forks: 4949
open_issues: 96
size_kb: 5612
language: "Shell"
created: "2026-02-12"
updated: "2026-11-09"
archived: false
license: "MIT"
commits_30d: 2
commits_90d: 6
commit_cadence: "monthly"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/naka_1717/status/2117501380969508891"]
fetched_at: "2026-11-10T09:14:35Z"
---

# Claude Code Game Studiosでゲームの企画からブラウザ試作まで進める

## 出来ること

- Claude Codeにゲーム案を渡すと、ジャンルに応じた質問から短い企画書を作り、ブラウザで遊べる試作品の作成へ進む。

## 目的・背景

- 役割分担と委譲ルールを持つ専門サブエージェントと、開発工程ごとのスキルをまとめたテンプレート。作者の盲検比較では3企画すべてで質問から作った企画書が選ばれたが、試作品自体の評価は同等だった。

## 依存関係

- GitとClaude Codeを用意する。READMEによると、Python 3はproject.yamlの読み取り、Bashはフックの実行、Chrome・Edge・Chromiumのいずれかは試作品のブラウザ確認に使う。

## 実行条件

- CLAUDE.mdとproject.yamlがあるプロジェクトルートでClaude Codeを起動する。エンジン未指定時の試作先はブラウザ。テンプレートはMITライセンスで、Claude Codeの利用料金は未確認。

## 最短手順

- GitHubでテンプレートからプロジェクトを作るか、リポジトリをクローンする。
- プロジェクトルートで claude を起動し、Claude Codeの入力欄から /prototype に続けてゲーム案を入力する。進め方を相談する場合は /start を入力する。

## 変更履歴

- 2026-11-10: 初回登録
