---
type: "repo"
name: "sushi"
genre: "model-serving"
url: "https://github.com/beamivalice/sushi"
author: "beamivalice"
repo: "beamivalice/sushi"
license: "MIT"
stars: 428
language: "Zig"
created: "2026-09-20"
updated: "2026-11-06"
added: "2026-11-06"
first_seen: "2026-11-06"
sources: ["https://x.com/dextune/status/2117812590042898627"]
flags: []
risk_notes: "Apple Silicon M1+ / macOS 26.2+ 専用で Linux・Windows・コンテナでは動かない。実用的なパックは RAM 48GB 以上（GLM 2.4bpw と MiMo は 128GB、DeepSeek STQ-1.75bpw は 96GB 以上＋332.1GB のディスク）を要求し、GPU wired limit を sudo sysctl で変更する必要がある。LICENSE 実取得は MIT だが GitHub API の license は NOASSERTION を返す（vendored/ported kernels は NOTICE 記載）。GLM 用 DFlash2 assistant は CC BY-NC-ND 4.0 で、そこから生成される派生物はローカル保持が条件。MiMo-V2.6-Flash は 1.5.1 以降サポート外（ロードは可能だがテスト・ベンチ・チューニング対象外）。commits_30d は 100 件/ページの上限に当たっており、実際はそれを上回る。"
forks: 36
open_issues: 9
commits_30d: 100
commit_cadence: "daily"
size_kb: 84473
archived: false
fetched_at: "2026-11-06T16:56:23Z"
last_release: "v1.5.1"
last_release_at: "2026-11-06"
---

# sushi — Apple Silicon で低ビット量子化モデルを動かすローカル推論サーバー

## 出来ること

- Apple Silicon（M1 以降）/ macOS 26.2 以降で、STQ・EXL3-Affine 形式の低ビット量子化モデルをローカル推論し、OpenAI 互換の HTTP API を既定で 127.0.0.1:12345 に公開する（README「Install」「Serve on your network」）。
- `sushi launch <agent>` で claude・codex・hermes・aider・opencode・pi・omp・grok・dsh をこのサーバーに向けて起動できる（docs/usage.md「Coding agents」）。エージェントのバックエンドとしてそのまま使える。
- 対応パックは Qwen3.8-Flash-Next（2bpw / STQ-2.75bpw / 4bpw）、GLM-5.3-Flash（2bpw / 2.4bpw、画像・動画入力）、DeepSeek-V4.1-Flash-1017 STQ-1.75bpw（experts を SSD からストリーム、1M コンテキスト）。
- 投機的デコード（Qwen・MiMo は MTP、GLM は DFlash2）と 8-bit KV キャッシュが既定で有効。
- SSD prefix cache（既定オン、上限 20GB）で長いエージェントセッションのプロンプトを再利用する。v1.5.0 で DeepSeek-V4.1 の書き込みが1ターン約100MB から約9MB に減り、30ターン（72k→176k トークン）で 3.8GB が 0.8GB になったとリリースノートに記載。
- `sushibar` というメニューバーアプリで、生成 tok/s・モデル・メモリ・prefill・GPU を表示し、サーバーの起動/停止・ポート切替・更新を行う。
- Web UI（Chat / Dashboard / Models / Settings）と `/metrics`・`/metrics.json` を提供。`--host 0.0.0.0 --api-key-env` で LAN 公開し、Bearer キーで認証できる。

## 目的・背景

- ddalcu の mlx-serve からの detached fork。独自の Sushi Trellis Quant（STQ）と EXL3-Affine ハイブリッド変換で、低ビットでも量子化劣化を抑えることを狙う（README 冒頭）。
- クラウド API に頼らず手元の Mac で大きめのモデルを動かし、コーディングエージェントの推論先にする用途を想定している。
- 2026-09-20 作成。約6週間で v1.2.0 から v1.5.1 までリリースしており、開発は活発（pushed_at 2026-11-06）。
- 品質は KLD と top-1 一致率で提示（例: DeepSeek STQ-1.75bpw は KLD 0.1576 / top-1 89.13%、同 README で oQ2.5e の 0.1717 と比較）。ベンチは M5 Max 128GB 上での自社計測。

## 依存関係

- ハードウェア: Apple Silicon M1 以降。OS: macOS 26.2 以降（README 明記。Linux / Windows 不可）。
- 配布: `brew install beamivalice/tap/sushi`、または GitHub Releases の `sushi-bin-macos-arm64.tar.gz`（ad-hoc 署名）。実装言語は Zig。
- モデル: Hugging Face の `beamster/*` パックを `sushi pull` で `~/.sushi/models/beamster/<repo>` に取得する。他 org のパックは拒否される。
- メモリ: Qwen 2bpw は 48GB（32GB はストリーミング可）、Qwen STQ-2.75bpw は 64GB、Qwen 4bpw / GLM 2bpw は 96GB、GLM 2.4bpw と MiMo 2.3bpw は 128GB、DeepSeek STQ-1.75bpw は 96GB 以上（experts を SSD ストリーム）。
- ディスク: DeepSeek パックは 332.1GB（うち 189GiB は Engram テーブルで行単位読み出し）、SSD prefix cache が最大 20GB。
- 権限: GPU メモリ上限を `sudo sysctl iogpu.wired_limit_mb=<N>` で設定する（再起動で戻る。108 超の `--ssd-budget-gb` では `vm.global_user_wire_limit` も必要）。
- ライセンス: LICENSE の実取得結果は MIT（Copyright 2026 Theinruj Toranavikrai / David Dalcu）。ただし GitHub API の license は NOASSERTION を返す。port 済みカーネルや vendored コードは NOTICE に列挙。GLM 用 DFlash2 assistant は CC BY-NC-ND 4.0（非商用・改変不可）で、そこから `dflash2/` に生成される派生物はローカル保持が条件。

## 実行条件

- Apple Silicon の Mac 実機が必須。CI・コンテナ・VPS では動作しない。
- 選んだパックの RAM 要件を満たすこと。下回る場合は `--ssd-budget-gb N` でストリーミング動作になるが、N とコンテキストの合計が GPU 上限に収まる必要がある。
- `sudo sysctl` を実行できる管理者権限。上限を上げすぎると macOS が応答しなくなる旨が README に明記されている。
- 初回に数十〜数百GB のダウンロードと、それに見合う空きディスク。Web UI からのダウンロードは空きが 1/20 未満になる場合に拒否される。
- DeepSeek を 128GB Mac で 1M コンテキスト運用する場合は `--ssd-budget-gb` の既定（96、または 108）と wired limit の組み合わせを README の表どおりに合わせる。

## 最短手順

- 1. インストール: `brew install beamivalice/tap/sushi`
- 2. パック取得（48GB Mac の例）: `sushi pull qwen3.8-flash-next:2bpw`
- 3. GPU 上限を設定: `sudo sysctl iogpu.wired_limit_mb=43000`（48GB Mac の推奨値）
- 4. サーバー起動: `sushi serve --model ~/.sushi/models/beamster/Qwen3.8-Flash-Next-Sushi-2bpw --mtp --kv-quant 8 --mtp-head-kv-quant --qwen-gdn 16 --ctx-size 131072 --max-tokens 32000 --prefix-cache-disk 20GB --prefix-cache-entries 1 --temp 1`
- 5. AI から呼ぶ（推奨・README 記載の方法）: サーバー起動中に `sushi launch hermes`（`claude` / `codex` / `aider` / `opencode` なども可）を実行すると、そのエージェントがこのサーバーを向いて起動する。`--print` を付けると設定と起動スクリプトの出力だけを行う。
- 6. 手動で叩く場合: OpenAI 互換の base URL は `http://127.0.0.1:12345/v1`。LAN 越しなら `export SUSHI_KEY=<secret>` と `sushi serve ... --host 0.0.0.0 --api-key-env SUSHI_KEY` で起動し、`Authorization: Bearer <key>` を付けて `http://<mac-ip>:12345/v1` に送る。
- 7. 動作確認: `sushibar` のメニュー、または `http://127.0.0.1:12345/` の Dashboard、`/metrics` で生成速度とキャッシュ状態を見る。

## 変更履歴

- 2026-11-06: 初回登録
