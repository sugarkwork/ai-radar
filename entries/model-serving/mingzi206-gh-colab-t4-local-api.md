---
name: "Colab T4 Local OpenAI API Replication Package"
genre: "model-serving"
url: "https://github.com/mingzi206-gh/colab-t4-local-api"
repo: "mingzi206-gh/colab-t4-local-api"
license: "unknown"
stars: 51
language: "Python"
created: "2026-11-08"
updated: "2026-11-08"
forks: 16
open_issues: 0
commits_30d: 2
commit_cadence: "monthly"
commits_90d: 2
size_kb: 59
archived: false
flags: ["unverified"]
risk_notes: "ライセンスはGitHub API上でunknownで、READMEもプロジェクトのLICENSEは未選定と記載。Colabの利用条件・リソースは変化し、無料利用、長時間稼働、中断なしの復旧は保証されない。128Kコンテキストは設定値で、T4上で任意の長さを処理できる保証はない。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/mingzi206/status/2119431410549416162"]
fetched_at: "2026-11-22T13:03:14.890090+00:00"
---

# Colab T4 Local OpenAI API Replication Package

## 出来ること

- Windows上のローカルゲートウェイからCloudflareの一時トンネルを通じてColab T4上のllama.cppを利用し、ローカルにOpenAI互換APIを提供する構成。モデルは自身のGoogle Driveにキャッシュできる。READMEでは健康状態、モデル一覧、チャットの各APIを公開すると説明している。

## 目的・背景

- ローカルPCにNVIDIA GPUがなくても、Colab T4上のモデルをローカルアプリから利用するためのパッケージ。READMEは、同一PC上のプログラムがローカル入口へアクセスできるため、公開ネットワークやLANで待ち受けないよう案内している。

## 依存関係

- README記載の準備手順ではPython 3.12以上（参考環境は3.13）とrequirements.txtを使用する。Colab、Google Drive、Cloudflare一時トンネルを利用する構成。

## 実行条件

- Windows PowerShellで実行する。自分のプロキシとDriveの設定、本人のOAuth認証が必要。Colabのアカウント条件や利用制限は変化する。README記載の既定モデルIDはdeepseek-heretic-9b、コンテキスト設定は131072、未指定時の生成上限は4096トークン。既定コンテキスト値はT4での処理保証ではない。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- READMEの手順に従い、Python 3.12以上で仮想環境を作成してrequirements.txtをインストールし、config.example.jsonをconfig.jsonへコピーする。自分の設定とOAuthを用意した後、doctor.py --json、unittest discover、start.ps1の順に実行する。別の端末から_colab_verify_chain.pyで実リクエストを確認できる。Driveの完全な復元確認は_colab_persist_drive.py --verify-restoreで行うが、ネットワークと時間を要する。詳細な前提条件と停止・障害対応はDEPLOYMENT.mdを参照する。

## 変更履歴

- 2026-11-23: 初回登録
