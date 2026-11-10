---
repo: "qkal/canny"
name: "Canny"
genre: "agent-framework"
url: "https://github.com/qkal/canny"
author: "qkal (Kal)"
license: "MIT"
stars: 134
language: "TypeScript"
created: "2026-09-11"
updated: "2026-09-22"
forks: 18
open_issues: 6
size_kb: 266
archived: false
commits_30d: 0
commits_90d: 23
commit_cadence: "monthly"
last_release: "v0.3.0"
last_release_at: "2026-09-22"
flags: ["unverified"]
risk_notes: "投稿は「Jev repos」の一つとして紹介するが、Canny は TypeSafe 製ではなく qkal 個人のプロジェクトで、Jev は任意の判定器（キー未設定でも決定論的ゲートは動く）。確認できたこと: 実装は実在し src/*.ts 約81KB・test 約97KB、CI（Node 22/24/26 + macOS + smoke + CodeQL）が直近成功、手元で 246 tests passed、Stop の block→allow→replay も実測で再現。確認できなかったこと: star 134 の真正性は API からは検証不能（未確認）。注意すべき事実: 23コミット全てが 2026-09-17〜22 の6日間に1名で入り、以後 48日コミットなし（30日コミット0、contributors は qkal 1名のみ、AI ボット名義のコミットは無く web-flow は GitHub のマージコミッター）。134 stars / 18 forks に対し watchers 0、外部PRは 2026-10-01 と 10-21 から未マージ。README 自身がプロジェクト全体の効果は未測定と明記し、bench も成果差なし（両アーム全通過、25ペアで 1.6±3.4 秒差）。未回答のセキュリティ指摘 issue #26（Jev 判断の乗っ取り JPDH、2026-10-14、コメントなし）が open。既知の実装制限: Windows のパス正規表現（#24）、python3 -m unittest 等の検出漏れ（#27/#28）、シェル経由の書き込み検出は一部記法のみ（find -exec、xargs、python -c 等は不可）。dist/ プリビルト同梱・npm 未配布のため供給網は作者1名に依存。キー設定時は編集差分（4,000字上限）と最終メッセージが TypeSafe に送信される。"
type: "repo"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/thegreatest_sv/status/2114378197932617766"]
fetched_at: "2026-11-09T21:34:42Z"
---

# Canny — 「完了」を台帳の証拠で止める Claude Code / Codex 監督フック

## 出来ること

- Claude Code と Codex CLI のフックとして動き、コード編集の後にテスト・ビルド・lint・型チェックが一度も exit 0 で通っていない状態でエージェントが「完了」と報告すると、Stop をブロックして理由（変更ファイル、最後のコマンドと終了コード、何がチェックに数えるか）を返す。
- セッション中のシェルコマンド・終了コード・編集パスを追記専用の台帳（JSONL）に残し、canny replay で全 Stop 判定を台帳から再導出して照合できる。
- PreToolUse の決定論的チェック: 秘密鍵パターン（AWS/GitHub/Slack/Stripe/Google/OpenAI/Anthropic、秘密鍵ブロック等）を含む書き込みを拒否、テスト削除や .skip/.only 付与を Claude では確認・Codex では拒否、npm test 2>&1 | tail のように終了コードを隠すコマンドを set -o pipefail 付きに書き換え。
- Jev（TypeSafe の判定モデル）は任意で、「この編集は CLAUDE.md のルールを破るか」「このメッセージは完了宣言か」の2問だけを担当。回答はエージェントへの注記になるか完了ゲートを緩める方向にしか働かず、ブロックの根拠にはならない。
- canny init / remove / trust / status / sessions / replay の CLI で、プロジェクト単位またはホーム単位のフック設定を管理する。

## 目的・背景

- 発端は「エージェントがテストを一度も走らせずに done と言う」問題。README は、Claude Code が heredoc でファイルを書いただけで完了報告した実例を挙げ、CLAUDE.md はモデルに覚えておくよう頼むだけで検証されない、と説明する。
- 設計原則は「事実はコードへ、判断は Jev へ、ブロックできるのは事実だけ」。ファイルが変わった／コマンドが exit 1 だった／同じ失敗が3回続いた、といった台帳で証明できる事実だけがゲートを閉じ、確率判断はゲートを開ける方向にしか使わない。
- 対象は Claude Code や Codex CLI を日常的に使う開発者。破壊的コマンドの禁止ではなく「作業が検証されたか」を見る点が、既存のガード系ツールとの違いだと位置づけている。

## 依存関係

- Node.js 22 以上と git。ランタイム依存パッケージは 0（package.json に dependencies なし、devDependencies は typescript / vitest / oxlint / prettier / @types/node のみ）。
- 配布は npm ではなく GitHub リポジトリ。コンパイル済みの dist/ が同梱されているのでビルド工程は不要。
- Jev を使う場合のみ TypeSafe の API キー（TYPESAFE_API_KEY）と https://api.typesafe.ai/v1/systemone への到達性が必要。CANNY_JEV_URL で同一リクエスト形状の別エンドポイント（ローカルモデル等）に差し替え可能。
- Jev の料金は入力 $42/10億トークン（$0.042/100万）、出力無料、既定 alias は jev-latest。キーを設定しなければ外部送信は発生しない。
- フック対象は Claude Code の settings.json 系と Codex CLI の hooks.json。Codex は初回に /hooks での信頼操作が必要。

## 実行条件

- macOS / Linux を想定。Windows はパス正規表現が '/' 前提で tests/ や .env 判定が誤動作する未修正 issue がある（#24）。
- ガードしたいプロジェクトのルートで canny init を実行してフック設定を書き込む（プロジェクト単位 or --global）。0.3.0 で追加された SessionStart フックのため、既存プロジェクトは再 init が要る。
- 状態と台帳は ~/.canny（CANNY_HOME で変更可）。フックは fail-open で、例外時は {} を返すため Canny の不具合で作業が止まることはない。
- Claude Code は Stop の連続ブロックが8回で打ち切られ、strict: true のときだけブロックを続ける。プロジェクト設定 .canny.json の verify / ignore / rules / allow は canny trust するまで無効（リポジトリ側から検査を黙って緩められないようにするため）。
- キーを設定した場合、編集差分（4,000字に切り詰め）・抽出したプロジェクトルール・エージェントの最終メッセージが TypeSafe に送信され、応答キャッシュとして ~/.canny/jev/ に残る。

## 最短手順

- エージェントに任せる場合（README の貼り付けプロンプト）: 「Install Canny (https://github.com/qkal/canny) … 1. node --version が 22 以上か確認 2. ~/.canny/src が無ければ git clone、あれば pull --ff-only 3. プロジェクトルートで node ~/.canny/src/dist/cli.js init 4. echo canny-check の後に status でイベントが記録されたか確認」をそのまま渡す。
- 手で入れる場合: git clone https://github.com/qkal/canny.git ~/.canny/src → プロジェクトルートで node ~/.canny/src/dist/cli.js init → 必要なら ln -s ~/.canny/src/dist/cli.js ~/.local/bin/canny。
- AI／自作スクリプトからフックとして呼ぶ形は node ~/.canny/src/dist/cli.js hook --agent claude（Codex は --agent codex）。フックイベント1件の JSON を stdin に渡すと判定 JSON を stdout に返す。
- 例: {"hook_event_name":"Stop","session_id":"s1","cwd":"/path/proj","stop_hook_active":false} を渡すと、未検証の編集が残っていれば {"decision":"block","reason":"Canny: … no check has passed since the last edit …"} が返る。テスト通過イベント（PostToolUse の Bash, npm test, exit 0）を挟むと次の Stop は {} になり、canny replay で両判定が再現される。
- チェックとして数えるコマンドを増やす場合はプロジェクト直下の .canny.json に {"verify": ["^just check"], "ignore": ["^generated/"], "rules": ["…"], "allow": ["test-removal"], "strict": false} を置き、canny trust を実行する。

## 変更履歴

- 2026-11-09: 初回登録
