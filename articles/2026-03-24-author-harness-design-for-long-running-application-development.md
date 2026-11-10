---
name: "Harness design for long-running application development"
genre: "article"
url: "https://www.anthropic.com/research/harness-design-long-running-apps"
published: "2026-03-24"
flags: ["unverified"]
risk_notes: "生成アプリの独立再現、構成要素ごとの寄与、別タスクへの一般化、実験用ハーネスのコード配布・再利用条件は未確認。"
type: "article"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/N01ennn/status/2118005145954931181"]
fetched_at: "2026-11-10T11:24:02Z"
---

# 長時間のアプリ開発を支えるエージェント設計とブラウザQA

## テーマ

- Prithvi Rajasekaranが、計画・実装・評価の分担を長時間のアプリ開発に適用した事例。初版では実装前に検証可能な受け入れ条件を合意し、評価役がPlaywright MCPで稼働中のアプリを操作する。

## 著者の主張

- 同じClaude Opus 4.5と同じ依頼を使ったゲーム制作ツールの比較では、単独構成は20分・9ドルで試遊時に入力が反応せず、フル構成は6時間・200ドルで試遊時にキャラクターを動かせたと著者は報告する。フル構成でも当たり判定に粗さが残った。
- Opus 4.6を用いた改訂版ではスプリント分割を外し、ブラウザ上の音楽制作アプリを3時間50分、トークン費用124.70ドルで生成した。QAは途中で録音ボタンが実際にはマイク入力を取得しないことなどを検出した。

## 裏取り・注意点

- 時間・費用・動作は記事内の著者報告。単独構成とフル構成では仕様展開や実行時間も異なるため、評価役単体の効果や他案件での費用対効果はこの比較から判断できない。
- 改訂版のモデルは原文でOpus 4.6。費用は各実験の記録であり、再実行時の見積もりにはモデル利用量や実行条件が必要になる。

## 出典

- [Anthropic Engineering — Harness design for long-running application development](https://www.anthropic.com/research/harness-design-long-running-apps)

## 変更履歴

- 2026-11-10: 初回登録
