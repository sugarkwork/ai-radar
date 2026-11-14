---
name: "Drama Skills"
genre: "coding-agent"
url: "https://github.com/zenstory-ai/drama-skills"
repo: "zenstory-ai/drama-skills"
license: "MIT"
stars: 4202
language: "Python"
created: "2026-07-16"
updated: "2026-11-10"
forks: 739
open_issues: 2
commits_30d: 80
commit_cadence: "daily"
commits_90d: 100
size_kb: 79228
archived: false
flags: ["unverified"]
risk_notes: "README記載の「视频生成成本约40元」は作者によるサンプルの説明で、一般的な費用を示すものではありません。実際の費用は記載されていません。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/ganfanren_ai/status/2118721879242633643"]
fetched_at: "2026-11-13T21:12:06.095938+00:00"
---

# Drama Skills

## 出来ること

- 短劇・漫劇の制作工程を、原著分析、分集脚本、ビジュアル設定、画像・動画提示詞、確認後の素材生成、編集、レビューまで12個のスキルで支援します。READMEには、Markdown文書で制作判断を記録する方法、文書間の参照や連続性ロックを検査するスクリプト、生成前に内容とパラメーターをプレビューして明示確認する手順が記載されています。

## 目的・背景

- 作者は、自社の漫劇制作ラインで使った工程や過去のプロジェクト資産をもとに、制作判断をファイルで管理し、Agent CLIで提示詞を作成するスキル群としてまとめたと説明しています。これはREADMEにある作者の説明です。

## 依存関係

- Claude Code、Codex、またはAgent Skill規格に対応するプログラミングAgentが前提です。インストール手順にはNode.jsのnpxが必要とあり、スクリプトはPython 3.9以降、編集にはPATH上のffmpegとffprobeが必要と記載されています。画像・動画・音声などの生成には外部インターフェースを使う手順が示されていますが、プロバイダーや料金は特定されていません。

## 実行条件

- README記載のGitHubインストール方法は `npx skills add zenstory-ai/drama-skills -y -g` です。`-g`を外すと現在のディレクトリへのインストールになります。手動利用ではリポジトリをcloneし、必要なスキルのディレクトリをAgentのスキルディレクトリへリンクします。生成処理は、対象内容・パラメーター等をファイルでプレビューし、明示的に確認してから実行する手順です。

## 最短手順

- READMEの例では、まず `$short-drama` でプロジェクトを初期化し、`$short-drama-write` で第1話を書き、`$short-drama-assets`、`$short-drama-storyboard`、`$short-drama-video-prompts` などで素材や提示詞を準備します。生成は `$short-drama-produce` でプレビュー後に確認し、素材ができたら `$short-drama-edit` で編集します。

## 変更履歴

- 2026-11-14: 初回登録
