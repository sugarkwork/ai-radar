---
name: "Ghidra"
genre: "other"
url: "https://github.com/NationalSecurityAgency/ghidra"
repo: "NationalSecurityAgency/ghidra"
license: "Apache-2.0"
stars: 100613
language: "Java"
created: "2019-03-01"
updated: "2026-11-18"
forks: 11442
open_issues: 2225
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 417663
archived: false
flags: ["unverified"]
risk_notes: "READMEは特定バージョンに既知のセキュリティ脆弱性があると告知している。利用前にSecurity Advisoriesで影響を確認する必要がある。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/RealMarvelX/status/2119329098929426902"]
fetched_at: "2026-11-19T07:19:13.113417+00:00"
---

# Ghidra

## 出来ること

- コンパイル済みコードを対象に、逆アセンブル、アセンブル、デコンパイル、グラフ表示、スクリプト実行などの解析ができる。対話形式と自動処理の両方で利用でき、独自の拡張やスクリプトをJavaまたはPythonで作成できるとREADMEに記載されている。

## 目的・背景

- NSA Research Directorateが作成・保守するソフトウェアリバースエンジニアリングのフレームワーク。READMEでは、複雑な解析作業の規模拡大やチーム作業の課題に対応し、カスタマイズ可能で拡張可能な研究基盤を提供する目的を説明している。

## 依存関係

- 公式のビルド手順ではJDK 25 64-bit、Gradle 9.1.0以上（またはGradle Wrapper）、Python 3.9〜3.15とpipが必要。Linux/macOSではGCCまたはClangとmake、WindowsではVisual Studio 2017以降またはMicrosoft C++ Build ToolsとMSVC、Windows SDK、C++ ATLが必要とされている。

## 実行条件

- 公式のビルド済みリリースの導入にはJDK 25 64-bitが必要。リリースZIPを展開し、`./ghidraRun`（Windowsは`ghidraRun.bat`）で起動する。PyGhidraの起動スクリプトも案内されている。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- ビルド済みリリースを使う場合は、JDK 25 64-bitを用意し、GitHub ReleasesのAssetsから`ghidra_<version>_<release>_<date>.zip`を取得して展開し、`./ghidraRun`（Windowsは`ghidraRun.bat`）を起動する。既存インストール先への上書き展開は避けるようREADMEに記載されている。

## 変更履歴

- 2026-11-23: 初回登録
