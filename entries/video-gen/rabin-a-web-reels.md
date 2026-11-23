---
name: "web-reels"
genre: "video-gen"
url: "https://github.com/rabin-a/web-reels"
repo: "rabin-a/web-reels"
license: "unknown"
stars: 0
language: "JavaScript"
created: "2026-11-07"
updated: "2026-11-08"
forks: 0
open_issues: 0
commits_30d: 5
commit_cadence: "weekly"
commits_90d: 5
size_kb: 208
archived: false
flags: ["unverified"]
risk_notes: "ElevenLabsの音声利用にはAPIキーが必要で、有料とREADMEに記載。API料金の詳細は不明。ライセンス欄はGitHub APIでunknownだが、READMEはMITと記載している。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/progrrammer/status/2119193502802444758"]
fetched_at: "2026-11-18T04:18:13.736630+00:00"
---

# web-reels

## 出来ること

- 実際のWebサイト画面をスマートフォン枠内に表示し、ズームや強調表示、タップを加えた短尺プロモーション動画を作成する。字幕、AI音声、効果音、任意のBGM、エンドカードを組み合わせ、9:16・4:5・1:1・16:9形式の動画とカバー画像を出力する。投稿用テキストも生成し、画面上の数値をサイトの引用と照合する仕組みがREADMEに記載されている。

## 目的・背景

- 事業者のWebサイトを紹介するTikTok、Instagram Reels、YouTube Shorts、Facebook向けの動画シリーズを作成するClaude Codeスキル。READMEによると、ページの閲覧、タップ、スクロールのみを行い、文字入力、フォーム送信、ログイン、投稿はしない。

## 依存関係

- Node.js 18.17以降、エンジンフォルダーへのplaywright-coreのインストール、Chrome系ブラウザー、ffmpeg、ffprobe、Python 3（標準ライブラリのみ）が必要。実音声には任意のELEVENLABS_API_KEYが必要で、未設定時は無音のプレースホルダー音声を使える。

## 実行条件

- ブラウザーはChrome、Chromium、Edge、Braveに対応し、別のブラウザーを使う場合はCHROME_PATHを設定する。コマンドはbrand/brand.jsonを含むプロジェクトフォルダーから実行する。

## 最短手順

- Claude Codeで `/plugin marketplace add rabin-a/web-reels`、続いて `/plugin install web-reels@web-reels` を実行する。導入後、例として `Make a reel series for https://my-bakery.example` のように依頼する。環境確認には `node <plugin>/skills/web-reels/engine/cli.mjs doctor` を使う。

## 変更履歴

- 2026-11-23: 初回登録
