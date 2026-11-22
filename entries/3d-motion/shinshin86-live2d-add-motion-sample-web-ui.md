---
name: "live2d-add-motion-sample-web-ui"
genre: "3d-motion"
url: "https://github.com/shinshin86/live2d-add-motion-sample-web-ui"
repo: "shinshin86/live2d-add-motion-sample-web-ui"
license: "MIT"
stars: 298
language: "JavaScript"
created: "2026-07-13"
updated: "2026-11-03"
forks: 19
open_issues: 0
commits_30d: 12
commit_cadence: "weekly"
commits_90d: 46
size_kb: 8927
archived: false
flags: []
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
risk_notes: ""
sources: ["https://x.com/dextune/status/2119173045797708268"]
fetched_at: "2026-11-17T07:21:49.457543+00:00"
---

# live2d-add-motion-sample-web-ui

## 出来ること

- Live2Dモデルの既存パラメータ向けに、JSONでモーションを作成し、生成・検証してWeb UIで再生できる。READMEでは、生成スクリプト、独立したバリデーター、ヘッドレスブラウザーでの検証を挙げている。

## 目的・背景

- READMEによると、`.motion3.json`はモデルパラメータごとのキーフレームカーブを記述するJSONであり、既存パラメータの範囲内ならテキスト編集でモーションを作成できる。Cubism Editorを必要としない方式を提供する。

## 依存関係

- README記載の要件はPython 3（標準ライブラリのみ）とモダンブラウザー。ブラウザー検証にはChromeが必要。カラー互換モジュールはpixi-live2d-display 0.4.0に依存すると説明されている。

## 実行条件

- モデルのパラメータに合うモデル別モーション定義が必要。READMEは、モデルの配置・設定に`tools/setup_model.py`、モーション生成に`tools/gen_motions.py`、検証に`tools/validate_motions.py`を案内している。

## 最短手順

- README記載の手順：`python3 tools/setup_model.py <model zip or folder>`でモデルを設定し、`python3 tools/gen_motions.py`で生成、`python3 tools/validate_motions.py`で検証する。`python3 tools/serve.py`でWeb UIを配信する。

## 変更履歴

- 2026-11-22: 初回登録
