---
repo: "multica-ai/andrej-karpathy-skills"
name: "Karpathy Guidelines（karpathy-guidelines スキル）"
genre: "coding-agent"
url: "https://github.com/multica-ai/andrej-karpathy-skills"
license: "unknown"
stars: 230810
language: ""
created: "2026-01-27"
updated: "2026-04-20"
forks: 22965
open_issues: 139
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 20
archived: false
last_release: ""
last_release_at: ""
author: "forrestchang（multica-ai 組織）"
flags: ["unverified"]
risk_notes: "効果は未検証：README の定性チェックリスト以外に実測・ベンチマークがなく、効能は著者の主張にとどまる。Karpathy 本人の監修・寄稿はなく、第三者が本人のX投稿（2026-01-26）を4原則に再構成した非公式プロジェクト（旧リビジョンの README には非公式である旨の免責があったが現行 README では削除済み）。ライセンスは LICENSE ファイルがなく API は null（README・SKILL.md・plugin.json は MIT と記載）のため unknown 扱い。2026-04-20 以降コミットがなく stale、open_issues 139 は Issues 無効化（has_issues=false）のため実質 PR。README のインストール手順は forrestchang 名義の URL で、multica-ai へ301リダイレクトする移管前の記述のまま。"
type: "repo"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/sumika45379/status/2112884125120319643", "https://x.com/ai_300/status/2118846893404897593?a=P4rnRTlJRTZ6LwYBFuI&s=46", "https://x.com/ai_300/status/2118846893404897593", "https://api.github.com/repos/multica-ai/andrej-karpathy-skills", "https://github.com/multica-ai/andrej-karpathy-skills/blob/HEAD/README.md", "https://api.github.com/repos/multica-ai/andrej-karpathy-skills/commits?per_page=3", "https://github.com/multica-ai/andrej-karpathy-skills"]
fetched_at: "2026-11-08T15:09:44Z"
---

# andrej-karpathy-skills — Karpathy の観察を4原則にした coding-agent 向けガイドライン／skill

## 出来ること

- AI コーディングの失敗を減らす4原則を、そのままエージェントに読ませられる形で提供する：Think Before Coding（仮定を明示し、曖昧なら止まって聞く）、Simplicity First（頼まれた以上の機能・抽象化を作らない）、Surgical Changes（依頼に直結する行だけ変える）、Goal-Driven Execution（成功条件を先に決め、検証できるまで回す）。
- 配布形態が4つ用意されている：skills/karpathy-guidelines/SKILL.md（frontmatter 付きスキル、2518バイト）、CLAUDE.md（プロジェクト常設の指示、2357バイト）、Claude Code プラグイン（.claude-plugin/plugin.json + marketplace.json）、Cursor 用ルール（.cursor/rules/karpathy-guidelines.mdc）。
- 同じ内容の中国語版 README（README.zh.md）と、適用例を並べた EXAMPLES.md（約14.8KB）が同梱されている。
- 4原則はそれぞれ「〜してはいけない」ではなく判定テストを持つ（例：変更行はすべてユーザーの依頼に遡れるか／シニアエンジニアなら過剰と評するか）ので、レビュー時のチェックリストとしても使える。

## 目的・背景

- 出発点は Andrej Karpathy が 2026-01-26 に X へ書いた所感で、そこでは「モデルは勝手に誤った仮定を置いて突き進む」「100行で済むものを1000行で作る」「理解が不十分なコメントやコードを副作用で書き換える」といった挙動が指摘されている。README の引用はこのポストの記述とほぼ一致することを実際のポストで確認した。
- ただし4原則そのものは Karpathy の文章ではなく、リポジトリ作者（forrestchang、現在は multica-ai 組織へ移管）がポストの観察を整理したもの。Karpathy 本人の監修・寄稿・推薦を示す記述はリポジトリ内になく、以前のリビジョンの README には「Karpathy の公式プロジェクトではなく本人が維持しているものでもない」という免責が明記されていた（現行 README ではこの免責が削除されている）。出典リンク自体は明示されている。
- 設計思想は「速さより慎重さ」。README は、些細な修正や明白な一行変更には全原則を適用せず判断で省略せよと自ら注記しており、非自明な作業での高コストな失敗を減らす用途に限定している。
- スター230,810・フォーク22,965はこの種のガイドライン集としては極端に大きいが、これはリポジトリ全体の人気であって個々の原則の有効性を示す数字ではない。

## 依存関係

- コード依存はゼロ。Node/Python パッケージも外部APIもなく、配布物は Markdown と JSON のみ（リポジトリサイズ20KB）。
- 利用側の前提として、スキルや常設指示を読み込めるエージェントが必要：Claude Code（プラグイン機構または CLAUDE.md）か Cursor（プロジェクトルール）。
- ライセンスは要注意。LICENSE ファイルが存在せず GitHub API の license は null のため unknown 扱いだが、README・SKILL.md の frontmatter・plugin.json はいずれも MIT と記載している。再配布する場合は MIT 表示を保持する前提で扱うのが安全。
- README のインストール手順は forrestchang/andrej-karpathy-skills を指したままで、この URL は multica-ai/andrej-karpathy-skills へ301リダイレクトする（同一リポジトリ、ID 1142983825）。手順通りで問題なく入るが、表示されるオーナー名が README 冒頭の説明と食い違う。

## 実行条件

- 特定モデル専用ではない。SKILL.md は frontmatter の description に「コードを書く・レビューする・リファクタリングするとき」と発火条件を書いており、対応するエージェントならどれでも読ませられる。
- プラグインとして入れる場合は Claude Code の /plugin が使えること、CLAUDE.md 方式ならプロジェクト直下に置けること、スキル方式ならスキルディレクトリを読む設定になっていることが条件。
- 過剰適用に注意：4原則は「速さより慎重さ」に振ってあるため、タイポ修正や自明な一行変更では手順が重くなる。README 自身が判断で省略せよと書いている。
- 効果の実測値はない。採用判断は、自分のリポジトリで差分の無駄や過剰抽象化が減ったかを数週間単位で見て決めるしかない（この点は未確認のまま）。

## 最短手順

- 1) Claude Code から呼ぶ（README の推奨手順）：Claude Code 内で `/plugin marketplace add forrestchang/andrej-karpathy-skills` を実行し、続けて `/plugin install andrej-karpathy-skills@karpathy-skills` を実行する。プラグイン名は andrej-karpathy-skills、マーケットプレイス名は karpathy-skills（.claude-plugin/marketplace.json の name/id と一致）。
- 2) スキルとして手元に置く場合：リポジトリの `skills/karpathy-guidelines/SKILL.md` を、Claude Code のスキル配置先 `<project>/.claude/skills/karpathy-guidelines/SKILL.md`（全プロジェクト共通なら `~/.claude/skills/karpathy-guidelines/SKILL.md`）にコピーする（この配置先は Claude Code のスキル配置の慣例で、このリポジトリの README には記載がない）。frontmatter は `name: karpathy-guidelines` と `description: Behavioral guidelines to reduce common LLM coding mistakes. Use when writing, reviewing, or refactoring code ...` の2行が要で、description が呼び出し条件になる。
- 3) 呼び出し方：description の条件に合う作業（実装・レビュー・リファクタ）でエージェントが自動的に選ぶ。確実に効かせたいときは「karpathy-guidelines を適用してから実装して」のようにスキル名を明示する。
- 4) プロジェクト常設にする場合：リポジトリ直下に `curl -o CLAUDE.md https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md` で CLAUDE.md を取得して置く（既存ファイルへは追記）。既存の CLAUDE.md があるなら、4原則の見出しだけをマージする。
- 5) Cursor で使う場合：`.cursor/rules/karpathy-guidelines.mdc` をプロジェクトの `.cursor/rules/` に置く。手順の詳細は同梱の CURSOR.md にある。

## 変更履歴

- 2026-11-09: 初回登録
