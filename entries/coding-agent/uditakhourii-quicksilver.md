---
repo: "UditAkhourii/quicksilver"
name: "quicksilver"
genre: "coding-agent"
url: "https://github.com/UditAkhourii/quicksilver"
license: "MIT"
stars: 142
language: "JavaScript"
created: "2026-09-25"
updated: "2026-09-25"
forks: 11
open_issues: 3
commits_30d: 0
commit_cadence: "stale"
commits_90d: 2
size_kb: 70
archived: false
flags: ["unverified"]
risk_notes: "効果数値は作者自身の12タスク・ベンチマーク（bench/）による自己申告で、第三者による追試や自動テストは無い。bench の再実行には有料の Jev API キーが必要。対象ファイル/ログの内容は TypeSafe の API（api.typesafe.ai）へ送信されるため機密情報には使えない（.env・鍵・証明書・credentials、2MB 超、バイナリはスキップし .gitignore を尊重すると README に記載）。2026-09-25 の初回コミット2件以降の更新が無く、メンテ状況は不明。"
type: "repo"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/thegreatest_sv/status/2114378197932617766"]
fetched_at: "2026-11-09T21:36:56Z"
last_release: ""
last_release_at: ""
---

# quicksilver — 大量読み込みの判断を Jev に任せ、Claude には shortlist だけ渡す Claude Code Skill

## 出来ること

- リポジトリ全体や大量ファイルに「このファイルは認証まわりを実装しているか」等の yes/no 判定を一括実行し、該当ファイルだけを確信度付きで返す（qs filter）。
- 巨大ログの行単位トリアージ（qs filter --lines）。数字や ID だけが違う重複行をまとめ、一致した行番号レンジで返す。
- 一括分類（qs classify --labels "bug,feature,question"）、検索候補の関連度ランキング（qs rank）、巨大ファイル内の該当行探索（qs find）、長文への単発 yes/no・選択・スコア質問（qs ask）。
- 出力は LLM が読みやすい圧縮形式で、境界事例には ? を付け、末尾に「走査件数・一致数・所要時間・Jev トークン/費用・Claude が読まずに済んだトークン」の receipt を出す。--json で機械可読、--save で全件保存。
- Skill として入れると Claude Code が「読んで判断するだけ」の作業を自動的に委譲する。Claude 側のコンテキスト消費とトークン課金を減らすのが目的。

## 目的・背景

- Claude Code のセッションの大きな割合が「重要かどうかを決めるためだけの読み込み」に消える。187ファイルから認証関連の4件を探す、3,000行のログから本当の障害行を拾う、といった作業でコンテキストがノイズで埋まる。
- そこで判断だけを TypeSafe の System One モデル「Jev」に渡す。Jev は約1秒で型付きの判定（確率・ラベル・スコア）を返し、料金は入力 $0.042/100万トークン・出力無料。Claude は残った shortlist だけを読む。
- 作者の主張では12タスクのベンチで Claude トークン -86%（中央値 -82%）、12件中8件で精度同等、最大20倍高速、Jev 費用は中央値 $0.004/タスク。ただし自己計測で独立検証は無い。
- 向く用途は needle-in-haystack の探索、明確なラベルでの一括ルーティング、「X はどこか」の候補絞り込み。向かないのは主観的・社内規約依存のラベル（commit 種別など）、似たコードの判別（安全/脆弱の双子）、文章生成・編集・多段推論・算術・日付比較、grep で厳密に解けるもの。

## 依存関係

- Node.js 18 以上（glob 展開を使う場合は Node 22 以上）。npm 依存パッケージはゼロで、単一の .mjs CLI と SKILL.md のみ。
- Jev API キーが必須（https://console.typesafe.ai で取得）。JEV_API_KEY または TYPESAFE_API_KEY 環境変数、もしくは ~/.quicksilver/config.json に保存される。
- 実行時に https://api.typesafe.ai への外向き HTTPS 通信が必要（POST /v1/systemone、既定モデル jev-latest、既定並列16）。API 利用は TypeSafe 側の課金。
- Claude Code（Skill / plugin として読み込む）または素のシェル。macOS/Linux 用 install.sh、Windows 用 install.ps1 も同梱。

## 実行条件

- Jev の API キーと従量課金（入力 $0.042/100万トークン、出力無料）を受け入れること。12タスクのベンチ全体で Jev 費用は $0.45 と README に記載。
- 判定対象を第三者 API に送ってよいこと。.env・秘密鍵・証明書・credentials は送らず、.gitignore を尊重し、バイナリと 2MB 超はスキップする実装だが、機密リポジトリでの利用は不可。
- 「重要かどうか」を yes/no・固定ラベル・スコアで表現できる作業であること。算術・件数カウント・日付比較・生成系は対象外（Jev は不得意と明記）。
- 数千件規模では wall-clock は Claude と同程度で、利得はトークンとコンテキストに限られる。速度重視なら --fast（約10倍速いが微妙な判定は精度低下）。

## 最短手順

- 1. Node 18+ を用意し、npx github:UditAkhourii/quicksilver を実行（npm 未公開のため github: 指定）。installer が skill を ~/.claude/skills/quicksilver にコピーする。
- 2. https://console.typesafe.ai で Jev キーを取得。対話インストーラが一度だけ尋ねる。非対話なら --key オプション、環境変数 JEV_API_KEY / TYPESAFE_API_KEY でも可。
- 3. Claude Code を再起動（または新規セッション）。「このリポジトリの認証まわりはどのファイル？」のように頼めば Skill が自動発火する。AI（Claude Code）から呼ぶ手段はこの Skill 経由、または下記 CLI。
- 4. Claude Code plugin として入れる場合: /plugin marketplace add UditAkhourii/quicksilver の後、/plugin install quicksilver@quicksilver。
- 5. CLI 直接: node ~/.claude/skills/quicksilver/scripts/qs.mjs status でキー確認。以降 filter "Does this file handle user sessions?" src、filter "Does this line report a failure?" app.log --lines、classify --labels "bug,feature,question" --items issues.jsonl、rank "where do we issue refunds?" src --top 5。--json で機械可読出力。
- 6. キー削除は npx github:UditAkhourii/quicksilver setup --remove（キーは ~/.quicksilver/config.json に保存）。

## 変更履歴

- 2026-11-09: 初回登録
