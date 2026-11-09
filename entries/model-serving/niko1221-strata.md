---
repo: Niko1221/Strata
name: Strata
genre: model-serving
url: https://github.com/Niko1221/Strata
license: MIT
stars: 41050
language: C++
created: 2026-09-24
updated: 2026-11-06
added: 2026-11-03
sources: ["https://x.com/superfang119/status/2117561102481731751", "https://x.com/coldniko/status/2118994582054559808?a=gQ4FPf05vMDrlWcVfV0&s=46", "https://x.com/coldniko/status/2118994582054559808", "https://github.com/Niko1221/Strata/releases/tag/v0.2.12", "https://api.github.com/repos/Niko1221/Strata/releases/tags/v0.2.12", "https://raw.githubusercontent.com/Niko1221/Strata/main/README.md", "https://api.github.com/repos/Niko1221/Strata", "https://x.com/_ryu15_/status/2119318395430551580?a=yCDo-wHy6DxHFi53EG0&s=46", "https://x.com/_ryu15_/status/2119318395430551580", "https://github.com/Niko1221/Strata", "https://raw.githubusercontent.com/Niko1221/Strata/main/data/experimental-speed-projection/README.md", "https://huggingface.co/pentacoxian-dev/Qwen3.8-Flash-Next-IQ3E-Q8D-MTP-GGUF"]
forks: 4495
open_issues: 1052
commits_30d: 100
commits_90d: 100
commit_cadence: daily
size_kb: 92409
archived: false
fetched_at: "2026-11-06T22:54:09Z"
last_release: v0.2.11
last_release_at: 2026-11-05
type: "repo"
author: "Niko1221"
source_post: "https://x.com/coldniko/status/2118994582054559808"
first_seen: "2026-11-07"
amplifiers: []
flags: ["unverified"]
risk_notes: "Mac31%・Linuxほぼ3倍等はリリースノートで同じ条件の根拠がない箇所がある。control vectorは特定Qwen向け実験で既定off。 今回の動作・推論・生成・性能は未検証。"
---

# Strata

## 出来ること

- ローカル推論エンジン本体＋デスクトップアプリ＋ターミナル CLI の3形態で、チャット／コーディング／画像入力（optional）をローカルで動かす。
- 重みが VRAM に収まらないモデルを **GPU・システム RAM・SSD の3層**で分担させて実行する。DeepSeek V4.1 Flash はメモリに載らない部分を SSD から都度読み出す方式で、ディスク容量を要求する代わりに動作する。
- 対応モデル（README 記載分）: Qwen3.8-Flash-Next（ISTA-DASLab / Unsloth / Gyro の各種量子化）、Qwen3.6-35B-A3B（Unsloth UD-Q4_K_XL 等）、DeepSeekV4.1-Flash-1017（1.75〜2.25 bpw / Coder 版）。
- `localhost` に OpenAI 互換／Anthropic 互換 API を立て、`strata connect` で各コーディングツールの接続手順を出す。
- 接続先として README が明記しているツール: Claude Code / Codex CLI / OpenCode / oh-my-pi / pi.dev / Hermes Agent / OpenClaw。
- v0.2.11 で Unsloth の新しい Qwen3.8-Flash-Next（1〜4bit）、NVIDIA / Radeon のプロンプト処理高速化、少ない枚数でのマルチカード起動、チャットをファイルとして保存する機能が入った。

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
- 2026-11-06: Unsloth の 1〜4bit Qwen3.8-Flash-Next、マルチカード起動、チャットのファイル保存を追記（v0.2.11）

## 追加出典・確認範囲（2026-11-09）

GPU/RAM/SSDを組み合わせるローカル推論基盤Strataのv0.2.12変更と実験機能の追記。

DFlash2 drafter、CUDA/HIP/Metal/SYCLなど対象構成で最適化が異なる。

Mac31%・Linuxほぼ3倍等はリリースノートで同じ条件の根拠がない箇所がある。control vectorは特定Qwen向け実験で既定off。

対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:31:03.401130+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

### 今回取得した公式メタ情報

既存フロントマターの過去値は維持し、今回の取得値を下に併記する。どちらも実行・性能の追試ではない。

| 項目 | 値 |
|---|---|
| repo | Niko1221/Strata |
| url | https://github.com/Niko1221/Strata |
| license | MIT |
| language | C++ |
| created | 2026-09-24 |
| updated | 2026-11-07 |
| stars | 42010 |
| forks | 4601 |
| open_issues | 1194 |
| commits_30d | 100 |
| commits_90d | 100 |
| commit_cadence | daily |
| size_kb | 92755 |
| archived | False |
| fetched_at | 2026-11-09T00:31:03.401130+00:00 |


- @coldniko: https://x.com/coldniko/status/2118994582054559808
- @_ryu15_: https://x.com/_ryu15_/status/2119318395430551580
- 対象資料: https://github.com/Niko1221/Strata
- 参照: https://github.com/Niko1221/Strata/releases/tag/v0.2.12
- 参照: https://api.github.com/repos/Niko1221/Strata/releases/tags/v0.2.12
- 参照: https://raw.githubusercontent.com/Niko1221/Strata/main/README.md
- 参照: https://api.github.com/repos/Niko1221/Strata
- 参照: https://x.com/_ryu15_/status/2119318395430551580
- 参照: https://raw.githubusercontent.com/Niko1221/Strata/main/data/experimental-speed-projection/README.md
- 参照: https://huggingface.co/pentacoxian-dev/Qwen3.8-Flash-Next-IQ3E-Q8D-MTP-GGUF

- 2026-11-09: 関連出典と確認範囲を追記。既存の記述・過去の数値・原文プロンプトは維持。今回の実行確認なし。
