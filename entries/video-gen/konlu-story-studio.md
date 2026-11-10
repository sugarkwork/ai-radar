---
repo: "konlu/story-studio"
name: "Story Studio（故事工坊）"
genre: "video-gen"
url: "https://github.com/konlu/story-studio"
license: "unknown"
stars: 842
language: "Python"
created: "2026-10-26"
updated: "2026-11-03"
forks: 182
open_issues: 0
commits_30d: 3
commit_cadence: "monthly"
commits_90d: 3
size_kb: 43077
archived: false
flags: ["unverified"]
risk_notes: "公開文書を確認。依存関係の自動セットアップ、文字起こしと分鏡の整合精度、剪映のバージョン別互換性、最新リリースは未検証。README はコードと Skill 仕様に MIT を明記する一方、GitHub API の計測値は unknown。収録台本・参考画像の個別の再利用条件は未確認。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/ganfanren_ai/status/2117245468526944568"]
fetched_at: "2026-11-10T08:28:58+00:00"
---

# Story Studio（故事工坊）｜口播台本から剪映の編集用草稿まで

## 出来ること

- 歴史・人物紹介の題材選び、冒頭のフック、口播台本、分鏡と配図、剪映専門版の草稿作成を工程単位で依頼できる。
- README によると、録音済み MP3 から字幕用の時刻情報を取得し、画像と音声をタイムラインに並べ、ズームのキーフレームを入れた編集用草稿を生成する。字幕の画面表示は依頼時に指定できる。

## 目的・背景

- 台本作成、音声、分鏡、編集を一つの Skill でつなぎ、既存素材がある工程から再開できる。付属台本は構成や語り口の参照用で、史実の根拠は別途確認する。

## 依存関係

- メディア工程では uv 管理の Python 3.11、Node.js 20+ LTS、Coli（sherpa-onnx）、FFmpeg・ffprobe、pyJianYingDraft を使用する。

## 実行条件

- Codex や Claude Code など、Skill 対応のホストが必要。テキストのみの台本作成にはメディア依存関係の導入は不要と README に記載されている。草稿の編集にはデスクトップ版の剪映専門版を使う。
- README では Skill 自体は無料。豆包 TTS を使う場合はサービスの認証情報が必要で、音声合成やホストの画像生成には利用先の API 料金が発生する場合がある。

## 最短手順

- 対象リポジトリを Codex の Skill ディレクトリ（例 `~/.codex/skills/story-studio`）に配置する。
- Codex で『`$story-studio` を使って、歴史人物を紹介する中国語の口播台本と冒頭フック案だけを書いて』と依頼する。草稿から試す場合は録音済み MP3 と画像のフォルダを指定し、剪映草稿の作成だけを依頼する。

## 変更履歴

- 2026-11-10: 初回登録
