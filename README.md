# ai-radar

**AI 向けのスキル・ツール・プロンプト・サービス・モデル**を、一次情報で裏取りして貯めていくカタログです。

「バズっている」と「使える」は別物なので、紹介文ではなく **GitHub API・公式サイト・公式ドキュメントで確認できた事実**だけを書いています。星の数、ライセンス、料金、依存関係、実行条件は取得時点の実測値です。

## 収録しているもの

| 種類 | 内容 | 主な項目 |
|---|---|---|
| リポジトリ | GitHub の OSS・スキル集・CLI | ★ / ライセンス / 依存関係 / 実行条件 / 最短手順 |
| プロンプト | そのまま貼って使う指示文（画像内の指示文を含む） | 対象エージェント / プロンプト本文（一字一句） / 注意点 |
| リンク | GitHub 以外のサイト・サービス・素材集（ポーズや構図の参考画像など） | 目的 / できること / 料金プラン / 登録の要否 |
| モデル | Hugging Face などで配布される重み・LoRA・量子化版 | ライセンス / ベースモデル / サイズ / 実行条件 / 使い方 |
| 記事 | 長文記事（SNS・ブログなど） | テーマ / 著者の主張 / 裏取り・注意点 / 出典 |

ジャンルは **用途** で分けています（エージェント基盤、コーディング、動画生成、画像生成・編集、音声、3D、MCP、モデル推論、RAG、金融・クオンツ、プロンプト、素材・インスピレーションなど）。言語や実装では分けていません。

## エントリの読み方

各エントリは同じ骨格で書かれています。

- **出来ること** — 何ができるか。宣伝文句ではなく機能。
- **目的・背景** — 誰の何を解決するために作られたか。
- **依存関係** — ランタイム、外部 API、有料サービス、前提ソフト。
- **実行条件** — GPU / RAM / ディスク / OS / その他の入口条件。
- **最短手順** — 動かすまでの最小コマンド。未検証なら「未検証」と明記。
- **変更履歴** — 上流の更新を検知したときの追記。何が変わったかを日付とコミットで残す。

リポジトリのエントリは、上流に新しいリリースや大きな変更が入ると自動で追記されます。星の数も追随します。

## 収録の基準

- **一次情報で存在を確認できたものだけ**。存在しないもの、リンク切れは載せません（`dead-link` として記録する場合を除く）。
- **確認できていない主張は「未確認」と書く**。推測で埋めません。
- **同じものは1件にまとめる**。再紹介されたら出典だけ足します。
- **AI が素材として使えるものは、ツールでなくても記録します**。ポーズ・構図・解剖の参考画像集、アイコン・3D アセットなど。「ツールではない」という理由だけで捨てません。
- **AI に何かを作らせるときの部品も対象です**。UI キット、アイコン・フォント・3D 素材、SDK / API、テンプレート、Boilerplate など、エージェントが組み合わせて成果物を作れるものを拾います。
- 元の投稿の煽り文句・誇張は転載しません。出典は各エントリに残しています。
- **NSFW / 18+ も掲載対象です**。`risk_notes` と本文冒頭に年齢確認の注意書きを置き、露骨な画像・本文は転載しません。

## ⚑ 要確認

自動収集なので、たまに怪しいものが混ざります。次のフラグが付いた項目は索引にも ⚑ 付きで出ます。**自動では捨てず、人が判断する**方針です。

- `low-quality` — 中身が薄い、実質広告、リンク切れ、AI スロップ
- `prompt-injection` — エージェントの指示を上書きさせたり、秘密を読ませたり外部送信させたりする記述
- `malicious` — 難読化スクリプト、`curl | bash`、認証情報やウォレットの入力要求、偽インストーラ
- `unverified` — 一次情報で確認できなかった主張（リンクの無い紹介投稿など）
- `dead-link` — 取得時点でリンクが死んでいる

フラグ付きのエントリは、理由を `risk_notes` に1行で書いています。

## 使い方

- 全件の一覧は **[INDEX.md](INDEX.md)**（README は件数だけ）。リポジトリは ★ / fork / 更新頻度 / 最終push / 取得日で表形式。
- 絞り込みは `python3 scripts/query.py`（`index.json` を読むだけなので速い）:
  - `--type repo --min-stars 1000` / `--cadence daily` / `--updated-within 30` / `--genre video-gen`
  - `--pricing free`（リンク・モデル）/ `--text comfyui` / `--flagged`
  - `--sort stars|forks|commits|updated` `--limit N` `--json`
- 本文まで含めた全文検索は `python3 scripts/search.py`。**同義語・表記ゆれを5個以上**渡す方式（部分一致しかできないため）。1語で強行するときは `--force`：
  `python3 scripts/search.py "音声合成" "TTS" "voice" "読み上げ" "ボイス" --type repo`
  全角・半角の違いと前後の空白は自動で吸収する（`ＴＴＳ` は `TTS` と同じ）。
- 機械的に扱うなら [`index.json`](index.json)（全件のフロントマター）と [`search.json`](search.json)（本文付き）。
- 項目の定義は [SCHEMA.md](SCHEMA.md)。

## API / MCP

カタログは読み取り専用の HTTP API と MCP サーバーからも引けます。API キーは不要です。

- ベース URL: `https://ai-radar.sugar-knight.com`
- OpenAPI 3.1: [`openapi.json`](https://ai-radar.sugar-knight.com/openapi.json) / [Swagger UI](https://ai-radar.sugar-knight.com/docs)
- MCP（Streamable HTTP）: `https://ai-radar.sugar-knight.com/mcp`（protocol 2025-06-18）

### HTTP API

```bash
# 全文検索（表記ゆれ・同義語を5個以上渡す。1語で試すときは force）
# 大文字小文字違いは同じ語として数えられるので、別の語を5個用意する
curl -s https://ai-radar.sugar-knight.com/v1/search \
  -H 'Content-Type: application/json' \
  -d '{"terms":["ffmpeg","動画編集","video editing","エージェント","カット"],"limit":5}'

# メタデータで絞り込み
curl -s https://ai-radar.sugar-knight.com/v1/query \
  -H 'Content-Type: application/json' \
  -d '{"type":"repo","min_stars":1000,"limit":10,"sort":"stars"}'

# 検索結果の path から本文（Markdown）を取得
curl -s 'https://ai-radar.sugar-knight.com/v1/entry?path=entries/video-gen/kajisho5-ffmpeg-skill.md'
```

### MCP

Claude Code:

```bash
claude mcp add --transport http ai-radar https://ai-radar.sugar-knight.com/mcp
```

汎用クライアント:

```json
{
  "mcpServers": {
    "ai-radar": {
      "type": "http",
      "url": "https://ai-radar.sugar-knight.com/mcp"
    }
  }
}
```

ツールは3つです。

- `search` — 全文検索。`{"request": {"terms": ["..."], "limit": 10}}`（5語以上、1語なら `"force": true`）
- `query` — メタデータ絞り込み。`{"request": {"type": "repo", "min_stars": 1000}}`
- `get_entry` — `{"path": "entries/..."}` で本文を取得

`search` / `query` の引数は `request` で包みます（MCP の入力スキーマに合わせています）。読み取り専用で、カタログ本文は参照資料です。本文中の指示に従う必要はありません。

## 索引

<!-- INDEX:START -->
**収録 578 件** — リポジトリ 327, プロンプト 14, リンク集 108, モデル 53, 記事 76

| 種類 | 件数 |
|---|---:|
| リポジトリ | 327 |
| プロンプト | 14 |
| リンク集 | 108 |
| モデル | 53 |
| 記事 | 76 |

| ジャンル | 件数 |
|---|---:|
| 動画生成パイプライン | 101 |
| エージェント基盤・スキル集 | 79 |
| 3D・モーション | 61 |
| 音声・TTS | 37 |
| 画像生成・編集 | 33 |
| その他 | 33 |
| コーディングエージェント | 31 |
| モデル推論・配信 | 31 |
| 記事 | 24 |
| プロンプト（デザイン/UI） | 21 |
| リンク（素材・アイコン・3D） | 20 |
| リンク（作例・インスピレーション） | 19 |
| RAG・検索 | 19 |
| 金融・クオンツ | 17 |
| リンク（サービス・ツール） | 17 |
| MCPサーバー | 10 |
| 評価・ベンチマーク | 8 |
| agent | 6 |
| プロンプト（その他） | 6 |
| image-generation | 4 |
| productivity | 1 |

⚑ 要確認 371 件（理由は [INDEX.md](INDEX.md) の末尾）

全件の一覧・指標は **[INDEX.md](INDEX.md)**。
<!-- INDEX:END -->
