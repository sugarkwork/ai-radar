---
repo: "tamaratran/fast-jev-compaction"
name: "fast-jev-compaction"
genre: "coding-agent"
url: "https://github.com/tamaratran/fast-jev-compaction"
license: "MIT"
stars: 7917
language: "TypeScript"
created: "2026-09-17"
updated: "2026-09-18"
forks: 581
open_issues: 125
commits_30d: 0
commit_cadence: "monthly"
commits_90d: 30
size_kb: 245
archived: false
flags: ["unverified"]
risk_notes: "【主張と実体の差分】投稿の主張は概ね実装と一致するが、3点ずれる。(1)「Jev が古いと採点」— 実装は『古さ』を直接採点せず、call_<id>（呼び出しを残すべきか）と result_<id>（結果を逐語で残すべきか）の2つの noul 確率を閾値0.5で切るだけ。年齢や使用済みかどうかの特徴量は入力に明示されない。(2)「何も書き換えない／一字一句そのまま」— 保持された項目は同一オブジェクトで返るが、結果だけ不要と判定された場合は先頭300文字＋注記に切り詰められる（削除ではなく改変）。Jev に送る state も 25k トークンに収めるため段階的に省略される。(3)「npm ライブラリとしても使える」— npm の fast-jev-compaction は latest 0.4.1 を 2026-09-24 に maintainer aleksvega が公開した第三者フォークで、README に『Fork of tamaratran/fast-jev-compaction』と明記され、jev-compact / jev-gate など別 CLI を含む。リポジトリ側 package.json は 0.2.0、plugin.json は 0.3.0 で、このリポジトリのコードがそのまま npm 名で配布されているわけではない。【実績の不自然さ】stars 7,917 / forks 581 / open issues 125 に対し、コミットは全30件が 2026-09-17〜18 の2日間のみ、直近30日は0件、リポジトリは34ファイル・245KB。contributors に devin-ai-integration[bot] が入り、主要コミットは Devin AI 共著。数字の大きさと開発量・更新停止が釣り合わず、star の真正性は未確認（不正と断定はできない）。【有効性】作者による削減率・精度のベンチマークは未公開（issue #160 が benchmarks を求めて起票、回答なし）。第三者の計測（issue #154）は AUC 0.70〜0.83 で順位は安定するが、fitState() の段階で絶対スコアが 0.25〜0.80 に動き、固定閾値0.5だと全保持（実質無効）や過剰削除になりうると報告。issue #65 は『narration は残り根拠が消える』過剰削除を報告。【デモ】投稿の14秒動画を取得しフレームを確認したところ、GitHub の README をスクロールする画面で、API を叩いた実行記録ではなかった。リポジトリ同梱の SwiftUI デモも README に『It never calls the API; it exists to be screen recorded.』と明記され、演出用。【依存・権利】MIT（LICENSE は Copyright (c) 2025）。TypeSafe の有料 API が必須で、無料枠や無償トークンは未確認。Claude Code の function hooks は早期アクセスで仕様変更リスクあり（hooks/README.md 自身が明記）。issue #151 / #153 では Team 組織や SDK・ヘッドレス環境で session.compact が使えない報告があり、環境により動作しない可能性。【未確認】作者自身の効果測定、star の真正性、TypeSafe の無料枠、Claude Code 2.1.274 以外での動作。"
type: "repo"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/sumika45379/status/2112672741140955231"]
fetched_at: "2026-11-08T14:15:41Z"
---

# fast-jev-compaction — 要約せずにツール記録だけを削る Claude Code 用コンパクション

## 出来ること

- Claude Code の /compact と自動圧縮を、要約ではなく「元のメッセージ列から不要なツール呼び出しと結果だけを削除した履歴」に置き換える。
- ツール呼び出しごとに TypeSafe の判定モデル Jev へ yes/no の確率を2問（呼び出しを残すか、結果を逐語で残すか）投げ、既定の閾値0.5以上なら保持する。
- 結果だけ不要と判定された場合は、結果を先頭300文字＋1行の注記に切り詰める。呼び出しごと不要なら呼び出しと結果をまとめて削除する。
- ユーザー／アシスタントの本文テキストは削除も要約もせず、順序を保ったまま残す。
- TypeScript ライブラリとしても使え、compact() / compactMessages() に任意のトランスクリプトを渡せる。HTTP 層は JevAsker インターフェースで差し替え可能。
- Jev 呼び出しの失敗、応答不正、キー未設定、履歴が状態予算に収まらない場合は例外を投げ、Claude Code 側は標準の要約コンパクションへフォールバックする。

## 目的・背景

- 通常のコンテキスト圧縮は LLM に古い往復を要約させるため、ファイルパス・正確なエラー文・守るべき制約が落ちる。fast-jev-compaction は「何も書き換えず、Jev が不要と判断したツール呼び出し／結果だけを消す」ことで、直していたエラー文などを逐語のまま残そうとする。発端は RoundtableSpace（@RoundtableSpace）の投稿で、同アカウントは「Normal compaction asks an LLM to summarize old turns, and summaries lose file paths, exact errors, and constraints」と主張している（https://x.com/RoundtableSpace/status/2110819247001923688）。ただしこれは宣伝投稿であり、独立した評価ではない。設計上、Jev に渡す state 自体は 25k トークンに収めるため段階的に省略・短縮される（モデルが見る入力は原文全文ではない）。

## 依存関係

- Node.js 18 以上。TypeSafe の API キー（環境変数 TYPESAFE_API_KEY かプラグイン設定 apiKey）が必須で、https://api.typesafe.ai/v1/systemone への到達性が要る。Jev の料金は入力 $42/Btok（$0.042/Mtok）、出力無料。Claude Code 側は function hooks の早期アクセス機能（型定義は 2.1.274）で、CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1 を設定する必要がある。実行時の npm 依存はなく、開発用に vitest / tsx / typescript のみ。

## 実行条件

- TypeSafe のアカウントとキー、外部 HTTPS 通信が前提。圧縮対象は pinned（最初のメッセージと直近6メッセージ）以外のツール呼び出しだけで、テキストは対象外。履歴が短い、または推定削減率が既定25%未満だと標準要約にフォールバックする。Jev へは会話全体を state として毎リクエスト再送するため、履歴が 25k トークン上限に近いとリクエスト数が増える。トークン数はトークナイザではなく文字数からの推定。

## 最短手順

- ライブラリとして使う場合: `npm install fast-jev-compaction` の後、`import { compactMessages } from 'fast-jev-compaction'` で `const r = await compactMessages(messages, { preserveRecentMessages: 4 })` を呼ぶ。TYPESAFE_API_KEY を環境変数に置く。Claude Code プラグインとして使う場合: `~/.claude/settings.json` の env に CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1 と TYPESAFE_API_KEY を書き、`claude plugin marketplace add tamaratran/fast-jev-compaction` → `claude plugin install fast-jev-compaction@fast-jev-compaction` を実行して再起動または /reload-plugins。チェックアウトから試すなら CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1 claude --plugin-dir . 。

## 変更履歴

- 2026-11-09: 初回登録
