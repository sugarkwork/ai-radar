---
repo: "physicsdolphin/nv-uefi-unlocker"
name: "nv-uefi-unlocker"
genre: "other"
url: "https://github.com/physicsdolphin/nv-uefi-unlocker"
stars: 2223
forks: 202
open_issues: 21
size_kb: 25244
language: "Rust"
created: "2026-10-26"
updated: "2026-11-10"
archived: false
license: "GPL-2.0"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
last_release: "v2.1.11"
flags: ["unverified"]
risk_notes: "性能と互換性は開発元の報告に基づき、独立した実機試験は未実施。投稿にあるv2.1.9-diag.3のCSM環境向け復旧処理とUSBへのログ書き込みの保証は未確認。最新安定版のタグは確認したが、公開日時は未確認。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/neuronxwhite/status/2117526742260928906"]
fetched_at: "2026-11-10T09:24:07+00:00"
---

# nv-uefi-unlocker — OS起動前にGeForceのTensor演算設定を変更するUEFIツール

## 出来ること

- 開発元はRTX 20／30／40シリーズを対象とし、GTX 16は理論上の対応としている。設定は揮発性で、電源断で消える。

## 目的・背景

- UEFIのDXE段階で動作し、NVIDIAのOSドライバーが読み込まれる前にGPUの演算設定を変更する。開発元の測定ではFP16／BF16／TF32のTensorスループットが最大約2.6倍、画像・動画生成が14〜75%向上した。数値は機材・精度・ワークロードに依存する。

## 依存関係

- FAT32のUSBメディアと対応するNVIDIAファームウェアが必要。NVIDIAファームウェアは配布物に同梱されず、プロジェクト本体のGPL-2.0とは別の利用条件が適用される。

## 実行条件

- UEFI起動が必要。Windows向け準備環境はPowerShell 5以上、Linux向け配布バイナリはglibc 2.34以上。TuringではGSPの前提条件があり、起動やOSへの引き継ぎには機種固有の制約がある。

## 最短手順

- 公開の互換性表でGPUと機種を照合し、検証済みの機材と未検証の機材を区別する。 [互換性表](https://github.com/physicsdolphin/nv-uefi-unlocker/blob/main/docs/compatibility.en.md)
- 比較する場合は、同じモデル・精度・入力で処理時間を記録し、起動後のGPU状態とあわせて判定する。 [README](https://github.com/physicsdolphin/nv-uefi-unlocker/blob/main/README.en.md)

## 変更履歴

- 2026-11-10: 初回登録
