---
name: "myradio"
genre: "other"
url: "https://github.com/monoradio102/myradio"
repo: "monoradio102/myradio"
license: "unknown"
stars: 107
language: "HTML"
created: "2026-11-05"
updated: "2026-11-13"
forks: 15
open_issues: 0
commits_30d: 37
commit_cadence: "daily"
commits_90d: 37
size_kb: 23156
archived: false
flags: ["unverified"]
risk_notes: "GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/naka_1717/status/2118823104977965390"]
fetched_at: "2026-11-14T11:13:11.272114+00:00"
---

# myradio

## 出来ること

- 台本JSONと音声をリポジトリに置き、GitHub Pagesでキャラクター付きのHTML番組を公開する。音声に合わせてスライド・字幕・キャラクター・リンクカードを動かし、見出し移動、記事リンク、台本の閲覧に対応する。天気表示、SNS共有カード、埋め込み、コメント欄の機能もREADMEに記載されている。

## 目的・背景

- リポジトリを放送局として使い、キャラクターがニュースを読む番組を開設するためのテンプレート。番組内容は台本JSONで保持し、音声は直近30日分を公開する設計と説明されている。

## 依存関係

- GitHubアカウントとGitHub Pagesを使用する。各回の台本JSON、読み上げ音声MP3、キャスターの差分PNGを用意する。音声合成サービスは任意で、READMEはCOEIROINK、VOICEVOX、Kokoro、ElevenLabsなどを例示し、各音声の利用規約確認を案内している。天気表示にはOpen-Meteo、コメント欄にはgiscusを利用できる。

## 実行条件

- GitHub Pagesの公開元をgh-pagesブランチに設定する。公開時はtools/publish.shがmainの内容と直近30日分の音声からgh-pagesを作成しpushする、とREADMEに記載されている。

## 最短手順

- Use this templateで自分のリポジトリを作成し、station.jsonの局情報を設定する。character/にキャスター画像を置き、episodes/とepisodes.jsonを自分の台本に差し替え、audio/<日付>-<言語>.mp3に音声を置く。GitHub Pagesの公開元をgh-pagesに設定してtools/publish.shを実行する。

## 変更履歴

- 2026-11-14: 初回登録
