---
name: "LiteLLM"
genre: "model-serving"
url: "https://github.com/BerriAI/litellm"
repo: "BerriAI/litellm"
license: "unknown"
stars: 63442
language: "Python"
created: "2023-07-27"
updated: "2026-11-17"
forks: 13367
open_issues: 5225
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 3042632
archived: false
flags: ["unverified"]
risk_notes: "GitHub APIの取得データではライセンスがunknownです。ライセンス条件は確認できていません。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/irongiantXBT/status/2122709093102285099"]
fetched_at: "2026-11-17T23:23:46.377355+00:00"
---

# LiteLLM

## 出来ること

- READMEによると、LiteLLMは100以上のLLMプロバイダーをOpenAI形式の統一インターフェースから呼び出すためのAI Gatewayです。Python SDKとして直接利用する方法と、チーム向けのProxy Serverとして運用する方法が紹介されています。READMEはvirtual keys、支出追跡、guardrails、負荷分散、管理ダッシュボードも機能として挙げています。

## 目的・背景

- READMEでは、プロバイダーごとに異なるSDK、認証方式、リクエスト形式、エラー型を扱う複雑さを減らすことを目的として説明しています。

## 依存関係

- READMEの導入例ではPython SDKにuvを使用し、Proxy Serverには`uv tool install 'litellm[proxy]'`を使っています。SDK例では利用するプロバイダーのAPIキーを環境変数に設定します。

## 実行条件

- READMEの例ではPythonから`litellm`をインポートして呼び出す方法と、Proxy Serverを起動して利用する方法が示されています。必要なAPIキーや設定は利用するプロバイダー・構成に応じて用意します。

## 最短手順

- Python SDKは`uv add litellm`で導入し、利用するプロバイダーのAPIキーを環境変数に設定して`litellm.completion(...)`を呼び出します。Proxy Serverは`uv tool install 'litellm[proxy]'`で導入し、README例では`litellm --model <モデル名>`で起動します。

## 変更履歴

- 2026-11-22: 初回登録
