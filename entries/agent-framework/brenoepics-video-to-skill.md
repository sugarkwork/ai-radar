---
repo: brenoepics/video-to-skill
name: video-to-skill
genre: agent-framework
url: https://github.com/brenoepics/video-to-skill
license: MIT
language: Rust
created: 2026-08-05
updated: 2026-11-04
added: 2026-11-04
first_seen: 2026-11-04
sources:
  - https://x.com/studio_yebisu/status/2117472457628291124
  - https://x.com/AI_Caffeine/status/2117511846236135490
flags: []
risk_notes: "画面録画をAIモデルに送る構成。社内動画や機密情報を含む場合は送信内容の確認が必要（投稿者も同様の注意をしている）。"
stars: 164
forks: 14
open_issues: 7
commits_30d: 100
commits_90d: 100
commit_cadence: daily
size_kb: 1761
archived: false
fetched_at: "2026-11-04T01:11:16Z"
last_release: v0.3.0
last_release_at: 2026-11-02
---

# video-to-skill

## 出来ること

- チュートリアル動画（YouTube のURL、またはローカルの動画ファイル）を、コーディングエージェントが繰り返し使える**手順書（Skill）**に変換する。
- 音声の文字起こしではなく**画面**を読む方式。画面に出ているコマンド、パラメータ、数式を拾い、各ステップにタイムスタンプとスクリーンショットを付ける。
- 生成した手順を**独立したエージェントが隔離環境で実行して検証**する。
- ローカルで動く（Rust 実装）。Claude Code / Codex / Cursor などのコーディングエージェントから使う。

## 目的・背景

2026-08 公開、v0.3.0。ソフトの設定手順や CLI の使い方は文章より動画の方が充実していることが多いが、動画はエージェントが直接読めない。画面を読んで手順化し、実行検証まで回すことで「動画を見た後の作業」を自動化する。日本語圏では「Codex の Record & Replay との違いは、既存のYouTube教材も入力にできる点」として紹介された。

## 依存関係

- Rust バイナリ（Releases）またはビルド環境
- 画面解析に使うマルチモーダルモデル（API キー）
- 対応エージェント（Claude Code / Codex / Cursor など）

## 実行条件

- 動画の画面をモデルに送るため、**機密情報を含む録画は送信内容の確認が必要**。
- 長い動画は処理時間とトークン消費が増える。
- 検証ステップは隔離環境で実行される（サンドボックス要件は未確認）。

## 最短手順

```text
Releases からバイナリを取得、または README の手順でビルド
動画URL またはファイルを渡して Skill を生成
```

## 変更履歴

- 2026-11-04: 初回登録（★163 / v0.3.0 / MIT / 30日100+コミット）
