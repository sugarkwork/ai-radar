---
repo: "wj-sidiss/otopilot"
name: "Otopilot"
genre: "video-gen"
url: "https://github.com/wj-sidiss/otopilot"
last_release: "v1.9.4"
flags: ["unverified"]
risk_notes: "機能は公式READMEとリリースノートで確認した。動画の生成、品質、処理時間、素材サービスの稼働、ライセンスフィルターの判定精度は実測していない。READMEはGitHubのraw配信で確認した。公開リリースページで最新版のタグを確認したが、公開日時の年とタイムゾーンは確認できていない。"
stars: 230
forks: 42
open_issues: 9
size_kb: 19685
language: "JavaScript"
created: "2026-10-14"
updated: "2026-11-08"
archived: false
license: "MIT"
commits_30d: 63
commits_90d: 63
commit_cadence: "daily"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/Ryrenz/status/2117982457303585119"]
fetched_at: "2026-11-10T11:18:09Z"
---

# Otopilot — 台本から字幕・サムネイル付き動画を組み立てるローカル制作ツール

## 出来ること

- 台本に沿って素材を探し、音声と字幕を組み合わせてMP4、SRT、JPGサムネイル、YouTube用の投稿資料を生成する。YouTubeへの投稿は手動。

## 目的・背景

- 台本の段落をシーンに対応させ、各段落の読み上げ区間に合わせて映像を組み立てる。READMEによると、素材検索でNC・ND付き画像を除外し、該当素材のクレジットを出力する。コードはMITで、素材・音声・音楽にはそれぞれの利用条件が適用される。

## 依存関係

- Node.js 22以上、npm、ffmpeg/ffprobe。パネル内で台本を自動生成するにはClaudeまたはvidIQのキーが必要。台本を持ち込めば、Wikimediaなどのキー不要の素材ソースと音声合成で進められる。Piperはローカル実行用のモデル設定が必要で、Azure Speechにはキーが必要。

## 実行条件

- パネルはlocalhost:4173で動く。キー不要の構成でもオンライン素材の取得には通信が必要。非公式のEdge音声が使えない場合はOS音声に切り替えられる。READMEではmacOSとLinuxを実験的対応としている。vidIQのAIクリップ生成やfal.aiのリップシンクは有料オプション。

## 最短手順

- リポジトリのディレクトリで `npm ci --ignore-scripts`、`node ff-yol.js`、`node panel.js` の順に実行し、ローカルパネルへ台本を貼り付けて生成する。
- AIから使う場合は、リポジトリを作業フォルダーにしてClaude CodeまたはCodexを起動し、題材、動画の尺、出力形式を指定して制作を依頼する。

## 変更履歴

- 2026-11-10: 初回登録
