---
repo: HKUDS/CLI-Anything
name: CLI-Anything
genre: agent-framework
url: https://github.com/HKUDS/CLI-Anything
license: Apache-2.0
stars: 58277
language: Python
created: 2026-03-08
updated: 2026-09-22
added: 2026-11-05
first_seen: 2026-10-20
source_post: https://x.com/opensourcelab9/status/2112672719175331872
sources:
  - https://clianything.cc/
flags: []
risk_notes: ""
forks: 5245
open_issues: 240
size_kb: 42270
archived: false
---

# CLI-Anything

## 出来ること

- GUI でしか操作できないソフト（GIMP、LibreOffice、Blender、CAD など）を、エージェントが叩ける **CLI として扱えるようにする**。各ソフト向けの「ハーネス」を集めたレジストリ（CLI-Hub）から入れるか、無いものは自分で生成する。
- 入口は3つ:
  1. 既製を使う … `pip install cli-anything-hub` → `cli-hub install gimp`
  2. エージェントに探させる … 専用スキルを入れて「CLI-Hub で合うものを探して作業して」と頼む
  3. 無ければ作る … `/plugin install cli-anything` を入れ、7段階の手順でハーネスを生成
- 生成した CLI にはプレビューと軌跡（trajectory）ループが付き、CAD のビルド、3D シーン、図、ゲーム、字幕などの成果物まで通しで作れる、と README は説明している。
- README では 18 アプリのデモと 2,461 件のテスト通過、技術レポート（arXiv:2606.03854）を掲げている。

## 目的・背景

「今日のソフトの利用者は人間、明日の利用者はエージェント」という前提で、既存ソフトに CLI の皮をかぶせる。MCP サーバーを自作する代わりに、GUI ソフトの操作をコマンド列に落とす発想。

## 依存関係

- Python（`pip install cli-anything-hub`）。生成側は Claude Code などのエージェントとプラグイン機構。
- **元のソフト本体は別途インストールが必要**（GIMP なら GIMP、Blender なら Blender）。
- 生成したハーネスはソフトのバージョンに依存する。アップデートで壊れることがある。

## 実行条件

- Apache-2.0。
- **最終push が 2026-09-22、commits_30d = 0**（2026-11-05 時点）。投稿は「最新 v0.4.0」としており、リポジトリの最新リリースも v0.4.0。活発に開発中というわけではない点は把握しておく。
- ★58,277 は投稿時点の「★54,399」より増えている（API 実測）。
- GUI ソフトを CLI 化する都合上、ファイルの保存先や権限はそのソフトの設定に従う。サンドボックス前提の運用と相性が悪い場合がある。

## 最短手順

```bash
pip install cli-anything-hub
cli-hub list            # 使えるハーネスを見る
cli-hub install gimp
```

## 変更履歴

- 2026-11-05: 初回登録（★58,277 / Apache-2.0 / Python / 最終push 2026-09-22）
