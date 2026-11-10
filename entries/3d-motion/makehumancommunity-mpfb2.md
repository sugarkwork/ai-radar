---
repo: "makehumancommunity/mpfb2"
name: "MPFB2"
genre: "3d-motion"
url: "https://github.com/makehumancommunity/mpfb2"
last_release: "v2.0.18"
flags: ["unverified"]
risk_notes: "公式資料に基づく確認。Blenderでの動作、Python経由の自動化、外部モーションキャプチャとの互換性、制作時間や工程全体の費用は未検証。GitHubの最新タグは確認したが、公開日時の年とタイムゾーンは確認できていない。 GitHub APIでライセンスを確認できていません。"
stars: 694
forks: 103
open_issues: 70
size_kb: 90231
language: "Python"
created: "2021-02-06"
updated: "2026-10-24"
archived: false
license: "unknown"
commits_30d: 34
commits_90d: 67
commit_cadence: "daily"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/Y0urDumble/status/2117030430507401326"]
fetched_at: "2026-11-10T08:16:20Z"
---

# MPFB2 — Blenderで体型を調整してリグ付き人物を作る

## 出来ること

- 人体メッシュを生成し、体重や体の長さなどのパラメータで体型を調整する。標準リグを付け、目・髪・衣服などの素材を追加できる。

## 目的・背景

- Blender上で、ポーズ付けやアニメーションに使う人物の素体を作るための拡張機能。Blender Extensionsの掲載ページでは自動リギングとIK・FKへの対応が案内されている。

## 依存関係

- Blender 4.2以上。MakeHuman本体との連携は任意で、連携する場合はMakeHuman 1.2.0以上。肌や目、歯などの素材を増やすにはMakeHumanのシステム素材パックを使う。

## 実行条件

- Blender内で利用できる無料の拡張機能。公式LICENSEではコードはGPLv3以降、同梱素材はCC0 1.0と区別しており、開発元は生成物に権利を主張していない。外部素材の利用条件は素材ごとに確認する。

## 最短手順

- Blenderの設定にある拡張機能一覧でMPFBを検索して導入する。MPFBパネルで人物を生成し、体型を調整する。Rigging → Add Rig → Add Standard Rigで標準リグを追加してから、Apply Assetsで目や髪、衣服を加える。
- AIで作業を補助する場合は、公式のPythonサンプルを参照させ、HumanService.create_human()で素体を作るスクリプトを生成し、内容を確認してMPFBを有効にしたBlender内で実行する。

## 変更履歴

- 2026-11-10: 初回登録
