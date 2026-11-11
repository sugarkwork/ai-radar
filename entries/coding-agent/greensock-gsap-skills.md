---
repo: "greensock/gsap-skills"
name: "GSAP AI Skills"
genre: "coding-agent"
url: "https://github.com/greensock/gsap-skills"
license: "MIT"
stars: 18218
language: "unknown"
created: "2026-03-04"
updated: "2026-07-29"
forks: 1148
open_issues: 15
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 59
archived: false
flags: ["unverified"]
risk_notes: "スキル導入前後の生成品質、エージェントごとの自動読み込み、生成コードのブラウザ動作は未検証。GitHubの公開リリース一覧に掲載はなく、最新リリースのタグと日時は記載していない。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/thegreatest_sv/status/2115876572464812071"]
fetched_at: "2026-11-10T12:45:27Z"
---

# GSAP AI Skills｜AIエージェント向けの公式アニメーション実装ガイド

## 出来ること

- AIコーディングエージェントが、GSAPのタイムラインで複数の動きを順序づける方法、ScrollTriggerでスクロールに連動させる方法、SplitTextなどでテキストを演出する方法を参照できる。

## 目的・背景

- Agent Skills形式の実装ガイド。用途別のSKILL.mdにAPIの使い方や実装パターンを整理している。公式の参照例にはVanilla JS、React、Vue、Nuxtでの実装がある。参照例は実装方法の根拠であり、スキルによる生成品質の改善幅は測定していない。

## 依存関係

- CLIで導入する場合はnpm/npxと対応エージェントを使う。生成したアプリ側では公開npmパッケージのgsapを使い、Reactの公式例は@gsap/reactも使う。

## 実行条件

- エージェントがスキルを読み込める環境を用意し、生成したWebアニメーションはブラウザで確認する。ScrollTriggerなどは使用前に読み込んで登録する。スキル集はMIT。公式ガイドではGSAP本体と全プラグインを公開npmから入手でき、商用利用も無料と案内している。

## 最短手順

- 対象プロジェクトで `npx skills add https://github.com/greensock/gsap-skills` を使い、対応エージェントに追加する。
- エージェントに『gsap-scrolltrigger スキルを参照し、カードが表示領域に入ったらフェードインする処理を実装して。動きを減らす設定にも対応して』と依頼する。
- 対象アプリにgsapを導入し、生成されたコードをブラウザで開いて、スクロール時と動きを減らす設定の両方で挙動を確認する。

## 変更履歴

- 2026-11-11: 初回登録
