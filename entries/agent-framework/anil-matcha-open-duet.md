---
repo: Anil-matcha/open-duet
name: Open Duet
genre: agent-framework
url: https://github.com/Anil-matcha/open-duet
license: Apache-2.0
stars: 6686
language: Python
created: 2023-05-25
updated: 2026-11-03
added: 2026-11-03
sources:
  - https://x.com/silvanrec/status/2117272930543403244
  - https://x.com/aridot_/status/2117286296653648315
  - https://x.com/alextalksai/status/2117282806782992875
forks: 843
open_issues: 18
commits_30d: 100
commits_90d: 100
commit_cadence: daily
size_kb: 5441
archived: false
fetched_at: "2026-11-03T15:42:12Z"
---

# Open Duet

## 出来ること

- 名前・役割・エンジン・ワークスペース・メモリ・承認設定を持つ**AI 同僚（named agent）**を作り、チームとして動かす。リードが専門エージェントに作業を委任でき、共有ルームで協調もできる。
- メモ：エージェントはノートを保存し、関連ノートや過去会話を想起・検索する。記憶内容は人間が確認・編集できる。
- ルーティン：スケジュール実行・Webhook・手動の3種。結果は毎回人間が確認し、承認要求に答える。**ルーティンが勝手に承認することはない**。
- 権限モードは Ask first / Accept edits / Plan only の3段。ツール実行と承認判断はアプリ内で確認できる。
- Composio の自前キー経由で GitHub / Gmail / Google Calendar などを接続し、指定した Claude / Codex エージェントにのみアクセスを付与する。変更は承認待ちになる。MCP Marketplace から個別ツールも追加できる。
- Today ビュー（承認待ち・質問・ルーティン結果・エンジン障害・期限タスクの集約）、タスクボード、カレンダー、スキル＆テンプレート、ワークスペースのファイル閲覧、履歴エクスポート。
- スマホアプリ（自前サーバーとペアリング）でチャット・回答停止・ツール呼び出しの許可/拒否。

## 目的・背景

Grok Bot / Claude Duet / OpenAI Dots / Meta Muse / Instinct / Manus Cue など「AI 同僚」型プロダクトのセルフホスト代替を名乗る。作者は Anil-matcha、Apache-2.0。リポジトリは 2023-05-25 作成と古いが、現在の中身は 2026 年に作り直されており pushed は 2026-11-03。デスクトップアプリ／自前サーバー／開発チェックアウトの3形態で動かせ、別運営の hosted サービス（suparagent.ai）も用意されている。

## 依存関係

- デスクトップアプリ（ソースからの起動）: **Node.js 22 以上、uv**、および同一マシン上で動くエンジン最低1つ。CLI 系エンジンは事前にインストールとサインインが必要。API ベースのエンジンは Settings → Engines で設定する。
- セルフホスト: Linux サーバー、HTTPS、Docker または Node.js + uv、エンジン。
- **モデル本体は同梱されない。** エンジンとプロバイダのアカウントは自分で用意し、モデル利用料は各プロバイダへ直接支払う。
- Docker は任意の隔離エージェント環境（agent computers）にのみ必要。
- チーム委任のリードは **Claude または Codex** を使う必要がある。

## 実行条件

- デスクトップアプリのインストーラは**未署名かつプラットフォーム検証が限定的**。README はデスクトップ版の状態を「実験的」と明記している。
- セルフホストサーバーは 1 オーナー＋ペアリング済み端末向けの実験運用で、複数ユーザーの組織利用は想定外。
- 既知の制約（README 記載）: チーム委任は新機能、スマホアプリはソースのみで Android エミュレータでのみ試行（iOS・実機未検証、プッシュ通知なし）、Docker コンピュータ・ブラウザツール・macOS ネイティブプレビューは experimental でオプトイン、接続アプリは Composio のモックに対するテストのみ、MCP Marketplace と音声文字起こしは実サービス未検証。
- 更新フローは SHA-256 検証済みインストーラを提示する方式で、リリース間の自動更新は未検証。

## 最短手順

```bash
git clone https://github.com/Anil-matcha/open-duet.git
cd open-duet/desktop
npm run app
# 初回起動でエンジン・ワークスペース・承認モードを選択
# Settings → Engines でエンジンが ready か確認 → エージェントを作成
```

## 変更履歴

- 2026-11-03: 初回登録（star 6,685 / pushed 2026-11-03 / Apache-2.0）
