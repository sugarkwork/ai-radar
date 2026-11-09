---
name: "Remotion Agent Skills"
genre: "link-asset"
url: "https://www.remotion.dev/docs/ai/skills"
author: "Remotion"
pricing: "free"
pricing_detail: "スキルは無料。Remotion 本体は個人・従業員3人以下の組織なら商用利用も無料。それを超える営利組織は Company License（Automators: $0.01/レンダー・月$100〜、Creators: $25/月/シート）、Enterprise は月$500〜（2026-11-09 時点）"
signup_required: false
flags: ["unverified"]
risk_notes: "投稿は『Anthropic が動画制作の5段階ワークフローを公開した』と主張するが、Anthropic の Claude Opus 5.5 発表（2026-09-22）に該当する記述はなく、一次情報で確認できない。実際に公式提供されているのは Remotion の Agent Skills で、投稿の手順はそれを Claude Code で使う第三者の再構成とみられる。投稿の『step-by-step breakdown』リンクはログイン必須の X 記事で本文未確認。添付動画は Claude Code 風の時計仕掛けダッシュボードを Remotion で描いた作例で、プロンプトや手順は写っていない。"
type: "link"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/Bober_smart/status/2113694502183420368"]
fetched_at: "2026-11-09T07:06:51Z"
---

# Remotion Agent Skills — コーディングエージェントにRemotionの作法を教える公式スキル

## 目的

- Remotion（React コンポーネントを MP4 に書き出す動画フレームワーク）の公式 Agent Skills。Claude Code / Codex / Kimi Code / Cursor などに読み込ませ、動画コードを自己流で書かせず、フレームワークの作法どおりに生成させるために使う。

## 何ができるか

- `npx skills add remotion-dev/skills` または `gh skill install remotion-dev/skills` で導入する。`bun create video` / `npx create-video@latest` でもプロジェクト作成時に追加できる。
- スキルはプロジェクト作成、コンポジション設計、アニメーション・レイアウト・タイポグラフィ・メディア要素、字幕、地図アニメーション、Studio でのプレビュー、レンダリング、既存プロジェクトのアップグレードまでをカバーする。
- Remotion のドキュメントは各ページを Markdown で取得できるため、エージェントに URL を渡して最新の API を読ませられる。
- 生成物は Remotion Studio でフレーム単位に確認し、`npx remotion render` で MP4 に書き出せる。

## 料金

- スキルの利用は無料。
- Remotion 本体は個人と従業員3人以下の組織なら商用利用も無料。
- それを超える営利組織は Company License が必要。Automators は $0.01/レンダー・月$100〜、Creators は $25/月/シート、Enterprise は月$500〜。

## 登録の要否

- 不要。npm / GitHub から取得でき、アカウント登録なしで使える。Node.js と Remotion プロジェクトは別途必要。

## 変更履歴

- 2026-11-09: 初回登録
