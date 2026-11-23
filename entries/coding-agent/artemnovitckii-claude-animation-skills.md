---
name: "Claude animation skills"
genre: "coding-agent"
url: "https://github.com/artemnovitckii/claude-animation-skills"
repo: "artemnovitckii/claude-animation-skills"
license: "unknown"
stars: 894
language: "JavaScript"
created: "2026-11-01"
updated: "2026-11-17"
forks: 128
open_issues: 5
commits_30d: 5
commit_cadence: "weekly"
commits_90d: 5
size_kb: 2443
archived: false
flags: ["unverified"]
risk_notes: "READMEではgit cloneの手順をエンドツーエンドでテストしたと述べているが、独立した動作確認はしていない。MITライセンスの記載はREADMEにある一方、GitHub API上のlicenseはunknown。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/ganfanren_ai/status/2119276245695516673"]
fetched_at: "2026-11-18T16:09:46.071451+00:00"
---

# Claude animation skills

## 出来ること

- Claude Codeのスキルとして、グラフ、地図ルート、分解図、ローポリやボクセルなど複数スタイルの縦型アニメーションを制作できる。短い仕様をもとにMP4（1080×1920、30 fps）とセーフエリア付きコンタクトシートを出力する手順が記載されている。解説動画向けのスキルでは、台本、ナレーション、字幕タイミング、ショットを作成してレンダリングする。

## 目的・背景

- 映像素材を用意せず、Claude Codeを使ってリール向けアニメーションを作るためのスキル集。

## 依存関係

- README記載のセットアップでは、ffmpeg、Node.js 18以降、Python 3.9以降が必要。セットアップでthree.js、Playwright、GSAPを導入し、HyperFramesを準備する。音声付きの2スキルでは、追加で約1 GBのモデルをダウンロードする。

## 実行条件

- macOSまたはLinux。Claude Code内でスキルを呼び出して使う。音声付きスキルはローカルで動作し、READMEではAPIキー不要と説明されている。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- README記載の手順: `brew install ffmpeg node`（未導入の場合）、`git clone https://github.com/artemnovitckii/claude-animation-skills.git ~/claude-animation-skills`、`cd ~/claude-animation-skills && ./install.sh`。音声付きスキルには `./install.sh --voice` を実行する。Claude Codeで `/graph ...` や `/map-route ...` などのスキルを呼び出す。

## 変更履歴

- 2026-11-23: 初回登録
