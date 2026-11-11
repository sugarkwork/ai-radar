---
repo: "davekiss/mods"
name: "davekiss/mods（leaks）"
genre: "coding-agent"
url: "https://github.com/davekiss/mods"
last_release: ""
last_release_at: ""
flags: ["unverified"]
risk_notes: ["READMEを確認した。プラグインは実行しておらず、節約額の推計精度、週次利用枠への実際の影響、対応するClaude Codeのバージョン、ログの外部送信がないという作者の説明は未検証。", "GitHubの公開Releases一覧にリリースの掲載はなかった。"]
stars: 12
forks: 1
open_issues: 6
size_kb: 78
language: "JavaScript"
created: "2026-10-12"
updated: "2026-10-29"
archived: false
license: "MIT"
commits_30d: 11
commits_90d: 11
commit_cadence: "weekly"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/sumika45379/status/2116145600156856583"]
fetched_at: "2026-11-10T12:58:05+00:00"
---

# davekiss/mods の /leaksでClaude Codeのトークン消費を見直す

## 出来ること

- 直近7日間の会話ログを分析し、長い会話の再読み込みやキャッシュ期限切れ後の再書き込みなどを、削減見込みと対処法付きで表示する。期間は `/leaks --days 30` で変更できる。
- 作者のREADMEによると、自動圧縮の目安を40万トークンに設定する修正を画面から適用できる。入力欄の上には長い会話やキャッシュ期限に関する警告が出て、その場で圧縮できる。

## 目的・背景

- 応答ごとのトークン使用量をAPI単価に換算し、早めに圧縮した場合などをログから再計算する。サブエージェントのキャッシュを1時間に延ばす設定は、書き込み単価の上昇を含めても試算が有利な場合に提案する。
- 表示額はAPI料金換算の推計値。サブスクリプションの請求額や週次枠の残量の実測値ではない。対策ごとの推計には重複があり、早めの圧縮では会話の細部が要約される。

## 依存関係

- Claude Codeプラグインとして使うにはClaude CodeとNode.js 22以上が必要。分析エンジンはNode.jsで単体実行もできる。リポジトリのライセンスはMIT。

## 実行条件

- 対象の会話履歴がローカルの `~/.claude/projects` にあり、応答の `message.usage` を読み取れること。作者は分析を端末内で行うと説明している。設定変更は提案内容を確認してから画面で適用する。

## 最短手順

- Claude Codeで `/plugin marketplace add davekiss/mods`、続けて `/plugin install leaks@davekiss` を入力する。新しいセッションを開いて `/leaks` を実行する。

## 変更履歴

- 2026-11-11: 初回登録
