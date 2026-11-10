---
name: "Claude Code v2.1.283 の設定監査 /doctor prompt-audit"
genre: "coding-agent"
url: "https://github.com/anthropics/claude-code/releases/tag/v2.1.283"
author: "Anthropic"
published: "2026-09-25"
flags: ["unverified"]
risk_notes: "監査の検出精度、提案による改善効果、適用依頼前にファイルが変更されないという公式説明の実環境での挙動、監査固有の料金は未確認。発見投稿が案内するX記事のテンプレートとディレクトリ構成も未確認。"
type: "article"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/Bober_smart/status/2116170627631517814"]
fetched_at: "2026-11-10T05:59:29Z"
---

# Claude Code の指示ファイルを /doctor prompt-audit で点検する

## テーマ

- 古いモデル向けの指示、存在しないファイルやコマンドへの参照、設定ファイル間の矛盾を見つけ、修正案を確認する。

## 著者の主張

- Anthropicはv2.1.283で `/doctor prompt-audit` と別名の `/checkup prompt-audit` を追加した。公式ガイドによると、Claude Codeのセッション内で実行でき、単一ディレクトリに絞る例は `/doctor prompt-audit .claude/skills/deploy`。
- 公式ガイドの既定範囲は `CLAUDE.md`、`CLAUDE.local.md`、`AGENTS.md` と、`.claude/` および `~/.claude/` 配下のルール、スキル、コマンド、サブエージェント、出力スタイル。同梱の `/claude-api` スキルが有効である必要がある。

## 裏取り・注意点

- 公式ガイドは `CLAUDE.md` 1ファイルあたり200行未満を目安とし、矛盾する指示のどちらが選ばれるかは予測しにくいとしている。
- 公式ガイドは、監査結果に修正案が含まれ、適用を依頼するまでファイルは変わらないと説明している。今回の確認は公開資料に基づき、実行時の挙動や検出精度は未検証。

## 出典

- [Anthropicのv2.1.283リリースノート](https://github.com/anthropics/claude-code/releases/tag/v2.1.283)
- [Claude Code公式ガイドの指示ファイル監査](https://code.claude.com/docs/en/memory#audit-your-instruction-files)

## 変更履歴

- 2026-11-10: 初回登録
