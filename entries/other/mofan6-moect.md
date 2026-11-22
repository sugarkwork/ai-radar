---
name: "Moect"
genre: "other"
url: "https://github.com/mofan6/Moect"
repo: "mofan6/Moect"
license: "GPL-3.0"
stars: 770
language: "Python"
created: "2026-10-31"
updated: "2026-11-14"
forks: 177
open_issues: 5
commits_30d: 33
commit_cadence: "daily"
commits_90d: 33
size_kb: 26895
archived: false
flags: ["unverified"]
risk_notes: "対応対象は Windows 微信 4.x だが、READMEではすべての4.xバージョンへの対応を保証していない。メディア保存はローカルキャッシュ、利用可能な認証情報、元ファイルに依存する。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/Ryrenz/status/2119233908625518683"]
fetched_at: "2026-11-17T19:13:02.988532+00:00"
---

# Moect

## 出来ること

- Windows上で微信の好友・群聊、朋友圈、收藏表情、微信收藏を整理してエクスポートする。HTML、JSON、JSONL、TXT、CSV、Markdown、Excel形式に対応し、HTMLはオフラインで閲覧・検索・時間指定ができる。ZIPとAES-256による暗号化も選べる。READMEによると、メディアの保存可否はローカルキャッシュ、利用可能な認証情報、元ファイルに左右され、取得できない添付は状態が表示される。

## 目的・背景

- 会話、朋友圈、表情などを自分のPCに保存し、オフラインで閲覧・検索できるようにするWindowsデスクトップツール。READMEでは、チャットデータベースとメッセージ解析はローカルで行い、チャット記録を受け取るサーバーはないと説明している。

## 依存関係

- 開発・構築にはPython 3.11、pywebview / WebView2、React / TypeScriptを使用する。インストール版にはPythonとフロントエンドが含まれる。

## 実行条件

- Windows 10 version 1809以降またはWindows 11のx64環境と、Microsoft Edge WebView2 Runtimeが必要。対象はWindows 微信 4.xだが、すべての4.xバージョンへの対応は保証されていない。インストーラーでWebView2 Runtimeが不足している場合、自動準備にネット接続が必要。

## 最短手順

- README記載の一鍵インストールパッケージを取得してインストールする。PC版微信にログインしてMoectを起動し、「连接微信」を選ぶ。既存の復号済みバックアップを開く方法、またはデモデータで試す方法もある。会話を選んで形式や時間範囲などを指定し、エクスポートタスクを作成する。朋友圈は微信で対象の投稿を手動で閲覧してから、Moectでリソーススナップショットを更新する。

## 変更履歴

- 2026-11-22: 初回登録
