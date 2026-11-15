---
name: "muse-grok-x-search"
genre: "other"
url: "https://github.com/kgmkm/muse-grok-x-search"
repo: "kgmkm/muse-grok-x-search"
flags: ["unverified"]
risk_notes: "Grok Buildはベータ版で、利用可能なプランは変更される可能性がある。必要なプランや利用条件はセットアップ時に公式情報で確認すること。"
stars: 108
forks: 17
open_issues: 0
size_kb: 14
language: "unknown"
created: "2026-11-03"
updated: "2026-11-03"
archived: false
license: "MIT"
commits_30d: 2
commits_90d: 2
commit_cadence: "monthly"
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/noa_gpt/status/2121774600321486897"]
fetched_at: "2026-11-15T05:24:57.545513+00:00"
---

# muse-grok-x-search

## 出来ること

- MuseからGrok Buildの組み込みx_searchを呼び出し、Xの公開投稿を検索する。READMEでは、日付・アカウント・URLとともにトレンド投稿、返信、引用を取得すると説明している。検索結果はGrokが生成する要約であり、重要な判断では元投稿をURLから確認するよう記載されている。

## 目的・背景

- Museのソーシャル検索がInstagram、Facebook、Threadsを対象とし、Xを対象としていない点を補うための専用スキル。作者は自身の環境で2026-11-01にエンドツーエンドで試したと報告している。これは作者の報告であり、独立した実測ではない。

## 依存関係

- README記載の要件は、シェルアクセス可能な環境のMuse、Grok Build CLI、およびGrok Buildを利用できるアカウント。READMEではSuperGrok／X Premium系プランまたはXAI_API_KEYを挙げている。検索にはGrok Buildのサブスクリプション利用枠を消費すると説明している。

## 実行条件

- 初回利用時にGrok Buildへのサインインが必要。READMEではMuseがデバイスコード認証を開始し、利用者自身の端末で表示されたURLを開いて承認すると説明している。利用者自身のアカウントと契約を使い、投稿・返信・いいね・リポスト・フォローなどの書き込み操作には使わないよう定めている。

## 最短手順

- MuseにこのリポジトリのURLを渡してスキルのインストールを依頼する。手動の場合はSKILL.mdとskill.yamlをMuseのカスタムスキルフォルダー ~/workspace/custom-skills/grok_x_search/ に置く。初回利用時にデバイスコード認証を行い、Museに自然文でX上の反応や投稿を調べるよう依頼する。

## 変更履歴

- 2026-11-15: 初回登録
