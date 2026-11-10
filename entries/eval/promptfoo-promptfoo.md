---
repo: "promptfoo/promptfoo"
name: "promptfoo"
genre: "eval"
url: "https://github.com/promptfoo/promptfoo"
author: "Promptfoo (OpenAI)"
license: "MIT"
stars: 27000
language: "TypeScript"
created: "2023-04-28"
updated: "2026-11-09"
forks: 2700
open_issues: 951
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
size_kb: 813364
archived: false
last_release: "0.125.1"
last_release_at: "2026-10-25"
flags: ["unverified"]
risk_notes: "有効性の数値（README の「10M+ users」等）はベンダー自己申告で、独立検証や本環境での再現はしていない。導入・eval・redteam の実行も未実施。Community の red teaming は月10k probes 上限で、SonarQube 出力・チーム共有・カスタムプラグイン・RBAC/SSO・監視は Enterprise 限定（公開価格なし、Custom 見積り）。LLM 採点の assertion は確率的で、しきい値・grader・--repeat の調整が必要。red team の検出結果は誤検知を含む前提で人間が triage する必要がある。README は OpenAI 傘下であることを明記しており、今後のライセンスや提供形態の変更リスクは残る。redteam は有害出力を誘発しうるため、管理下のアプリ以外には使わない。"
type: "repo"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/wquguru/status/2113181135522214168"]
fetched_at: "2026-11-09T21:37:12Z"
---

# promptfoo — プロンプト評価とレッドチーミングを CI に載せる OSS CLI

## 出来ること

- プロンプト・モデル/プロバイダ・テストケースを YAML のマトリクスで宣言し、1コマンドで全組み合わせを評価する。結果はローカル Web UI（promptfoo view）で横並び比較できる。
- assertions で出力を自動判定する。決定的なもの（contains-json、javascript、similar など）とモデル採点（llm-rubric、factuality、context-faithfulness など）を同じテストに混在できる。
- レッドチーミング: redteam プラグイン（harmful、pii、bola、bfla、contracts など）と strategies（jailbreak、jailbreak-templates など）で敵対的入力を生成し、対象アプリに投げて脆弱性レポートを作る。docs は 50+ の脆弱性タイプを自動スキャンすると記載する。
- CI 連携: eval は失敗1件以上または pass rate しきい値未満で exit code 100、その他のエラーは 1。GitHub Action（promptfoo/promptfoo-action@v1、type: redteam）や cron 実行の雛形がある。
- AI エージェントから呼ぶ口がある: promptfoo mcp --transport stdio の MCP サーバ（run_evaluation、redteam_run、validate_promptfoo_config など）と、Node ライブラリとしての利用。
- 結果共有はクラウド/Enterprise 側の機能: promptfoo share はアカウント（API キー）が必要で、SonarQube 形式の出力やチームダッシュボードは Enterprise 限定。

## 目的・背景

- LLM アプリの品質と安全性を、感覚ではなく再現可能なテストで担保するためのツール。README は「trial-and-error をやめて、安全で信頼できるエージェントを出荷する」ことを掲げる。
- 2023-04-28 作成、TypeScript 実装、MIT。GitHub の説明文は「Test your prompts, agents, and RAGs. Red teaming/pentesting/vulnerability scanning for AI.」で、command line と CI/CD 統合を明示している。
- README に「Promptfoo is now part of OpenAI. Promptfoo remains open source and MIT licensed.」とあり、OpenAI 傘下でも OSS/MIT を維持するとしている。
- 投稿の「紅隊（レッドチーム）を CI に接続する」という整理は、redteam run を CI で回す手順と GitHub Action の redteam タイプとして一次情報で確認できる。

## 依存関係

- Node.js 22.22.0 以上（package.json の engines）。npm パッケージ名は promptfoo、CLI の bin は promptfoo と pf。
- 導入は npm install -g promptfoo、npx promptfoo@latest、brew install promptfoo、pip install promptfoo のいずれか。
- 実行時依存は74パッケージ（@anthropic-ai/sdk、openai 系、@libsql/client、OpenTelemetry など）。評価対象モデル/エンドポイントの API キーは別途必要。
- redteam の一部プラグインは HuggingFace データセット（HF_TOKEN）や hosted 生成を使う。Community の red teaming は月10k probes まで。
- コードは MIT。Enterprise（チーム共有、RBAC/SSO、カスタムプラグイン、SonarQube 出力、API、監視）はリポジトリ外の別製品。

## 実行条件

- Node.js 22.22+ と、対象プロバイダの API キー（例: OPENAI_API_KEY）。評価はローカルで走り、プロンプトは既定で外部に送られないと README は説明する。
- 料金: Community は無料（全 eval 機能 + red teaming 月10k probes）。Enterprise は「Custom」で公開価格はなく、SonarQube 形式の出力は Enterprise 限定と docs に明記されている。
- LLM 採点の assertion は確率的なので、決定的な assertion と併用し、必要な箇所は --repeat でばらつきを測ってしきい値を調整する。red team の検出は誤検知を含む前提で人間が triage する。
- docs の警告: 敵対的テストは攻撃的・有害な入力を作り、対象システムに有害な出力をさせうる。管理下のアプリに限定し、生成物の扱いに注意する。
- CI では exit code をゲートにする。失敗時 100 は PROMPTFOO_FAILED_TEST_EXIT_CODE で変更でき、pass rate のしきい値は PROMPTFOO_PASS_RATE_THRESHOLD で決まる。

## 最短手順

- 1. 導入: `npm install -g promptfoo`、または `npx promptfoo@latest init --example getting-started`。後者は promptfooconfig.yaml・prompts/・テストを含むサンプル一式を展開する。
- 2. promptfooconfig.yaml の最小形: `prompts: [file://prompt1.txt]`、`providers: [openai:gpt-6-luna]`、`tests: [{vars: {language: French, input: Hello world}, assert: [{type: contains-json}, {type: similar, value: was geht, threshold: 0.6}]}]`。prompts と providers の直積が評価マトリクスになる。
- 3. 評価: `npx promptfoo@latest eval -c promptfooconfig.yaml -o results.json`。合否は assertion が決め、`npx promptfoo@latest view` でローカル UI を開いて差分を見る。
- 4. CI ゲート: eval は失敗1件以上または pass rate が PROMPTFOO_PASS_RATE_THRESHOLD 未満で exit code 100、その他エラーは 1 を返す。GitHub Actions ではこの終了コードで job を落とし、必要なら results.json の `results.stats.failures` を jq で見て明示的に exit 1 する（docs に例がある）。
- 5. レッドチーム: `npx promptfoo@latest redteam init my-redteam --no-gui` で雛形を作り、`targets: [{id: https://your-app.example/chat}]` と `redteam: {purpose: "カスタマーサポートBot", plugins: [harmful, pii, bola], strategies: [jailbreak, jailbreak-templates], numTests: 5}` を設定する。
- 6. 生成と実行: `npx promptfoo@latest redteam run`（generate + eval の短縮）、レポートは `npx promptfoo@latest redteam report`。CI では `npx promptfoo@latest redteam run --tag ci.run-id=$CI_RUN_ID -o output.json` のように実行し、GitHub Actions なら `uses: promptfoo/promptfoo-action@v1` に `type: 'redteam'`・`config`・API キーを渡す。
- 7. エージェントから駆動: `.cursor/mcp.json` もしくは Claude Desktop の設定に `{"mcpServers": {"promptfoo": {"command": "npx", "args": ["promptfoo@latest", "mcp", "--transport", "stdio"]}}}` を追加し、run_evaluation・redteam_generate・redteam_run・validate_promptfoo_config などのツールを呼ばせる。MCP を使わない場合は CLI をサブプロセスで実行し、exit code と results.json を読む。

## 変更履歴

- 2026-11-09: 初回登録
