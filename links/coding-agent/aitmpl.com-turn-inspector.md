---
name: "Turn Inspector"
genre: "coding-agent"
url: "https://www.aitmpl.com/component/mods/ui/turn-inspector"
pricing: "free"
pricing_detail: "無料。配布元 davila7/claude-code-templates は MIT ライセンス（GitHub API で license.spdx_id = MIT を実測）。aitmpl.com には /pricing が存在せず（HTTP 404）課金ページはない。`npx` で取得するだけでアカウント登録は不要（Claude Code 本体の契約・認証は別途必要）。"
signup_required: false
author: "Daniel Avila (davila7)"
flags: ["unverified"]
risk_notes: "確認できたこと: aitmpl.com の製品ページ（HTTP 200）に仕様・オプション・導入コマンド・バージョン要件が記載され、配布リポジトリの README と一致する。デモ動画を取得してフレームを確認し、右側ペインに「Context window 58.5k / 1.0M 6%」と system / earlier / new / output の内訳バー、#1 answer 54.1k / #2 1x Read 54.2k / #3 answer 58.5k のようなターン行が実際に映っていることを目視確認した。未確認のこと: トークン削減などの効果数値は存在せず、著者の「重くなった原因を勘で探さずに済む」という主張のみ。Claude Desktop のサイドパネル表示とバージョン範囲（2.1.287+ で既定有効、2.1.259〜2.1.286 は環境変数が必要）はドキュメント記述のみで、当環境では実機検証していない。本 Mod は表示・観測専用でコンテキストを減らす機能はない。"
type: "link"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/opensourcelab9/status/2113238959862284769"]
fetched_at: "2026-11-08T18:31:27Z"
---

# Turn Inspector — Claude Code のコンテキスト内訳をターン単位で見る Mod

## 目的

- Claude Code のセッションで、モデルへのリクエスト（ターン）ごとにコンテキストウィンドウが何にどれだけ使われたかを横ペインで可視化する。
- 会話が重くなった原因を勘で探すのではなく、システムプロンプト・過去ターン・新規入力・出力の内訳として確認するための観測ツール。

## 何ができるか

- ペイン上部にコンテキスト使用量（トークン数・％・バー）を表示し、バーを system / earlier / new / output に色分けする。
- ターンごとに1行を表示し、プロンプト単位でグルーピングする（1つのプロンプトがツール往復で複数リクエストになるため）。行には「2× Read, Bash」「answer」「cut off」のような応答内容と、その時点の使用量が並ぶ。
- 行を展開すると内訳が見える: System, tools & memory / Earlier turns / User message / Tool result · <tool> / Thinking / Text response / Tool use / Cut off。
- 数値は API の usage に基づく実測（input = uncached + cache read + cache write）。「~」付きは推定で、エンジンがリクエスト単位の合計しか返さないため約4文字/トークンで各ブロックに按分している。
- コマンド: `/turns` で開く、`/turns clear` で記録済みターンを消す、`/turns stop` で閉じる。既定では最新ターンに追従して展開状態を保つ。
- オプション（settings の pluginConfigs 配下）: `columns`（既定 56、36〜120）、`maxTurns`（既定 200、古い順に破棄）、`openOnStart`（既定 false）。
- 表示位置: フルスクリーンレイアウト（`/tui fullscreen`、110桁以上のターミナル）ではトランスクリプト横にドック、クラシックレイアウトではプロンプト上。Claude Desktop ではセッションのサイドパネルに描画。
- 導入は `npx claude-code-templates@latest --mod ui/turn-inspector` の1行。`.claude/skills/turn-inspector/` に書き込まれ、trusted なプロジェクトで `turn-inspector@skills-dir` として自動ロードされる。単発なら `claude --plugin-dir .claude/skills/turn-inspector`。
- 動作要件: Mods は Claude Code 2.1.287+ で既定有効。2.1.259〜2.1.286 では `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1` が必要。2.1.296 でテスト済み（リポジトリ内の 2.1.283 宣言に対して）。npx で導入するため Node.js 環境が前提。
- 観測専用で、フックはイベントをそのまま通過させる（セッションの挙動を変えない）。サブエージェントのリクエストは一覧に出ない（別の agent-flow Mod の担当）。

## 料金

- 無料。配布元リポジトリ davila7/claude-code-templates は MIT ライセンス（GitHub API の license.spdx_id = MIT で確認）。
- aitmpl.com に /pricing ページは存在せず（HTTP 404）、課金・有料プランの導線はない。
- npx でそのまま取得でき、アカウント登録や API キーの用意は不要。ただし Claude Code 本体の利用契約（Anthropic のサブスクリプションまたは API）は別途必要。

## 登録の要否

- 登録不要。`npx claude-code-templates@latest --mod ui/turn-inspector` を実行するとファイルが `.claude/skills/turn-inspector/` に展開されるだけで、サインアップやログインは求められない。
- 設定はユーザー設定または管理設定の `pluginConfigs["turn-inspector@skills-dir"].options` に置く（`--plugin-dir` で読み込む場合は `"turn-inspector"`）。
- プロジェクトが trusted である必要がある。`/turns` が候補に出ない場合は Mod が未ロードなので、`claude --debug` の `~/.claude/debug/latest` で `hooks module turn-inspector@… loaded` を確認する。

## 変更履歴

- 2026-11-09: 初回登録
