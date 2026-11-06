---
type: "repo"
name: "TencentDB Agent Memory（チームで共有するエージェント記憶ハブ）"
genre: "agent-framework"
url: "https://github.com/TencentCloud/TencentDB-Agent-Memory"
repo: "TencentCloud/TencentDB-Agent-Memory"
license: "MIT（GitHub API は NOASSERTION）"
stars: 30561
language: "TypeScript"
created: "2026-04-07"
updated: 2026-11-04
added: "2026-11-06"
first_seen: "2026-11-05"
sources: ["https://x.com/AIExplorerTim/status/2118151566398279695", "https://tencentcloud.github.io/TencentDB-Agent-Memory/", "https://www.npmjs.com/package/@tencentdb-agent-memory/memory-tencentdb"]
flags: []
risk_notes: "投稿の『トークン最大61.38%削減／タスク成功率33%→50%／PersonaMem精度48%→76%』は配布元の公表値で、独立再現は確認していない。投稿の『1.5万スター』は古く、実際は3万超（取得時点）。構成上、会話・文書・コードの内容がローカルの memory-core / memory-hub に蓄積されるため、チームで使う場合は誰が何を読めるかの権限設計（private / team / restricted）を先に決める必要がある。導入は `.env` にLLMパラメータを2組（memory用とproxy用）書く必要があり、APIキーが要る。MongoDB バックエンドは実験的で既定オフ。"
forks: 2982
open_issues: 887
commits_30d: 24
commit_cadence: daily
size_kb: 66453
archived: false
fetched_at: "2026-11-06T09:14:12Z"
last_release: v2.0.3
last_release_at: 2026-10-26
commits_90d: 67
---

# TencentDB Agent Memory — 会話・文書・コードを4種類の「記憶資産」に変えてチームで配る記憶ハブ

## 出来ること

- エージェントの文脈を**4種類の再利用可能な記憶資産**として切り出す：**Chat Memory**（会話・好み・事実・決定・やり取りの履歴）、**Skill**（手順の蓄積）、**LLM-Wiki**（文書をリンク付きの構造化ページに変換）、**CodeGraph**（コードのシンボル・ファイル・呼び出し関係・影響経路）
- **階層化された記憶**：L0 生の会話 → L1 名前・好み・制約 → L2 プロジェクト／シナリオ単位の知識 → L3 長期的な人物像、と段階的に蒸留し、必要な層だけを引く
- **Skill はプロンプト断片ではない**：バージョン、リソースファイル、発火条件（トリガ境界）、実行手順、検証ルールを持つ単位として登録・配布される。個人Skillは既定で非公開、レビュー後にチームへ共有し他エージェントに割り当てる
- **エージェント側の実装は不要**：Proxy が1つ立ち、エージェントの base URL をそこへ向けるだけで記憶が効く。プラグイン・フック・MCPサーバの追加は要らない（Claude Code / Codex / CodeBuddy / WorkBuddy / Hermes / OpenClaw / DeepSeek Harness ほか、汎用の接続手順も用意）
- **コールドスタート対策**：既存リポジトリをインポートすると CodeGraph が自動で索引を作り、文書は Wiki の構造化ページになる。過去のエージェント会話も取り込めるので、新しいメンバーやエージェントが初日からチームの続きから始められる
- **人手で管理する記憶パネル**：チームとエージェントを作り、記憶資産のレビュー・共有・割当を1か所で行う。所有権・バージョン・状態・公開範囲・利用回数・エージェントの紐付けを管理
- 公開範囲は3段階：`private`（所有者のみ）／`team`（チーム全員）／`restricted`（User / Role / Agent 単位のACL）。ロールはグローバルの System Admin と、チーム単位の Admin / Member の二層

## 目的・背景

- 出発点は「エージェントを使うときの繰り返し作業をどう減らすか」。プロジェクトの前提を毎セッション説明し直す、読んだ文書を別のエージェントがまた1ページ目から読む、うまくいった手順を次の誰かが再発見する、というムダを記憶資産の循環で置き換える
- モデル自体は変えない。モデルの外側に記憶層を置き、フレームワークから切り離した形で資産を持ち運べるようにするのが設計の中心
- 投稿は中国語圏のアカウントによる紹介で、stars が短期間で伸びたことを引き合いに出している（取得時点で3万超、fork 約3千）

## 依存関係

- Node.js 22.16 以上。`deploy/global-images` から `memory-core` + `memory-hub` + `proxy` の3サービスをまとめて起動する構成
- `.env` に**LLMパラメータを2組**（memory グループ用と proxy グループ用）書く。ここに使うモデルのAPIキーが必要
- npm パッケージ `@tencentdb-agent-memory/memory-tencentdb` も公開されている
- ストレージは既定の構成で動く。MongoDB バックエンドは実験的（既定オフ）
- 旧バージョン（v1.x / v0.x）からのデータ移行ツールあり（新規導入では不要）

## 実行条件

- 導入は Docker 前提の3サービス構成。パネルは `http://localhost:8125`
- **APIキーが必須**（記憶の蒸留にLLMを呼ぶため）。完全ローカルで閉じたい場合はローカルのOpenAI互換サーバを指す構成にする必要がある
- チーム利用では権限設計が実質的な前提作業。`private` の資産は所有者しか読めないので、共有前提の運用にするなら最初に `team` / `restricted` の割当を決める
- 数字（トークン削減・成功率・PersonaMem精度）は配布元のベンチマークで、独立検証ではない
- 言語：パネル・文書は英語と中国語。日本語対応は投稿時点で進行中とされている

## 最短手順

```bash
git clone https://github.com/TencentCloud/TencentDB-Agent-Memory.git
cd TencentDB-Agent-Memory/deploy/global-images

cp .env.example .env
$EDITOR .env            # LLMパラメータを2組（memory 用 / proxy 用）設定

./start-all.sh          # memory-core + memory-hub + proxy を一括起動
# 完了時に、そのままエージェントへ貼れる接続用の一行が表示される

# パネル
open http://localhost:8125
```

```text
# エージェント側（例: Claude Code）
# 既存の base URL を Proxy のアドレスに差し替えるだけ。プラグインもMCPサーバも不要。
# 具体的な設定手順は INSTALL.md の該当節を参照。
```

## 変更履歴

- 2026-11-06: 初回登録
