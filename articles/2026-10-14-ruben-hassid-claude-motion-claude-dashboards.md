---
name: "Claude Motion と Claude Dashboards の使い方"
genre: "article"
url: "https://ruben.substack.com/p/claude-motion-and-dashboards"
published: "2026-10-14"
author: "Ruben Hassid"
flags: ["unverified"]
risk_notes: "記事中の「Pro・MaxでMotionとDashboardsが使える」という記述は、AnthropicのMotion公式ヘルプではMotionはTeam・Enterprise向けとされており一致しない。Claude Codeからの公開手順や著者の作成時間・分析値は独立検証されていない。"
type: "article"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/okapi_fukugyo/status/2119299912882123032"]
fetched_at: "2026-11-18T21:14:44.202705+00:00"
---

# Claude Motion と Claude Dashboards の使い方

## テーマ

- Claude Motionで短いアニメーションを作る方法と、Claude Dashboardsでデータを可視化する方法を、利用条件・プロンプト例・編集・共有まで紹介する記事。

## 著者の主張

- 著者は、Motionでは対象視聴者・掲載場所・長さを指定し、Dashboardsではチャートの種類だけでなく答えたい問いや意思決定を指定するとよいと説明。CSVの利用、チャートのSQLクエリ確認、結果の編集、Motionへの変換などの手順と例を掲載している。著者がClaude Code経由で自身のニュースレター123件を分析・動画化したという記述や所要時間・数値は著者の報告であり、独立実測ではない。

## 裏取り・注意点

- Anthropic公式ヘルプは、Motionがプロンプトからテキスト・チャート・図形・画像を動かすコードベースの短いアニメーションであり、動画生成モデルによる実写映像や人物の生成ではないと説明している。Motionはベータ版でTeam・Enterpriseプランが対象。公式Dashboardsヘルプは、データソースに対してチャートごとのSQLクエリを作成し、クエリと最終更新時刻を確認できると説明し、Pro・Max・Ultra・Team・Enterpriseが対象としている。記事のアクセス欄にあるMotionのPro・Max対応は公式Motionヘルプと食い違うため、プラン情報は公式資料で要確認。Dashboardsは探索的な問い向けで、結果のクエリを確認するよう公式が案内している。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 出典

- 記事本文・公開日: https://ruben.substack.com/p/claude-motion-and-dashboards
Anthropic公式 Motion ヘルプ: https://support.claude.com/en/articles/17454997-get-started-with-claude-motion
Anthropic公式 Dashboards ヘルプ: https://support.claude.com/en/articles/17454700-get-started-with-claude-dashboards

## 変更履歴

- 2026-11-23: 初回登録
