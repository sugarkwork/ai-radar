---
repo: benjitaylor/skills
name: Stageshow（benjitaylor/skills）
genre: agent-framework
url: https://github.com/benjitaylor/skills
license: 未確認（リポジトリ全体の LICENSE なし。各スキル個別のライセンス表記）
language: TypeScript
created: 2026-10-26
updated: 2026-11-04
added: 2026-11-03
author: "@benjitaylor"
source_post: "https://x.com/tetumemo/status/2117618086392316274"
sources:
  - https://x.com/shannholmberg/status/2116957574008590445
  - https://benji.org/stageshow
stars: 1897
forks: 131
open_issues: 1
commits_30d: 2
commits_90d: 2
commit_cadence: monthly
size_kb: 1171
archived: false
fetched_at: "2026-11-04T22:52:03Z"
last_release: stageshow-v1.1.0
last_release_at: 2026-11-04
---

# Stageshow（benjitaylor/skills）

## 出来ること

- エージェントが作る「それっぽくない製品UI」を、実在プロダクトの見た目に寄せるスキル。静止画・フィーチャーカード・カーソルデモ・ベントーグリッドを React で組み立てる。
- 構図とモーションのガイド、コピー元のキット、サンプル集、**自分の成果物を撮影して自己検証するツール**が入っている。
- AI生成UIが崩れる5パターン（詰め込みすぎ／スカスカ／アプリ全体を1枚のカードに縮める／全部同じ強さで平坦／ブランドらしさが出ない）を明示し、それを避ける手順で進む。
- 7ステップで制作する：媒体（静止画かアニメか、配置とサイズ）→ ルック（light / dark / blueprint / glass、アクセント1色）→ ストーリー（3〜5ビート）→ 既存の gold example から一番近いものを起点 → 画面（実語は数個、残りはプレースホルダ行）→ 振り付け（ビートを重ね、最初に戻るループ）→ リハーサル（撮影して全フレームを確認し修正）。
- v1.1.0 でキット部品に Button / Card（`flush` で分割カード） / Divider / Kbd と、入力中のコメントがその場で投稿済みコメントに変わる Draft が加わった。リハーサルは `--gate` 付きの撮影が必須で、失敗すると終了コード1を返す。
- デザイントークンを読むため、既存プロダクトの色・フォント・角丸に合わせられる。
- Grok Build / Claude Code / Codex / Gemini で利用可。

## 目的・背景

X の Head of Design である Benji Taylor が、自分のデザイン時の判断（100個程度の小さな決定）をスキルとして書き出したもの。2026-10-26 公開。日本語圏では @tetumemo の引用ポスト、英語圏では @shannholmberg の分解ポスト経由で拡散した。リポジトリには Stageshow 以外のスキルも含まれる。

## 依存関係

- Node.js（`npx skills add` でインストール）
- React（生成物が React コンポーネント）
- 対応エージェント：Claude Code / Codex / Gemini CLI / Grok Build など

## 実行条件

- 特段のGPU要件なし。
- レンダリング確認のためヘッドレスブラウザを利用する（撮影ステップ）。
- リポジトリ全体の LICENSE が無いため、業務利用前に各スキルディレクトリのライセンス表記を確認すること。

## 最短手順

```bash
npx skills add benjitaylor/skills --skill stageshow
# バージョン固定: npx skills add benjitaylor/skills#stageshow-v1.1.0 --skill stageshow
# 使い方: https://benji.org/stageshow
```

## 変更履歴

- 2026-11-03: 初回登録（★1,255 / pushed 2026-10-31）。引用元 @shannholmberg の分解ポストと @tetumemo の紹介ポストを出典に記録
- 2026-11-04: キット部品（Button/Card/Divider/Kbd/Draft）追加と --gate の厳格化（stageshow-v1.1.0）
