---
name: "15 Motion Design Styles"
genre: "prompt-design"
url: "https://github.com/Vincentwei1021/mg-styles-15"
repo: "Vincentwei1021/mg-styles-15"
license: "MIT"
stars: 3717
language: "Python"
created: "2026-10-02"
updated: "2026-11-19"
forks: 464
open_issues: 2
commits_30d: 19
commit_cadence: "weekly"
commits_90d: 27
size_kb: 568393
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/flxrnc/status/2123392905934999811"]
fetched_at: "2026-11-20T03:12:59.104192+00:00"
---

# 15 Motion Design Styles

## 出来ること

- 15種類のモーションデザインの作例を閲覧し、各作品のスタイル説明、完全なプロンプト、ソースコードを参照できる。READMEによると、映像はSVG、Canvas、WebGL、Three.jsなどのコードで描画し、3D作品にはBlenderを使用。音楽と効果音も各作品のaudio.pyで合成する。

## 目的・背景

- プロンプトからコードで制作した15本の10秒作品を、スタイルの参考や自作の手がかりとして公開している。作者は各作品について、2回のレビューと修正を行ったと説明している。

## 依存関係

- READMEに記載された制作工程では、フレーム取得にheadless Chrome、映像と音声の結合にffmpegを使用する。3D作品の映像はBlenderでレンダリングする。個々の作品を実行する際の依存関係はREADME抜粋からは特定できない。

## 実行条件

- 閲覧はGitHub Pagesの作品ページから可能。READMEが説明するレンダリング工程では、各作品のWebページが任意時刻のフレームを描画し、headless Chromeでフレームを取得してffmpegでMP4にまとめる。3D作品ではBlenderを使用する。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- READMEの作品一覧から気になるスタイルのPromptとSourceを開き、プロンプト、ソース、完成映像を見比べる。全15作品の映像はREADME記載のGitHub Pagesから閲覧できる。

## 変更履歴

- 2026-11-23: 初回登録
