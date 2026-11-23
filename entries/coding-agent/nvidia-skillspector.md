---
name: "SkillSpector"
genre: "coding-agent"
url: "https://github.com/NVIDIA/SkillSpector"
repo: "NVIDIA/SkillSpector"
license: "Apache-2.0"
stars: 26672
language: "Python"
created: "2026-03-21"
updated: "2026-11-16"
forks: 2376
open_issues: 163
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 15426
archived: false
flags: ["unverified"]
risk_notes: "READMEの脆弱性割合（分析対象31,132件中26.1%に脆弱性、5.2%に悪意の可能性）はプロジェクト側の記載で、ここでは調査手法や結果を独立検証していない。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/saiitoshii/status/2119195054476869800"]
fetched_at: "2026-11-18T05:11:25.966288+00:00"
---

# SkillSpector

## 出来ること

- AIエージェント向けスキルを走査し、17カテゴリにわたる71の脆弱性パターンを検出する。高速な静的解析に加えて任意のLLM意味解析、OSV.devを使った依存関係の脆弱性照会、リスクスコアと推奨事項、既知の検出結果を抑制するベースライン機能を備える。ターミナル、JSON、Markdown、SARIF形式でレポートを出力できる。これらはREADMEに記載された機能であり、検出精度は独立検証していない。

## 目的・背景

- READMEは、AIエージェントのスキルが暗黙の信頼のもとで実行され、十分な事前確認がないことを課題として挙げ、インストール前に安全性を調べる用途を説明している。NVIDIA Verified Skills pipelineの一部として、公開前にスキャン・評価・署名を行うとも記載されている。

## 依存関係

- READMEによると、インストールにはuvまたはpipを使う。LLM解析にはプロバイダーの認証情報が必要で、MCP機能を使う場合はインストール時にmcp extraを指定する。Docker利用ではローカルでイメージをビルドできる。

## 実行条件

- パッケージのPython要件は>=3.12,<3.16。READMEは、YARAの事前ビルドwheelがあるPython 3.12または3.13をインストール例に推奨している。3.14/3.15ではネイティブビルドが必要となり、CツールチェーンやPython開発ヘッダーが必要になる場合がある。Pythonなしで使うDocker手順も記載されている。

## 最短手順

- READMEのCLI-only例: `uv tool install --python 3.13 git+https://github.com/NVIDIA/skillspector.git`。ローカルのスキルを走査する例: `skillspector scan ./my-skill/`。静的解析のみなら `skillspector scan ./my-skill/ --no-llm`。

## 変更履歴

- 2026-11-23: 初回登録
