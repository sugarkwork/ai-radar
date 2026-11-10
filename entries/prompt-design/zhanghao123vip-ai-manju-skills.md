---
repo: "zhanghao123vip/ai-manju-skills"
name: "AI 漫剧 Skills"
genre: "prompt-design"
url: "https://github.com/zhanghao123vip/ai-manju-skills"
flags: ["unverified"]
risk_notes: "最新リリースは未確認。動作検証はREADMEの作者報告に基づく。残りの題材の個別動作、各対応環境での再現性、生成物の品質は今回独立に検証していない。"
stars: 695
forks: 124
open_issues: 0
size_kb: 101
language: "unknown"
created: "2026-10-31"
updated: "2026-11-01"
archived: false
license: "MIT"
commits_30d: 2
commits_90d: 2
commit_cadence: "monthly"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/ganfanren_ai/status/2117526594839601153"]
fetched_at: "2026-11-10T09:23:57Z"
---

# AI 漫剧 Skills｜縦型ショートドラマの制作準備テンプレート

## 出来ること

- 物語のアイデアをもとに、企画書、人物・小道具・背景などの画像生成プロンプト、各話の台本、絵コンテ・動画生成プロンプト、表紙や投稿文の案を段階的に出力する。
- 既定は全30話、各話約4分、縦型9:16。アイデアを送る際に変更できる。

## 目的・背景

- 玄幻修仙や宮廷劇など21題材を、それぞれ独立したSKILL.mdに収録する。長い制作資料は分割して出力し、同じ会話で次の工程に進める。
- 作者は現行版がWorkBuddyで動作したと報告している。以前の玄幻修仙版は実使用、宮斗など7題材はインストール確認または第1段階の試行までで、残りの題材は個別の実測が済んでいない。

## 依存関係

- テンプレート自体に追加パッケージは不要。Claude Code、Skillの取り込みに対応したWorkBuddy、またはDeepSeekなどのチャット環境で使う。画像・動画の生成には、出力したプロンプトを対応する生成ツールに渡す。

## 実行条件

- 設定の混線を防ぐため、1作品につき1会話で1テンプレートを使う。動画ツールを替える場合は、参照画像の指定 {{Mixed N}} を利用先の構文に置き換える。
- テンプレートのライセンスはMIT。READMEは生成物の権利と公開時の規約確認を利用者の責任としている。外部サービスの利用料金は利用先による。

## 最短手順

- チャットで使う場合は、題材のSKILL.md全文を新規会話に貼り付ける。AIが「模板已就绪」と返したら物語のアイデアを1文で送る。
- Claude Codeでは、題材フォルダを ~/.claude/skills/ に配置し、Claude Codeに物語のアイデアを送る。続きは「继续」、第3話の演出資料は「第3集手册」で依頼する。

## 変更履歴

- 2026-11-10: 初回登録
