---
name: "Build once, run on any agent: A practical guide to agent skills"
genre: "article"
url: "https://github.blog/ai-and-ml/github-copilot/build-once-run-on-any-agent-a-practical-guide-to-agent-skills/"
published: "2026-11-12"
flags: []
type: "article"
added: "2026-11-13"
first_seen: "2026-11-13"
risk_notes: ""
sources: ["https://x.com/CodetocashAi/status/2121224709291319659"]
fetched_at: "2026-11-13T16:11:55.484636+00:00"
---

# Build once, run on any agent: A practical guide to agent skills

## テーマ

- GitHubのAndrea Griffithsによる、繰り返し行うエンジニアリング作業をエージェントスキルとして記述し、異なるエージェントクライアントで活用するための実践ガイド。記事ではスキルを、作業の実行条件と方法を記した SKILL.md を中心にしたバージョン管理可能なディレクトリとして説明している。

## 著者の主張

- 記事は、スキルごとに明確な作業、入力、出力を定め、プロジェクト固有の情報はマニフェストに分けることを推奨する。Data Forge の例では、スキルを役割ごとに分け、共有マニフェストや共通のデータアクセス経路を使って連携させる。Claude Code、Cursor、GitHub Copilot向けのファイルは、skills/*/SKILL.md を元にパッケージスクリプトで生成する例を示している。著者はさらに、人間の確認点やCIチェックを設け、別のクライアントでも必要な参照、ツール、出力が利用できるか確認するよう勧めている。

## 裏取り・注意点

- 記事の説明では、スキルは指示を持ち運べても、実行に必要なツール、認証情報、権限は実行環境が提供する。スキルによる指示だけではデータベースアクセスを得られない。また、記事のGitHub Actionsの例は差分の静的レビューで、コード実行やテストを行わない。記事は導入例と推奨事項を示すもので、複数クライアント間の動作の同一性や、効果・信頼性を比較した独立測定値は提示していない。

## 出典

- 一次資料：GitHub Blog, “Build once, run on any agent: A practical guide to agent skills” — https://github.blog/ai-and-ml/github-copilot/build-once-run-on-any-agent-a-practical-guide-to-agent-skills/

## 変更履歴

- 2026-11-13: 初回登録
