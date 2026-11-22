---
name: "Pixelbolt"
genre: "coding-agent"
url: "https://github.com/skulitom/Pixelbolt"
repo: "skulitom/Pixelbolt"
license: "MIT"
stars: 113
language: "JavaScript"
created: "2026-09-27"
updated: "2026-11-17"
forks: 9
open_issues: 0
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 32685
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/dextune/status/2119188149075431723"]
fetched_at: "2026-11-17T09:10:40.402434+00:00"
---

# Pixelbolt

## 出来ること

- 編集可能なJSONレシピから、ピクセルアートのスプライト、タイル、アイコン、エフェクト、短いアニメーションを生成できます。PNGスプライトシート、テクスチャアトラス、APNG、GIF、動画編集ソフト用フレームとして出力でき、CLIまたはローカルMCPサーバー経由でエージェントから操作できます。ローカルブラウザスタジオで同じレシピを開き、再生・編集できます。READMEによると、炎・煙・水などの流体エフェクトはCPU上でシミュレーションし、各フレームを編集可能なパレットピクセルとして出力します。これはREADMEに記載された機能説明で、独立した実機検証ではありません。

## 目的・背景

- ゲーム開発者、ゲームジャムチーム、Web・動画制作者、および再現可能な画像を必要とするエージェント開発者向けです。小さな2Dゲーム素材をテキストとして編集可能な状態に保ち、エージェントがピクセルやフレーム単位で修正できる用途を想定しています。READMEは、写真・絵画調画像、画像モデルによる生成、GIFやAsepriteファイルの編集には向かないと説明しています。

## 依存関係

- README記載の基本利用条件はNode.js 20以降です。skills CLIを使う場合はNode.js 22.20以降が必要です。READMEは基本利用について、ほかにインストールするものやAPIキー、ネットワークサービスは不要と説明しています。

## 実行条件

- ソースから試す手順は、README記載のとおり `git clone https://github.com/skulitom/Pixelbolt.git`、`cd Pixelbolt`、`node bin/pixelbolt.js preview --open` です。Claude Code向けスキルは `npx -y pixelbolt@latest skill install` で導入できます。アニメーションは最大256×256ピクセル、プロジェクト全体で最大256フレームかつ4,194,304ピクセルです。単一静止画は総ピクセル上限内で各辺最大4096ピクセルとされ、PNGインポートは各チャンネル最大8ビットです。

## 最短手順

- Node.js 20以降がある環境で、README記載のCLI手順として `git clone https://github.com/skulitom/Pixelbolt.git`、`cd Pixelbolt`、`node bin/pixelbolt.js preview --open` を実行します。Claude Code向けスキルを使う場合は `npx -y pixelbolt@latest skill install` を実行します。

## 変更履歴

- 2026-11-22: 初回登録
