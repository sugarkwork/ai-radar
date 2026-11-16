---
name: "ray-sticker-shop"
genre: "image-gen"
url: "https://github.com/imraywang/ray-sticker-shop"
repo: "imraywang/ray-sticker-shop"
license: "MIT"
stars: 500
language: "Python"
created: "2026-11-05"
updated: "2026-11-05"
forks: 57
open_issues: 1
commits_30d: 1
commit_cadence: "monthly"
commits_90d: 1
size_kb: 16
archived: false
flags: ["unverified"]
risk_notes: "README указывает ориентировочную стоимость около $0.7 для 8 стикеров и 5 дополнительных материалов по официальным тарифам OpenAI; фактическая стоимость зависит от повторной генерации. Прохождение модерации и доход не гарантируются."
type: "repo"
added: "2026-11-16"
first_seen: "2026-11-16"
sources: ["https://x.com/ganfanren_ai/status/2119020240348835900"]
fetched_at: "2026-11-16T01:30:37.681458+00:00"
---

# ray-sticker-shop

## 出来ること

- READMEによると、参考画像やキャラクター画像から、キャラクターの一貫性を保った動く表情包一式を生成し、微信表情开放平台向け素材をまとめます。240×240 GIFを500KB以内に圧縮し、表紙・アイコン・バナー・赞赏图、掲載文案、納品用パッケージを作成すると説明されています。規格に沿った自動チェックも記載されています。

## 目的・背景

- READMEは、GIFを一枚ずつ作るとキャラクターの見た目が揺れやすく、微信の指定サイズにも合わせる必要があることを背景として挙げています。

## 依存関係

- Python 3.9以上、Pillow、画像生成に使うOPENAI_API_KEYが必要とREADMEに記載されています。中継サービスを使う場合はOPENAI_BASE_URLも設定します。

## 実行条件

- README記載の方法は、リポジトリのフォルダーをAgentのskillsディレクトリに置き、Claude CodeまたはCodexに画像から表情包を作るよう依頼するものです。APIキーがない場合は、Agentが提示するプロンプトをChatGPTで使い、生成画像を戻して合成する代替手順も説明されています。利用する形象について権利を持つことが必要で、審査結果は微信が決定し、審査通過や収入は保証されません。

## 最短手順

- READMEの例では、`git clone https://github.com/imraywang/ray-sticker-shop ~/.claude/skills/ray-sticker-shop`で配置し、Claude CodeまたはCodexに「把这张猫的照片做成一套表情包。」と依頼します。実行にはPython 3.9以上とPillowを用意し、API生成を使う場合はOPENAI_API_KEYを設定します。

## 変更履歴

- 2026-11-16: 初回登録
