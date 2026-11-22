---
name: "simcraft"
genre: "coding-agent"
url: "https://github.com/dotslashsimran/simcraft"
repo: "dotslashsimran/simcraft"
license: "MIT"
stars: 470
language: "Python"
created: "2026-11-05"
updated: "2026-11-09"
forks: 36
open_issues: 0
commits_30d: 3
commit_cadence: "monthly"
commits_90d: 3
size_kb: 9568
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/GitTrend0x/status/2121566394286248121"]
fetched_at: "2026-11-16T21:43:58Z"
last_release: ""
last_release_at: ""
---

# simcraft

## 出来ること

- Claude Codeが依頼内容に応じて読み込む24個のスキルを提供する。READMEには、動画制作、コーディング、学習、デザイン、計画のスキルが掲載されている。各スキルは手法、判断基準、スクリプトをまとめたフォルダーで構成される。

## 目的・背景

- チュートリアルで省かれがちな実務上の判断や確認方法を含め、作業ごとの手順を再利用できる形で提供する。READMEによると各スキルは、起こりうる問題、結果の確認方法、十分な品質の見極め方を扱う。

## 依存関係

- README記載の要件はPython 3.9以降。ブラウザー操作または動画レンダリングを行うスキルではNode 18以降、ffmpegを使う場合はPATH上のffmpegまたはFFMPEG環境変数の設定が必要。画像生成スキルのみAPIキーを使用し、環境変数または`~/.config/simcraft/keys.env`から読み込む。

## 実行条件

- Claude Codeで利用する。READMEは、リポジトリを配置し、各スキルのフォルダーを`~/.claude/skills`にリンクしてからClaude Codeを開く手順を示している。一部スキルには個別のセットアップスクリプトがあると記載されている。

## 最短手順

- README記載の手順は、リポジトリをcloneし、`~/.claude/skills`を作成し、`skills/*/*/`内の各フォルダーを同ディレクトリへリンクする。その後、リポジトリ内で`npm i`を実行し、Claude Codeで作業を依頼する。単一スキルだけを使う場合は、そのフォルダーだけをリンクする。

## 変更履歴

- 2026-11-14: 初回登録
