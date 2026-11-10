---
repo: "skylot/jadx"
name: "JADX"
genre: "other"
url: "https://github.com/skylot/jadx"
license: "Apache-2.0"
stars: 51735
language: "Java"
created: "2013-03-18"
updated: "2026-11-08"
forks: 5928
open_issues: 469
commits_30d: 28
commit_cadence: "daily"
commits_90d: 66
size_kb: 26440
archived: false
flags: ["unverified"]
risk_notes: "最新版のタグと公開日時は未確認。READMEの機能記載を確認した範囲で、逆コンパイルの精度、実行環境ごとの動作、AIによる要約の品質は実測していない。READMEは逆コンパイル時にエラーが生じうると明記している。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/RealMarvelX/status/2117596018908774636"]
fetched_at: "2026-11-10T09:49:38+00:00"
---

# JADXでAndroidアプリの構成を確認する

## 出来ること

- APK、DEX、AABなどのDalvikバイトコードをJavaコードに逆コンパイルし、AndroidManifest.xmlやアプリのリソースをデコードする。GUIでは宣言への移動、参照箇所の検索、全文検索ができる。

## 目的・背景

- 自社アプリの配布物に含まれる権限宣言、コンポーネント、処理の構成をレビューする。生成されたJavaコードには欠落やエラーがありうるため、確認が必要な箇所は手元のソースと照合する。

## 依存関係

- 通常の配布版には64ビットJava 11以降が必要。JRE同梱版は別途Javaを用意せずに使える。ソースからのビルドにはJDK 17以降が必要。

## 実行条件

- ローカルでCLIまたはGUIを利用できる。WindowsのZIP配布版には起動用のバッチファイルがある。JADXのライセンスはApache-2.0。入力には自社アプリなど、解析権限のあるファイルを使う。

## 最短手順

- セットアップ済みの環境で、自社のテストAPKを `jadx app.apk` で処理する。生成されたマニフェストを開き、確認したい権限やコンポーネントの宣言を探す。
- シェルを使えるAIエージェントから呼ぶ場合は、自社のテストAPKと出力先を明示し、同じJADX CLIをローカルで実行させる。生成されたマニフェストから指定の権限とコンポーネントを、該当箇所を添えて要約するよう依頼する。

## 変更履歴

- 2026-11-10: 初回登録
