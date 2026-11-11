---
repo: "1weiho/skills"
name: "cinematic-shot"
genre: "video-gen"
url: "https://github.com/1weiho/skills"
license: "MIT"
stars: 240
forks: 8
open_issues: 1
size_kb: 425
language: "JavaScript"
created: "2026-10-13"
updated: "2026-10-29"
archived: false
commits_30d: 19
commits_90d: 19
commit_cadence: "weekly"
flags: ["unverified"]
risk_notes: "作者のデモ映像の画質・再現性、対応エージェントごとの導入とレンダリング、実行時間や費用は未検証。GitHubの公開リリース一覧には掲載なし。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/sumika45379/status/2115934204747972903"]
fetched_at: "2026-11-10T12:48:23Z"
---

# cinematic-shotで製品UIの告知動画と静止画を設計する

## 出来ること

- 製品UIの斜めからの接写、浅い被写界深度、緩やかなカメラ移動、操作に合わせたカットを、告知動画の分鏡に落とし込む。同じ画づくりをヒーロー画像やSNSカードにも応用できる。 [README](https://raw.githubusercontent.com/1weiho/skills/main/README.md)

## 目的・背景

- 入力や結果表示など、UI上の動作で機能を見せる。作者の分鏡例では動作に合わせて尺を変え、見せ場で画面全体を映す。これは作者の制作例で、効果の比較実測ではない。 [分鏡例](https://raw.githubusercontent.com/1weiho/skills/main/skills/cinematic-shot/references/shot-list-example.md)

## 依存関係

- 導入にはREADME記載の `npx` とスキルを読み込めるエージェントを使う。映像のレンダリング環境はエージェント側で選ぶ。リポジトリはMITで、選んだ実行環境や撮影素材の利用条件と費用は別途確認が必要。 [README](https://raw.githubusercontent.com/1weiho/skills/main/README.md)

## 実行条件

- 撮影対象のUIと、見せたい操作や結果を用意する。動画では、各フレームが時刻だけで決まるように実装する方針をスキルが示している。 [スキル定義](https://raw.githubusercontent.com/1weiho/skills/main/skills/cinematic-shot/SKILL.md)

## 最短手順

- READMEの手順 `npx skills add 1weiho/skills --skill cinematic-shot` で対象スキルを追加する。スキルを読み込んだエージェントに、対象画面と見せたい操作を添えて『cinematic-shotを使って、新しい検索機能の告知動画を作って』と依頼する。 [README](https://raw.githubusercontent.com/1weiho/skills/main/README.md)

## 変更履歴

- 2026-11-11: 初回登録
