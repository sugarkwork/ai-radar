---
repo: "VisualxIntelligence/motion-tools-and-skills"
name: "motion-tools-and-skills"
genre: "3d-motion"
url: "https://github.com/VisualxIntelligence/motion-tools-and-skills"
license: "MIT"
stars: 9
forks: 2
open_issues: 0
size_kb: 8319
language: "JavaScript"
created: "2026-10-06"
updated: "2026-11-04"
archived: false
commits_30d: 8
commits_90d: 10
commit_cadence: "weekly"
last_release: ""
last_release_at: ""
flags: ["unverified"]
risk_notes: "スキルの動作、レンダリング品質、制作時間の短縮効果、参考動画の再現精度は未検証。個別ツールの対応バージョンと外部サービスの料金も未確認。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/CryptooGG_/status/2119312343892976064"]
fetched_at: "2026-11-10T12:08:45Z"
---

# motion-tools-and-skills — Claude Code で使うモーション制作スキルと作例集

## 出来ること

- Three.js と GSAP、HyperFrames、Remotion などを使う制作スキルや、ソース付きの映像テンプレートを再利用できる。ヘッドレスレンダリングや音と映像の同期確認を補助するツールも収録する。

## 目的・背景

- 既存のモーション制作プロジェクトから、AI エージェントに渡せる制作手順と作例を集めたリポジトリ。複製できない資料は参照先として別に整理されている。 [README](https://github.com/VisualxIntelligence/motion-tools-and-skills/blob/main/README.md)

## 依存関係

- 使用する技術はスキルごとに異なる。例えば Blender の製品映像スキルは Cycles または Octane を使い、音楽ビデオ用スキルは Fal.ai のキーを要する。

## 実行条件

- README によると、音楽ビデオ用スキルの VFX 工程は macOS 向け。リポジトリの独自文書などは MIT で、取り込んだコードや素材には上流ライセンスが適用される。利用するフォルダの LICENSE と素材の条件を確認する。 [SOURCES.md](https://github.com/VisualxIntelligence/motion-tools-and-skills/blob/main/SOURCES.md)
- 確認時点の GitHub Releases ページには公開リリースが表示されていなかった。 [Releases](https://github.com/VisualxIntelligence/motion-tools-and-skills/releases)

## 最短手順

- 用途に合うスキルを選び、フォルダの NOTES.md で依存関係を確認する。Windows ではフォルダを %USERPROFILE%\.claude\skills\ にコピーし、macOS・Linux・WSL では ~/.claude/skills/ にシンボリックリンクを作る。Claude Code に、例えば『kinetic-reel を使って、このコピーからタイポグラフィ中心の短い告知映像を作って』と依頼する。 [README の導入手順](https://github.com/VisualxIntelligence/motion-tools-and-skills#using-a-skill)

## 変更履歴

- 2026-11-10: 初回登録
