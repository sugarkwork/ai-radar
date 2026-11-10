---
repo: "fulcradynamics/agent-skills"
name: "Fulcra Agent Skills"
genre: "rag"
url: "https://github.com/fulcradynamics/agent-skills"
author: "Fulcra (fulcradynamics)"
license: "unknown"
stars: 16
language: "Python"
created: "2026-05-26"
updated: "2026-11-06"
forks: 11
open_issues: 38
commits_30d: 10
commit_cadence: "weekly"
commits_90d: 79
size_kb: 1237
archived: false
last_release: ""
last_release_at: ""
flags: ["unverified"]
risk_notes: "未確認・要注意: (1) ライセンス。GitHub API の license は null（リポジトリ直下に LICENSE ファイルが無く、/license も404）だが、README 末尾と全 SKILL.md の frontmatter は MIT と明記している。APIのSPDXが未検出のため frontmatter は unknown とし、MIT を正式な許諾条件として断定しない。(2) 投稿が書く「1フォルダだけ読み取り専用で渡す」は、共有コマンド（share create の --data-type / --file / --user-id / --group-id、permissions[].allowed_fulcra_userid）と、受信側が file download で読む運用までは確認したが、フォルダ単位の読み取り専用ACLを1コマンドで付ける仕様は一次情報で確認できていない。(3) `npx skills add fulcradynamics/agent-skills` は未実行（README記載のコマンドをそのまま転記）。(4) 効果に定量データは無く、README・公式サイトの説明はベンダー自身の主張。(5) 20本のスキルのうち fulcra-memory / fulcra-workspaces / fulcra-prefs / fulcra-connect / fulcra-get-started / connect-our-agents / fulcra-agent-groups / fulcra-situational-awareness のみ本文を読み、残りはREADME要約とファイル一覧までの確認。"
type: "repo"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/sumika45379/status/2113469217362333991"]
fetched_at: "2026-11-09T21:42:11Z"
---

# Fulcra Agent Skills — エージェントの記憶と共有文脈をFulcraに置くSKILL.md集

## 出来ること

- エージェントの記憶をFulcraのファイルストアに書き出す。1エージェントごとに `agent/<agent-name>/` を作り、`index.md`（目次）、`log.md`（更新履歴）、`progress.md`（直近の作業と次にやること）、`role.md`（役割・手順）、`session/`（セッション要約）、`task/`（複数セッションにまたがる作業）、`knowledge/`（参考知識）、`inbox/`（非同期の受け取り）をOKF形式のMarkdownで維持する。
- 同じパスへの再アップロードが版として積まれるため、`file stat` で履歴を見て `restore_file(version_id)` で前の状態に戻せる。巻き戻す前には必ず新しいバックアップを取る運用がSKILL.mdに書かれている。別エージェントへの記憶の複製（clone）は fulcra-agent-backup 側の担当。
- セッション開始時の“記憶の読み直し”を自動化する。`data-updates "1 day"`（MCPでは `get_data_updates`）で直近に変わったファイルと取り込みデータを一覧し、必要なら該当ファイルだけ読む。全ファイルを毎回ダウンロードしない設計。
- 同一アカウント内の複数エージェントを `workspace/<name>/` で協調させる。`index.md` に目的と参加者、`MomentAnnotation/<uuid>` チャネルにJSONエンベロープ（message_id・送信者・宛先・topic・in_reply_to）を文字列で記録し、返信は同じtopicを引き継ぐ。役割・タスク・セッションもファイルで残る。
- アカウントをまたぐ受け渡しは connect-our-agents（1接続につき自分のチャネル1本だけを、指定した相手にだけ共有。相手のアカウントの他のデータは見えない）と fulcra-agent-groups（各エージェントが自分のoutboxをグループへ共有）で行う。ファイル単体は `share create --file <path> --user-id <相手>` で共有し、受信側は `file download` で読む。
- 嗜好の記憶（fulcra-prefs）は `MomentAnnotation` の「User Preference」に key/value/scope/strength を記録し、セッション開始時に読み出して競合は新しい方を優先する。ほかにデータ取り込み（fulcra-ingest）、追跡（fulcra-tracking）、ダッシュボード、Webアプリ構築など、READMEに主要10本・リポジトリに計20本のスキルがある。
- 同じ操作をCLIとMCPの両方から行える。MCPツール名は `list_files` / `read_file` / `write_file` / `record_data` / `get_records` / `get_data_updates` / `restore_file`、CLIは `uv tool run fulcra-api file upload|list|stat|download`、`get-records`、`data-updates` など。

## 目的・背景

- Fulcra は自らを「The User-Owned Context Backend for AI Agents」とうたうサービスで、エージェント同士をつなぐ共有ハブ兼ファイル保管庫。公式サイトの説明では「ユーザー所有のコンテキストレイク」で、あらゆる種類のデータを1カ所に置き、エージェントが読み書きする。運営はHUMANやVeracodeに関わったセキュリティ畑の人々だと公式サイトに記載がある。
- ビジネスモデルはサブスクリプション。公式サイトは「保存時も送信時も暗号化」「データは販売・ライセンスしない」「どのツールに何を共有するかはユーザーが細かく決める」と表明している。機能の中心はエージェント間メッセージングと、エージェントが持ち回れる文脈の保管。
- このリポジトリは、そのFulcraをエージェントに使わせるための手順書集。公式のスキル集ページは「多くのエージェントは優秀な他人で、前回の会話以降に何が変わったか知らず、別のエージェントの続きを引き継げない」という問題設定を示し、Fulcraを「自分が管理する1つの文脈」として各エージェントに教えるための入口と位置づけている。READMEも「一度入れれば、頼めば何をすべきかエージェントが分かる」と説明する。
- ライセンスは README 末尾と各 SKILL.md の frontmatter が MIT と明記。ただし GitHub API の license 検出は null で、リポジトリに LICENSE ファイルが無い（本項目はAPI値に合わせて unknown とし、MITは自己申告として扱う）。

## 依存関係

- Fulcraアカウントが必須。OAuth 2.0（Auth0）のデバイスコードフローで認証し、クレジットカードは不要で初回接続時にアカウントが作られる。
- CLI経路: `uv tool run fulcra-api`（PyPIの `fulcra-api`）。uv が入っていない環境では `uvx fulcra-api` も作例として使われている。認証情報は `~/.config/fulcra/credentials.json` に保存され、アクセストークンは自動更新される。
- MCP経路: 任意のMCP対応クライアントに `https://mcp.fulcradynamics.com/mcp` を登録する。シェルに外向き通信が無い環境ではCLIではなくMCPへ切り替えるようSKILL.mdが指示している。
- スキルの導入: `npx skills add`（vercel-labs/skills）または `skills/` 配下のフォルダをエージェントのスキルディレクトリ（例 `.claude/skills/`）へコピー。Node.jsは導入時のみで、実行時には不要。
- 一部スキルは追加依存を持つ。fulcra-analytics は Python パッケージ（pyproject.toml、uv.lock）を同梱し、ダッシュボード系は Python のローカルサーバを使う。記憶・共有の中心スキル（fulcra-memory / fulcra-workspaces / fulcra-connect）はMarkdownとCLI/MCPだけで動く。

## 実行条件

- 料金（2026-11-09 時点、https://fulcra.ai/product/pricing）: Free は $0 で 5GB のファイル・データ、エージェント間メッセージ数百万件、Insights は直近7日。Pro は $14.99/月 または $149.99/年（17%割引）でメッセージ・ストレージ・Insightsが無制限。Scale はカスタム見積り。無料プランにクレジットカードは不要。
- アカウント登録は必須だが、専用の申込みフォームではなく「初回接続時にアカウントが作られる」方式。CLIまたはMCPの接続ページ（fulcradynamics.com/connect/claude、/connect/chatgpt）から入る。
- クラウド依存。記憶・ワークスペース・共有チャネルはユーザーのFulcraアカウント側に保存され、ローカルディスクだけでは完結しない。ダッシュボードや分析（fulcra-analytics）は手元で動くが、元データはFulcraから取得する。
- プライバシー面: 公式は保存時・通信時の暗号化、データ非販売、共有範囲のgranular設定を表明。スキル側も `progress.md` に機密の個人データ・認証情報・内部推論を載せないこと、共有は相手ごとに必要最小限（チャネル1本、ファイル単位）にすることを明示している。共有は相手のアカウント全体ではなく指定したデータ型・ファイルに限られる。
- 定期実行はホスト次第。SKILL.mdはスケジューラやリスナーが実在する場合のみ定期チェックを提案するとしており、Fulcra側がエージェントを起動し続けるわけではない。

## 最短手順

- 1. スキルを入れる: `npx skills add fulcradynamics/agent-skills`（README記載）。1本だけなら `npx skills add fulcradynamics/agent-skills/connect-our-agents` のようにパス指定（公式スキル集ページの記載）。手動なら `skills/fulcra-memory/` を `.claude/skills/fulcra-memory/` へコピー。
- 2. CLIを認証する: `uv tool run fulcra-api auth login --get-auth-url` を実行し、返った Web auth URL とコードをユーザーに提示する。ユーザーがブラウザで完了したら `uv tool run fulcra-api auth login --device-code <DEVICE_CODE> --poll-timeout=5` で確定。認証情報は `~/.config/fulcra/credentials.json` に残る。
- 3. MCPで使う場合: クライアントのMCP設定に `https://mcp.fulcradynamics.com/mcp` をHTTPサーバとして登録する（Claude/ChatGPTは公式の接続ページ経由）。登録後は `list_files` / `read_file` / `write_file` / `get_data_updates` などのツールが見える。
- 4. 接続確認: `uv tool run fulcra-api user-info` でユーザーIDとタイムゾーンが返ることを確認し、`uv tool run fulcra-api file list /agent/` でファイルストアを一覧する。
- 5. 記憶を1つ書いて読み戻す: `uv tool run fulcra-api file upload ./progress.md /agent/<agent-name>/progress.md` → `uv tool run fulcra-api file stat /agent/<agent-name>/progress.md` で版を確認 → `uv tool run fulcra-api data-updates "1 day"` で変更として現れることを確認。SKILL.mdは書き込み後に同じアカウントから読み戻して内容一致を確かめるまで「保存した」と言わないよう指示している。
- 6. エージェントに任せる: プロンプトに「Get started with Fulcra at https://github.com/fulcradynamics/agent-skills」と渡すと fulcra-get-started が接続→方向づけ→最初の成果物まで案内する。以後はセッション開始時に fulcra-situational-awareness の `data-updates` スキャン、区切りの良いところで fulcra-memory の progress 同期を回す。

## 変更履歴

- 2026-11-09: 初回登録
