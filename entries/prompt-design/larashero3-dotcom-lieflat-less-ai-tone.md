---
name: "Lieflat Less AI Tone"
genre: "prompt-design"
url: "https://github.com/larashero3-dotcom/lieflat-less-ai-tone"
repo: "larashero3-dotcom/lieflat-less-ai-tone"
license: "unknown"
language: "Python"
flags: ["unverified"]
risk_notes: "研究の語料はリポジトリに含まれず、報告された数値は第三者が直接検証できない。意味層の判定は単一モデルで、READMEは抽出確認で15–30%の誤判定があったと述べている。商用利用には別途ライセンス購入が必要と記載されている。 GitHub APIでライセンスを確認できていません。"
stars: 7586
forks: 535
open_issues: 5
size_kb: 4682
created: "2026-08-20"
updated: "2026-11-11"
archived: false
commits_30d: 14
commits_90d: 27
commit_cadence: "weekly"
type: "repo"
added: "2026-11-13"
first_seen: "2026-11-13"
sources: ["https://x.com/fhwofjow51260/status/2118683436122837064"]
fetched_at: "2026-11-13T16:09:41.501205+00:00"
---

# Lieflat Less AI Tone

## 出来ること

- 文章の特徴をスクリプトで検出し、意味判定の候補をモデルで確認して、指標・研究参照・原文例・改稿案を含む検出レポートを作る。ユーザーの返答後に改稿し、再検査して前後を比較する。比喩の適切さなど機械判定が難しい項目は人手確認として扱う。

## 目的・背景

- READMEによると、単純な禁止語リストや一括改稿では文章の特徴を捉えきれず、自然な表現まで変更するおそれがある。作者は対照研究と配対再測定をもとに検出項目を選び、最小改稿と情報保持を重視する方法を説明している。研究結果は作者の報告であり、語料はリポジトリに含まれないため第三者が数値を直接検証できない。

## 依存関係

- READMEに記載された検出・報告用スクリプトはPythonで実行する。意味層の候補判定には会話内のモデルを使う。READMEには候補判定でJevを利用した研究記述があるが、実行時の必須サービスや依存パッケージ一覧はこの資料から確認できない。

## 実行条件

- README記載の実行例は `python3 scripts/detect.py` と `python3 scripts/report.py` を使用する。Agent Skills対応AIにskillをインストールして利用する方法も記載されている。配布・利用条件はREADME記載のCC BY-NC 4.0で、商用利用は別途ライセンス購入が必要。

## 最短手順

- 1. Agent Skills対応AIにリポジトリ内の `lieflat-less-ai-tone` skillをインストールする。README記載のコマンド例は `npx skills add larashero3-dotcom/lieflat-less-ai-tone`。2. 成稿を渡し、検出レポートを確認する。3. 提案への返答後に改稿し、再検査・前後比較を行う。ローカル利用ではREADME記載の `python3 scripts/detect.py <ファイル>` で検出を開始する。

## 変更履歴

- 2026-11-13: 初回登録
