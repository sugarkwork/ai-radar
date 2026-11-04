---
repo: "blixvip/NullMotion"
name: "NullMotion"
genre: 3d-motion
url: "https://github.com/blixvip/NullMotion"
license: "MIT"
stars: 1335
language: "HTML"
created: "2026-09-18"
updated: 2026-10-31
added: "2026-11-03"
first_seen: "2026-11-03"
sources: []
flags: []
risk_notes: ""
forks: 133
open_issues: 8
commits_30d: 16
commit_cadence: weekly
size_kb: 51523
archived: false
commits_90d: 34
fetched_at: "2026-11-04T22:52:07Z"
last_release: v1.0.1
last_release_at: 2026-10-06
---

# NullMotion

## 出来ること

- 完成したモーショングラフィックス広告と、その元になったラフ草案（HyperFrames の下書き）を上下に同期再生し、「どう作られたか」をフレーム単位で追える。
- 草案のビートを `drafts.json` に記述すると、セクション分割・カット点・コンタクトシートが自動生成される。
- 分解した内容を1本の MP4 として書き出せる。
- 自前の参考映像を取り込める（取り込んだ素材はローカルに留まり、Git 管理外）。
- 3本のリファレンスを同梱しているので、クローン直後に動く。

## 目的・背景

「完成品だけ見せられても再現できない」というモーションデザインの学習障壁を、制作過程そのものを再生可能な形で残すことで下げる試み。編集ソフトの代替ではなく、参考作品の解剖ビューアに近い。

## 依存関係

- Node.js 22 以上（`npm start` でローカルサーバーが起動。npm 依存のインストールは不要）。
- MP4 書き出しは Chrome または Edge（WebCodecs と `requestVideoFrameCallback` を使用）。再生自体はモダンブラウザなら動く。
- 任意: `ffmpeg` / `ffprobe`（自前素材の取り込み、セクション計画、音声抽出）、Python 3（`scripts/import-motionclone.py`）。

## 実行条件

- サーバーは `127.0.0.1:4343`。ブラウザは同一オリジンにしかアクセスしない。
- 同梱のブランド素材・参考映像は各権利者に帰属し、プロジェクトのライセンス対象外と明記されている（再配布時は注意）。
- ホステッド製品「Null Studio」（カット一時停止、字幕、YouTube/Twitch/Kick のクリップ機能）とは別物で、このリポジトリには含まれない。README が明示的に区別している。

## 最短手順

```sh
git clone https://github.com/blixvip/NullMotion.git && cd NullMotion
npm start
# http://127.0.0.1:4343 を開き、リファレンスを選んで Download → Whole preview
```

## 変更履歴

- 2026-11-03: 初回登録（★1,326 / pushed 2026-10-31 / MIT / v1.0.1）
