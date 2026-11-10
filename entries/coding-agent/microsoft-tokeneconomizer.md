---
repo: "microsoft/TokenEconomizer"
name: "TokenEconomizer"
genre: "coding-agent"
url: "https://github.com/microsoft/TokenEconomizer"
stars: 5576
forks: 345
open_issues: 30
size_kb: 6997
language: "Python"
created: "2026-10-13"
updated: "2026-11-08"
archived: false
license: "Apache-2.0"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
last_release: "v0.1.0"
flags: ["unverified"]
risk_notes: "最新リリースの公開日時は未確認。導入と動作は実機で再現しておらず、掲載の削減率は著者のベンチマークに限られる。別のリポジトリやモデルでの効果は未確認。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/opensourcelab9/status/2117504564941508613"]
fetched_at: "2026-11-10T09:19:56Z"
---

# TokenEconomizer — コーディングエージェントの反復作業にかかるトークン費用を抑えるプラグイン

## 出来ること

- 過去セッションからリポジトリ固有の知識を抽出して再利用し、未使用ツールを後続セッションから外し、同じ失敗が続くと別のアプローチを促す。知識の再利用機能は既定でオフ。

## 目的・背景

- 同じリポジトリで作業を重ねる際に、環境の再調査や同じ失敗の繰り返しに費やすトークンを減らす。著者のSWE-Bench評価では、エージェントとモデルの5組で平均コストが18.4〜30.9%低下し、5組中4組でPass@1が向上した。

## 依存関係

- Python 3.10以上と対応バージョンのエージェントが必要。公開READMEにはClaude Code、Codex、GitHub Copilot CLI、Piの導入手順がある。

## 実行条件

- プラグインはApache-2.0。専用APIキーは不要で、補助モデル呼び出しには利用中のエージェントの契約または認証を使い、その費用もレポートに計上する。Claude CodeとCodexはクローン元からプラグインを読み込む。

## 最短手順

- 公開リポジトリをクローンし、Codex CLIの `codex plugin marketplace add` にクローンのパスを渡してから、`codex plugin add tokeneconomizer@tokeneconomizer` で追加する。
- 対象リポジトリでCodexを起動し、フォルダーとプラグインのフックを確認して信頼を設定する。Codexを再起動し、セッション内で `$tokeneconomizer:status` を呼んで状態を確認する。通常の依頼に対しては有効なフックが自動で動く。

## 変更履歴

- 2026-11-10: 初回登録
