---
name: "Project Maya"
genre: "model-serving"
url: "https://github.com/mw00/project-maya"
repo: "mw00/project-maya"
license: "MIT"
stars: 3028
language: "C++"
created: "2026-10-06"
updated: "2026-11-18"
forks: 422
open_issues: 181
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 46546
archived: false
flags: ["unverified"]
risk_notes: "速度・品質の数値はREADME記載のユーザー報告・プロジェクト側の測定値で、独立した再測定は確認していません。commits_30d と commits_90d は各API取得が100件で、提示値は取得上限に達しています。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/dextune/status/2119305676069671413"]
fetched_at: "2026-11-18T22:13:13.450193+00:00"
---

# Project Maya

## 出来ること

- READMEによると、GLM-5.3、GLM-5.3-Flash、DeepSeek-V4.1-Flash-1017、MiniMax-M3.1-Flashをローカル環境で動かす推論ソフトウェアです。ブラウザ上のチャットとモニター、画像入力、複数リクエスト処理、ツール呼び出し対応のOpenAI・Anthropic互換APIを備えると説明されています。

## 目的・背景

- 作者は、大規模モデルをデータセンターではなく手元のGPUで実行することを目的として説明しています。会話で使うエキスパートをGPU、RAM、NVMe SSD間で移動し、ハードウェアを測定して設定を調整する仕組みだとREADMEに記載されています。

## 依存関係

- READMEで明示されているハードウェアはNVIDIA GPU（V100またはRTX 20以降）で、AMDとWindowsにも対応するとされています。必要メモリはモデルや量子化版により異なり、VRAMとRAMの合計を基準に選ぶ案内があります。個別のビルド依存パッケージは提示されたREADME抜粋から確認できません。

## 実行条件

- READMEのクイックスタートは `git clone https://github.com/mw00/project-maya.git && cd project-maya` の後に `./setup.sh` を実行する手順です。セットアップでモデルを選択・ダウンロードし、ビルドして起動すると説明されています。Windowsでは `./setup.sh` の代わりに `START-MAYA.bat` を使うと記載されています。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- Linux等では `git clone https://github.com/mw00/project-maya.git && cd project-maya` を実行し、続けて `./setup.sh` を実行します。WindowsではREADMEの案内に従い `START-MAYA.bat` を使用します。モデルの選択や必要メモリはREADMEが案内するモデル表と `docs/MEMORY.md` で確認できます。

## 変更履歴

- 2026-11-23: 初回登録
