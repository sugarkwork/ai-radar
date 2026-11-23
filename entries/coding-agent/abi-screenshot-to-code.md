---
name: "Screenshot to Code"
genre: "coding-agent"
url: "https://github.com/abi/screenshot-to-code"
repo: "abi/screenshot-to-code"
license: "MIT"
stars: 81296
language: "Python"
created: "2023-11-14"
updated: "2026-11-15"
forks: 9957
open_issues: 150
commits_30d: 4
commit_cadence: "weekly"
commits_90d: 6
size_kb: 11072
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 依存関係。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/RealMarvelX/status/2119329098929426902"]
fetched_at: "2026-11-19T07:27:23.647244+00:00"
---

# Screenshot to Code

## 出来ること

- スクリーンショット、モックアップ、Figmaデザイン、画面録画をもとに、機能するコードやプロトタイプを生成します。README記載の対応スタックはHTML + Tailwind、HTML + CSS、React + Tailwind、Vue + Tailwind、Bootstrap、Ionic + Tailwindです。

## 目的・背景

- デザイン画像やウェブサイトの画面録画から、実装可能なコードに変換するツールとして紹介されています。READMEには作例が掲載されていますが、生成結果の品質は独立に確認していません。

## 依存関係

- ローカル実行には、OpenAI、Anthropic、GeminiのいずれかのモデルプロバイダーAPIキーが必要です。画像生成・編集などにはReplicateのAPIキーが推奨され、READMEでは画像編集と背景除去はキー未設定時に利用できないと説明されています。

## 実行条件

- README記載の構成はReact/ViteフロントエンドとFastAPIバックエンドです。バックエンドの依存関係をPoetryでインストールし、PlaywrightのChromiumをセットアップして起動します。フロントエンドはpnpmで依存関係をインストールして起動します。Dockerでの起動手順も記載されています。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- ローカル実行では、backend/.envに利用するプロバイダーのAPIキーを設定し、READMEのコマンドに従ってバックエンド依存関係とPlaywright ChromiumをセットアップしてUvicornを起動します。続いてfrontendでpnpm install、pnpm devを実行します。READMEにはホスト版を試す方法も案内されています。

## 変更履歴

- 2026-11-23: 初回登録
