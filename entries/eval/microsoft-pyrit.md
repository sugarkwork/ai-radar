---
name: "PyRIT (Python Risk Identification Tool for generative AI)"
genre: "eval"
url: "https://github.com/microsoft/PyRIT"
repo: "microsoft/PyRIT"
license: "MIT"
stars: 4801
language: "Python"
created: "2023-12-12"
updated: "2026-11-12"
forks: 1050
open_issues: 285
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 506810
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-13"
first_seen: "2026-11-13"
sources: ["https://x.com/mingzi206/status/2118628554883883348"]
fetched_at: "2026-11-13T00:13:04.411900+00:00"
---

# PyRIT (Python Risk Identification Tool for generative AI)

## 出来ること

- 生成AIシステムのセキュリティ・安全性上の弱点を見つけるための評価を支援する。CLIから再現可能な評価を実行するScanner、ブラウザーで結果を確認できるCoPyRIT GUI、独自のレッドチームワークフローを組み立てて拡張するPython frameworkを備える。OpenAI、Anthropic、Azure OpenAI、Microsoft Foundry、Azure Machine Learning、Google Gemini、Google Vertex AI、AWS Bedrock、Hugging Face、Ollama、Groq、OpenRouter、Cohere、GitHub Copilotなどへの接続をREADMEに記載。利用可能な機能は接続先とモデルに依存する。出典: https://github.com/microsoft/PyRIT

## 目的・背景

- PyRITは、生成AIシステムにおけるセキュリティと安全性の弱点を調べるため、Microsoft AI Red Teamとオープンソース貢献者が開発するツールキット。自動スキャン、適応型マルチターン攻撃、人間主導のテストを扱う。出典: https://github.com/microsoft/PyRIT

## 依存関係

- READMEにはPython frameworkと、オプションのLiteLLM adapterが記載されているが、依存パッケージやバージョンの一覧は提示されていない。

## 実行条件

- Python frameworkとして提供され、CLIスキャナーとGUIも利用可能。接続先の設定方法や各機能の条件はREADMEのリンク先ドキュメントに案内されており、このREADMEだけでは詳細を特定できない。利用可能な機能は接続先とモデルに依存する。出典: https://github.com/microsoft/PyRIT

## 最短手順

- READMEからGet started（https://microsoft.github.io/PyRIT/）へ進み、インストールと設定の案内を確認する。バージョン選択機能でインストール版に対応するドキュメントを選ぶようREADMEで案内されている。

## 変更履歴

- 2026-11-13: 初回登録
