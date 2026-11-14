---
name: "Inochi2D"
genre: "3d-motion"
url: "https://github.com/Inochi2D/inochi2d"
repo: "Inochi2D/inochi2d"
license: "BSD-2-Clause"
stars: 1863
language: "D"
created: "2020-10-08"
updated: "2026-11-10"
forks: 76
open_issues: 13
commits_30d: 1
commit_cadence: "monthly"
commits_90d: 6
size_kb: 4381
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/aikangarooking/status/2121444332091965629"]
fetched_at: "2026-11-14T08:07:11.688502+00:00"
---

# Inochi2D

## 出来ること

- レイヤーアートから作成した2Dメッシュを実行時にパラメータに応じて変形し、2Dアートに奥行きや動きを見せるリアルタイム2Dパペットアニメーション用ライブラリ。Inochi2D Puppet標準のリファレンス実装。SDKはD言語のほか、C FFIを通じて他言語から利用でき、Godot向けGDExtensionとWebAssembly構成も用意されている。

## 目的・背景

- READMEでは、標準とそのリファレンス実装を提供するリポジトリと説明されている。作者の説明では、このリポジトリ自体はエンドユーザー向けではなく、リガーには開発中のInochi Creator、VTuberにはInochi Sessionを案内している。

## 依存関係

- Dプロジェクトではdubから追加する。C FFIのビルドにはLDC2とdubが必要。Godotバインディングのビルドには対象バージョンのGodotをPATHに設定するか、GODOT_PATHで指定する。WebAssembly利用にはパッチ済みdruntimeソースツリーが必要で、README記載の導入方法はLinuxのみ。

## 実行条件

- README記載の要件は、SSE4+対応x86-64 CPUまたはNEON対応AArch64 CPU。大きなモデルには1 GB以上のRAMが必要で、GPU要件はレンダラーバックエンドによる。非D言語依存はPOSIX準拠C標準ライブラリのみ。nogc移行完了まではUNIX系でglibcが最良の利用体験とされる。

## 最短手順

- Dから利用する場合はdubのプロジェクト設定にパッケージとして追加する。C/C++/Rustなどから利用する場合はLDC2とdubを用意し、リポジトリのルートで `dub build --config=dynamic` を実行してC FFI SDKをビルドする。Godot GDExtensionはGodotのパスを設定してから `dub build :godot` を実行する。

## 変更履歴

- 2026-11-14: 初回登録
