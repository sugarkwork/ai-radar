---
type: "link"
name: "Claude Code カスタムサブエージェント（公式ドキュメント）"
genre: "coding-agent"
url: "https://code.claude.com/docs/en/sub-agents"
author: "Anthropic"
pricing: "paid"
pricing_detail: "Claude Code は Free プラン非対応。Pro $20/月（年払い $17/月・$200 一括）、Max $100/月、Ultra $200/月。API のトークン従量課金でも利用可。"
signup_required: true
source_post: "https://x.com/sumika45379/status/2113106822983032965"
sources: ["https://code.claude.com/docs/en/sub-agents", "https://claude.com/pricing", "https://x.com/sumika45379/status/2113106822983032965"]
first_seen: "2026-10-22"
added: "2026-11-08"
flags: ["unverified"]
risk_notes: "投稿の数値と効果の主張は著者の体験談で、一次情報の裏付けがない。「3体で合計32万7千トークン」「親に戻ったのは報告3本だけ」「5行制限のおかげで親の会話が小さいまま」は @sumika45379 の要約（元投稿は @0xbobaaa）であり、独立した検証はない。公式ドキュメントが説明するのは「各サブエージェントは独自のコンテキストウィンドウで動き、要約だけを返す」という仕組みまでで、節約量や報告行数の効果は保証していない。「返事は5行まで」はエージェント本文（システムプロンプト）に書く指示であって、Claude Code が行数を強制する機能ではない。引用元 https://x.com/0xbobaaa/status/2107892817292939588 は t.co 解決が 404 で、本文・動画・元の定義ファイルを確認できない（配布リポジトリは存在しない）。添付画像 https://pbs.twimg.com/media/HWWvkhaa4AAPVqD.jpg は origin_post_id=2118292245107683494 の画像で、vision で見た結果 .claude/agents ではなく benjitaylor/skills の stageshow（製品画面デモ用スキル）の解説画像だった。本候補の根拠には使っていない。料金は 2026-11-08 時点の claude.com/pricing で確認。ドキュメントは 2026-11-03 更新。"
fetched_at: "2026-11-08T17:36:08Z"
---

# Claude Code カスタムサブエージェント

## 目的

- メイン会話を検索結果・ログ・ファイル内容で埋めずに、副作業を別コンテキストの専用エージェントに任せ、要約だけ受け取るための公式の仕組み。
- 同じ種類の作業を何度も同じ指示で発生させているなら、その指示を .claude/agents/ の1ファイルに固定して再利用できる。

## 何ができるか

- .claude/agents/<name>.md（プロジェクト単位）または ~/.claude/agents/<name>.md（全プロジェクト共通）に、Markdown 本文と YAML frontmatter を1枚置くだけで定義できる。必須は name と description のみ。
- description を手がかりに Claude が委譲先を判断する。ファイル本文がそのままサブエージェントのシステムプロンプトになり、Claude Code 本体のシステムプロンプトは渡されない。
- tools に Read, Edit, Bash のように許可ツールを列挙して権限を絞れる。model、permissionMode、maxTurns、mcpServers、hooks、skills、isolation: worktree なども frontmatter で指定できる。
- 各サブエージェントは独自のコンテキストウィンドウで動き、親の会話には結果の要約だけが返る。バックグラウンド実行が既定で、作業を続けながら並行して走らせられる（同時実行の既定上限は20）。
- 定義ファイルの追加・編集は数秒で反映される。ただし新しく agents ディレクトリを作った場合はセッションの再起動が必要。
- 配布はプロジェクトの .claude/agents/ を Git にコミットする方法のほか、プラグイン、--agents の JSON、組織の managed settings でも行える。

## 料金

- Claude Code は Free プランに含まれない。Pro $20/月（年払いなら $17/月相当・$200 一括）、Max $100/月、Ultra $200/月。
- API 経由ならトークン従量課金。サブエージェント自身のリクエストもメイン会話と同じ利用上限・課金に計上されるため、並行実行するとその分消費が増える。
- ドキュメントの閲覧自体は無料。

## 登録の要否

- 利用には Claude アカウントと Claude Code が使えるプラン（Pro 以上）、または API キーが必要。
- 読むだけなら登録不要。プロジェクトの .claude/agents/ に置く定義はリポジトリにコミットすればチームで共有できる。

## 変更履歴

- 2026-11-09: 初回登録
