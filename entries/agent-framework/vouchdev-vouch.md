---
name: "vouch"
genre: "agent-framework"
url: "https://github.com/vouchdev/vouch"
repo: "vouchdev/vouch"
flags: ["unverified"]
risk_notes: "READMEの説明に基づく機能であり、効果や実行結果は未検証。LLM機能にはANTHROPIC_API_KEYを渡す手順が記載されているが、料金や利用条件は不明。"
stars: 67
forks: 62
open_issues: 45
size_kb: 22305
language: "Python"
created: "2026-05-17"
updated: "2026-08-23"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/Bober_smart/status/2116978958121964030"]
fetched_at: "2026-11-10T14:15:17.698097+00:00"
---

# vouch

## 出来ること

- LLMエージェント向けのGitネイティブな知識ベースを提供する。MCPサーバー、JSONLツールサーバー、CLIを備え、エージェントが提案した書き込みを人が承認してから保存する。承認済みクレームを根拠にトピックページをコンパイルし、引用を検証するとREADMEに記載されている。

## 目的・背景

- 複数のエージェントやチームで共有知識を書き込む際、誰が何の根拠で記録を承認したかを追跡できるようにすることを目的としている。承認済み成果物はリポジトリ内の`.vouch/`にYAMLクレームやMarkdownページとして保存され、Gitでレビューや履歴管理を行う。

## 依存関係

- READMEには、Pythonのみでのインストール方法と、Dockerでの起動方法が記載されている。ローカル開発ではPythonとNodeが必要とされ、LLM機能を有効にする手順ではANTHROPIC_API_KEYを渡す。

## 実行条件

- CLI・MCPサーバー利用、ブラウザーコンソール利用、ローカル開発の手順がREADMEに記載されている。ローカル開発の`make console`はNodeが必要。

## 最短手順

- README記載のCLI導入例は`pipx install vouch-kb`。Claude Code連携は対象プロジェクトで`vouch install-mcp claude-code`を実行する。READMEにはDockerによるデモ起動方法も記載されている。

## 変更履歴

- 2026-11-11: 初回登録
