---
repo: "viettranx/3dviz-pro-max"
name: "3Dviz Pro Max"
genre: "3d-motion"
url: "https://github.com/viettranx/3dviz-pro-max"
flags: ["unverified"]
risk_notes: "描画・導入は独立に再現していない。README掲載の作者評価は各条件1件で、品質向上の一般化は未確認。作者資料でもCodexアプリへの導入とClaude Codeのマーケットプレイス経由の導入は未検証。冒頭の村の映像はスキル開発前の素材で、再配布権は確認中。"
stars: 1212
forks: 138
open_issues: 2
size_kb: 71449
language: "JavaScript"
created: "2026-09-10"
updated: "2026-09-11"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 9
commit_cadence: "monthly"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/CryptooGG_/status/2119312343892976064"]
fetched_at: "2026-11-10T12:11:29+00:00"
---

# 3Dviz Pro Max｜Claude Code・Codex向けの対話型3D制作スキル

## 出来ること

- 文章でシーンを指定し、既存のプロジェクト構成に合わせて、操作可能なThree.jsシーンを組み立てる。Blenderを使うベイク工程も収録する。

## 目的・背景

- レシピ、テンプレート、描画フレームの確認を組み合わせ、エージェントが画面上の結果を見ながらシーンを調整する。READMEには作者によるGPU描画の記録がある。

## 依存関係

- ブラウザー向けの例はThree.jsを使用する。画面キャプチャを使う場合はPlaywrightとChromiumを別途用意する。BlenderベイクにはBlenderが必要で、READMEは4.2 LTS以降を推奨している。

## 実行条件

- 作者はmacOS上のClaude Codeで、ローカルチェックアウトをプラグインとして読み込めたと報告している。描画の再現性は未検証。
- リポジトリ独自のコード・データ・制作素材はMIT。BodyParts3Dのメッシュや同梱フォントには個別条件があり、冒頭の村の映像は再配布権を確認中。

## 最短手順

- Claude Codeではローカルチェックアウトを `claude --plugin-dir /path/to/3dviz-pro-max` で読み込み、`/3dviz-pro-max:3dviz-pro-max` を選ぶ。Codexでは同梱のスキルフォルダー全体を認識対象の場所に配置し、新しいセッションでスキル名を明示する。
- 『3dviz-pro-maxを使って、歩き回れる小さなファンタジーの村を作り、描画結果を確認して』と依頼する。フレームを取得できた場合は画面上の結果を点検する。

## 変更履歴

- 2026-11-10: 初回登録
