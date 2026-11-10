---
repo: iOfficeAI/OfficeCLI
name: OfficeCLI
genre: other
url: https://github.com/iOfficeAI/OfficeCLI
license: Apache-2.0
stars: 33171
language: C#
created: 2026-03-15
updated: "2026-10-30"
added: 2026-11-05
first_seen: 2026-11-04
source_post: https://x.com/thegreatest_sv/status/2117687388214272339
sources: []
flags: []
risk_notes: ""
forks: 2271
open_issues: 145
commits_30d: 80
size_kb: 322871
archived: false
commits_90d: 100
commit_cadence: "daily"
fetched_at: "2026-11-09T21:41:06Z"
last_release: "v1.0.160"
last_release_at: "2026-10-30"
---

# OfficeCLI

## 出来ること

- Word（.docx）・Excel（.xlsx）・PowerPoint（.pptx）を、**Office をインストールせずに**読み・書き・自動化する単一バイナリのCLI。ネイティブ依存なし。
- 文書をパス指定のツリーとして扱い、`add` / `set` / `remove` で要素を編集する。例:
  ```bash
  officecli create deck.pptx
  officecli add deck.pptx / --type slide --prop title="Q4 Report" --prop background=1A1A2E
  ```
- 内蔵のHTMLレンダリングエンジンで .docx / .xlsx / .pptx を HTML または PNG に変換できる。生成 → 見る → 直すループをエージェント側で閉じられるのが特徴。
- `officecli watch deck.pptx` でローカル（既定 `http://localhost:26315`）にライブプレビューを開き、編集のたびに自動更新する。
- エージェント向けにスキルファイルを配布しており、`officecli install` がバイナリをPATHに置き、検出したAIコーディングエージェント（Claude Code、Cursor、Windsurf、GitHub Copilot など）へスキルを導入する。
- GUI が必要な場合は同社の AionUi（デスクトップアプリ）が OfficeCLI を内部で使う。

## 目的・背景

エージェントにOffice文書を扱わせる際、従来はCOM automation（Windows＋Office必須）やPythonライブラリの組み合わせが必要だった。単一バイナリとスキル配布で、OSを問わず「エージェントが自分で文書を作って確認できる」状態を狙っている。README の作例（プレゼン・論文・予算表など）はいずれもエージェントが生成したものと明記されている。

## 依存関係

- 実行に .NET ランタイムや Office は不要（自己完結バイナリ）。
- 導入方法は Releases のバイナリ、`install.sh` / `install.ps1`、Homebrew（`brew install officecli`）、npm（`@officecli/officecli`）。
- ライブプレビューはローカルHTTPポート（26315）を使う。

## 実行条件

- リポジトリサイズは約315MB（`size_kb` 322,871）。バイナリを取得する前提でディスク容量を見ておく。
- `curl -fsSL .../install.sh | bash` はベンダー公式のインストーラ。内容を確認せず実行したくない場合は Releases のバイナリを手動で置く。
- ライセンスは Apache-2.0。★3.3万・open issue 141件。

## 最短手順

```bash
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.sh | bash

officecli create deck.pptx
officecli watch deck.pptx            # http://localhost:26315
officecli add deck.pptx / --type slide --prop title="Hello, World!"
```

エージェントに導入させる場合は、チャットに `https://officecli.ai/SKILL.md` を読ませる。

## 変更履歴

- 2026-11-05: 初回登録（★33,059 / pushed 2026-10-30 / Apache-2.0 / v1.0.160）
