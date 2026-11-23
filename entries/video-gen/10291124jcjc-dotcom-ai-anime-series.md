---
name: "AI アニメ単元劇（AI Anime Series）"
genre: "video-gen"
url: "https://github.com/10291124jcjc-dotcom/ai-anime-series"
repo: "10291124jcjc-dotcom/ai-anime-series"
flags: ["unverified"]
risk_notes: "ライセンス欄のAPI取得値はunknown。READMEはscripts/をMIT、その他をCC BY-NC 4.0と記載しているため、利用対象のファイルごとにLICENSEを確認すること。 GitHub APIでライセンスを確認できていません。"
stars: 393
forks: 82
open_issues: 0
size_kb: 8229
language: "Python"
created: "2026-10-28"
updated: "2026-10-28"
archived: false
license: "unknown"
commits_30d: 3
commits_90d: 3
commit_cadence: "monthly"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/ganfanren_ai/status/2119281509605749143"]
fetched_at: "2026-11-18T16:15:51.534734+00:00"
---

# AI アニメ単元劇（AI Anime Series）

## 出来ること

- オリジナルキャラクターの設定から、ストーリーとショット表の作成、ストーリーボード・動画用プロンプトの組み立て、動画の確認・部分差し替え・連結までの制作フローを案内する。READMEによると、付属スクリプトでプロンプト生成、動画のフレーム抽出、グリッド画像作成、動画連結などができる。

## 目的・背景

- 固定した複数のキャラクターを使い、各話のテーマから継続的なAIアニメシリーズを制作するためのリポジトリ。READMEには、30秒・台詞なしの動画例と、キャラクター設定、ストーリーボード、プロンプト、完成動画が掲載されている。

## 依存関係

- README記載の制作手順では、即夢のキャンバスとSeedance 2.5を使用する。海外向けの代替としてDreaminaが案内されている。付属スクリプトにはPillowとffmpegが必要。Claude Skillとして使う手順もある。

## 実行条件

- スクリプト実行にはPython 3.9以上、ffmpeg、Pillow（`pip install pillow`）が必要。動画生成にはREADME記載の即夢会員とキャンバス・Seedance 2.5が必要。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- READMEの案内に従い、リポジトリを`~/.claude/skills/ai-anime-series`へcloneしてClaude Codeに導入する。テーマを指定して話の案を作り、キャラクター設定・ストーリーボード・動画プロンプトを用意する。動画生成は即夢キャンバスで行い、付属スクリプトでフレーム確認や連結を行う。スクリプトだけ使う場合は、まず`python scripts/setup_check.py my-series ep01`を実行する。

## 変更履歴

- 2026-11-23: 初回登録
