---
repo: "RobLe3/cc-blender-skill"
name: "cc-blender-skill"
genre: "3d-motion"
url: "https://github.com/RobLe3/cc-blender-skill"
license: "MIT"
stars: 156
forks: 18
open_issues: 0
size_kb: 23066
language: "Python"
created: "2026-04-27"
updated: "2026-10-12"
archived: false
commits_30d: 4
commits_90d: 4
commit_cadence: "weekly"
last_release: "v1.4.0"
flags: ["unverified"]
risk_notes: "動作と生成品質は独立に検証していない。作者資料でもClaude Codeでのスキル検出・振り分け、Blender 5.1.1以外の実機動作、Unrealへのインポートは検証範囲が限られる。発見投稿の参照動画からの編集可能プロジェクト再現は、本リポジトリの機能として確認できていない。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/CryptooGG_/status/2119312343892976064"]
fetched_at: "2026-11-10T12:09:32+00:00"
---

# cc-blender-skill — 自然言語でBlenderの制作工程を組み立てるスキル集

## 出来ること

- モデリング、材質、照明、カメラ、レンダリング、アニメーション、書き出しを30のスキルで扱う。参照画像やテクスチャに合わせる3D再構成の手順も収録する。

## 目的・背景

- 入口のtext-to-blenderが依頼に応じて専門スキルを読み込み、生成したBlender PythonをMCP経由で実行する。作者は剣、瓶、椅子など6種類のシーンでの検証を報告している。

## 依存関係

- 公式Blender Lab MCPはBlender 5.1以上、ahujasid版はBlender 4.0以上がREADME上の要件。両方ともBlenderアドオンと別プロセスのMCPサーバーを使う。
- wireframe-to-3dにはPython 3.9以上とopencv-python、numpy、scipy、Pillowが必要。リポジトリはMIT。

## 実行条件

- スキル検出、ファイル・シェル操作、画像確認、MCPに対応するエージェントホストを用意し、選んだMCPのアドオンを有効にした状態でBlenderを起動する。

## 最短手順

- プラグインREADMEに沿ってplugin/skills配下のスキルをCodexなら.agents/skills/、Claude Codeなら.claude/skills/などに登録し、選んだBlender MCPをホストに設定する。
- 空のBlenderシーンで、ホストからシーン情報を問い合わせて接続を確認する。Codexでは `$text-to-blender ティーポットを作り、三点照明でレンダリングして` と呼ぶ。Claude Codeでは同じ制作内容を自然言語で依頼する。

## 変更履歴

- 2026-11-10: 初回登録
