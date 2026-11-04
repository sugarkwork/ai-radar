---
repo: "eternityspring/shuohao-skills"
name: "shuohao-skills"
genre: video-gen
url: "https://github.com/eternityspring/shuohao-skills"
license: "Apache-2.0"
stars: 6003
language: "JavaScript"
created: "2026-08-06"
updated: 2026-10-26
added: "2026-11-03"
first_seen: "2026-11-03"
sources: []
flags: []
risk_notes: ""
forks: 833
open_issues: 1
commits_30d: 19
commit_cadence: weekly
size_kb: 15629
archived: false
commits_90d: 100
fetched_at: "2026-11-04T22:52:44Z"
---

# shuohao-skills

## 出来ること

- AI ショートドラマ（短劇）制作の工程を、そのままスキルに切った集合。原作小説の分解 → キャラクターバイブル → あらすじ/脚色方針 → 美術・小道具設定 → 脚本 → 開場の立ち位置 → 絵コンテ分割、までを受け持つ。
- **`character-refs`**: 物語のキャラクターの参考画像を実際に生成する。小説原作に限らず、オリジナルのキャラクターでも使える。一段落の説明から項目を分解して不足を補い、確認表を出してから、正面全身のアンカーを起点に顔アップ・90° 側面・背面・細部・45° アップを段階的に生成する。画像ごとに識別情報が付き、1枚単位で作り直せる。
- **`novel-staging`**: 脚本と絵コンテの間に、各場の開場の立ち位置（誰がどの家具のどちら側に座る／立つか、向き、群演）を決める工程を挟む。俯視図のレポートをブラウザでドラッグして調整できる。
- 各スキルは独立ディレクトリで、単体でコピーしても動く。`novel-characters` だけ入れる、といった部分導入ができる。
- 工程間の受け渡し（前段の出力を次段の入力にする）が README で定義され、5工程分のレポートを1ページにまとめる仕組みもある。
- 実制作で使ったものを公開している、と作者が明記。

## 目的・背景

短劇（縦型ショートドラマ）の制作パイプラインをエージェントに持たせるためのスキル集。特定ランタイムに依存せず、`SKILL.md` を読めるエージェントなら動く。Claude Code と Codex はインストーラが自動検出する。

## 依存関係

- Node.js 18 以上（同梱スクリプトは標準ライブラリのみで、npm 依存はない）。
- エージェントランタイム（Claude Code / Codex / その他 `SKILL.md` を読めるもの）。
- 画像生成は `character-refs` で必須: 自前 ComfyUI（Qwen Image 2.1）、codex 内蔵の画像生成、OpenAI Images API（gpt-image-2）、任意コマンドのいずれかを初回に選ぶ。主画像と派生画像で別のモデルも使え、1枚だけ作り直すときに切り替えることもできる。

## 実行条件

- API キーは不要（現在のセッションのクォータを使う）。画像生成を外部 API で行う場合のみキーが要る。
- **出力は中国語が既定**。`novel-characters` は英語原作でも中国語の人物設定を出し、英語が混ざるとバリデータが拒否する。レポートは `render --lang en` で英語にもできる（データ本体は原文のまま）。`character-refs` の確認表とレポートは中国語・英語・日本語に対応し、他の言語は `ui-template` で文案を訳して渡す。
- README 冒頭が求職・スポンサー募集の記述になっている（作者が離職中と記載）。内容の評価とは切り離して読む必要がある。

## 最短手順

```bash
git clone https://github.com/eternityspring/shuohao-skills.git
cd shuohao-skills
./scripts/install.sh              # Claude Code / Codex を自動検出して symlink
./scripts/install.sh novel-characters   # 1つだけ入れる
./scripts/install.sh character-refs     # 参考画像の生成だけ入れる
```

## 変更履歴

- 2026-11-03: 初回登録（★5,956 / pushed 2026-10-26 / Apache-2.0）
- 2026-11-04: character-refs（キャラ参考画像の生成）と novel-staging（開場の立ち位置）を追記、レポートの言語設定の記述を修正（5612d2a）
