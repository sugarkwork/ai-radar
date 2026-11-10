---
repo: "fletcherholt/3dmodel-skill"
name: "3dmodel"
genre: "3d-motion"
url: "https://github.com/fletcherholt/3dmodel-skill"
license: "unknown"
stars: 6
language: "unknown"
created: "2026-06-15"
updated: "2026-06-16"
forks: 0
open_issues: 0
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 59
archived: false
last_release: ""
last_release_at: ""
flags: ["unverified"]
risk_notes: "公開のGitHub Releasesページにリリース掲載なし。スキルの起動、生成物の品質、反復による改善幅、対応バージョン、外部生成サービスの料金と利用条件は未検証。リポジトリのライセンスはunknownで、転載・再配布の許諾は未確認。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/CryptooGG_/status/2119312343892976064"]
fetched_at: "2026-11-10T12:10:45+00:00"
---

# 3dmodel — Claude Codeで3D素材とインタラクティブビューアを作るスキル

## 出来ること

- Blenderでのメッシュ制作とGLB出力、Three.jsでの回転・分解表示や透視表示、FusionでのパラメトリックCADを用途別に案内する。

## 目的・背景

- 形状を作成してレンダリングし、参照画像と照らして最も目立つ問題を一つ直し、再レンダリングする。作者はこの反復を推奨しており、改善幅は未計測。

## 依存関係

- 呼び出しはClaude Code。GLB制作にはBlender、WebビューアにはThree.jsを使う。Fusionの経路では稼働中のFusionとMCPブリッジを使う構成が記載されている。

## 実行条件

- Blender経路はヘッドレス実行を想定し、ビューア経路ではブラウザ上で表示を確認する。外部の3D生成サービスや自己ホスト型モデルはベースメッシュを生成する場合の選択肢。

## 最短手順

- SKILL.mdとreferencesを含むフォルダを ~/.claude/skills/3dmodel に配置する。Claude Codeで /3dmodel を呼び出し、参照画像と成果物の形式を伝える。例えば『この画像を参考に卓上ランプを作り、Blenderでレンダーを確認してGLBに書き出して』と依頼する。

## 変更履歴

- 2026-11-10: 初回登録
