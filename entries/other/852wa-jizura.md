---
name: "JIZURA 字面"
genre: "other"
url: "https://github.com/852wa/JIZURA"
repo: "852wa/JIZURA"
stars: 2232
forks: 295
open_issues: 3
size_kb: 64467
language: "HTML"
created: "2026-09-23"
updated: "2026-11-10"
archived: false
license: "MIT"
commits_30d: 9
commits_90d: 76
commit_cadence: "weekly"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/8co28/status/2120104769218056643"]
fetched_at: "2026-11-11T04:11:04.652121+00:00"
---

# JIZURA 字面

## 出来ること

- 歌詞をもとに、レイアウト・動き・装飾などを組み合わせて文字PVを構成し、ブラウザでプレビューできます。MP4、連番PNG、透過PNG、After Effectsで編集できる構成データ（JSON）を書き出せます。READMEでは、歌詞・曲・書き出しはブラウザ内で処理され、サーバーには送信されないと説明されています。

## 目的・背景

- 文字PV（リリックモーション）の表現を組み合わせて、カットを自動構成するブラウザアプリです。READMEによると、表現は1,715の部品と27のスタイルで構成され、シードを変えると別の構成を生成できます。

## 依存関係

- READMEに記載されたブラウザ版の動作環境は、MP4書き出しにWebCodecs対応ブラウザ（Chrome / Edge推奨）。フォントは使用する書体をGoogle Fontsから読み込み、オフライン時はPCのフォントで代用します。

## 実行条件

- GitHub Pages上で使えるほか、READMEでは`index.html`をダウンロードしてローカルで開く方法も案内されています。MP4書き出しに対応しない環境でも、プレビューと連番PNG書き出しを利用できます。

## 最短手順

- ブラウザでアプリを開き、歌詞を入力して必要に応じて曲を読み込みます。「おまかせで作る」で構成を生成し、プレビュー後にMP4またはPNG形式で書き出します。タイミングは曲の拍検出または手動同期で調整できます。

## 変更履歴

- 2026-11-11: 初回登録
