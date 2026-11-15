---
name: "dsh-pet-live2d"
genre: "other"
url: "https://github.com/A8Chann/dsh-pet-live2d"
flags: ["unverified"]
risk_notes: "APIのlicense値はunknown。READMEのバッジにはMIT + CC BY-NC-SA 4.0とあるが、ライセンスの適用範囲は添付READMEだけでは確認できない。 GitHub APIでライセンスを確認できていません。"
repo: "A8Chann/dsh-pet-live2d"
stars: 78
forks: 10
open_issues: 1
size_kb: 8268
language: "JavaScript"
created: "2026-09-20"
updated: "2026-11-09"
archived: false
license: "unknown"
commits_30d: 42
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/dextune/status/2121641813136290022"]
fetched_at: "2026-11-15T00:28:17.031408+00:00"
---

# dsh-pet-live2d

## 出来ること

- READMEによると、DSH Web GUI上にLive2Dのデスクトップペットを表示し、ドラッグ・拡大縮小、マウス追従、クリック操作、着せ替え、DSHのセッションイベントに応じた動作や表情の切り替えを行う。ペットの位置やサイズはlocalStorageに保存される。

## 目的・背景

- READMEでは、DSHの会話や状態表示に加えて、ツール実行・承認待ち・子エージェント・ターン終了などのイベントをペットの動作、表情、台詞で示し、ログを見ずに進捗を把握できるようにするものと説明している。

## 依存関係

- DSHのWeb GUIプラグインとして動作し、DSH >= 0.1.5-rc.1が必要。WebGL対応ブラウザーが必要。Live2D Cubism Coreはプラグインに同梱されず、初回利用時にLive2D公式CDNから取得するとREADMEに記載されている。

## 実行条件

- DSHのweb profileで利用する。README記載の対応OSはWindows、macOS、Linux。Cubism Coreの初回取得時にはネットワーク接続が必要で、取得後はキャッシュを使う。

## 最短手順

- DSHで「プラグイン」→「プラグインを追加」を開き、`dsh-pet-live2d`を入力してインストールし、「立即启用」を選ぶ。その後`dsh web`を再起動する。READMEでは、コマンドラインの場合は`dsh plugin --profile web add dsh-pet-live2d`も案内している。

## 変更履歴

- 2026-11-15: 初回登録
