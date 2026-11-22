---
name: "公文 Skills · dyz-gongwen-skills"
genre: "coding-agent"
url: "https://github.com/duyunzhoudyz/dyz-gongwen-skills"
flags: ["unverified"]
risk_notes: "GitHub APIのlicense値はunknownですが、READMEのバッジはPolyForm NC 1.0を示しています。ライセンス本文の条件はこの資料では確認できません。 GitHub APIでライセンスを確認できていません。"
repo: "duyunzhoudyz/dyz-gongwen-skills"
stars: 883
forks: 38
open_issues: 0
size_kb: 18429
language: "Python"
created: "2026-10-15"
updated: "2026-11-13"
archived: false
license: "unknown"
commits_30d: 91
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-16"
first_seen: "2026-11-16"
sources: ["https://x.com/Ryrenz/status/2119008208849133570"]
fetched_at: "2026-11-16T21:44:04Z"
last_release: "v1.1.0"
last_release_at: "2026-11-04"
---

# 公文 Skills · dyz-gongwen-skills

## 出来ること

- 公文書の起草、改稿、校正、AI文体の修正、データ整理、GB/T 9704-2012に沿ったWord整形など、17のコアSkillsと5つの業種別パックを提供します。

## 目的・背景

- 機関・公共事業体・国有企業の文書作成を支援し、入力資料にない事実を補わないことや、機密情報をオンラインAIに入力しないことをREADMEで案内しています。README掲載の比較・評価結果は作者側の報告です。

## 依存関係

- 排版とExcelグラフにはPython 3.9以上、python-docx、openpyxlが必要とREADMEに記載されています。これらがない場合、排版SkillはWPS/Wordでの手動設定手順を示すとされています。

## 実行条件

- 一括インストールはWindows、macOS、Linux向けに案内されています。ウェブLLMや内网モデルではdist/prompts/内の提示詞をコピーして使用でき、内网利用向けにオフラインパッケージを生成する手順もあります。

## 最短手順

- Agentツールでは、リポジトリを取得してWindowsでpowershell -ExecutionPolicy Bypass -File .\install.ps1、macOS/Linuxでbash install.shを実行します。対象ツールを指定する場合はpython tools/install.py --target qwenのように実行します。ウェブLLMではdist/prompts/のgongwen.mdを会話の冒頭に貼り付けます。

## 変更履歴

- 2026-11-16: 初回登録
