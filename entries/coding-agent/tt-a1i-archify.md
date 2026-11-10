---
repo: "tt-a1i/archify"
name: "Archify"
genre: "coding-agent"
url: "https://github.com/tt-a1i/archify"
last_release: "v3.2.0"
flags: ["unverified"]
risk_notes: "生成された図の正確性や可読性、各エージェントでの導入と書き出しの動作は独立に検証していない。GitHubの公開ページで最新版タグを確認したが、完全な公開日時は未確認。"
stars: 95261
forks: 6499
open_issues: 353
size_kb: 1523129
language: "JavaScript"
created: "2026-04-15"
updated: "2026-11-10"
archived: false
license: "Apache-2.0"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/opensourcelab9/status/2115209466392228235"]
fetched_at: "2026-11-10T12:02:00Z"
---

# Archify — AIとの会話で作るインタラクティブな構成図

## 出来ること

- 自然文から、ノードを選んで経路をたどれるHTMLの構成図を生成する。手元にコードがない設計案から始め、会話で認証の追加や経路の強調を指示できる。 [公式README](https://raw.githubusercontent.com/tt-a1i/archify/main/README.md)
- v3.2.0では結論を先頭に置く1ページ解説を追加。公式リリースノートによると、解説をPNG・WebP・JPGの長画像に書き出し、ブラウザの印刷機能でPDFにできる。 [公式リリースノート](https://github.com/tt-a1i/archify/releases/tag/v3.2.0)

## 目的・背景

- エージェントが型付きJSONの中間表現を作り、付属のCLIがスキーマや配置を検証してHTMLを生成する。経路表示は図に記述された関係をたどるため、実システムの通信経路を確認するには別途観測が必要。 [公式README](https://raw.githubusercontent.com/tt-a1i/archify/main/README.md)

## 依存関係

- CLIはNode.js 18以上。会話で使うにはCodex CLIやClaude Codeなど、Skillを読み込めるエージェントを用意する。 [パッケージ定義](https://github.com/tt-a1i/archify/blob/main/archify/package.json) [英語版README](https://github.com/tt-a1i/archify/blob/main/README_EN.md)

## 実行条件

- 生成したHTMLをブラウザで開く。現行ソースはApache-2.0で公開されており、エージェントや第三者サービスの料金・利用条件は各提供元に従う。 [英語版README](https://github.com/tt-a1i/archify/blob/main/README_EN.md)

## 最短手順

- Codex CLIで試す場合、公式READMEの一時利用手順 `npx skills use tt-a1i/archify@archify --agent codex` でSkillを読み込む。 [英語版README](https://github.com/tt-a1i/archify/blob/main/README_EN.md)
- Codexに『Archifyで、ブラウザがAPIを呼び、APIがRedisを確認する構成を図にして』と頼む。生成されたHTMLを開き、必要に応じて同じ会話で変更を指示する。 [公式README](https://raw.githubusercontent.com/tt-a1i/archify/main/README.md)

## 変更履歴

- 2026-11-10: 初回登録
