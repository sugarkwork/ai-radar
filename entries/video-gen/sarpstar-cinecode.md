---
type: "repo"
name: "sarpstar/cinecode"
genre: "video-gen"
url: "https://github.com/sarpstar/cinecode"
author: "sarpstar"
source_post: "https://x.com/tetumemo/status/2118939001508049254"
sources: ["https://x.com/tetumemo/status/2118939001508049254?a=z-qc7j3yzRbkzflmyo4&s=46", "https://x.com/tetumemo/status/2118939001508049254", "https://x.com/sarpstar/status/2118006090088517853", "https://api.github.com/repos/sarpstar/cinecode", "https://github.com/sarpstar/cinecode/blob/HEAD/README.en.md", "https://api.github.com/repos/sarpstar/cinecode/actions/workflows/tests.yml/runs?per_page=3", "https://x.com/RoundtableSpace/status/2119048471537762361", "https://github.com/sarpstar/cinecode"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "無料なのはMITのキットで、エージェント契約や任意TTS/APIは別料金。Opus5.5が必須との一次根拠はなく、当方のレンダリング確認はない。 当方でインストール・推論・生成・ベンチ再現はしていない。"
repo: "sarpstar/cinecode"
license: "MIT"
language: "Python"
created: "2026-11-03"
updated: "2026-11-03"
stars: 1591
forks: 288
open_issues: 7
commits_30d: 7
commits_90d: 7
commit_cadence: "weekly"
size_kb: 13754
archived: false
fetched_at: "2026-11-09T00:30:57.616487+00:00"
---

# sarpstar/cinecode

## 出来ること

動画生成モデルではなく、Three.js/Canvasをheadless Chromeで描画しffmpegでMP4にするClaude Code/Cursor向け制作スキル。

## 目的・背景

紹介対象は `sarpstar/cinecode`。対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:57.616487+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

## 依存関係

Node22+、Python3.9+、ffmpeg、Chrome、GPUとエージェント環境。SKILL.md・references・39スクリプト等を原チェックで確認。

## 実行条件

無料なのはMITのキットで、エージェント契約や任意TTS/APIは別料金。Opus5.5が必須との一次根拠はなく、当方のレンダリング確認はない。

コード本体の許諾と、基底モデル・同梱素材・外部API・音声/人物等の利用条件は別に確認する。

## 最短手順

1. [公式README](https://github.com/sarpstar/cinecode#readme)で対応版と依存を確認する。
2. 上記の対象固有条件を満たす環境を用意し、配布元の手順を選ぶ。
3. 外部サービスの料金・認証・データ送信とライセンスを確認してから導入する。

本調査では導入・ビルド・起動をしていないため、成功済みのコマンドとしては掲載しない。

## 出典

- @tetumemo: https://x.com/tetumemo/status/2118939001508049254
- @RoundtableSpace: https://x.com/RoundtableSpace/status/2119048471537762361
- 対象資料: https://github.com/sarpstar/cinecode
- 参照: https://x.com/sarpstar/status/2118006090088517853
- 参照: https://api.github.com/repos/sarpstar/cinecode
- 参照: https://github.com/sarpstar/cinecode/blob/HEAD/README.en.md
- 参照: https://x.com/RoundtableSpace/status/2119048471537762361

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
