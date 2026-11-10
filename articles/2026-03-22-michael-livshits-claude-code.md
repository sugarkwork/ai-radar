---
name: "Claude Codeの補足情報と実行時の権限制御"
genre: "article"
url: "https://michaellivs.com/blog/system-reminders-steering-agents/"
author: "Michael Livshits"
published: "2026-03-22"
flags: ["unverified"]
risk_notes: "リマインダーの効果は実測していない。実行権限は実行基盤で判定する。"
type: "article"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/bernvadell/status/2113700655080546601"]
fetched_at: "2026-11-10T04:15:56Z"
---

# Claude Codeの補足情報と実行時の権限制御

## テーマ

- エージェントが判断する時点で補足情報を渡す設計。

## 著者の主張

- 長時間の作業では必要な時点で注意点や状態を伝え、補足情報と操作の許可を別に扱う。

## 裏取り・注意点

- Claude Code公式Hooksで補足情報をモデルに渡す仕組みを確認。外部データと実行基盤の指示は出所を区別する。

## 出典

- https://michaellivs.com/blog/system-reminders-steering-agents/
- https://code.claude.com/docs/en/hooks

## 変更履歴

- 2026-11-10: 初回登録
