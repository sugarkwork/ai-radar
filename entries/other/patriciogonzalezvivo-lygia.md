---
name: "LYGIA Shader Library"
genre: "other"
url: "https://github.com/patriciogonzalezvivo/lygia"
repo: "patriciogonzalezvivo/lygia"
license: "unknown"
stars: 3505
language: "GLSL"
created: "2021-04-06"
updated: "2026-10-24"
forks: 226
open_issues: 26
commits_30d: 1
commit_cadence: "monthly"
commits_90d: 10
size_kb: 13773
archived: false
flags: ["unverified"]
risk_notes: "GitHub APIではlicenseがunknown。READMEにライセンス条件の記載は提示資料内で確認できない。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/0xCarrera/status/2123762450935771202"]
fetched_at: "2026-11-22T04:48:48.078828+00:00"
---

# LYGIA Shader Library

## 出来ること

- GLSLなど複数のシェーディング言語向けの再利用可能なシェーダー関数ライブラリ。READMEはクロスプラットフォーム対応をうたい、主要な環境・エンジン・フレームワーク向けの統合例を挙げている。シェーダー内で必要な関数を#includeし、例では画面比率調整、色の量子化、円描画の関数を使う。

## 目的・背景

- シェーダーの試作、移植、プロジェクトへの組み込みに使うための、細かく選択可能な関数群として紹介されている。

## 依存関係

- ローカル利用では、シェーダー環境に#include依存関係を解決する手段が必要。WebではVite、esbuild、webpack向けのGLSLプラグイン例がREADMEに示されている。

## 実行条件

- 提示された例はGLSLシェーダー。ローカル版はリポジトリをcloneするかsubmoduleとして追加でき、npmプロジェクトにはnpm bundleの案内がある。クラウド環境ではhttps://lygia.xyz/resolve.jsまたはhttps://lygia.xyz/resolve.esm.jsを読み込み、依存関係をオンライン解決する方法が記載されている。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- READMEの例に従い、プロジェクトから `git clone https://github.com/patriciogonzalezvivo/lygia.git` で取得し、シェーダー内で必要な関数を `#include "lygia/..."` として参照する。利用環境側で#include依存関係を解決する設定が必要。

## 変更履歴

- 2026-11-23: 初回登録
