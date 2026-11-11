---
name: "Manufacturing WeChat Mini Program Starter"
genre: "other"
url: "https://github.com/changhaoting1998-star/manufacturing-wechat-miniapp-starter"
repo: "changhaoting1998-star/manufacturing-wechat-miniapp-starter"
stars: 703
forks: 39
open_issues: 0
size_kb: 35
language: "JavaScript"
created: "2026-10-27"
updated: "2026-10-27"
archived: false
license: "MIT"
commits_30d: 3
commits_90d: 3
commit_cadence: "monthly"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/Ryrenz/status/2118344838739288282"]
fetched_at: "2026-11-11T21:06:16.461930+00:00"
---

# Manufacturing WeChat Mini Program Starter

## 出来ること

- 製造現場での生産完了、材料使用、品質、異常、作業時間、フォームの記録を収集し、MESへ検証済みイベントを送るための構成を示す。従業員アクセス申請と承認、勤怠、給与通知の確認、動的フォーム、冪等性を備えたMES出力の例を含む。READMEでは、効率比較は管理者の判断支援とし、配置や雇用の変更には人による確認を求めている。

## 目的・背景

- 紙やチャット、シフト後の報告による現場記録の遅れを減らし、イベント発生時点に近い構造化データを収集することを目的とする。READMEでは、MESを作業指示・工程・生産・品質記録の正本とし、Mini Programを従業員向けの収集・フィードバック層として位置づけている。

## 依存関係

- ゼロ依存のテストおよびデモ実行にはNode.js 20以上が必要。実運用には、運用者が用意するMESアダプター、永続リポジトリ、CloudBase IDプロバイダーなどの接続が必要とREADMEに記載されている。

## 実行条件

- README記載のローカル実行方法は `npm test` と `npm run demo`。Mini Programのセットアップでは、サンプル設定の複製、ローカルでのAppID設定、ゲートウェイの永続ストレージおよびIDプロバイダーへの接続、権限設定、WeChat Developer Toolsでのコンパイルとプレビューが案内されている。ゲートウェイは運用者による認証・ストレージ接続なしではデプロイできない設計とされる。

## 最短手順

- READMEのQuick startに従い、Node.js 20以上の環境で `npm test`、続けて `npm run demo` を実行する。Mini Programとして試す場合は、サンプル設定をローカルに複製してAppID等を設定し、CloudBaseのID・ストレージ接続を構成してからWeChat Developer Toolsでプレビューする。

## 変更履歴

- 2026-11-11: 初回登録
