---
name: "GSAP"
genre: "3d-motion"
repo: "greensock/GSAP"
url: "https://github.com/greensock/GSAP"
flags: ["unverified"]
pricing: "free"
pricing_detail: "公式READMEでは商用利用を含めてプラグインも無償。標準ライセンスでは、Webflowのビジュアルアニメーション作成機能と競合するノーコードツールの開発を促進・支援する用途などに制限がある。"
stars: 30400
forks: 2367
open_issues: 6
size_kb: 14943
language: "JavaScript"
created: "2012-09-21"
updated: "2026-11-04"
archived: false
license: "unknown"
commits_30d: 1
commits_90d: 1
commit_cadence: "monthly"
risk_notes: "GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/CryptooGG_/status/2119312343892976064"]
fetched_at: "2026-11-10T12:07:30+00:00"
---

# GSAPでWebアニメーションをタイムライン化する

## 出来ること

- CSSプロパティや属性の値を時間に沿って補間し、イージングを指定できる。複数のアニメーションをタイムラインにまとめ、順序や再生位置を調整できる。

## 目的・背景

- Webページ上のモーションをJavaScriptで管理する。AIコーディング支援を使う場合は、対象要素、動きの順序、所要時間を指定してコードを生成し、タイムライン上の設定を後から編集できる。

## 依存関係

- GSAPコアに外部依存はないとREADMEに記載されている。追加プラグインを使う場合は、必要なものをインポートして `gsap.registerPlugin()` で登録する。

## 実行条件

- DOM要素を動かす例はブラウザーで動かす。npmから導入してJavaScriptでインポートするか、HTMLのscriptタグで読み込める。
- 無償利用にも標準ライセンスが適用される。Webflowと競合するノーコードのアニメーション作成ツールに組み込む場合は用途制限を確認する。

## 最短手順

- 既存のWebプロジェクトで `npm install gsap` を実行し、対象要素に `class="box"` を付ける。
- JavaScriptで `import gsap from 'gsap';` と読み込み、`gsap.timeline().to('.box', { x: 100, duration: 0.6, ease: 'power2.out' }).to('.box', { opacity: 0, duration: 0.3 });` を記述してブラウザーで確認する。
- AIコーディング支援から使う場合は、対象要素と順序を渡して、既存の画面コードに `gsap.timeline().to()` の呼び出しを追加するよう依頼する。GSAPのAPIは生成されたJavaScriptから呼び出す。

## 変更履歴

- 2026-11-10: 初回登録
