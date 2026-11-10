---
repo: "KKKKhazix/agent-autoloop"
name: "Agent Autoloop"
genre: agent-framework
url: "https://github.com/KKKKhazix/agent-autoloop"
license: "MIT"
stars: 4268
language: "TypeScript"
created: "2026-11-03"
updated: "2026-11-09"
added: "2026-11-04"
first_seen: "2026-11-04"
source_post: "https://x.com/ganfanren_ai/status/2117893040778195451"
sources: ["https://x.com/naka_1717/status/2119271760206123187"]
flags: ["unverified"]
risk_notes: "starsの投稿値と確認値は時点差がある。承認の実効性・無人稼働は今回試験していない。 今回の動作・推論・生成・性能は未検証。"
forks: 776
open_issues: 2
size_kb: 1170
archived: false
last_release: "v1.7.1"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
fetched_at: "2026-11-09T21:33:28Z"
last_release_at: "2026-11-09"
type: "repo"
author: "KKKKhazix"
amplifiers: []
---

# Agent Autoloop

## 出来ること

- コマンドライン Agent（Claude Code、Codex など）を**常駐させて自分で仕事を拾わせる**ための軽量な中台。ターミナルを開いていない間も、キューに積まれた仕事を順に処理する。
- 仕事の入口を**イベントソースのプラグイン**として差し替えられる: 定期実行、HTTP 受信、GitHub Webhook（新 Issue など）、Issue のポーリング。
- 判断を Agent に任せきらず、**確認が必要な場面だけカードを通知チャネルへ送る**（Feishu / DingTalk / WeCom / Slack / Discord / デスクトップ通知）。回答するとそのまま処理が続く。
- Agent 側・通知側・デリバリ（CI/CD）側もプラグイン。`agent-autoloop add <git URL>` でサードパーティのプラグインを追加できる。
- 中核は約1,850行で実行時依存ゼロ。時計を読まず、乱数を使わず、外へリクエストを送らない設計（同じ入力なら同じ結果）。認証情報は各プラグイン側に留める。
- CLI と MCP の両方から状態確認・カードへの回答ができる。状態は SQLite に永続化。
- **Windows 対応**（v1.6.1）: PowerShell のインストーラを用意し、インストールと中台の常駐を Windows でも実行できる（macOS / Linux は curl）。
- **ルールの操作と検証**: `pause` / `resume` / `run <ルール>` で個別ルールを止め・再開・即時実行でき、`check` / `rules explain` / `emit --dry-run` で設定とイベントの行き先を確かめられる。
- **内蔵 Agent の起動方法を差し替えられる**: 環境変数を設定してから起動する自前スクリプトを `program` に指定でき、ACP に対応する Agent（Gemini CLI / OpenCode）は `use: "acp"` で元のセッションを引き継げる。

## 目的・背景

「人がターミナルの前に座っている間しか Agent が働かない」問題を、スケジューラとイベント駆動で埋める。サーバーを借りず、手元の Mac / Linux 1台で回すことを前提にしている。作成は 2026-11-03 で、翌日には ★1,803。

## 依存関係

- Node 24、Git、curl。
- 動作させるには、**すでにログイン済みのコマンドライン Agent** が1つ必要（Claude Code / Codex など）。プロンプトを受け取って最後の返答を出力できる CLI なら何でもよい。
- macOS または Linux。Windows は README の対応に含まれていない。

## 実行条件

- ライセンスは MIT。★1,803、fork 353、issue 9（2026-11-04 時点）。公開から日が浅く、API や設定項目は変わる可能性がある。
- README のベンチマーク数値は「Apple M5 Pro / 24 GB / Node 24.21.0」の1台で取ったもので、他環境では `npm run benchmark` の基準を満たさないことがあると明記されている。
- 認証情報は読まない設計だが、Agent が実行する操作そのもの（ファイル変更、デプロイ）は権限を持つ。確認カードの運用ルールは導入側で決める。

## 最短手順

```bash
# インストール（README / INSTALL.md の手順に従う）
curl -fsSL https://raw.githubusercontent.com/KKKKhazix/agent-autoloop/main/install.sh | sh
agent-autoloop            # 設定と状態の確認
# 通知チャネル・イベントソース・Agent を設定に登録してから常駐させる
```

## 変更履歴

- 2026-11-04: 初回登録（★1,803 / MIT / v1.0.0 / 作成 2026-11-03）
- 2026-11-06: Windows 対応、ルールの pause/resume/run と検証コマンド、内蔵 Agent の差し替え・ACP 接続を追記（v1.6.1 / 49562af）

## 追加出典・確認範囲（2026-11-09）

常駐エージェントの処理を管理するAgent Autoloopの再紹介。

削除・再起動・支払い・外部送信の4場面で確認する設計というREADMEの記述を原チェックで照合。

starsの投稿値と確認値は時点差がある。承認の実効性・無人稼働は今回試験していない。

対象固有の機能・制約の説明は2026-11-08（原記録）のチェック記録を基にしている。メタ情報は2026-11-09T00:31:33.624096+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

### 今回取得した公式メタ情報

既存フロントマターの過去値は維持し、今回の取得値を下に併記する。どちらも実行・性能の追試ではない。

| 項目 | 値 |
|---|---|
| repo | KKKKhazix/agent-autoloop |
| url | https://github.com/KKKKhazix/agent-autoloop |
| license | MIT |
| language | TypeScript |
| created | 2026-11-03 |
| updated | 2026-11-08 |
| stars | 4101 |
| forks | 747 |
| open_issues | 1 |
| commits_30d | 100 |
| commits_90d | 100 |
| commit_cadence | daily |
| size_kb | 1146 |
| archived | False |
| fetched_at | 2026-11-09T00:31:33.624096+00:00 |


- @naka_1717: https://x.com/naka_1717/status/2119271760206123187
- 対象資料: https://github.com/KKKKhazix/agent-autoloop

- 2026-11-09: 関連出典と確認範囲を追記。既存の記述・過去の数値・原文プロンプトは維持。今回の実行確認なし。
