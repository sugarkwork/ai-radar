---
type: "repo"
name: "Kimodo"
genre: "3d-motion"
url: "https://github.com/nv-tlabs/kimodo"
author: "NVIDIA / nv-tlabs"
repo: "nv-tlabs/kimodo"
license: "Apache-2.0"
stars: 4130
forks: 464
open_issues: 22
language: "Python"
created: "2026-03-16"
updated: "2026-10-15"
added: "2026-11-09"
first_seen: "2026-11-09"
fetched_at: "2026-11-09T21:31:31Z"
commits_30d: 18
commits_90d: 20
commit_cadence: "weekly"
size_kb: 44539
archived: false
flags: ["unverified"]
risk_notes: "コードはApache-2.0、重みはモデル別。SOMA-RP-v1.2はNVIDIA Open Model Licenseで商用利用可能、SMPLX-RP-v1はNVIDIA R&D Model License。Scenarioは別サービスで無料プランの生成物は個人・評価用途に限る。実行・生成品質・Scenario操作は未検証。"
sources: ["https://x.com/cutetoxicguy/status/2119558081352729010", "https://github.com/nv-tlabs/kimodo", "https://research.nvidia.com/labs/sil/projects/kimodo/", "https://huggingface.co/nvidia/Kimodo-SOMA-RP-v1.2", "https://www.scenario.com/changelog/models-ddc0ba11e58ceb39c3f086a7a659e51e6d9901488515f459cc733d5b04deedb6", "https://www.scenario.com/pricing"]
last_release: ""
last_release_at: ""
---

# Kimodo — テキストと制約から3D骨格モーションを生成

## 出来ること

- テキストから人物やヒューマノイドの骨格モーションを生成し、複数の指示をつないで一連の動きにする。
- 全身キーフレーム、手足の位置・回転、2D経路・通過点を指定して動きを制御する。生成結果はCLIやローカルのタイムライン型デモで扱える。
- SOMA人型・Unitree G1ロボット・SMPL-Xの各骨格向けモデルを提供。NPZ、G1向けMuJoCo qpos CSVなどを出力する。

## 目的・背景

NVIDIAのモーション拡散モデルの公式実装。Rigplayモデルは約700時間の光学モーションキャプチャを使用し、ルート移動と身体姿勢を二段階に分けて予測する。画像や完成キャラクターではなく骨格の動きが生成物なので、キャラクターのメッシュ・リグとリターゲティングが別途必要。

SOMA-RP-v1.2のモデルカードは1生成あたり最大10秒、30fpsと記載。モデル内部は簡略化した30関節で、公開・出力時に77関節へ変換するため、77関節という数字だけで指の細かな動きが生成されるわけではない。足滑りや指示不一致、物体を認識せず接触が合わないこともある。

## 依存関係

Python・PyTorch・テキストエンコーダーなどを使用。重みはCLIやデモから初回生成時に自動取得される。コードはApache-2.0だが、各モデル・第三者資産には別条件がある。

- **SOMA-RP-v1.2**：NVIDIA Open Model License。モデルカードは商用利用可能と記載。
- **SMPLX-RP-v1**：NVIDIA R&D Model License。SOMA版の商用条件を流用せず、別途条件を確認する。
- v1.1では評価データの一部が学習に混入。公式は比較評価に修正版v1.2を推奨している。

## 実行条件

公式はLinuxで開発、WindowsはDocker利用を案内。全てGPUで処理する場合は約17GB VRAMと記載。`TEXT_ENCODER_DEVICE=cpu`でテキストエンコーダーをCPUに移すと、公式報告ではVRAMを3GB未満に抑えられるが、速度は低下する。GPU・CPU・メモリ条件と実速度は実行環境に依存し、当方では検証していない。

## 最短手順

[公式インストール手順](https://research.nvidia.com/labs/sil/projects/kimodo/docs/getting_started/installation.html)に従いセットアップし、`kimodo_demo`でローカルデモを起動する。CLI生成例とモデル選択は[公式クイックスタート](https://research.nvidia.com/labs/sil/projects/kimodo/docs/getting_started/quick_start.html)を参照。

## Scenarioでの利用

[Scenarioの2026年11月6日付更新](https://www.scenario.com/changelog/models-ddc0ba11e58ceb39c3f086a7a659e51e6d9901488515f459cc733d5b04deedb6)では、1プロンプト最大10秒・30fps、複数プロンプトの連結、SOMA 77関節のBVHとNPZ出力を案内している。これはクラウドサービスの実装であり、ローカルデモにあるすべての制約操作がScenarioでも使えるとは確認していない。

Scenarioはクレジット制。公式料金ページは無料枠50クレジット/日、有料Starter月15米ドルを掲載し、無料プランの生成物は個人・評価用途、商用利用は有料プランと説明する。Kimodo一回あたりの消費量は未確認。条件は利用時に確認する。

## 出典

- [NVIDIA研究ページ](https://research.nvidia.com/labs/sil/projects/kimodo/)
- [モデルカード：SOMA-RP-v1.2](https://huggingface.co/nvidia/Kimodo-SOMA-RP-v1.2)
- [SOMA骨格の説明](https://research.nvidia.com/labs/sil/projects/kimodo/docs/key_concepts/skeleton.html)
- [Scenario料金](https://www.scenario.com/pricing)
- [紹介投稿](https://x.com/cutetoxicguy/status/2119558081352729010)
- 関連：[VRMkimodo](camenduru-vrmkimodo.md)はVRM書き出しを追加した別フォーク。

## 変更履歴

- 2026-11-09: 初回収録。公式資料とScenarioの発表を照合。実行は未検証。
