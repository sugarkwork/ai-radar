---
repo: Niko1221/Strata
name: Strata
genre: model-serving
url: https://github.com/Niko1221/Strata
license: MIT
stars: 39048
language: C++
created: 2026-09-24
updated: 2026-11-02
added: 2026-11-03
sources:
  - https://x.com/superfang119/status/2117561102481731751
forks: 4236
open_issues: 1228
commits_30d: 100
commits_90d: 100
commit_cadence: daily
size_kb: 87595
archived: false
fetched_at: "2026-11-03T15:42:32Z"
last_release: v0.2.10
last_release_at: 2026-11-02
---

# Strata

## 出来ること

- ローカル推論エンジン本体＋デスクトップアプリ＋ターミナル CLI の3形態で、チャット／コーディング／画像入力（optional）をローカルで動かす。
- 重みが VRAM に収まらないモデルを **GPU・システム RAM・SSD の3層**で分担させて実行する。DeepSeek V4.1 Flash はメモリに載らない部分を SSD から都度読み出す方式で、ディスク容量を要求する代わりに動作する。
- 対応モデル（README 記載分）: Qwen3.8-Flash-Next（ISTA-DASLab / Unsloth / Gyro の各種量子化）、Qwen3.6-35B-A3B（Unsloth UD-Q4_K_XL 等）、DeepSeekV4.1-Flash-1017（1.75〜2.25 bpw / Coder 版）。
- `localhost` に OpenAI 互換／Anthropic 互換 API を立て、`strata connect` で各コーディングツールの接続手順を出す。
- 接続先として README が明記しているツール: Claude Code / Codex CLI / OpenCode / oh-my-pi / pi.dev / Hermes Agent / OpenClaw。

## 目的・背景

「Qwen3.8-Flash-Next on any consumer hardware」を掲げる、コンシューマ向けハードで大型モデルを動かすためのローカル推論スタック。作者は Niko1221、MIT、C++ 実装。2026-09-24 作成、約 86MB。GitHub Releases で v0.2.9（Windows / Linux / macOS の各インストーラ）を配布している。README に実測のスループット表が載っており、数値を出している点が特徴。

## 依存関係

- OS 別インストーラ（`Strata-0.2.9-windows-x64-setup.exe` / `.AppImage` / `.dmg`）または `install.sh` / `install.ps1`。初回起動時に GPU 向けエンジンをダウンロードする。
- モデルの重みは同梱されず、初回セットアップ時にダウンロードする。
- DeepSeek V4.1 Flash を使う場合は別途「DeepSeek エンジン」も取得する。
- アカウント登録は不要（README 明記）。
- AMD / Intel Arc / Apple Silicon / Strix Halo / DGX Spark はそれぞれ専用セットアップ手順（docs/）が用意されている。

## 実行条件

- 対応 GPU: NVIDIA RTX 20/30/40/50、AMD RX 7700〜7900・RX 9060/9070・AI PRO R9700（RX 6000 は experimental）、Intel Arc（Linux）、Apple Silicon M1 以降、Ryzen AI Max（Strix Halo）、DGX Spark（Linux）。
- ディスク: DeepSeek V4.1 Flash 2.00 bpw で**約 265GB の空き**が必要（1.75 bpw で約 245GB、Coder 版で約 197GB）。Qwen 系は各量子化サイズ次第。
- README の実測値（DeepSeek 2.00 bpw, Strata 0.2.5）: RTX 5070 12GB + RAM 64GB で 4〜6 tok/s（プロンプト約 110 tok/s @4K）、RTX 3060 12GB + RAM 46GB で 9〜11 tok/s、R9700 1枚 + RAM 251GB で 21〜25 tok/s。
- VRAM だけで完結する構成ではないため、**RAM と SSD の空き容量が実質的なボトルネック**になる。

## 最短手順

```bash
# Linux / macOS
curl -fsSL https://github.com/Niko1221/Strata/releases/latest/download/install.sh -o install.sh && sh install.sh
strata launch                      # 対話でモデルを選択
strata connect                     # 使うツール（Claude Code / Hermes Agent 等）の接続手順を表示

# DeepSeek V4.1 Flash を明示指定する場合
strata launch --family deepseek41 --model ist-das-2.00bpw --plan
```

## 変更履歴

- 2026-11-03: 初回登録（star 39,028 / pushed 2026-11-02 / v0.2.9）
