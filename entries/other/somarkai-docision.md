---
name: "Docision"
genre: "other"
url: "https://github.com/SoMarkAI/docision"
repo: "SoMarkAI/docision"
flags: ["unverified"]
risk_notes: "README記載の速度・精度に関する比較結果や、複数質問時の速度向上は独立検証していません。利用可能な自然言語と日本語対応はREADMEから確認できません。"
stars: 11
forks: 0
open_issues: 0
size_kb: 1849
language: "Python"
created: "2026-10-14"
updated: "2026-10-14"
archived: false
license: "Apache-2.0"
commits_30d: 0
commits_90d: 8
commit_cadence: "monthly"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/ai_hakase_/status/2119370852126908922"]
fetched_at: "2026-11-19T19:15:12.423009+00:00"
---

# Docision

## 出来ること

- 文書画像と質問ごとの候補を入力し、各質問について選択した候補と候補ごとの確率を出力します。READMEは文書分類、項目間の関係確認、完全性確認、ルールに基づく判定・振り分けを用途として挙げています。

## 目的・背景

- 同じ文書に対する複数の判断を扱い、質問ごとに異なる候補を指定できる文書理解モデルとして紹介されています。速度・精度の比較や複数質問による速度向上はREADME上の開発者の説明で、独立検証は確認できていません。

## 依存関係

- READMEの手順ではPython仮想環境を作成し、リポジトリを編集可能モードでインストールします。モデルはHugging Faceから別途ダウンロードします。MCPを使う場合は追加依存関係として`.[mcp]`をインストールします。

## 実行条件

- READMEの推論例は`demo_docision.py`をPythonで実行し、モデルディレクトリ、入力JSON、出力先を指定します。例では`CUDA_VISIBLE_DEVICES=0`を指定しています。MCPブリッジは実行中のDocisionモデルサービスに接続し、モデルはサービス側ホストで動作すると説明されています。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- READMEの例に従い、リポジトリをcloneしてPython仮想環境を有効化し、`python -m pip install -e '.' huggingface_hub`を実行します。`hf download SoMarkAI/Docision-1.0 --local-dir models/Docision-1.0`でモデルを取得し、`CUDA_VISIBLE_DEVICES=0 python demo_docision.py --model models/Docision-1.0 --input examples/multiple.json --output outputs/document-decisions.json`で推論します。入力JSONには画像パスと質問・候補を記述します。

## 変更履歴

- 2026-11-23: 初回登録
