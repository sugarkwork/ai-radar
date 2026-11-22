---
name: "astro-conversion-kit"
genre: "coding-agent"
url: "https://github.com/ethanplusai/astro-conversion-kit"
repo: "ethanplusai/astro-conversion-kit"
stars: 132
forks: 25
open_issues: 2
size_kb: 5720
language: "JavaScript"
created: "2026-10-22"
updated: "2026-10-31"
archived: false
license: "MIT"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/AIExplorerTim/status/2118910064606233060"]
fetched_at: "2026-11-16T21:44:14Z"
last_release: ""
last_release_at: ""
---

# astro-conversion-kit

## 出来ること

- Agent SkillsとNodeスクリプトで、公開サイトの内容を取得し、Astroサイトへ移行する。READMEは、ページ・メディア・リダイレクト・SEO情報の保持、検証ゲート、複数幅での画面比較、PRとステージング用成果物の作成を説明している。結果の数値は作者による報告であり、独立実測ではない。

## 目的・背景

- WordPressサイトを中心に、既存サイトのURL、コンテンツ、メタデータ、メディアのパス、リダイレクトや外観を引き継いだ静的Astroサイトへ移すことを目的とする。READMEによると、取得は公開ページを対象に行い、デフォルトでは既存サイトの不具合も再現し、修正案は提案として提示する。

## 依存関係

- Node.js、git、画面確認用のPlaywright Chromiumが必要。GitHubでリポジトリとPRを自動作成する場合は、ログイン済みのghとGitHubアカウントが必要。ステージング・本番ホスティングにはVercelまたはCloudflareアカウントを利用できる。README記載の対応環境はmacOSまたはLinuxで、Windowsは非対応。

## 実行条件

- README記載のNode要件は22系の22.23.4以降、または24.22.1以降。サイト取得は公開情報を対象とし、管理者ログイン、フォーム送信、DNS変更を行わないと説明されている。変換作業はastro-rebuildブランチで行い、mainへの反映は利用者がPRをマージする方式。

## 最短手順

- コーディングエージェントに「Convert https://example.com to Astro with https://github.com/ethanplusai/astro-conversion-kit」と入力する方法がREADMEに記載されている。手動導入では、README記載の `npx skills add ethanplusai/astro-conversion-kit` を使う。READMEにはクローン後の依存導入、Chromium導入、preflight実行手順もある。ここでは手順の記載のみを根拠としており、実行確認はしていない。

## 変更履歴

- 2026-11-15: 初回登録
