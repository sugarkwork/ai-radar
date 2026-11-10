---
type: "repo"
name: "Security Audit Skill (Cloudflare)"
genre: "agent-framework"
url: "https://github.com/cloudflare/security-audit-skill"
author: "Cloudflare"
pricing: "free"
pricing_detail: "MIT のオープンソース。API キーや有料枠は不要（動かすエージェント側のモデル費用は別）。"
signup_required: false
repo: "cloudflare/security-audit-skill"
license: "MIT"
stars: 67955
language: "JavaScript"
created: "2026-06-18"
updated: "2026-09-14"
added: "2026-11-07"
first_seen: "2026-11-07"
sources: ["https://x.com/MengTo/status/2118384737626857724"]
flags: []
risk_notes: "監査ワークフローであり、スキャナや自動修正ツールではない。対象コードのビルド/テスト実行には OS 強制サンドボックス（外部ネットワーク遮断・許可制環境変数・リソース上限・scratch 以外書き込み不可）が前提で、満たせない環境では confirmed ではなく needs_validation 止まりになる。並列サブエージェントを起動できるコーディングエージェントが必須。タグ付きリリースは無く、最終コミットは 2026-09-14 で 30 日コミット 0（メンテは停止気味）。ライセンスは MIT。投稿の「studying brands」という説明は README / SKILL.md の内容（コードベースの脆弱性監査）と一致しない。"
forks: 4455
open_issues: 123
commits_30d: 0
commit_cadence: "monthly"
size_kb: 143
archived: false
fetched_at: "2026-11-09T21:32:45Z"
last_release: ""
last_release_at: ""
source_post: "https://x.com/MengTo/status/2118384737626857724"
commits_90d: 3
---

# Security Audit Skill（cloudflare/security-audit-skill）

## 出来ること

- コーディングエージェントを「セキュリティ監査者」に変える Agent Skill。リポジトリ/API/サービス/CLI/ライブラリ/デーモンを、偵察 → カバレッジ主導の探索 → 候補の反証検証 → 構造化出力 → 独立レコード検証 → 対象非依存レポートの6フェーズで回す。
- 偵察フェーズで architecture.md（構成・信頼境界・入力面）と coverage-ledger.json（決定的なカバレッジ台帳）を作り、以降の探索はその台帳のユニット単位で hunter を割り当てる。1回で終わらせず、critic で穴を探して追加ウェーブを回す。
- 候補ごとに「見つけたエージェントとは別の」検証エージェントを立てて反証を試みる（adversarial validation）。判定は confirmed / needs_validation / rejected の3種で、confirmed だけが source trace と限定的な再現結果を持ち、severity が付く。needs_validation には severity を付けない。
- findings.json は report-schema.json で定義され、同梱の依存ゼロ Node スクリプト（validate-findings.cjs、validate-coverage-ledger.cjs）で機械検証できる。台帳は Phase 1 と更新のたび、findings は Phase 4 と Phase 5 の置換後に検証する。
- 対象の種類に応じた攻撃クラスのcompanionを同梱: AI-AND-LLM（プロンプトインジェクション・エージェント/ツール・出力処理）、WEB-PROTOCOL-AND-AUTH（HTTP フレーミング・キャッシュ・認証）、CLIENT-SIDE（DOM インジェクション・postMessage・UI redress）、SUPPLY-CHAIN-AND-RELEASE、CLOUD-AND-DEPLOYMENT、MEMORY-SAFETY-AND-BINARY、DATA-ISOLATION-AND-LIFECYCLE、PROTOCOLS-RPC-AND-MESSAGING、RESOURCE-EXHAUSTION、DESKTOP-MOBILE-AND-LOCAL-IPC など12ファイル。
- guidance mode と full audit mode を分ける。セキュリティの質問や部分レビューではワークフロー全体を走らせず、コードベース監査/ペネトレーションテストを明示依頼したときだけ6フェーズと成果物書き出しに進む（曖昧なら1問だけ確認する）。
- 同じリポジトリへの複数回実行は additive。prior の coverage-ledger.json / findings.json を読み、未カバー領域と変更されたソースを狙い、古い証拠を「カバー済み」として再利用しない。
- 出力は REPORT.md / FINDINGS-DETAIL.md / NEEDS-VALIDATION.md の3ファイル。レポートは対象に依存しない形（ライブ攻撃手順を含めない）で生成される。

## 目的・背景

- Cloudflare が社内で使っている脆弱性発見ハーネスの出発点になったスキル。ブログ記事「Build your own vulnerability harness」で解説された多段・全社規模のシステムを、単一リポジトリで再現できる形に切り出したもの、と README が説明している。
- 設計原則は「実在の信頼境界を越えたものだけを confirmed にする」。チェックリスト逸脱や多層防御の欠落は脆弱性ではなく hardening note とし、severity は実証された impact を超えられない。同じ根拠で複数回走らせると単発より多く見つかる（テストでは1回で全体の約半分）として、カバレッジ台帳と反復を前提にしている。
- 2026-06-18 作成、最終 push は 2026-09-14。タグ・GitHub Release は無く、配布は main ブランチのみ。
- 投稿（X）は「ブランドを研究するスキル」と紹介しているが、リポジトリの実体はコードベースのセキュリティ監査スキルで、内容は一致しない。

## 依存関係

- ツール呼び出しと並列サブエージェントに対応したコーディングエージェント（Claude Code / Codex / Cursor など skills CLI 対応エージェント）。SKILL.md は agent-neutral に書かれており、parent / Task tool / research / general agent を各プラットフォームの相当機能に読み替える。
- Node.js。同梱の validate-findings.cjs / validate-coverage-ledger.cjs は依存ゼロの CommonJS（npm install 不要）。
- 対象コードのビルド・テスト・ブラウザ・エミュレータ・ファザーを動かす場合は OS 強制のサンドボックスが必須（外部ネットワーク遮断、許可制の空環境、読み取り専用の対象とツールチェーン、scratch のみ書き込み、CPU/メモリ/プロセス/ファイルサイズ/実行時間の上限）。用意できなければ対象コードは実行せず needs_validation として報告する。
- 導入は skills CLI（https://skills.sh、npx skills add）。npm パッケージや MCP サーバとしての配布は無い（package.json も .mcp.json もリポジトリに存在しない）。

## 実行条件

- シェル実行とサブエージェント起動ができるエージェントであること。単体の Web チャットでは、hunter/verifier を分離する設計上まともに動かない。
- 防御目的の読み取り専用監査。対象のビルドやテストはサンドボックス内の最小効果に限定し、デプロイ済みエンドポイント・本番・共有基盤・他者データの検査、成果物の公開、リリース改変、従量課金 API の消費は禁止事項として明記されている。
- 出力先の既定は ~/security-audit-skill/<repo-name>/run-<N>（N は次の未使用番号）。対象リポジトリ内に書くのは、ユーザーが明示的に指定し、バージョン管理がそのディレクトリ全体を無視すると親エージェントが確認できた場合のみ。
- ライセンスは MIT、archived ではない。ただしタグ付きリリースが無く 30 日コミット 0（最終コミット 2026-09-14）なので、更新は main を直接追う必要がある。
- モデル費用は動かすエージェント側の負担。スキル自体は無料で、API キーやサインアップは不要。

## 最短手順

- 1. スキルを入れる: npx skills add https://github.com/cloudflare/security-audit-skill --skill security-audit （ユーザー単位にしたければ --global を付ける）
- 2. 監査したいコードベースのルートでコーディングエージェントを起動する（リポジトリ全体、または対象パスを渡す）。
- 3. 「security audit this codebase」または「find security vulnerabilities in ./src」と依頼する。SKILL.md の description にあるトリガー（security audit / find vulnerabilities / pen-test the code）に一致すると自動で有効化される。
- 4. 出力先を固定したいときは「do a security review, output to ~/audits/my-project」のようにパスを添える。省略時は ~/security-audit-skill/<repo-name>/run-<N>。
- 5. 生成物を確認する: REPORT.md（要約）/ FINDINGS-DETAIL.md（confirmed の詳細）/ NEEDS-VALIDATION.md（未解決の論点）。findings.json は node validate-findings.cjs findings.json でスキーマ検証できる。
- 6. 小手調べなら guidance mode のまま「この認証フローで信頼境界を越える入力はある？」のように質問形式で聞くと、6フェーズを回さず関連部分だけ使う。

## 変更履歴

- 2026-11-07: 初回登録
