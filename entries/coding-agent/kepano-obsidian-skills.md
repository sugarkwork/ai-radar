---
repo: "kepano/obsidian-skills"
name: "Obsidian Skills"
genre: "coding-agent"
url: "https://github.com/kepano/obsidian-skills"
flags: ["unverified"]
stars: 51458
forks: 3639
open_issues: 76
size_kb: 44
language: "unknown"
created: "2026-01-02"
updated: "2026-09-15"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 3
commit_cadence: "monthly"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
risk_notes: ""
sources: ["https://x.com/Bober_smart/status/2117619229465641097"]
fetched_at: "2026-11-10T10:01:34+00:00"
---

# Obsidian Skills — AIにノート形式とVault操作を教えるスキル集

## 出来ること

- Obsidian固有のMarkdown、Bases、JSON Canvasの作成・編集手順をAIに渡せる。Markdownスキルには内部リンク、埋め込み、コールアウト、プロパティの書き方がある。 [Markdownスキル定義](https://github.com/kepano/obsidian-skills/blob/main/skills/obsidian-markdown/SKILL.md)
- CLIスキルはノート検索や読み取り、タスクやプロパティの操作例を提供する。READMEにはWebページからMarkdownを抽出するDefuddle用と、JSONやCSVからテンプレートを展開するKnap用のスキルも掲載されている。 [CLIスキル定義](https://raw.githubusercontent.com/kepano/obsidian-skills/main/skills/obsidian-cli/SKILL.md) [README](https://raw.githubusercontent.com/kepano/obsidian-skills/main/README.md)

## 目的・背景

- Obsidian固有の書式と操作をタスク別の指示として再利用するためのスキル集。たとえばMarkdownスキルは、プロパティを記述し、既存ノートをウィキリンクで結ぶ流れを示す。品質向上の度合いは実測していない。 [Markdownスキル定義](https://github.com/kepano/obsidian-skills/blob/main/skills/obsidian-markdown/SKILL.md)

## 依存関係

- READMEはAgent Skills仕様に対応した環境としてClaude Code、Codex、OpenCodeを挙げている。DefuddleやKnapを使う作業には、それぞれ対応するCLIが必要。リポジトリのライセンスはMIT。 [README](https://raw.githubusercontent.com/kepano/obsidian-skills/main/README.md)

## 実行条件

- ファイル編集には、対象のVaultをAIが読み書きできる必要がある。CLI経由で操作する場合は、エージェントから `obsidian` コマンドを実行でき、Obsidianが起動していることが前提。 [CLIスキル定義](https://raw.githubusercontent.com/kepano/obsidian-skills/main/skills/obsidian-cli/SKILL.md)

## 最短手順

- Codexでは、READMEに沿ってリポジトリの `skills/` 内の各スキルをCodexのスキル配置先に置く。対象Vaultを作業フォルダーにし、『obsidian-markdownスキルを使い、既存ノートへのウィキリンクとtagsを含むMarkdownノートの下書きを作って』と依頼する。 [README](https://raw.githubusercontent.com/kepano/obsidian-skills/main/README.md) [Markdownスキル定義](https://github.com/kepano/obsidian-skills/blob/main/skills/obsidian-markdown/SKILL.md)
- CLIを試す場合はObsidianを起動し、AIに『obsidian-cliスキルで、Vault名を指定してキーワードを検索し、結果を要約して』と依頼する。スキル定義には `obsidian vault="My Vault" search query="test"` の例がある。 [CLIスキル定義](https://raw.githubusercontent.com/kepano/obsidian-skills/main/skills/obsidian-cli/SKILL.md)

## 変更履歴

- 2026-11-10: 初回登録
