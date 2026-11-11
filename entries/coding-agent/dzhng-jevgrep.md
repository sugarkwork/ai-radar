---
repo: "dzhng/jevgrep"
name: "Jevgrep"
genre: "coding-agent"
url: "https://github.com/dzhng/jevgrep"
license: "MIT"
stars: 3205
language: "TypeScript"
created: "2026-09-26"
updated: "2026-11-08"
forks: 245
open_issues: 10
commits_30d: 71
commit_cadence: "daily"
commits_90d: 100
size_kb: 11750
archived: false
last_release: "v0.8.0"
flags: ["unverified"]
risk_notes: "CLIは実行していない。作者の費用比較を独立に再現しておらず、他のリポジトリへの一般化、速度改善、各プロバイダーの現行料金、GitHubリリースの完全な公開日時は未確認。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/thegreatest_sv/status/2116142322543198271"]
fetched_at: "2026-11-10T12:54:07+00:00"
---

# Jevgrep — 自然言語で関連コードを探すエージェント向けCLI

## 出来ること

- リポジトリ内の挙動を自然言語で質問すると、関連ファイルと行番号付きのソース抜粋を標準出力に返す。Python、TypeScript／JavaScript、Go、Rustでは宣言を解析し、その他のテキストには代替処理を使う。

## 目的・背景

- 未知のコードベースで読むべき箇所を絞るため、Jevでフォルダ、ファイル、宣言の関連性を判定する。
- 作者の調整済みPython SWE-bench 10課題では両条件とも8件を解決した。Sol費用は28.6%減で、ここにはJev費用が含まれない。Jev込みの別の0.4.3再試行では、解決数を維持し総費用が25.8%減ったと報告している。

## 依存関係

- CLIはNode.js 22以上とnpmを使用する。READMEではSkillの導入にNode.js 22.20以上、npm／npx、ネットワーク接続が必要とされる。Vercel AI Gateway、TypeSafe、OpenRouter、OpenCode Zen、またはTypeSafe互換エンドポイントのキーを使う。

## 実行条件

- macOS、Linux、Windowsに対応。CLIはMITライセンス。検索対象に含まれるソースは設定したプロバイダーに送信される。既定の除外処理は機密情報の完全な除去を保証しない。

## 最短手順

- `npm install -g @dzhng/jevgrep` で導入し、`jg auth` でプロバイダーを設定する。
- 作業リポジトリで `jg skill` を実行し、Claude CodeやCodexなどにSkillを導入する。エージェントに挙動の調査を依頼し、ターミナルから `jg "How are telemetry events recorded and sent?" .` を呼ばせる。返されたファイルと行番号を手掛かりに原文を確認する。

## 変更履歴

- 2026-11-11: 初回登録
