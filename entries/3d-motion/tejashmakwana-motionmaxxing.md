---
name: "motionmaxxing"
genre: "3d-motion"
repo: "Tejashmakwana/motionmaxxing"
url: "https://github.com/Tejashmakwana/motionmaxxing"
last_release: ""
last_release_at: ""
flags: ["unverified"]
risk_notes: "現行版の生成品質、実行互換性、レンダリング性能は独立検証していない。作者のブラインド比較は旧版を対象とした単一評価者の結果で、作例の映像品質も評価していない。紹介投稿の冒頭にある参照動画の再現能力は、このリポジトリについて確認できていない。"
stars: 1509
forks: 154
open_issues: 1
size_kb: 21795
language: "JavaScript"
created: "2026-10-06"
updated: "2026-10-06"
archived: false
license: "Apache-2.0"
commits_30d: 0
commits_90d: 2
commit_cadence: "stale"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/CryptooGG_/status/2119312343892976064"]
fetched_at: "2026-11-10T12:08:26Z"
---

# motionmaxxingでモーショングラフィックスを設計し、編集可能なHTMLとMP4に出力する

## 出来ること

- Webサイトを起点にブランドの素材を集め、企画と絵コンテを作り、編集可能なHTMLとMP4を出力する。検査結果と目視判断はNOTE.mdに記録する。

## 目的・背景

- 作者はプロのモーション作例をフレーム単位で分析し、イージングやカットの設計ルールに落とし込んだと報告している。旧版のブラインド比較では、単一評価者が10件中9件でスキル使用版を選んだ。
- スクリプトは空白フレームや終端の静止時間などを検査する。文字の読みやすさと画面内の主役の判定は目視で行い、レイアウト検査は画像やcanvasに描かれた文字を検出できないと作者は記載している。

## 依存関係

- Node.js 22以上、Python 3、ffmpeg、Google Chrome。HTMLランタイムにはGSAPを同梱し、3Dレイヤーには同梱のThree.jsを使う。
- 本体はApache-2.0。GSAP、Three.js、opentype.js、Interには個別のライセンスが適用される。配布時の条件はリポジトリのNOTICEと各ライセンスを参照する。

## 実行条件

- HTMLはChromeでフレーム単位に描画し、ffmpegでローカル出力する。ナレーション・効果音・音楽の生成には任意のElevenLabs APIキーを使い、無音でも制作できる。Codex CLIによる画像生成も任意。外部サービスの料金は未確認。
- 公開GitHub Releasesページにリリースの掲載はなかった。

## 最短手順

- リポジトリを `~/.claude/skills/motionmaxxing` に配置し、READMEの案内に従って `bash ~/.claude/skills/motionmaxxing/install.sh` で依存関係を確認する。
- Claude Codeで `/motionmaxxing https://example.com を題材に無音の短い紹介動画を作って。制作前に企画と絵コンテを見せて` と依頼する。制作後は `film/index.html`、`film/final.mp4`、`film/NOTE.md` を確認する。

## 変更履歴

- 2026-11-10: 初回登録
