---
repo: career-ops-hq/career-ops
name: career-ops
genre: other
url: https://github.com/career-ops-hq/career-ops
license: MIT
stars: 81473
language: JavaScript
created: 2026-04-04
updated: "2026-11-09"
added: 2026-11-05
first_seen: 2026-11-04
source_post: https://x.com/thegreatest_sv/status/2117687388214272339
sources: []
flags: []
risk_notes: "求人ボードの公開ATSフィードを読む。各サイトの利用規約に従うこと。CV・応募先などの個人情報をローカルに保存するため、ワークスペースの管理には注意。"
forks: 14978
open_issues: 442
commits_30d: 100
size_kb: 132913
archived: false
commits_90d: 100
commit_cadence: "daily"
fetched_at: "2026-11-09T21:40:45Z"
last_release: "career-ops-v1.39.0"
last_release_at: "2026-11-05"
---

# career-ops

## 出来ること

- 求人応募の**前段**（探索 → 評価 → 書類作成）をAIエージェントで回す。求人ボード／ATSのフィードを走査し、CVと照合して各求人を1〜5で採点する。
- 評価は A–H の8ブロック構成。役割要約、CV一致度（要件ごとの重みと、その重みがJD本文・構造・推定のどれ由来かを明示し、推定は最上位に置けない）、レベル戦略、報酬調査、パーソナライズ、面接準備（STAR+R）まで含む。
- ブロックGで「掲載がまだ有効か／再投稿か」を**観察として**記録する。就労資格（スポンサー不可の明記など）はハードブロッカーとして扱う。
- ATS向けの履歴書・カバーレターを求人ごとに調整。**応募の送信は自動化せず、提出ボタンは人間が押す**設計。
- 応募トラッカー（`pipeline.md`）とTUIダッシュボード。LinkedInの求人アラートメールを貼り付けて取り込む導線もある（`node linkedin-import.mjs`、Googleアカウント不要）。
- 応募の**後**も扱う（v1.39）。面接招待を貼ると課される条件（AI使用不可・録画・カメラON・ID提示・パネル形式）を列挙し、確認メールの下書きを作る（送信は本人）。`panelist-roles.mjs` は面接官を役割で分類し、面接中に聞いた優先事項を次のラウンドの計画に引き継ぐ。
- 英国の Skilled Worker スポンサー免許の登録簿と応募先を照合する `sponsor-check.mjs` がある（読み取りのみ、`--tracker` でトラッカー内の企業をまとめて確認）。CV は自分が書いていない定型句やダッシュを検出すると PDF / LaTeX 出力を止める。
- README は16言語（日本語・韓国語・中国語ほか）で用意されている。

## 目的・背景

作者 @santifer が自分の転職で使ったものを公開したもの。README には「740件を評価し68件に応募、12面接・1内定」という本人の記録が書かれている。企業側のAIスクリーニングに対し、候補者側が応募先を**選ぶ**ためのAIという位置づけ。

## 依存関係

- Node.js（`npx` で導入するため）。
- Playwright の Chromium はPDF生成と求人の死活確認（`--verify`）で使う。未導入でも走査自体は動く。
- データはローカルのワークスペースに置かれ、Codex / OpenCode / Claude Code などのエージェントCLIから操作する。

## 実行条件

- 初回は `npx @santifer/career-ops init` でワークスペースを作る。以降の操作はエージェントに読み込ませたスキル側で行う（CLIのコマンドは `init` のみ）。
- `node scan.mjs` はATSフィードの返答をそのまま信じるため、閉じた求人が残ることがある。`--verify` を付けるとPlaywrightで生存確認して落とす（トークン消費なし）。
- 求人サイトの規約に従う。★8万・fork 1.4万と大きい一方、open issue も450件超ある。
- 評価スクリプトが LLM に送る氏名・メール・電話・プロフィールリンクは、`config/profile.yml` の `privacy.redact_contact_info: true` で伏せられる（opt-in、対象は Gemini / OpenAI / OpenRouter の評価スクリプトのみ）。`config/privacy.yml` に書いた値は送信前にリクエスト自体を止める。

## 最短手順

```bash
npx @santifer/career-ops init      # ./career-ops に展開し依存を導入
cd career-ops && npm install
npx playwright install chromium    # PDF生成・--verify を使う場合
node scan.mjs --verify             # 求人走査＋掲載の死活確認
npm run serve:dashboard            # TUIダッシュボード
```

以降はエージェント（Claude Code / Codex / OpenCode）でワークスペースを開き、求人評価と書類作成を行う。

## 変更履歴

- 2026-11-05: 初回登録（★80,253 / pushed 2026-11-05 / MIT / career-ops-v1.38.0）
- 2026-11-05: v1.39.0 — 面接招待の条件抽出・パネル分類・確認メール下書き（`invite-match.mjs` / `panelist-roles.mjs`）、CV の定型句検査、英国スポンサー照合（`sponsor-check.mjs`）、連絡先の伏せ字（opt-in）、求人プロバイダ16種追加（cd37937）
