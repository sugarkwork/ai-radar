---
repo: "fadewalk/serenity-stock-choke"
name: "serenity-stock-choke"
genre: finance-quant
url: "https://github.com/fadewalk/serenity-stock-choke"
license: "MIT"
stars: 508
language: "Python"
created: "2026-05-29"
updated: 2026-10-06
added: "2026-11-05"
first_seen: "2026-11-04"
source_post: "https://x.com/bkdgiffug/status/2118117336393949625"
sources: []
flags: []
risk_notes: ""
forks: 56
open_issues: 0
size_kb: 61
archived: false
commits_30d: 4
commits_90d: 7
commit_cadence: weekly
fetched_at: "2026-11-05T00:04:29Z"
last_release: v3.2.1
last_release_at: 2026-10-06
---

# serenity-stock-choke

## 出来ること

- 「ボトルネック（卡脖子）選股」をエージェントのスキルとして実装したもの。Claude Code / Codex などコマンドを実行できるエージェントに入れて使う。Python 実装で外部依存はほぼ無い。
- 6ステップの分析手順を踏む。①セクターの周期を判定（需要爆発 / 技術転換 / 供給制約）→ ②サプライチェーンを遡ってボトルネックの層を特定 → ③その節点にいる銘柄を四象限のシグナルカードで抽出 → ④「本物のボトルネック」か便乗かを選別 → ⑤強気／弱気シグナルの対照 → ⑥操作提案とリスク付きの構造化レポート出力。
- 対象は A株・香港株・米国株。電力、光モジュール/CPO、半導体製造装置、軍需、新エネルギー車、医療機器、創薬、OLED などの板塊を例に挙げている。

## 目的・背景

発想は「ホルムズ海峡」型。巨大な需要が来たとき、上流のどこか1層だけが供給不足になり、そこを押さえた企業が価格決定権を持つ——という見立てを、エージェントに定型手順として踏ませる。README は元ネタの米国株事例（InP 基板、CPO レーザーなど）を表で挙げつつ、**それが「後知恵の生存者サンプル」であってフレームの期待リターンではない**と自分で注記している。

## 依存関係

- Python。エージェント側は Claude Code / Codex などのスキル機構（リポジトリをクローンしてスキルとして読み込ませる）。
- README は「リポジトリの URL をエージェントに貼ると、クローン・導入・検証まで自分でやる」導入手順を用意している。中身を確認せず貼るのは避けたい場合は手動でクローンする。

## 実行条件

- ライセンスは MIT。
- **投資助言ではない**。README も「補助的な研究ツールで、大盘を予測せず、売買推奨もしない。会社の生産能力や顧客情報は自分で検証すること」と書いている。
- 出力の質はエージェントの調査能力に依存する。銘柄名やシグナルは一次情報（決算・開示）で裏取りが要る。
- 直近の更新は 2026-10-06 で、活発ではない。

## 最短手順

```bash
git clone https://github.com/fadewalk/serenity-stock-choke.git
# あとはエージェントのスキルディレクトリに置くか、SKILL.md の手順に従って読み込ませる
```

## 変更履歴

- 2026-11-05: 初回登録（★508 / MIT / Python / 最終push 2026-10-06）
