---
name: "One IP"
genre: "other"
url: "https://github.com/zhihui-hu/one-ip"
repo: "zhihui-hu/one-ip"
flags: ["unverified"]
risk_notes: "結果は第三者サービスに依存し、レート制限やクロスオリジン制約の影響を受ける場合がある。READMEはIP種別と評判スコアを参考情報としている。"
stars: 1235
forks: 1388
open_issues: 1
size_kb: 5784
language: "TypeScript"
created: "2026-09-09"
updated: "2026-11-12"
archived: false
license: "AGPL-3.0"
commits_30d: 18
commits_90d: 58
commit_cadence: "weekly"
type: "repo"
added: "2026-11-12"
first_seen: "2026-11-12"
sources: ["https://x.com/ruyi3699/status/2118563022801338575"]
fetched_at: "2026-11-12T18:09:18.512178+00:00"
---

# One IP

## 出来ること

- IPv4/IPv6の所在・事業者・ASN・評判スコア・地図表示、DNS/WebRTC漏洩検出、AI・動画配信サービス等への接続診断、Cloudflareエッジネットワークを使った速度測定、WHOIS、Global Ping、ブラウザー指紋・環境検出、サービス状態確認を提供する。中英語、ライト/ダークテーマ、モバイル表示に対応し、ブラウザー標準のWebMCPもサポートするとREADMEに記載されている。

## 目的・背景

- IP情報の確認、ネットワーク接続の診断、ブラウザー環境の確認、サービス状態の確認を一つのツール箱で行う。READMEは検出結果を環境調査用とし、各プラットフォームの公式判定を示すものではないとしている。

## 依存関係

- README記載の技術構成はReact 19、Vite 8、TypeScript 6、Cloudflare Workers。データ・診断元としてNet.Coffee、ip-api、Globalping、IANA/RDAP、各プラットフォームの公式状態情報源を挙げている。ブラウザー検出にはFingerprintJSとCreepJSを使用する。

## 実行条件

- CloudflareへのデプロイではCloudflare Workers & Pagesにリポジトリを取り込み、ビルドコマンド `pnpm build`、デプロイコマンド `pnpm deploy` を使う。READMEによると基本機能にAPIキーは不要。Docker自営またはローカル開発手順もREADMEに記載されている。

## 最短手順

- CloudflareのDeployボタンを使うか、Cloudflare Workers & Pagesでリポジトリを取り込み、`pnpm build` と `pnpm deploy` を実行する。

## 変更履歴

- 2026-11-12: 初回登録
