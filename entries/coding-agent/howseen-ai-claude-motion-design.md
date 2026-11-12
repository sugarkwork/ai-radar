---
name: "claude-motion-design"
genre: "coding-agent"
url: "https://github.com/howseen-ai/claude-motion-design"
repo: "howseen-ai/claude-motion-design"
license: "MIT"
stars: 811
language: "Python"
created: "2026-09-27"
updated: "2026-10-04"
forks: 105
open_issues: 2
commits_30d: 0
commit_cadence: "monthly"
commits_90d: 32
size_kb: 4219
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-12"
first_seen: "2026-11-12"
sources: ["https://x.com/PromptLabCN/status/2120750742785171596"]
fetched_at: "2026-11-12T06:11:47.616288+00:00"
---

# claude-motion-design

## 出来ること

- Claude Code向けスキルとして、HTMLとPlaywrightで映像フレームを生成し、ffmpegでエンコードする手順を案内する。READMEは、映像を時間tから決まるseek(t)関数で描画し、サブフレームを合成してモーションブラーを加え、ビートマップに沿ってシーンや効果音を配置する構成を説明している。

## 目的・背景

- READMEは、映像全体をコードで管理することで、同じ入力から同じフレームを再生成し、シーン単位で変更できる設計を掲げる。編集アプリや有料ライセンスに依存しない制作方法を目的としている。

## 依存関係

- README記載の環境はChromium、ffmpeg、Python。Python依存パッケージはplaywright、imageio-ffmpeg、numpy、pillow。ChromiumはPlaywright経由で導入する。

## 実行条件

- Claude Codeへskill/motion-designを配置し、Python依存パッケージとPlaywright用Chromiumを導入する。READMEの例では、素材取得スクリプトが音楽・効果音・ロゴ・フォントをダウンロードする。素材は同梱・再配布されず、それぞれのライセンスに従う。

## 最短手順

- READMEの手順は、skill/motion-designを~/.claude/skills/へコピーし、playwright、imageio-ffmpeg、numpy、pillowをpipで導入してChromiumをインストールする。Claude Codeで動画を依頼するか/motion-designを実行する。サンプルではexamples/howseen-launchで素材取得、HTTPサーバー起動、render.pyによる静止画確認と全編レンダリング、audio.pyによる音声生成を行い、最後にffmpegで映像と音声をmuxする。コードの実行や素材のダウンロードは今回行っていない。

## 変更履歴

- 2026-11-12: 初回登録
