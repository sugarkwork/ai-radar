---
type: "repo"
repo: "sp-yduck/overlaysubs"
name: "OverlaySubs — PC音声のリアルタイム翻訳オーバーレイ字幕"
genre: "productivity"
url: "https://github.com/sp-yduck/overlaysubs"
author: "sp-yduck"
license: "MIT"
language: "Rust"
stars: 51
forks: 5
open_issues: 1
created: "2026-11-05"
updated: "2026-11-09"
commits_30d: 60
commits_90d: 60
commit_cadence: "daily"
size_kb: 2259
archived: false
risk_notes: "コードはMIT。アプリ利用はOverlaySubs利用規約に従う。PLaMo 3 Translateの利用はPLaMoコミュニティライセンスに従う。ビルドはコード署名なし（SmartScreen/Gatekeeper警告あり）。自動アップデートなし。起動時にGitHub Releases APIへ匿名で最新版確認（1回のみ、失敗時無視）。当方未インストール。 当方でインストール・動作・性能の実行検証はしていない。"
sources: ["https://x.com/sp_yduck/status/2119258606004801707", "https://github.com/sp-yduck/overlaysubs", "https://github.com/sp-yduck/overlaysubs/blob/main/README.md", "https://github.com/sp-yduck/overlaysubs/blob/main/LICENSE"]
added: "2026-11-09"
first_seen: "2026-11-09"
source_post: "https://x.com/sp_yduck/status/2119258606004801707"
fetched_at: "2026-11-09T21:41:38Z"
flags: ["unverified"]
last_release: "v0.5.0"
last_release_at: "2026-11-09"
---

# OverlaySubs — PC音声のリアルタイム翻訳オーバーレイ字幕

## 出来ること

PCで再生中の音声（WASAPIループバック/macOS ScreenCaptureKit）またはマイクをリアルタイムで文字起こし・翻訳し、常に最前面の半透明オーバーレイ字幕として表示。クリックスルー可能。履歴をテキスト/SRTで書き出し。

## 目的・背景

海外動画・ウェビナー・オンライン会議・ゲーム等の音声を、リアルタイムで自分の言語に変換して表示。完全ローカル処理でプライバシーを保つ。

## 依存関係

WASAPI/ScreenCaptureKit → 16kHz mono → Silero VAD → whisper.cpp → PLaMo 3 Translate（llama.cpp）→ overlay。Rust+Tauri。UIはHTML/JS/CSS。

## 実行条件

Windows 10/11 x64（Vulkan対応GPU・最新ドライバ必須）またはmacOS 13+ Apple Silicon。RAM 8GB+。GPUなしでもCPUティアで動作するが、Windowsでは旧ドライバだとGPU未使用でリアルタイム不可。モデルティア: High=VRAM 12GB+/Apple Silicon RAM 32GB+（Whisper large-v3-turbo + PLaMo 8B Q4_K_M ~6.9GB）、Mid=VRAM 8GB/Apple Silicon RAM 16GB（Whisper large-v3-turbo Q5_0 + PLaMo 2B Q4_K_M ~2.4GB）、Low=VRAM 4-6GB/Apple Silicon RAM 8GB（Whisper small + PLaMo 2B Q4_K_M ~2.3GB）、CPU=その他（Whisper base + PLaMo 0.8B Q4_K_M ~0.7GB）。

## 最短手順

GitHub ReleasesからOS別インストーラーを取得・実行。初回起動で利用規約同意→ハードウェア検査→モデル自動ダウンロード（HFから、再開・SHA-256検証付き）。グローバルホットキー（Ctrl/Cmd+Shift+T）で開始/停止。

## 注意点

コードはMIT。アプリ利用はOverlaySubs利用規約に従う。PLaMo 3 Translateの利用はPLaMoコミュニティライセンスに従う。ビルドはコード署名なし（SmartScreen/Gatekeeper警告あり）。自動アップデートなし。起動時にGitHub Releases APIへ匿名で最新版確認（1回のみ、失敗時無視）。当方未インストール。

## 変更履歴

- 2026-11-09: 初回収録。公式資料を確認し、未実行の範囲を明記。
