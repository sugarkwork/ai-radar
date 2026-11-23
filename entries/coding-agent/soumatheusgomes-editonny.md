---
name: "editonny"
genre: "coding-agent"
url: "https://github.com/soumatheusgomes/editonny"
repo: "soumatheusgomes/editonny"
license: "MIT"
stars: 832
language: "Python"
created: "2026-10-19"
updated: "2026-10-21"
forks: 100
open_issues: 12
commits_30d: 22
commit_cadence: "daily"
commits_90d: 27
size_kb: 486028
archived: false
flags: []
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
risk_notes: ""
sources: ["https://x.com/AIExplorerTim/status/2119263644177588604"]
fetched_at: "2026-11-18T08:17:37.453892+00:00"
---

# editonny

## 出来ること

- Claude CodeとCodex向けの動画編集スキル。自然言語で指示し、無音やミスのカット、字幕追加、音声調整、画角変更、発話内容に合わせたモーションシーン作成を依頼できる。READMEによると、文字起こしとレンダリングはローカルで行う。

## 目的・背景

- 動画素材を指定して編集内容を伝え、エージェント経由で編集プロジェクトを作成・確認・書き出しする。READMEは、元映像を保ち、設定を提案して利用者の確認後に作業を進める手順を説明している。

## 依存関係

- README記載の要件は、Claude CodeまたはCodex、ランチャー用Python 3.9以上、uv、FFmpegとffprobe、Node.jsとnpx（22.13以上または24以上）。字幕確認用OCRとしてmacOSではApple Vision、またはTesseractが必要。エンジンはuv経由でPython >=3.10,<3.14を使用する。

## 実行条件

- READMEによると、文字起こしとレンダリングはローカルで実行し、これらにLLM APIキーは不要。外部生成機能は任意で、費用発生やメディア送信の前に利用者の許可が必要とされている。

## 最短手順

- READMEの案内に従ってリポジトリを取得し、`python3 install.py --target both`を実行する。続けてインストール先の`editonny.py doctor`と`editonny.py media status`を実行し、完全なセットアップには`skills/editonny/SKILL.md`の手順を使う。導入後にエージェントを再起動し、Claude Codeでは`/editonny`、Codexでは`$editonny`を呼び出す。

## 変更履歴

- 2026-11-23: 初回登録
