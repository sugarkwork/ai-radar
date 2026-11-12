---
name: "Klik Motion-Graphics System"
genre: "coding-agent"
url: "https://github.com/t3knobox/klik-anim-skill-creation"
repo: "t3knobox/klik-anim-skill-creation"
license: "unknown"
stars: 96
language: "Python"
created: "2026-08-03"
updated: "2026-08-06"
forks: 19
open_issues: 0
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 761
archived: false
flags: ["unverified"]
risk_notes: "ライセンスはGitHub API上で不明。利用許諾の条件は確認できていない。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-12"
first_seen: "2026-11-12"
sources: ["https://x.com/PromptLabCN/status/2120750742785171596"]
fetched_at: "2026-11-12T06:12:46.568650+00:00"
---

# Klik Motion-Graphics System

## 出来ること

- Remotionでのアニメーション制作向けに、要素の動き方を扱う`klik-anim`、カメラ移動を扱う`klik-cam`、プロンプトから動画制作までの工程を扱う`klik-remotion-method`を提供する。READMEは、`klik-anim`をイージング・タイミング・振付・視線誘導・チェックリストなどの指針、`klik-cam`をカメラ文法とチェックリスト、`klik-remotion-method`を要件整理、静止画ストーリーボード、実行計画、実装、QAの工程として説明している。

## 目的・背景

- 単体のアニメーション制作には`klik-anim`と`klik-cam`、プロンプトからの動画制作には3スキルすべてを使う構成を案内している。READMEによると、KlikスキルはRemotion公式スキルを現行APIの参照元とし、未導入の場合はAPIを推測せず導入範囲を利用者に確認するよう指示する。

## 依存関係

- `klik-anim`は単独で利用可能。`klik-cam`は`klik-anim`に依存し、`klik-remotion-method`は両方に依存する。Remotion公式のagent skillsは事前導入が推奨される。音声分析でより詳細な分離を使う場合は`demucs`が任意で必要とされる。READMEは、`demucs`がない場合も周波数帯域による分析にフォールバックすると説明している。

## 実行条件

- READMEに記載された導入先はClaude Code（CLIまたはVS Code拡張）とCowork。Claude Codeではリポジトリからスキルフォルダーをコピーし、Coworkでは`dist/`の`.skill`ファイルをチャットに追加して保存する。READMEは、約30秒以上の動画制作でセッション使用量制限に達することがあると作者の注意事項として記載している。これは独立実測の結果ではない。

## 最短手順

- Claude Codeでアニメーション用スキルを使う場合、README記載の手順は、Remotion公式スキルを導入し、リポジトリを取得して`klik-anim`と`klik-cam`を`~/.claude/skills/`へコピーし、セッションを再起動して`/`一覧に表示されることを確認する流れ。全工程を使う場合は`klik-remotion-method`もコピーする。Coworkでは`dist/`から必要な`.skill`ファイルを追加して保存する。

## 変更履歴

- 2026-11-12: 初回登録
