---
name: "AIの出力がバラバラにならなくなる、Pydantic AIの「型で縛る」使い方"
genre: "article"
url: "https://x.com/i/article/2106661615588327424"
published: "2026-10-23"
author: "opensourcelab9"
flags: []
risk_notes: "公開日は投稿のcreatedAt（2026-10-23T23:38:27Z）ベース。記事ページは非ログインでログイン画面へ飛ぶため、記事側の独立した公開日は未確認。記事のstars 20,375とv2.54.0は執筆時点（2026-10-03）の値で、2026-11-09時点は21,099 stars・最新v2.66.0。READMEのモデル名は現在 openai:gpt-6.1-sol に変更済み。Issue #1192はnot_plannedで閉じた利用者報告であり、リトライ枯渇の仕様根拠としては弱い。記事はコード未実行を明記。末尾と中盤にLINE登録の配布導線あり。"
type: "article"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/opensourcelab9/status/2113777101186969610"]
fetched_at: "2026-11-09T08:44:06Z"
---

# AIの出力がバラバラにならなくなる、Pydantic AIの「型で縛る」使い方

## テーマ

- X（@opensourcelab9）の日本語長文記事。2026-10-23公開。Pydantic AI公式READMEの「Data extraction」節にある感情判定サンプルを題材に、LLMの出力を型で縛る利点と限界を解説する。
- 題材のコードは `class Sentiment(BaseModel)` に `label: Literal['positive','negative','neutral']` と `score: float = Field(ge=-1, le=1)` を置き、`Agent(..., output_type=Sentiment)` に渡してレビュー取得ツールを1つ持たせるだけの短い例。
- 想定読者はPythonでAIの分類・採点結果を表やDBへ流している人。対象はPydantic AI（Python、MIT、2026-11-09時点 stars 21,099）。

## 著者の主張

- 指示を磨いてもモデルを替えても表記ゆれや範囲外の値が止まらないなら、足りないのは指示ではなく「受け取る値の形を先に決めること」。
- 型が保証するのは形と範囲だけ。3値のどれかで点数が範囲内であれば、皮肉をpositiveと判定しても型としては通る。内容の正しさは別に検査が要る。
- 検証が走らない経路がある。JSONスキーマを辞書で渡す `StructuredDict` は受け取ったJSONを検証せず、スキーマ解釈はモデル任せ（公式ドキュメントに明記）。Issue #9270では enum 外の値がそのまま返る例が報告されている。
- 検証に通らない状態が続くと、やり直しの回数を使い切ってエラーで止まる（記事はIssue #1192を引く）。やり直しは既定1回で、`Agent(retries={'output': N})` で変更できる。
- ツールの引数も、ツール本体が動く前に型で検証される。入口のミスも早く見つかる。
- 型の確認はAPIキー不要の `TestModel` で、内容の確認は正解付きの入力を数十件そろえて人が照合する。この2段に分けるのが業務接続の近道、というのが記事の結論。

## 裏取り・注意点

- README一致: v2.54.0 時点のREADMEは記事のコードと一致（モデル名 `openai:gpt-6-sol`、Sentiment定義、出力例 `label='positive' score=0.9`）。ただし現在のmainではモデル名が `openai:gpt-6.1-sol` に変わっており、記事のコードをそのままコピーすると古い。
- StructuredDict: 公式Outputドキュメントに「Pydantic AI will not perform any validation of the received JSON object and it's up to the model to correctly interpret the schema」と明記。記事の記述は正確。
- やり直し回数: 同ドキュメントに「The budget defaults to 1」と明記。既定1回という記事の記述は正確。
- テスト: Testingガイドは `TestModel` を「the simplest and fastest way」と位置づけ、モデル呼び出し・APIキーなしで動く。記事の記述は正確。
- 数値の現在値: 記事の「20,375 stars（2026年10月3日取得）」は執筆時点の値。2026-11-09取得のGitHub APIでは 21,099 stars / 3,136 forks。記事の「同日v2.54.0公開」も実在し、v2.54.0 の published_at は 2026-10-03T03:21:28Z。ただし最新は v2.66.0（2026-11-04）。
- Issue #1192 は「Structured output validation keeps failing」という利用者の不具合報告で、2025-08-15に not_planned でクローズ済み。リトライ枯渇時の挙動の一次根拠としては弱く、仕様は公式ドキュメント側で確認するのが確実。
- Issue #9270 は機能要望（open, reopened, duplicate/enhancement ラベル）。StructuredDict に検証が無いことの傍証としては使えるが、仕様の一次記述ではない。
- 記事内の画像は記事自身が作った説明図（「出力を流す前に形を決める」「ラベルがゆれる／点数が範囲外」「受け取る値の形を先に決める」と label 3値・score の -1〜1 スライダー）で、公式ドキュメントのスクリーンショットではない。図は主張の要約であり、独立した裏付けにはならない。
- 記事は「この記事ではコードを動かしていません」と明記しており、positive/0.9 はREADMEの出力例の引用。再現性・費用は未検証。
- 記事の中盤と末尾にLINE友だち追加の導線があり、公式サンプル10本のカード配布へ誘導している。記事単体では完結せず、続きは配布物側。
- 記事本文は非ログインでは取得できない（記事URLはHTTP 200だがログイン画面へリダイレクト）。本文はローカルの取得ツールおよび封筒の articleText を根拠にした。公開日も投稿の createdAt（2026-10-23T23:38:27Z）ベースで、記事ページ側の独立した公開日は未確認。
- 参照している第三者のZenn記事（sog4be「Pydantic AI 本番運用半年」2026-04-28）は実在を確認したが、Qiitaの model_validator 記事（2026年3月）は本文突合まで未実施。

## 出典

- 記事: https://x.com/i/article/2106661615588327424
- 投稿: https://x.com/opensourcelab9/status/2113777101186969610
- Pydantic AI リポジトリ: https://github.com/pydantic/pydantic-ai
- README Data extraction（v2.54.0）: https://raw.githubusercontent.com/pydantic/pydantic-ai/v2.54.0/README.md
- 公式ドキュメント Output: https://pydantic.dev/docs/ai/core-concepts/output/
- 公式ドキュメント Testing: https://pydantic.dev/docs/ai/guides/testing/
- Issue #9270: https://github.com/pydantic/pydantic-ai/issues/9270
- Issue #1192: https://github.com/pydantic/pydantic-ai/issues/1192
- リリース v2.54.0: https://github.com/pydantic/pydantic-ai/releases/tag/v2.54.0

## 変更履歴

- 2026-11-09: 初回登録
