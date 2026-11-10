---
repo: "0xCodez/DuoDesk"
name: "DuoDesk"
genre: "other"
url: "https://github.com/0xCodez/DuoDesk"
last_release: "v2.5.0"
flags: ["unverified"]
risk_notes: "最新リリースの公開日時と配布物の署名状態は未確認。対応 OS の組み合わせ別の動作、転送性能、通信の安全性は独立検証していない。Claude Code と Opus 5.5 の利用および開発規模は、候補が指す X 投稿を直接取得できず未確認。"
stars: 486
forks: 79
open_issues: 7
size_kb: 21153
language: "JavaScript"
created: "2026-10-30"
updated: "2026-10-31"
archived: false
license: "GPL-3.0"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/AiAircle34052/status/2117462521783447830"]
fetched_at: "2026-11-10T09:06:21Z"
---

# DuoDesk — 複数端末でマウス・キーボードとクリップボードを共有

## 出来ること

- README によると、Mac・Windows・Linux・Android 間でマウスとキーボード、クリップボード、ファイルを共有できる。機能ごとの対応条件は端末や OS によって異なる。

## 目的・背景

- TwinDesk のフォークで、GPL-3.0 を継承する。デスクトップでは Electron がペアリングや接続を扱い、OS 固有の入力や画面処理はネイティブヘルパーが担当する。

## 依存関係

- ソースからのビルドには README 上で Node.js 18 以上が必要。macOS のヘルパーには Swift コンパイラ、Windows には .NET Framework の C# コンパイラ、Android のビルドには JDK 17 以上を使う。

## 実行条件

- macOS は 13 以降、Windows は 10 または 11。README は macOS の初回起動時に画面収録、アクセシビリティ、入力監視の権限を求めると記載している。Android の画面や入力操作には、構成によってワイヤレスデバッグのペアリングが必要。

## 最短手順

- [公式リリース](https://github.com/0xCodez/DuoDesk/releases/tag/v2.5.0)で各端末の OS に対応する配布物を確認する。各端末でアプリを起動し、同じローカルネットワーク上で Connection 画面からペアリングする。接続後にマウス移動やクリップボード共有を試す。

## 変更履歴

- 2026-11-10: 初回登録
