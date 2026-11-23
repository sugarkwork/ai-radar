---
name: "dsh-plugin-bundle"
genre: "agent-framework"
url: "https://github.com/lili-luo/dsh-plugin-bundle"
repo: "lili-luo/dsh-plugin-bundle"
license: "MIT"
stars: 341
language: "JavaScript"
created: "2026-11-06"
updated: "2026-11-13"
forks: 35
open_issues: 1
commits_30d: 16
commit_cadence: "weekly"
commits_90d: 16
size_kb: 713
archived: false
flags: ["unverified"]
risk_notes: "READMEは封号が発生しているとし、特に活動・贈与系プランで多いと述べている。付費プランも安全とは確認されておらず、利用にはアカウント停止リスクがある。コンテキスト解锁スクリプトはローカルのagyバイナリを書き換える。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/mingzi206/status/2119313690659057933"]
fetched_at: "2026-11-19T01:16:32.300057+00:00"
---

# dsh-plugin-bundle

## 出来ること

- DeepSeek Harness（DSH）にAntigravityを接続するプラグインを提供する。READMEによると、接続には本機の公式`agy acp`を使い、ログイン状態は公式プロセス内に保持される。プラグインは鍵を保存せず、リクエストを別ゲートウェイへ転送しないと説明されている。また、任意のローカルスクリプトでagyクライアントの既定256Kコンテキストを約1Mに変更する機能がある。

## 目的・背景

- DSHでAntigravityを利用するためのプラグイン組み合わせ。READMEは、Googleによるプロンプト検査への緩和策としてプラグイン側でプロンプト処理を行うと説明している。封号が発生しているとも記載されており、利用条件ごとの発生状況はREADMEの説明で、独立した確認はない。

## 依存関係

- DeepSeek Harness、公式Antigravity CLIの`agy`およびそのACP機能を利用する。任意のコンテキスト解锁スクリプトはプラグインと一緒にはインストールされず、ローカルの`agy`バイナリを書き換える。

## 実行条件

- README記載のプラグイン導入コマンドは`dsh plugin --profile web add "git+https://github.com/lili-luo/dsh-plugin-bundle.git#main&path:/dsh-llm-antigravity-acp"`。動作に必要なOS、バージョン、プラン条件はREADME抜粋では確認できない。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- READMEのコマンドで`dsh-llm-antigravity-acp`をDSHのwebプロファイルへ追加する。コンテキスト解锁は任意の別スクリプトであり、agyバイナリを書き換えるとREADMEに記載されている。

## 変更履歴

- 2026-11-23: 初回登録
