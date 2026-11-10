---
type: "repo"
name: "gstack（Garry's Stack）"
genre: "agent-framework"
url: "https://github.com/garrytan/gstack"
repo: "garrytan/gstack"
license: "MIT"
stars: 140943
language: "TypeScript"
created: "2026-03-11"
updated: "2026-11-09"
added: "2026-11-07"
first_seen: "2026-11-07"
sources: ["https://x.com/awe0_io/status/2118663188875247930"]
flags: []
risk_notes: "① repo description と発見元の「23 tools」は現状と不一致。repo description の「23 tools」は現状と不一致で、ツリー上は <dir>/SKILL.md が 62 個（test fixture 等の入れ子を含め 77）。README の表も 23 行では収まらない。1.97 で /plan-eng-review と /investigate は廃止され、ディレクトリだけが残る（setup は入れない）。② バス係数 1: contributors は garrytan 1,013 / 次点 17 で、直近30日の commit は全件 garrytan。③ full tier は Claude Code のみ認定。Codex CLI / Cursor / Gemini / OpenClaw / Hermes 等は experimental で、/careful などの安全フックは「advisory, not blocked」＝強制されない。④ /codex と /claude-code のセカンドオピニオンはもう一方の有料 CLI へのログインが前提。⑤ バージョン刻みが極端（v1.92.55.0 → v1.96.0.0 の間に 123 版、リリースは約3日毎）で、スキル名・CLI フラグが短期間で動く。⑥ クローンは 259,677KB（約254MB）・4,959 ファイル（うち test 2,866）で重く、--depth 1 前提。⑦ macOS 推奨の Aside ブラウザは商用製品（無くても同梱 Chromium で動く）。⑧ Windows は Smart App Control が未署名バイナリを拒否（issue #2595）。⑨ 8か月で14万★は個人リポジトリとしては異常値で、独立利用の実績を示す指標ではない。"
forks: 20797
open_issues: 89
commits_30d: 100
commit_cadence: "daily"
size_kb: 264884
archived: false
fetched_at: "2026-11-09T21:33:02Z"
last_release: "v1.98.0.0"
last_release_at: "2026-11-08"
commits_90d: 100
---

# gstack — 1スプリント分の役割（CEO/設計/レビュー/QA/リリース）を Claude Code に配るスキル群

## 出来ること

- /office-hours が6つの強制質問で要件をリフレームし、design doc を書いて下流スキルに渡す（「毎日のブリーフィングアプリ」→「個人チーフオブスタッフAI」のように言い方を訂正させる）
- /plan-ceo-review（スコープ拡張/維持/縮小の4モード）、/plan-design-review（各軸0-10採点＋AI slop検出）、/plan-devex-review（TTHW測定）で実装前に計画を潰す。1.97 で /autoplan が CEO→design→DX→eng を自動で通す1コマンドになり（eng が最後）、/plan-eng-review はその eng フェーズへ統合、/investigate は eval で効果が確認できず廃止
- /plan-ceo-review には任意の停止ゲートがある（`./setup --ceo-review-gate` / `GSTACK_CEO_REVIEW_GATE=on` / `gstack-config set ceo_review_gate on`）。レビュー出力に `Findings` か `Top risks` の見出しと1始まりの番号付きリスク一覧が無いとターンを終えられない。既定は無効、3回止めると `exhausted` で通す
- /review が「CIは通るが本番で壊れる」バグを探し、明白なものは自動修正。弱められたテスト・タイムアウト・抑制は人名付きで人間に上げる
- /qa が実ブラウザ（Aside か同梱 Chromium）を操作して再現→失敗する回帰テスト→原因修正→再検証。/qa-only は報告のみ。Webページの無い CLI/API/ジョブ/Webhook も対象
- /ship → /land-and-deploy でテスト・カバレッジ・ドキュメント監査→PR→マージ→CI待ち→デプロイ→本番ヘルス確認まで一本
- /cso が OWASP+STRIDE の静的監査（Docker があれば限定実行スキャンと修正候補まで）
- /browse /scrape /make-pdf /diagram /design-* は同梱の実行バイナリ（browse・pdf・design）で動く。プロンプトだけでなく実コードがある
- チームモード: リポジトリに required フックを置くと、同僚の Claude Code も自動で gstack を使う（stable チャンネル＝月木のタグ付きリリース、最短72時間間隔・重要修正は約1日以内）
- 1.97 から新規インストールの既定は stable チャンネル（main の全マージを追わない）。contributor のチェックアウトと Capy 機は main。`gstack-config set update_channel main|stable` で切り替える
- /learn と GBrain 連携でプロジェクト固有の学習をセッション跨ぎで蓄積

## 目的・背景

- YC の CEO である Garry Tan が自分の開発フローをそのまま公開したもの。README が明言する通り「process, not a collection of tools」で、本体はツール群ではなく Think → Plan → Build → Review → Test → Ship → Reflect の順序と、段間の受け渡し（design doc が plan 系に、test plan が /qa に流れる）の規定。単発プロンプト集との違いは、各スキルが前段の成果物を読む前提で書かれている点と、/browse などの実バイナリを同梱している点。

## 依存関係

- Claude Code（full tier の唯一の認定ホスト）、Git、Bun 1.3.3 以上（CI テスト済みは 1.4.2。1.3.3 未満は setup が拒否）
- Windows は Bun に加えて Node.js 必須（Bun の Playwright パイプ不具合 bun#4253 の回避）
- 他ホストは `--host <name>`: codex / opencode / cursor / factory / kiro / copilot / agy / gemini / openclaw / hermes。すべて experimental（フックは advisory のみ）
- セカンドオピニオン（/codex, /claude-code）は相手側 CLI へのログインが前提
- ブラウザ系: macOS 15+ の Aside（任意・商用）→ 無ければ同梱 Chromium。/setup-browser-cookies はフォールバック時のみ
- /cso の実行スキャンは Docker、ネイティブ側はツールチェーン（Windows は VS2022 Build Tools + PowerShell）
- /design-motion は ffmpeg。GBrain は別リポジトリ（garrytan/gbrain）

## 実行条件

- macOS / Linux が full サポート。Windows は Git Bash か WSL で「インストールとコアスキルのみ」
- ディスク約258MB（264,280KB、4,949ファイル）。--depth 1 の単一ブランチクローンが前提
- Claude Code 側の有料プラン/API キー。gstack 自体は MIT・無料（premium tier なし）
- ネットワーク: 更新チェックは既定 ON（`gstack-config set update_check false` で停止）、テレメトリは既定 OFF、外部レビューは既定 ON（初回に通知、`codex_reviews disabled` で停止）。外部送信は `gstack-egress list` で監査可能
- Linux で Chromium が起動しない場合（Ubuntu 24.04+ の AppArmor）は GSTACK_CHROMIUM_NO_SANDBOX=1

## 最短手順

- Claude Code で: `git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup`
- CLAUDE.md に gstack セクションを追加（`/browse` を全ブラウジングに使い、`mcp__claude-in-chrome__*` を使わない、の2行だけでよい。スキル一覧は Claude Code が自分で列挙する）
- Claude Code を再起動 → `/office-hours` に作りたいものを話す → `/review` → `/qa <staging URL>` の順で試す
- 他ホスト（Hermes 等）: `git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/gstack && cd ~/gstack && ./setup --host hermes`（全部入れるなら `--host auto`）→ `./setup --status` で導入先とバージョンを確認
- 困ったら `~/.claude/skills/gstack/bin/gstack-doctor`（チェック毎に ok/warn/not configured/fail と修正コマンドを出す。fail 以外は exit 0）
- 任意: チームモード `./setup --team && bin/gstack-team-init required` でリポジトリ側に必須化を仕込む

## 変更履歴

- 2026-11-07: 初回登録
- 2026-11-07: v1.97.0.0。/plan-eng-review と /investigate の廃止（/autoplan の eng フェーズへ統合、/investigate は eval で効果なし）、/plan-ceo-review の任意停止ゲート、新規インストール既定の stable チャンネル化、playwright 1.65 への更新を反映
