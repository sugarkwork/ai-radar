---
type: "prompt"
name: "Claude Code 向け UI 設計ルール19条"
genre: "prompt-design"
url: ""
author: "@Av1dlive"
source_post: "https://x.com/Av1dlive/status/2117357666913923190"
sources: []
added: "2026-11-03"
flags: []
risk_notes: ""
target: "Claude Code"
transcribed_from: "image"
prompt_sha1: "e1e267bd756d36384835e6ebfb6dd2b97702b890"
---

# Claude Code 向け UI 設計ルール19条

## 目的

生成 AI が作る UI が「同じ見た目・同じ質感」に寄る問題に対して、数値と制約で縛るためのプロンプト。色の役割、セマンティックトークン、タップ領域の実寸、既定値の選び方、応答時間のしきい値、画面ごとのレビュー観点を19条にまとめている。

## 前提

- 画像内の指示文を全文文字起こししたもの（`transcribed_from: image`）。原文の改行・番号・見出しを保持している。
- Claude Code（または CLAUDE.md を読むエージェント）。ルール6が CLAUDE.md への追記を前提にしている。
- 画像だけでは「どのファイルに置くか」は指定されていない。投稿者はリプライで「トークンファイルを先に用意してから最初の画面を作る（seed it first）」と答えており、順序が重要だと述べている。

## プロンプト本文

```text
claude code prompt: design like a $300/hr designer

Before you build or change any screen, follow these rules. If a rule conflicts with what I
ask, tell me before breaking it.

Colors
1. Primary sets the mood. Accent is only for buttons and highlights. Neutrals are background
grays. Background, text and border each do one job.

Design system
2. Keep raw colors, spacing and fonts in one file.
3. Use semantic tokens like text-muted, never raw values like gray-500.
4. For each component: when to use it, default variant, every state.
5. Build real screens first, then turn repeated parts into blocks.
6. Add new rules to CLAUDE.md as one line plus the reason.

Taps and layout
7. Touch targets: 44x44pt iOS, 48x48dp Android with 8dp gaps, 24x24px web (44px for primary
actions). Grow hit areas with padding.
8. On mobile, primary action at the bottom. Nothing tapped often in the top corners.
9. Use patterns people already know. Don't invent navigation.
10. Personalize content, never navigation.

Choices
11. Show the most-used options, advanced ones behind "More".
12. Long lists are fine if grouped, sorted or searchable.
13. Default to what's best for the user. No pre-checked upsells, no hidden fees, cancel as
easy as signup.
14. No time-based popups, fake urgency or discount traps.

Speed
15. Feedback under 100ms. Loading state after 1s. Progress percent and cancel after 10s. Aim
under 400ms on common actions.

Finish
16. Real icons from one set, such as Lucide, never emoji.

Review after every screen
17. Flag any raw value that isn't a token.
18. Every block has loading, empty and error states.
19. List anything you weren't sure about so I can test it with real users.
```

## 使い方

1. プロジェクトの `CLAUDE.md`（または同等のシステム指示）に貼る。
2. **先に**デザイントークンのファイル（色・余白・フォント）を作らせる。空のまま画面を作らせると、生の値がその場で発明される（投稿者のリプライによる指摘）。
3. 画面を作るたびにルール17〜19のレビューを回させる。

## 注意点

- 44pt / 48dp / 24px といった数値は各プラットフォームのガイドライン由来の値で、プロンプト内の記述以上の根拠は示されていない。適用前に自プロジェクトの基準と突き合わせる。
- 「Lucide」など特定のアイコンセットを名指ししているため、別セットを使う場合は置き換える。
- 投稿は英語。日本語 UI に適用する場合、文言トーンに関するルールは含まれていない点に注意。

## 変更履歴

- 2026-11-03: 初回登録（画像から全文文字起こし）
