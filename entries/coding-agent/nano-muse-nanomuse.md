---
type: "repo"
repo: "nano-muse/nanoMuse"
name: "nanoMuse — 自分のデバイスで動くオープンソースパーソナルエージェント"
genre: "coding-agent"
url: "https://github.com/nano-muse/nanoMuse"
author: "nano-muse"
license: "GPL-3.0"
language: "Swift"
stars: 3358
forks: 402
open_issues: 149
created: "2026-09-23"
updated: "2026-11-09"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
size_kb: 120903
archived: false
risk_notes: "Meta Platformsとは無関係の独立コミュニティプロジェクト。MuseはMetaの商標。中国大陸の携帯番号登録が必要な場合がある。デスクトップ版は未公証・未署名。当方未インストール。 当方でインストール・動作・性能の実行検証はしていない。"
sources: ["https://x.com/wmoto_ai/status/2119285380898050372", "https://github.com/nano-muse/nanoMuse", "https://github.com/nano-muse/nanoMuse/blob/main/README.md", "https://github.com/nano-muse/nanoMuse/blob/main/LICENSE"]
added: "2026-11-09"
first_seen: "2026-11-09"
source_post: "https://x.com/wmoto_ai/status/2119285380898050372"
fetched_at: "2026-11-09T21:36:30Z"
flags: ["unverified"]
last_release: "v1.0.9"
last_release_at: "2026-10-29"
---

# nanoMuse — 自分のデバイスで動くオープンソースパーソナルエージェント

## 出来ること

Linuxシェル、ブラウザ、MCPサーバー・スキル、スマホアプリやPC画面の操作（APIがないものも画面越しに）。削除・送信・支払い前に確認を求める。パスワードやCAPTCHAはユーザーに委ね、Doneで再開。

## 目的・背景

Meta Muse風のパーソナルエージェントを、クラウドに依存せず自分のデバイスで動かす。オープンソース・低コスト・自分でホスト可能。

## 依存関係

Android: OpenMinis 1.13 + proot + Alpine Linux。Desktop: DeepSeek Harnessプラグイン。Phone operator: MobileGym/MemGUI-Bench/PhoneHarness/Open-AutoGLM/ClawGUI等の思想を参考。

## 実行条件

Android 8.0+ arm64、iPhone/iPad（TestFlight）、macOS 12+（Apple Silicon/Intel）、Windows 10+、Linux x64（AppImage/.deb/.tar.gz）、Docker、Webブラウザ（デモ）。アカウントはメールまたは中国大陸の携帯番号で登録。

## 最短手順

GitHub ReleasesからOS別インストーラーを取得。初回サインイン後、コミュニティリレーの無料枠が使える（開発者負担）。なくなったらown-keyへ。自分のサーバーでリレーをhostすることも可能。

## 注意点

Meta Platformsとは無関係の独立コミュニティプロジェクト。MuseはMetaの商標。中国大陸の携帯番号登録が必要な場合がある。デスクトップ版は未公証・未署名。当方未インストール。

## 変更履歴

- 2026-11-09: 初回収録。公式資料を確認し、未実行の範囲を明記。
