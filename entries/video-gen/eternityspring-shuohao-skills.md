---
repo: "eternityspring/shuohao-skills"
name: "shuohao-skills"
genre: video-gen
url: "https://github.com/eternityspring/shuohao-skills"
license: "Apache-2.0"
stars: 5956
language: "JavaScript"
created: "2026-08-06"
updated: 2026-10-26
added: "2026-11-03"
first_seen: "2026-11-03"
sources: []
flags: []
risk_notes: ""
forks: 827
open_issues: 1
commits_30d: 19
commit_cadence: weekly
size_kb: 15629
archived: false
commits_90d: 100
fetched_at: "2026-11-03T23:05:24Z"
---

# shuohao-skills

## 出来ること

- AI ショートドラマ（短劇）制作の工程を、そのままスキルに切った集合。原作小説の分解 → キャラクターバイブル → あらすじ/脚色方針 → 美術・小道具設定 → 脚本 → 絵コンテ分割、までを受け持つ。
- 各スキルは独立ディレクトリで、単体でコピーしても動く。`novel-characters` だけ入れる、といった部分導入ができる。
- 工程間の受け渡し（前段の出力を次段の入力にする）が README で定義され、5工程分のレポートを1ページにまとめる仕組みもある。
- 実制作で使ったものを公開している、と作者が明記。

## 目的・背景

短劇（縦型ショートドラマ）の制作パイプラインをエージェントに持たせるためのスキル集。特定ランタイムに依存せず、`SKILL.md` を読めるエージェントなら動く。Claude Code と Codex はインストーラが自動検出する。

## 依存関係

- Node.js 18 以上（同梱スクリプトは標準ライブラリのみで、npm 依存はない）。
- エージェントランタイム（Claude Code / Codex / その他 `SKILL.md` を読めるもの）。
- 画像生成はキャラ参照を作る場合のみ: 自前 ComfyUI（Qwen Image）、codex の画像生成、OpenAI API キー（GPT Image 2）、任意コマンドのいずれかを初回に選ぶ。

## 実行条件

- API キーは不要（現在のセッションのクォータを使う）。画像生成を外部 API で行う場合のみキーが要る。
- **出力は中国語前提**。`novel-characters` は英語原作でも中国語の人物設定を出し、英語が混ざるとバリデータが拒否する。他言語運用には改修が要ると README に明記。
- README 冒頭が求職・スポンサー募集の記述になっている（作者が離職中と記載）。内容の評価とは切り離して読む必要がある。

## 最短手順

```bash
git clone https://github.com/eternityspring/shuohao-skills.git
cd shuohao-skills
./scripts/install.sh              # Claude Code / Codex を自動検出して symlink
./scripts/install.sh novel-characters   # 1つだけ入れる
```

## 変更履歴

- 2026-11-03: 初回登録（★5,956 / pushed 2026-10-26 / Apache-2.0）
