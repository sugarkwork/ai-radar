---
repo: "browser-use/video-use"
name: "video-use"
genre: "video-gen"
url: "https://github.com/browser-use/video-use"
stars: 30840
forks: 3574
open_issues: 164
size_kb: 923
language: "Python"
created: "2026-04-12"
updated: "2026-10-08"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 5
commit_cadence: "monthly"
flags: ["unverified"]
risk_notes: "最新リリース、ElevenLabsと利用エージェントの料金・契約条件は未確認。トークン比較は作者の試算で、入力削減量、カット品質、ノイズ低減、再レンダリングの検出精度は独立に実測していない。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/opensourcelab9/status/2117383755581346183"]
fetched_at: "2026-11-10T08:48:11Z"
---

# video-use — コーディングエージェントで素材動画を編集するスキル

## 出来ること

- 素材を棚卸しして編集案を提示し、承認後に言いよどみや無音を詰めて edit/final.mp4 に書き出す。字幕を焼き込めるほか、作業記録を project.md に残す。
- 作者の説明では、カットに30 msの音声フェードを適用し、出力のカット境界を点検して問題があれば最大3回再レンダリングする。

## 目的・背景

- 単語単位の時刻付き文字起こしを編集判断の主入力にし、必要な区間だけフレーム列・波形・単語ラベルをまとめた画像を参照する。作者のREADMEでは、3万フレームを各1,500トークンとして入力する想定と、約12 KBの文字と少数の画像を使う構成を比較している。

## 依存関係

- Pythonの依存関係を uv または pip で導入し、ffmpeg と ffprobe を PATH に置く。文字起こしには ElevenLabs Scribe のAPIキーが必要。リポジトリのライセンスはMIT。

## 実行条件

- シェルを使えるClaude Codeなどのエージェントでスキルを読み込む。Scribeによる文字起こしでは、素材から抽出した音声をElevenLabsへ送信する。

## 最短手順

- Claude Codeで公式READMEのセットアップ手順に沿って video-use スキルを登録し、FFmpeg、Python依存関係、ElevenLabs APIキーを設定する。
- 素材フォルダを作業ディレクトリにしてClaude Codeを起動し、素材をローンチ動画に編集するよう依頼する。提示された編集案を承認し、edit/final.mp4 を確認する。

## 変更履歴

- 2026-11-10: 初回登録
