---
name: "system-design-skill"
genre: "coding-agent"
url: "https://github.com/codejunkie99/system-design-skill"
repo: "codejunkie99/system-design-skill"
flags: ["unverified"]
risk_notes: "READMEによると、実利用はまだなく、テストはURL短縮サービスの模擬インタビュー1回のみ。応答時間、レート制限、tier境界の一部は提案値で、ピーク負荷の2倍設定に標準的根拠はない。README記載の範囲では依存関係の詳細は確認できない。"
stars: 9
forks: 1
open_issues: 0
size_kb: 12
language: "unknown"
created: "2026-11-01"
updated: "2026-11-01"
archived: false
license: "MIT"
commits_30d: 1
commits_90d: 1
commit_cadence: "monthly"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/Av1dlive/status/2116940187662217667"]
fetched_at: "2026-11-10T14:10:16.314296+00:00"
---

# system-design-skill

## 出来ること

- 8段階の短いインタビューで要件と規模を整理し、容量見積もり、段階ごとの必要度判断、選択肢とトレードオフの記録、Mermaid図、プレモーテムを作成する。承認用のDESIGN.mdを作り、承認されるまでコードを書かない。

## 目的・背景

- コーディングエージェントがコードを書く前に、ユーザーとシステム設計を行い、決定事項をDESIGN.mdに記録して実装の基礎にする。

## 依存関係

- READMEはスキルがnameとdescriptionのfrontmatterを持つ単一のSKILL.mdファイルで、Claude Code向けと説明している。その他の依存関係はREADMEから確認できない。

## 実行条件

- Claude Code向け。設計、アーキテクチャ、またはシステムの計画を依頼すると開始し、直接起動する場合は /system-design を入力する。

## 最短手順

- 全プロジェクトで使う場合は `git clone https://github.com/codejunkie99/system-design-skill.git ~/.claude/skills/system-design`。単一プロジェクトでは `.claude/skills/system-design` に配置する。エージェントに作りたいものを伝えるか、`/system-design` で起動し、生成されたDESIGN.mdを確認・承認してから実装へ進む。

## 変更履歴

- 2026-11-11: 初回登録
