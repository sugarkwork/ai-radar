---
name: "剪坊"
genre: "other"
url: "https://github.com/tuyetloanpham08-png/jianfang"
repo: "tuyetloanpham08-png/jianfang"
license: "unknown"
stars: 7
language: "Swift"
created: "2026-10-20"
updated: "2026-10-20"
forks: 1
open_issues: 0
commits_30d: 2
commit_cadence: "monthly"
commits_90d: 2
size_kb: 133
archived: false
flags: ["unverified"]
risk_notes: "Apple Silicon MacとmacOS 26以降が必要。プレビュー版はApple Developer ID署名・公証がなく、初回起動時にmacOSの許可操作が必要な場合がある。READMEではIntel Macで未検証とされる。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/TuyetloanP81840/status/2118592167165960208"]
fetched_at: "2026-11-11T07:05:39.215402+00:00"
---

# 剪坊

## 出来ること

- READMEによると、剪坊はローカルで動作するmacOS動画編集アプリ。素材の取り込み、最大2本の動画トラックと4本の音声トラックでのタイムライン編集、字幕の追加・編集とSRTの読み書き、配楽の音量調整・フェード、プロジェクト保存・復元、H.264/AAC MP4のプレビューと書き出しに対応する。対応素材はSDR H.264 MP4/MOV、PNG/JPEG、WAV/AAC。

## 目的・背景

- READMEでは、ログイン・サブスクリプション不要で、素材をアップロードせずにローカル編集できるアプリと説明されている。公開プレビュー版は0.2.2。

## 依存関係

- 配布AppはmacOSのシステムフレームワークのみを使用し、他の動画編集ソフトやFFmpegは不要。ソースからビルドする場合はmacOS 26以降、Xcode（macOS 26以降のSDKを含む）、Swift 6、Gitが必要。Python 3とlibx264・libx265を含むFFmpegは開発用のデモ・テスト素材生成にのみ使うとREADMEに記載されている。

## 実行条件

- Apple Silicon MacとmacOS 26以降が必要。配布ZIPはarm64で、Intel Macは未検証。プレビュー版はApple Developer ID署名とApple公証がなく、ad-hoc署名のためmacOSで初回起動の許可が必要な場合がある。

## 最短手順

- READMEの手順は、Releasesから Jianfang-0.2.2-macOS.zip を取得（ソースコードのアーカイブではない方）、展開して剪坊.appを「アプリケーション」へ移動し、起動して新規の横版・縦版プロジェクトを作成するか既存プロジェクトを開く。初回起動時にブロックされた場合は、README記載のmacOS「プライバシーとセキュリティ」設定で確認して許可する。

## 変更履歴

- 2026-11-11: 初回登録
