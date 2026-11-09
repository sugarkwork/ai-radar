---
type: "repo"
repo: "sleeplesshan/dual-brain"
name: "Dual-Brain — 設計とコードの二視点レビュー用スキル"
genre: "coding-agent"
url: "https://github.com/sleeplesshan/dual-brain"
author: "sleeplesshan"
license: "MIT"
language: "Python"
stars: 101
forks: 6
open_issues: 0
created: "2026-05-24"
updated: "2026-11-06"
commits_30d: 6
commits_90d: 6
commit_cadence: "weekly"
size_kb: 130
archived: false
risk_notes: "MIT。投稿のMS関連社内ハッカソンでAI審査員から満点という説明は作者の自己申告で、公式採点記録・Microsoftの推薦や認証を確認したものではない。READMEは旧5事例ベンチの比較条件・トークン二重計上に問題があり旧総数を撤回と明記。普遍的な性能改善や低遅延は保証しない。 当方でインストール・動作・性能の実行検証はしていない。"
sources: ["https://x.com/sleepless_han/status/2119291833322729923", "https://github.com/sleeplesshan/dual-brain", "https://github.com/sleeplesshan/dual-brain/blob/main/README.md", "https://github.com/sleeplesshan/dual-brain/blob/main/LICENSE", "https://x.com/i/status/2119310441411469540"]
added: "2026-11-09"
first_seen: "2026-11-08"
source_post: "https://x.com/sleepless_han/status/2119291833322729923"
fetched_at: "2026-11-09T01:07:34+00:00"
flags: ["unverified"]
---

# Dual-Brain — 設計とコードの二視点レビュー用スキル

## 出来ること

Right Brainが目的・設計・全体への影響を、Left Brainが契約・境界条件・実コードを検査し、主エージェントが統合・修正・検証する。単純な編集はローカルの短いレビューに留める設計。

## 目的・背景

曖昧な設計・リファクタ・外部連携・繰返すプロジェクト判断向けのポータブルなスキル。発見ノルマや変更ノルマはなく、問題が無い結論も正常とする。

## 依存関係

スキル自体にランタイム依存なし。SKILL.mdとreferencesを一緒に保持し、Codex/Claude Code等の対応ホストで使う。エージェントの契約・利用料と実行機能は別。

## 実行条件

独立した子エージェントが使えない環境では二段階のローカル確認へ切り替え、独立レビューを実施したふりをしない。チャットだけなら提案・分析に限定し、ファイル書込み・テスト・記憶保存の実施を主張しない。

## 最短手順

Codexでは公式READMEの ~/.agents/skills/dual-brain、Claude Codeでは ~/.claude/skills/dual-brain などのスキル配置に導入し、$dual-brain / /dual-brain または名前で依頼する。既存導入との重複を避ける。Museのネイティブ永続導入はREADME自身が未検証と区別する。

## 注意点

MIT。投稿のMS関連社内ハッカソンでAI審査員から満点という説明は作者の自己申告で、公式採点記録・Microsoftの推薦や認証を確認したものではない。READMEは旧5事例ベンチの比較条件・トークン二重計上に問題があり旧総数を撤回と明記。普遍的な性能改善や低遅延は保証しない。

## 変更履歴

- 2026-11-09: 初回収録。公式資料を確認し、未実行の範囲を明記。

- 2026-11-09: 別の紹介投稿を追加。対象と公式情報を再確認。動作は未検証。
