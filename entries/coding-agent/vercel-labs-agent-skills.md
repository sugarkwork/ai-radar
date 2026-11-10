---
repo: "vercel-labs/agent-skills"
name: "Vercel Agent Skills"
genre: "coding-agent"
url: "https://github.com/vercel-labs/agent-skills"
stars: 33817
forks: 2956
open_issues: 196
size_kb: 11754
language: "JavaScript"
created: "2025-12-08"
updated: "2026-10-28"
archived: false
license: "unknown"
commits_30d: 5
commits_90d: 23
commit_cadence: "weekly"
last_release: "agent-skills-1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62"
flags: ["unverified"]
risk_notes: "レビュー精度や適用前後の性能差は未実測。GitHubのLatestページでタグは確認したが、年とタイムゾーンを含む公開日時は確認できなかった。READMEはMITと記載しているが、APIの測定値はunknown。エージェント側の料金と導入の実動作は未確認。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/thegreatest_sv/status/2117998992126591399"]
fetched_at: "2026-11-10T11:21:32+00:00"
---

# Vercel Agent SkillsでReactの性能とWeb UIをレビューする

## 出来ること

- React・Next.jsのコードを、データ取得の直列化、バンドルサイズ、再レンダリングなどの観点からレビューする。Web UIではキーボード操作やフォーカス表示、フォームなどを確認できる。 [公式README](https://github.com/vercel-labs/agent-skills/blob/main/README.md)

## 目的・背景

- Agent Skills形式でレビュー手順を共有する。React向け資料は対策を影響度順に整理し、実装例を添えている。対象プロジェクトでの改善幅は未実測。 [React向けガイド](https://github.com/vercel-labs/agent-skills/blob/main/skills/react-best-practices/AGENTS.md?plain=1)

## 依存関係

- READMEの導入手順はnpx経由のSkills CLIを使う。導入先にはAgent Skills対応のコーディングエージェントが必要。 [公式README](https://github.com/vercel-labs/agent-skills/blob/main/README.md) [CLIリファレンス](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)

## 実行条件

- Web UIレビューでは、エージェントが対象ファイルを読み取れ、公開ガイドラインを取得できる必要がある。スキル定義ではファイル名と行番号で指摘を返す。 [Web UIスキル定義](https://github.com/vercel-labs/agent-skills/blob/main/skills/web-design-guidelines/SKILL.md)
- READMEのライセンス表記はMIT。リポジトリのAPI測定値はunknownで、利用するエージェントの料金は未確認。 [公式README](https://github.com/vercel-labs/agent-skills/blob/main/README.md)

## 最短手順

- 対象プロジェクトで `npx skills add vercel-labs/agent-skills` を実行し、使うスキルを導入する。 [公式README](https://github.com/vercel-labs/agent-skills/blob/main/README.md)
- 対応エージェントに対象ファイルを指定して『このReactコンポーネントの性能上の問題をレビューして』と依頼する。UIの場合は『web-design-guidelinesを使ってこのファイルのアクセシビリティをレビューして』と依頼する。 [公式README](https://github.com/vercel-labs/agent-skills/blob/main/README.md) [Web UIスキル定義](https://github.com/vercel-labs/agent-skills/blob/main/skills/web-design-guidelines/SKILL.md)

## 変更履歴

- 2026-11-10: 初回登録
