---
name: "Bullet Physics SDK"
genre: "3d-motion"
url: "https://github.com/bulletphysics/bullet3"
repo: "bulletphysics/bullet3"
stars: 14872
forks: 3119
open_issues: 444
size_kb: 297050
language: "C++"
created: "2011-04-12"
updated: "2026-10-09"
archived: false
license: "unknown"
commits_30d: 0
commits_90d: 3
commit_cadence: "monthly"
flags: ["unverified"]
risk_notes: "GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/0xclayo/status/2123016316353155192"]
fetched_at: "2026-11-18T14:10:53.165757+00:00"
---

# Bullet Physics SDK

## 出来ること

- READMEでは、Bullet Physics SDKをリアルタイム衝突検出およびマルチフィジックスシミュレーション用のC++ソースコードとして説明し、VR、ゲーム、視覚効果、ロボティクス、機械学習などを用途に挙げています。PyBulletのPythonバインディングについては、ロボティクス、強化学習、VRでの利用を推奨しています。

## 目的・背景

- ゲーム、ロボティクス、機械学習などで使う物理シミュレーションと衝突検出を提供するSDKです。READMEはPyBulletを使った実行例や研究での引用方法も案内しています。

## 依存関係

- C++版の要件としてC++ 2003対応コンパイラが記載されています。任意のデモの一部にはOpenGL 2またはOpenGL 3が必要です。PyBulletの導入例はpipを使います。

## 実行条件

- Windows、Linux、Mac OSX、iOS、AndroidでテストしたとREADMEにあります。Linux/macOSでのCMakeビルド例はgccとcmakeを使用します。実験的なOpenCL GPU対応には高性能デスクトップGPUが必要とされ、OpenCL CPUデバイスでは動作しないと説明されています。

## 最短手順

- PyBulletの例: `pip3 install pybullet --upgrade --user` を実行し、README記載の `python3 -m pybullet_envs.examples.enjoy_TF_AntBulletEnv_v0_2017may` などでサンプルを起動します。C++版をLinux/macOSでビルドする例は `./build_cmake_pybullet_double.sh` です。

## 変更履歴

- 2026-11-23: 初回登録
