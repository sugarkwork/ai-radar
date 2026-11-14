---
name: "Rive C++ runtime"
genre: "other"
url: "https://github.com/rive-app/rive-runtime"
repo: "rive-app/rive-runtime"
license: "MIT"
stars: 1258
language: "C++"
created: "2023-06-02"
updated: "2026-11-13"
forks: 133
open_issues: 81
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 150393
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/aikangarooking/status/2121444332091965629"]
fetched_at: "2026-11-14T07:17:26.316369+00:00"
---

# Rive C++ runtime

## 出来ること

- `.riv`ファイルからアートボードとその内容を読み込み、アートボードのステートマシンを取得して操作できる。アートボードの階層変更を`Artboard::advance`で解決する。抽象`Renderer`インターフェースによる外部ベクターレンダラー接続と、Metal、Vulkan、D3D12、D3D11、OpenGL/WebGL向けGPUレンダラーを提供するとREADMEに記載。

## 目的・背景

- Riveの最低層C++ランタイム。READMEによると、RiveのApple、Android、Flutter、Unity、Unreal、Webランタイムがこのライブラリをラップする。

## 依存関係

- C++17ツールチェーン、gitが必要。ビルドスクリプトは初回実行時に固定バージョンのpremake5を取得する。対象レンダラーに応じて、Xcode、Windows SDK、LinuxのVulkanまたはOpenGL開発環境、Vulkan SDKが必要。

## 実行条件

- macOS/Linuxではclangとbash、WindowsではVisual Studio 2022のC++ Clang CompilerおよびMSBuild support for LLVM (clang-cl)が前提。WindowsのPowerShellラッパーもbashを呼び出すため、Git for WindowsまたはMinGWのbash環境がPATH上に必要。

## 最短手順

- README記載のビルド手順は、リポジトリを取得し、`tests/`でビルドスクリプトを実行する。macOS/Linux: `git clone https://github.com/rive-app/rive-runtime.git`、`cd rive-runtime/tests`、`../build/build_rive.sh release`。Windows: `git clone https://github.com/rive-app/rive-runtime.git`、`cd rive-runtime\tests`、`..\build\build_rive.ps1 release`。この候補ではコードの実行は行っていない。

## 変更履歴

- 2026-11-14: 初回登録
