---
name: "su-card-to-video"
genre: "video-gen"
url: "https://github.com/doublesq97-ui/su-card-to-video"
repo: "doublesq97-ui/su-card-to-video"
license: "MIT"
stars: 17
language: "Shell"
created: "2026-06-25"
updated: "2026-07-28"
forks: 3
open_issues: 0
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 1202
archived: false
flags: ["unverified"]
risk_notes: "READMEには、HyperFrames/GSAPなど複数のレンダリング方法が挙げられているが、各方法の具体的な対応条件は明記されていない。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/Sukiea1008/status/2122512547438096467"]
fetched_at: "2026-11-17T06:23:21.679357+00:00"
---

# su-card-to-video

## 出来ること

- HTML/CSSで16:9の図カードを作成し、HyperFrames/GSAPまたは他のWebレンダリング方式で簡単な動きを付け、FFmpegで映像と音声を合成してMP4動画を作成する。音声ファイルがない場合は無音の仮音声で手順を試せる。

## 目的・背景

- 顔出しや手作業の編集をせずに、文案・字幕・知識点を図カード形式の動画にするための最小AI動画テンプレート。Codexや他のAgentに渡して再利用できるローカルワークフローとして説明されている。

## 依存関係

- README記載の事前準備はNode.js 22以上、FFmpeg、HyperFrames。HyperFramesはグローバルインストールまたはnpxで利用する方法が示されている。

## 実行条件

- リポジトリのルートでnpm install、npm run doctor、npm run renderを実行する手順。用意した音声を使う場合はnpm run render -- ./my-voice.mp3を実行する。出力先はexamples/basic-16x9/output/final.mp4。READMEはmacOS向けのNode.jsとFFmpegのインストール例を示している。

## 最短手順

- リポジトリ全体をCodexに渡すか、リポジトリのルートでskill/SKILL.mdを読ませる。README記載の手順で依存ソフトを用意し、npm install、npm run doctor、npm run renderを実行する。音声を使う場合はnpm run render -- ./path/to/audio.mp3を指定する。

## 変更履歴

- 2026-11-22: 初回登録
