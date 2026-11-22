---
name: "Download Anything (DA)"
genre: "other"
url: "https://github.com/nengong/download-anything"
repo: "nengong/download-anything"
license: "unknown"
stars: 251
language: "Python"
created: "2026-11-04"
updated: "2026-11-08"
forks: 6
open_issues: 1
commits_30d: 32
commit_cadence: "daily"
commits_90d: 32
size_kb: 451
archived: false
flags: ["unverified"]
risk_notes: "READMEではMITと案内されているが、添付の測定値ではlicenseがunknown。対象プラットフォームごとの記載機能や取得可否は、実際の動作を独立に確認していない。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/GitTrend0x/status/2122653626900332544"]
fetched_at: "2026-11-17T23:27:57.115054+00:00"
---

# Download Anything (DA)

## 出来ること

- READMEによると、CLIとAgent Skillの2つの入口から、動画・画像・音声・記事・論文・電子書籍・共有ファイルなどを取得できる。字幕、カバー画像、独立音声トラック、BibTeX、Markdown、メタデータなどの付属ファイル保存、ファイル形式の検証、Obsidian Vaultへの同期も説明されている。対応範囲や成果はREADMEの記述であり、各サービスでの動作を独立に実測したものではない。

## 目的・背景

- 個人やAI Agentがリンク、識別子、アプリ共有文からコンテンツを取得し、関連資料とともに構造化して保存することを目的としている。READMEは共有文のノイズ除去、取得ファイルの検証、AI AgentやObsidianで扱いやすい形式への整理を説明している。

## 依存関係

- README記載ではPython 3.10以上が必要。音声・動画処理にはFFmpegを使用する。インストール時はPython依存パッケージを導入し、PyPIを優先し、タイムアウト時には清華または阿里雲ミラーへ切り替えると説明されている。

## 実行条件

- CLIインストール後、READMEの例では `da doctor --json` で環境を確認する。音声・動画の処理にはFFmpegが必要。百度网盘や夸克网盘など認証が必要なサービスでは、環境変数、credentials.yaml、またはデスクトップ環境からのログイン状態を使う手順が記載されている。

## 最短手順

- READMEの案内は、リポジトリを取得し、`python3 skills/download-anything/scripts/install.py` を実行してCLIを導入した後、Agentのユーザー用skillsディレクトリに `skills/download-anything` を配置する手順。インストール後に `da doctor --json` を実行して環境を確認し、CLIでは `da "URLまたは共有文" --json` の形式で入力する。

## 変更履歴

- 2026-11-22: 初回登録
