---
repo: Zagitta/gpu-unlock
name: gpu-unlock
genre: model-serving
url: https://github.com/Zagitta/gpu-unlock
author: Zagitta
license: GPL-2.0
stars: 16595
language: C
created: 2026-10-18
updated: 2026-10-29
added: 2026-11-04
first_seen: 2026-11-03
source_post: https://x.com/Fluyeporlaweb/status/2117544561861972226
sources:
  - https://github.com/Zagitta/gpu-unlock/blob/main/README.md
amplifiers:
  - https://x.com/0xluffy_eth/status/2117561830629675499
flags: [unverified]
risk_notes: "ブート時にカーネルモジュールでGPUの速度セレクタを書き換える構成。性能値は作者計測で第三者検証なし。GeForce の保証・NVIDIA の規約への影響は未確認。トップレベルに LICENSE ファイルが無く licenses/ 配下のみ。"
forks: 1654
open_issues: 118
commits_30d: 36
commits_90d: 37
commit_cadence: daily
size_kb: 193
archived: false
fetched_at: "2026-11-04T22:51:54Z"
---

# gpu-unlock

## 出来ること

- GeForce RTX 20/30/40 の**FP16 / BF16 / TF32（FP32 アキュムレーション）テンソルコア上限**を外す Linux 用カーネルモジュール。NVIDIA がコンシューマ向けに半分に制限している演算レートを、プロ向けカードと同じ全速で使えるようにする、という主張。
- NVIDIA ドライバのパッチでも VBIOS フラッシュでもない。ドライバがカードを掴む**前**のブート時に一度だけ解除し、ドライバ更新のたびにやり直す必要は無い、としている。
- 仕組み: cmpunlocker の V67/PLM 手法と UEFI 方式の「ドライバ前タイミング」を組み合わせ、速度セレクタ SS0 `0x88888888`（BF16 全速）と 4bit の SS1 `0x8`（IMLA4）を書き、ドライババインド前に FLR を実行する。
- 対応状況: **Ampere（RTX 30）は stable（100件以上のユーザー報告）**、**Ada（RTX 40）と Turing（RTX 20）は experimental**。RTX 50（Blackwell）は非対応で、実現見込みも低いと明記。
- 作者提示の数値（ストック電力制限・Dense GEMM）: RTX 3060 12GB 27→51 TFLOPS（+87%）、RTX 3080 65→113（+73%）、RTX 3090 75→125（+65%）、RTX 4090 165→329（+100%、ピーク MMA レート）。
- 実ワークロードの目安（作者計測）: LLM prefill +25〜55%、TTFT 25〜30%減、BF16 の LoRA/フル微調整 +25〜50%、画像生成（SDXL/SD1.5/Krea/DiT） +30〜55%、Wan 2.2 の BF16 動画 +15〜20%、FlashAttention/SDPA +50〜60%、llama.cpp/Ollama の量子化 GGUF は 0〜15%、デコード（メモリ律速）は変化なし。
- 4090 は電力上限に先に当たるため、大きな GEMM をストック電力で回すとピーク比のゲインは出にくい、とも書かれている。

## 目的・背景

コンシューマ向け GeForce とプロ向け RTX A シリーズの差が市場セグメンテーションによるもので、同じシリコンが半分のレートに制限されている、というのが作者の説明。Windows 版は作者自身が保守せず、第三者移植（Windows-GPU-UNLOCK）があるが、野良インストーラには警戒するよう注意喚起している。2026-10-18 作成、10-29 時点で 1.5 万 star。

## 依存関係

- Linux（Arch / Debian・Ubuntu / Fedora・RHEL 系。`make install` が `/etc/os-release` から判別）
- ビルド依存（カーネルヘッダ等）と `sudo`。`make install-arch` / `install-deb` / `install-rpm` で各形式をビルド・導入
- 対象 GPU: RTX 20/30/40 系。ノート向けは一部のみ記載
- ビルド時に NVIDIA/CachyOS の入力を HTTPS で取得し、ファームウェアをビルドディレクトリとパッケージ内に生成する
- Unraid 7.3.0 以降はプラグイン（`gpu-unlock.plg`）として配布されている。起動のたびに実行中カーネル向けのパッケージを取得して導入し、`/etc/modprobe.d` に `softdep nvidia pre: gpu_unlock` と targets を書く

## 実行条件

- **ブートローダのカーネルコマンドライン変更が必要**: `gpu_unlock.targets=all` を追加（GRUB / Fedora の grubby / systemd-boot / UKI は `/etc/kernel/cmdline`）。opt-in 方式で、起動ごとに有効化される。Unraid のプラグインを使う場合はコマンドラインではなく、プラグインの設定 `TARGETS` で対象を指定する。
- 電力・温度は標準のスロットリングがそのまま効くため、消費電力と発熱は増える（作者談）。
- 性能値はすべて作者の計測・主張で、独立した第三者検証は確認できていない。カード個体・電源・冷却で結果は変わる。
- GPU への影響や保証、NVIDIA の利用規約上の扱いは未確認。業務利用のカードに入れる前に自分で判断が必要。
- リポジトリ直下に `LICENSE` は無く、`licenses/` ディレクトリに同梱。README のバッジは GPL-2.0 表記。

## 最短手順

```bash
git clone https://github.com/Zagitta/gpu-unlock
cd gpu-unlock
make install                 # ディストリビューションを判別して導入
# カーネルコマンドラインに gpu_unlock.targets=all を追加して再起動
#   Debian/Ubuntu: /etc/default/grub の GRUB_CMDLINE_LINUX_DEFAULT → sudo update-grub
#   Fedora/RHEL:   sudo grubby --update-kernel=ALL --args="gpu_unlock.targets=all"
# Unraid 7.3 以降はプラグイン（gpu-unlock.plg）を入れ、設定の TARGETS を指定して再起動
```

## 変更履歴

- 2026-11-04: 初回登録（v2.0.0、⚑ 性能値は作者計測のため unverified）、Unraid 7.3 以降向けプラグイン配布を追記（unraid）
