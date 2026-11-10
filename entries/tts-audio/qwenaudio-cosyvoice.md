---
repo: "QwenAudio/CosyVoice"
name: "CosyVoice"
genre: "tts-audio"
url: "https://github.com/QwenAudio/CosyVoice"
flags: ["unverified"]
risk_notes: "GitHubの最新リリースタグと公開日時、ローカルでの推論・APIの動作、必要VRAMと実行速度、日本語の合成品質は未確認。掲載の評価値は開発元の報告。"
stars: 24353
forks: 2777
open_issues: 640
size_kb: 2797
language: "Python"
created: "2024-07-03"
updated: "2026-05-25"
archived: false
license: "Apache-2.0"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/okapi_fukugyo/status/2117616982518559161"]
fetched_at: "2026-11-10T09:57:09+00:00"
---

# CosyVoiceで日本語を含む多言語ナレーションを生成する

## 出来ること

- Fun-CosyVoice 3.0は日本語、英語、中国語など9言語のテキストを音声化できる。利用許諾のある参照音声を使った言語横断のゼロショット音声合成にも対応する。

## 目的・背景

- 台本から動画向けの音声素材を作れる。CosyVoiceの原論文では、多言語音声認識モデルから得た教師あり意味トークンで音声を表現する。
- 開発元の比較表では、Fun-CosyVoice3-0.5B-2512の英語テストで単語誤り率2.24%、CosyVoice2で2.57%と報告されている。この比較表には日本語の評価値がない。

## 依存関係

- 公式手順はCondaのPython 3.10環境、Gitサブモジュール、requirements.txtを使用する。学習済み重みはModelScopeまたはHugging Faceから別途取得する。

## 実行条件

- 公式READMEのDockerによるFastAPI・gRPC配備例はNVIDIAランタイムを使う。
- リポジトリのライセンスはApache-2.0。Fun-CosyVoice3-0.5B-2512の配布ページにもApache-2.0の表示がある。

## 最短手順

- 公式READMEのインストール手順に沿ってPython環境と依存関係を用意し、Fun-CosyVoice3-0.5B-2512の重みを配置する。example.pyのCosyVoice 3向け推論例で短い台本を音声化する。
- AIエージェントから呼ぶ場合は、README記載のFastAPIサーバーと付属クライアントを使う。掲載例のCosyVoice-300Mでサーバーを起動し、エージェントのツールから付属クライアントに台本と選択したモードの入力を渡して、保存した音声ファイルを後工程へ渡す。

## 変更履歴

- 2026-11-10: 初回登録
