---
repo: "elevenlabs/skills"
name: "ElevenLabs Skills"
genre: "tts-audio"
url: "https://github.com/elevenlabs/skills"
stars: 547
forks: 94
open_issues: 5
size_kb: 1031
language: "Python"
created: "2026-01-24"
updated: "2026-11-04"
archived: false
license: "MIT"
commits_30d: 13
commits_90d: 32
commit_cadence: "weekly"
flags: ["unverified"]
risk_notes: "最新リリースのタグと公開日時は確認できなかった。スキルの起動、生成音の品質・所要時間、個別API機能の課金条件と生成物の商用利用条件は未検証。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/Y0urDumble/status/2117396633889427646"]
fetched_at: "2026-11-10T08:52:35+00:00"
---

# ElevenLabs Skills — AIアシスタントからナレーション・効果音・BGMを生成

## 出来ること

- 台本を読み上げ音声に変換し、テキストから効果音や楽曲を生成できる。効果音スキルにはループ、長さ、プロンプトへの追従度を調整する設定がある。 [効果音スキル定義](https://github.com/elevenlabs/skills/blob/main/sound-effects/SKILL.md)

## 目的・背景

- Agent Skills仕様に沿って、対応アシスタントが用途に応じたAPI呼び出しを組み立てるための手順を提供する。公式READMEは起動判定と機能評価のコードを案内している。今回の確認は公開文書の閲覧まで。 [公式README](https://raw.githubusercontent.com/elevenlabs/skills/main/README.md)

## 依存関係

- インストールにはnpx、利用にはAgent Skills対応アシスタントが必要。呼び出し経路は公式CLI、Python SDK、JavaScript/TypeScript SDKから選べる。 [公式README](https://raw.githubusercontent.com/elevenlabs/skills/main/README.md)

## 実行条件

- インターネット接続とElevenLabs APIキーを用意し、実行環境で `ELEVENLABS_API_KEY` を設定する。リポジトリはMIT。サービス料金と生成物の利用条件は、利用する機能とプランに応じて公式の案内を確認する。 [効果音スキル定義](https://github.com/elevenlabs/skills/blob/main/sound-effects/SKILL.md) [公式料金表](https://elevenlabs.io/pricing)

## 最短手順

- `npx skills add elevenlabs/skills` で導入し、APIキーを設定する。対応アシスタントに『sound-effectsスキルで、木の扉がきしんで閉まる効果音を生成し、音声ファイルに保存してパスを返して』と依頼する。 [公式Agent Toolingガイド](https://elevenlabs.io/docs/eleven-api/resources/agent-tooling)

## 変更履歴

- 2026-11-10: 初回登録
