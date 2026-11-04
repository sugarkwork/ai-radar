# ai-radar entry schema

1項目 = 1ファイル。**種類ごとに置き場所が違う**。

| type | 置き場所 | 対象 |
|---|---|---|
| `repo` | `entries/<genre>/<owner>-<name>.md` | GitHub リポジトリ |
| `prompt` | `prompts/<genre>/<slug>.md` | URL を持たない単体プロンプト（画像内の指示文も含む） |
| `link` | `links/<genre>/<host>-<slug>.md` | GitHub 以外のサイト・サービス・ツール |
| `article` | `articles/<date>-<author>-<slug>.md` | 長文記事（SNS・ブログ） |
| `model` | `models/<genre>/<org>-<name>.md` | Hugging Face などのモデル配布（重み・LoRA・量子化版） |

フロントマターが唯一の正。`index.json` / `search.json` / `INDEX.md` はここから自動生成される。

## 共通フロントマター

```yaml
type: repo | prompt | link | article
name: 表示名
genre: <下記>
url: 一次URL（prompt は空可）
author: 著者・配布元（@handle かサイト名）
source_post: <元の投稿URL>                        # 出典（X に限らない）
sources: []            # 追加の参照URL（リプ欄のリンク等）
first_seen: YYYY-MM-DD # 最初に観測した投稿の日付
amplifiers: []         # 後から同じものを紹介した投稿（追従・転載の記録）
added: YYYY-MM-DD
flags: []              # low-quality / prompt-injection / malicious / unverified / dead-link
risk_notes: ""         # フラグの理由を1行で
```

## type 別の追加フィールド

### repo

```yaml
repo: owner/name       # 重複判定キー
license: MIT
language: Python
created: YYYY-MM-DD
updated: YYYY-MM-DD        # 上流の最終push日
stars: 12345
forks: 678
open_issues: 90
commits_30d: 42            # 直近30日のコミット数（100件で打ち切り＝100+ と表示）
commits_90d: 130
commit_cadence: daily      # daily | weekly | monthly | stale
last_release: v1.2.3
last_release_at: YYYY-MM-DD
size_kb: 12345
archived: false
fetched_at: YYYY-MM-DDTHH:MM:SSZ   # これらの値を GitHub API から取得した日時
```

指標は取得時点の値。エントリの最終更新日は INDEX.md 側に表示する（frontmatter には持たない）。

### prompt

```yaml
target: Claude Code | Codex | 汎用     # 想定する実行先
transcribed_from: text | image          # 画像から起こした場合は image
prompt_sha1: <本文の正規化ハッシュ>      # 重複判定キー
```

### link

```yaml
pricing: free | freemium | paid | unknown
pricing_detail: "無料枠 3プロジェクト / Pro $12/月（2026-11 時点）"
signup_required: true | false | unknown
```

### article

```yaml
published: YYYY-MM-DD
```

### model

```yaml
model: org/name                  # 重複判定キー（Hugging Face の repo id）
url: https://huggingface.co/org/name
author: 配布元
license: MIT | Apache-2.0 | other
license_name: minimax-h3-community-license-agreement   # license: other のとき
base_model: [org/name]           # 派生元（LoRA・蒸留・量子化）
downloads: 29390                 # 取得時点の累計ダウンロード
likes: 103
format: safetensors | gguf | diffusers | mlx
size: "3.9 GB"                   # 1ファイル、または配布全体
created: YYYY-MM-DD
updated: YYYY-MM-DD
pricing: free                    # 重みは無料。有料APIのみの提供は対象外
pricing_detail: "重み無料（ライセンス名）"
signup_required: false
```

エントリは「テーマ / 著者の主張 / 裏取り・注意点 / 出典（著者名とリンク）」の紹介に留める。

## ジャンル

モデルも用途で分類する（例: 動画モデルなら `video-gen`、ASR なら `tts-audio`）。

`agent-framework` / `coding-agent` / `video-gen` / `tts-audio` / `3d-motion` / `rag` /
`eval` / `mcp-server` / `model-serving` / `prompt-design` / `prompt-other` /
`link-inspiration` / `link-asset` / `link-service` / `article` / `other`

言語や実装ではなく**主用途**で分類する。

## 本文セクション

### repo
`## 出来ること` / `## 目的・背景` / `## 依存関係` / `## 実行条件` / `## 最短手順` / `## 変更履歴`

### prompt
`## 目的` / `## 前提` / `## プロンプト本文`（コードブロック・一字一句そのまま） /
`## 使い方` / `## 注意点` / `## 変更履歴`

### link
`## 目的` / `## 何ができるか` / `## 料金` / `## 登録の要否` / `## 変更履歴`

### article
`## テーマ` / `## 著者の主張` / `## 裏取り・注意点` / `## 出典`（著者名＋リンク） / `## 変更履歴`

### model
`## 出来ること` / `## 目的・背景` / `## 収録ファイル` / `## 実行条件` / `## 使い方` / `## 変更履歴`

## フラグ（安全性）

| flag | 意味 |
|---|---|
| `low-quality` | 中身が薄い・リンク切れ・実質広告・AIスロップ |
| `prompt-injection` | エージェントに指示を上書きさせる、秘密を読ませる、外部送信させる等の記述 |
| `malicious` | 難読化スクリプト、`curl \| bash`、ウォレット/認証情報の窃取、偽インストーラ |
| `unverified` | 一次情報で確認できなかった主張を含む |
| `dead-link` | 取得時点でリンクが死んでいる |

フラグ付きの項目は索引と日次レポートで `⚑` 付きで表示し、**必ず別枠でユーザーに通知する**。
自動で捨てない — 判断は人が行う。

## ルール

- 事実は GitHub API / 公式サイト / 公式ドキュメントで確認したものだけ書く。未確認は「未確認」。
- 元の投稿の煽り文句は転載しない。出典は `source_post` に残す。
- **参照リンクはリプ欄も見る**。本文に無くても作者のリプライに本命リンクがあることが多い。
- 同じ項目の再紹介は新規ファイルを作らず `sources:` に追記する。
- 履歴は書き換えない。修正は追記コミットで行う。
