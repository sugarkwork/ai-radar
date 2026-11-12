---
name: "Berth"
genre: "coding-agent"
url: "https://github.com/maxzyma/berth"
repo: "maxzyma/berth"
stars: 0
forks: 0
open_issues: 0
size_kb: 2298
language: "TypeScript"
created: "2026-10-26"
updated: "2026-11-11"
archived: false
license: "MIT"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-12"
first_seen: "2026-11-12"
sources: ["https://x.com/binbin_eth/status/2120710960247615505"]
fetched_at: "2026-11-12T03:43:42.535493+00:00"
---

# Berth

## 出来ること

- ターミナルで起動したエージェントとtmuxセッションを検出し、VS Codeからセッション一覧の表示、新規作成、接続、終了、起動時の再オープンを行う。記録された会話の再開は、会話ID・プロファイル・起動オプションを確認し、エージェントが会話IDを確認した場合に成立する。任意のiTerm2連携は復元済みペインへの再接続とタブへのエージェント状態表示を行う。README記載の説明であり、独立した実機検証結果ではない。

## 目的・背景

- 既存のターミナルコマンドやカスタムスクリプトを使い続けながら、起動したエージェントとtmuxセッションを管理する設計。VS Codeなどのフロントエンドは表示と再オープンを担当し、セッションに関する判断はcoreが担う。

## 依存関係

- セッションを動かすホストにtmux 3.0以上が必要。VS Code拡張はBerthとエディターのNode.jsランタイムを含み、別途のグローバルBerthやNode.js導入は不要。スタンドアロンCLIのインストールにはNode.js 20以上とnpmが必要。macOSでの復旧情報確認にはシステムの/usr/bin/perlを使用する。lsofとsqlite3はCodexの検出・会話検索に任意で使われる。

## 実行条件

- ローカルmacOS/LinuxではCLIとVS Code拡張を利用でき、tmuxが必要。Remote-SSH、Linuxコンテナ、WSLではリモート実行ホストにBerthとtmuxを導入する。ネイティブWindowsではWSL、Remote-SSHまたはDev Containerを使う。iTerm2連携はmacOSのみ。ブラウザーのみのエディターではtmuxバックエンドを実行できない。自動レイアウトProfileはローカルのmacOS/Linuxデスクトップで、フォルダーまたはワークスペースを開いた場合が対象。

## 最短手順

- VS Code拡張は `code --install-extension berthdev.berth` で導入する。スタンドアロンCLIを使う場合は `npm install -g @berthdev/berth` を実行し、利用するエージェントに `berth hooks install claude`、tmuxに `berth tmux install` を実行する。iTerm2連携は任意で `berth iterm2 install` を実行する。CodexのBerth hook定義を新規導入または変更した場合は、Codex内の `/hooks` で確認する。

## 変更履歴

- 2026-11-12: 初回登録
