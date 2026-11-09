---
name: "Claude Code に Blender のシーンをコードで書かせて voxel キャラを踊らせる手順（投稿）"
genre: "link-inspiration"
url: "https://x.com/Y0urDumble/status/2113374545302200732"
author: "@Y0urDumble (Dumble)"
pricing: "free"
pricing_detail: "無料。Blender（無料）＋ Claude Code（モデル利用料）＋ 2つの無料スキルで完結し、有料素材の購入は不要と投稿は述べる。"
signup_required: false
flags: ["unverified"]
risk_notes: "投稿内の `blender -b -P https://t.co/ueDlwhvcq2` のリンク先 scene.py は DNS 解決不可（HTTP 000、Wayback スナップショットも 0 件）で、投稿が想定したスクリプト／記事の実体を確認できない。X の引用元は Article 2109318233866006528 でログイン必須のため本文未取得。「Opus 5.5 が無料で1000倍良い」は投稿者の主張で、比較測定は無い。動画は 3D ビューポートそのものではなく UI オーバーレイ付きの演出済みデモ（ログ表示は擬似 UI）であり、719 voxels / 12 joints / 16 秒 / 120bpm は投稿者と動画の自己申告値。実際の再現には Blender 5.2 系と Claude Code、上記2スキルが必要。"
type: "link"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/Y0urDumble/status/2113374545302200732"]
fetched_at: "2026-11-08T20:07:36Z"
---

# Blender を開かずに voxel キャラを作って踊らせる — Claude Code にシーンをコードで書かせる手順

## 目的

- AI インフルエンサー生成で問題になる「顔のドリフト」を、3D モデル（ファイルとして固定される資産）に置き換えて回避する。投稿者は、Blender の UI を一切開かず、Claude Code に Python を書かせて headless 実行させ、voxel キャラのモデリング→リグ→ダンスまで通したと主張している。

## 何ができるか

- 投稿が示す6段の手順：(1) Blender 5.2（無料）と Claude Code を用意 (2) キャラの説明＋参照画像を1枚渡す（プロンプト例「voxel toy style, white sticker outline, bright background」）(3) Claude が Python を書いて `blender -b -P <script>` で headless 実行 (4) 先に4〜5フレームだけレンダさせて自分で確認させる（破綻を自分で見つける）(5) メッシュ→リグ→アニメの順に段階を分け、リグは同じプロンプトで頼む (6) 最後に本番レンダ（Eevee、普通の PC）。
- 投稿の実測値（自己申告）：719 voxels を層ごとに構築、12 ジョイント＋T-pose テスト、16 秒 / 120bpm のダンス、音楽も Python で合成（サンプル・外部アセットのダウンロードはゼロ）。
- 実見した動画でも同じ数字が UI 上に出る：BUILD 562/719 voxels → mesh.done(719 voxels) → rig.auto(joints=12) → rig.test(pose='T') → anim.dance(bpm=120, beats=12)。キャラは黄土色スーツ・白シャツ・赤ネクタイ・黒サングラス・口ひげ・ピンクのポンパドールという voxel 造形で、太い白フチと明るい背景という指定どおりの見た目。
- 再利用の勘所は「シーンをコードとして書かせる」「プレビュー数フレームで自己検証させる」「参照画像を1枚渡す」の3点。投稿者は参照無しの初版が「2008年の学校プロジェクト」のようだったと述べている。

## 料金

- 無料。Blender は無料、スキル2本も無料（MIT）。コストは Claude Code のモデル利用料のみ。

## 登録の要否

- 登録不要（Blender と Claude Code をローカルに入れるだけ）。ただし投稿内の手順リンク（scene.py）は現在 DNS 解決不可で開けないため、手順は投稿本文の記述と動画から再構成する必要がある。

## 変更履歴

- 2026-11-09: 初回登録
