---
repo: "NVIDIA/garak"
name: "garak (Generative AI Red-teaming and Assessment Kit)"
genre: "eval"
url: "https://github.com/NVIDIA/garak"
license: "Apache-2.0"
stars: 9967
language: "Python"
created: "2023-05-10"
updated: "2026-11-06"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/wquguru/status/2113181135522214168"]
flags: ["unverified"]
risk_notes: "検出精度・誤検知率の定量値は一次情報に記載がなく未検証。判定はキーワードまたは分類器ベースの検出器に依存し、スコアは正規化されていないためプローブ間の比較はできない。プローブの網羅性は保証されず、ペネトレーションテストの代替にはならない。実行は許可された対象に限る。"
forks: 1462
open_issues: 562
size_kb: 16934
archived: false
commits_30d: 91
commits_90d: 100
commit_cadence: "daily"
last_release: "v0.17.1"
last_release_at: "2026-10-16"
fetched_at: "2026-11-09T21:37:09Z"
type: "repo"
---

# garak — LLM 脆弱性スキャナ（NVIDIA）

## 出来ること

- LLM を対象に、ハルシネーション、データ漏洩、プロンプトインジェクション、誤情報、有害出力、ジェイルブレイクなどの弱点をプローブ（検査プロンプト群）で試し、検出器の判定と失敗率をレポートする CLI。
- 生成器（generator）を差し替えることで、Hugging Face のローカルモデル、OpenAI 互換 API、Anthropic、Cohere、Groq、AWS Bedrock、NVIDIA NIM、Ollama、LiteLLM、llama.cpp、任意の REST エンドポイントを同じ手順で検査できる。
- 実行ごとに JSONL レポートを出力し、送ったプロンプト・モデルの応答・判定スコアの対応を監査用に残す。
- probes / detectors / generators / evaluators / harnesses のプラグイン構造で、社内固有の検査や判定を追加できる。
- どのプローブをどの検出器で判定するかを --spec と --detectors で絞り込めるため、CI 向けの短い検査セットも組める。

## 目的・背景

- NVIDIA が公開する Apache-2.0 の LLM 脆弱性スキャナ。作者は nmap や Metasploit Framework の LLM 版という位置づけを明示している。
- 対象は「モデルの安全性（safety）」ではなく「セキュリティ」。モデルが推論時に望まない挙動をするか、出力ポリシーや alignment を破れるかを探す。
- 2023-05 にリポジトリが作られ、論文は 2024-06 公開の arXiv 2406.11036「garak: A Framework for Security Probing Large Language Models」。
- 静的なプロンプト集だけでなく、動的・適応的なプローブも組み合わせて探索する。

## 依存関係

- Python 3.11 以上（pyproject の requires-python）。
- pip 版は依存が重く、まっさらな OS で約 9GB。torch、transformers、datasets、openai、anthropic、litellm、huggingface_hub などを含む。
- 検査対象への到達手段が必要: 対象モデルの API キー（OPENAI_API_KEY など）、ローカルのモデル重み、または REST エンドポイントの接続設定。
- 追加 extras は audio、calibration、dra、tests、lint。音声系プローブや追加の判定器を使う場合に必要に応じて追加する。

## 実行条件

- ライセンスは Apache-2.0。★9,957 / 30日92コミット / 最終 push 2026-11-06 と活発。
- 検査は許可されたシステムに対してのみ実行する。ドキュメントが「exhaustive scan」で強いプロンプトを送ると警告している。
- 対象モデルへのネットワーク到達性が必要。API 版なら外向き HTTPS と API キー、ローカル版ならモデルを載せられる RAM / VRAM とディスク。
- 判定はキーワード一致か分類器で、スコアは正規化されていない。プローブ間の点数比較や、単一スコアでの合否判定には向かない。
- MCP サーバーは含まれない。AI エージェントからは CLI をサブプロセスで実行するか、Python から呼び出す。

## 最短手順

- 1. インストール: python -m pip install -U garak
- 2. 検査項目の確認: python -m garak --list_probes （検出器は --list_detectors、生成器は --list_generators）
- 3. OpenAI の場合: export OPENAI_API_KEY=... のうえで python -m garak --target_type openai --target_name gpt-5-nano --spec probes.encoding
- 4. ローカル Hugging Face の場合: python -m garak --target_type huggingface --target_name gpt2 --spec probes.dan.Dan_11_0
- 5. 任意の REST / OpenAI 互換エンドポイント: python -m garak --target_type rest.RestGenerator --target_name https://example.ai/llm --generator_options '{"rest":{"RestGenerator":{"req_template_json_object":{"text":"$INPUT"},"response_json":true,"response_json_field":"text"}}}' のように、リクエスト雛形と応答フィールドを JSON で渡す。
- 6. 検出器を固定する場合: --detectors all または --detectors <module>.<Class>。旧来の --probes は非推奨で、現在は --spec が正式。
- 7. AI エージェントからの呼び出し: subprocess で python -m garak を実行し、JSONL レポートを読む。Python 内なら from garak import cli; cli.main(['--target_type','openai','--target_name','gpt-5-nano','--spec','probes.encoding']) を呼ぶ。

## 変更履歴

- 2026-11-09: 初回登録
