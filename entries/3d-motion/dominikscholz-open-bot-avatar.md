---
name: "open-bot-avatar"
genre: "3d-motion"
url: "https://github.com/DominikScholz/open-bot-avatar"
repo: "DominikScholz/open-bot-avatar"
license: "MIT"
stars: 633
language: "TypeScript"
created: "2026-11-02"
updated: "2026-11-17"
forks: 58
open_issues: 3
commits_30d: 17
commit_cadence: "weekly"
commits_90d: 17
size_kb: 7988
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 依存関係。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/dextune/status/2119240990762631334"]
fetched_at: "2026-11-17T21:12:29.366032+00:00"
---

# open-bot-avatar

## 出来ること

- エージェント用アバターのJSON仕様とレンダラーを提供する。定義はSVGパスと目の位置で構成され、`validateAvatar`で定義を検証できる。`renderAvatarSvg`で静止SVGを生成し、`mountAvatar`でブラウザー要素に表示できる。色、表情、視線、奥行き、動きの設定に対応する。README記載。

## 目的・背景

- 対話型エージェントのアバターを、JSON定義と描画機能で作成・表示するためのプロジェクト。READMEによれば、エディターではアバターの選択、色変更、生成、インポートができる。

## 依存関係

- READMEは`open-bot-avatar`パッケージについて依存なしと説明している。

## 実行条件

- パッケージ利用の実行条件はREADMEに明記されていない。開発環境にはNode 22.18以上とpnpmが必要と記載されている。

## 最短手順

- `pnpm add open-bot-avatar`で導入する。`open-bot-avatar`から`getExample`、`open-bot-avatar/dom`から`mountAvatar`を読み込み、`mountAvatar(document.querySelector("#bot"), { definition: getExample("mug"), color: "#ff6a1a", followPointer: true })`のように表示する。終了時は返されたアバターの`destroy()`を呼ぶ。

## 変更履歴

- 2026-11-22: 初回登録
