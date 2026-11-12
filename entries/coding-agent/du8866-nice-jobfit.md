---
name: "JobFit"
genre: "coding-agent"
url: "https://github.com/DU8866-nice/jobfit"
repo: "DU8866-nice/jobfit"
flags: ["unverified"]
risk_notes: "実モデル利用時は履歴書が選択したAIプロバイダーに送信される。READMEにはプロバイダーへの送信をページ上で案内するとあるが、実際の公開デモでの設定やデータ処理は確認していない。"
stars: 1
forks: 0
open_issues: 1
size_kb: 495
language: "Python"
created: "2026-10-29"
updated: "2026-10-29"
archived: false
license: "MIT"
commits_30d: 7
commits_90d: 7
commit_cadence: "weekly"
type: "repo"
added: "2026-11-12"
first_seen: "2026-11-12"
sources: ["https://x.com/binbin_eth/status/2120710960247615505"]
fetched_at: "2026-11-12T03:43:51.902742+00:00"
---

# JobFit

## 出来ること

- 求人票の要件を必須・歓迎に分け、履歴書との一致を「一致・一部一致・不足」で整理する。該当箇所の引用、求人票にあって履歴書にない語、既存の記述に基づく編集案、就労資格に関するフラグを表示する。英語・中国語に対応するとREADMEに記載。モデルの引用は履歴書内に存在するかコードで検証し、見つからない引用は除去する。

## 目的・背景

- 履歴書と求人票の照合結果に根拠となる履歴書の引用を付け、モデルが存在しない経験や引用を作るリスクを抑えることを目指す。READMEでは、モデルの回答を下書きとして扱い、引用・編集案をコードで検査すると説明している。

## 依存関係

- README記載の構成は、バックエンドがPython 3.11以上、FastAPI、Pydantic、pypdf、python-docxおよびAnthropic・OpenAI互換SDK。フロントエンドはNode 22以上、React 19、TypeScript、Vite。実モデル利用にはAnthropicまたはDeepSeekのAPIキーが必要。キーがない場合はオフラインのデモモードで動作すると説明されている。

## 実行条件

- ローカル実行にはPython 3.11以上とNode 22以上が必要。バックエンドは初期状態でデモモード。実モデルを使う場合はプロジェクトルートの.envにANTHROPIC_API_KEYまたはDEEPSEEK_API_KEYを設定する。README記載の無料Render構成では初回ビルド後に公開され、15分間アクセスがないとスリープする。

## 最短手順

- READMEの手順では、backendで仮想環境を作成・有効化し、`pip install -e ".[dev]"`を実行してから`uvicorn jobfit.main:create_app --factory --reload`を起動する。別ターミナルでfrontendに移動し、`npm install`と`npm run dev`を実行する。

## 変更履歴

- 2026-11-12: 初回登録
