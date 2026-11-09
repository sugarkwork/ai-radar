---
name: "Poly Haven"
genre: "link-asset"
url: "https://polyhaven.com/"
author: "Poly Haven"
pricing: "free"
pricing_detail: "全アセット（HDRI/テクスチャ/3Dモデル）が CC0 で無料。商用利用可、クレジット不要、再配布可。Patreon は任意。API も無料・キー不要。"
signup_required: false
flags: ["unverified"]
risk_notes: "CC0・無料・アカウント不要は公式ライセンスページで確認。『luxury = 90% lighting』は投稿者の意見で、動画内のレンダーが Poly Haven のどの HDRI/テクスチャを使ったかはクレジットもファイル名もなく特定できない。公開 JSON API は 200 を確認したが、アセットごとの解像度・ファイルサイズ・レート制限は公式ページの表示範囲では未確認。投稿の $1,500–5,000 や 15秒/4ショット/3フォーマットの納品実績は未検証。"
type: "link"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/Y0urDumble/status/2114084322227503206"]
fetched_at: "2026-11-09T13:18:50Z"
---

# Poly Haven — CC0 の HDRI・テクスチャ・3D モデル素材ライブラリ

## 目的

- 投稿の LIGHT 工程。スタジオ HDRI と PBR テクスチャを Blender に取り込み、ガラス/液体/金の反射と照明を作るための素材ライブラリ。実行ツールではなく参照・素材。
- 無料で商用利用できる HDRI を探す用途に向く。ライティングの土台を一から作らず、既存の HDRI で環境光を立ててから Blender 側で調整する使い方。

## 何ができるか

- 16k+ の HDRI、PBR テクスチャ（diffuse/normal/roughness/displacement など）、3D モデルをダウンロード。Blender の Asset Browser や通常の画像/EXR 読み込みで使う。
- 公開 JSON API `https://api.polyhaven.com/assets?t=hdris` が 200 で応答（2026-11-09 実測）。MCP for Blender の `search_assets` / `import_asset` から Poly Haven の HDRI/テクスチャ/モデルを検索・取り込みできる。
- Poly Haven 自身の MCP サーバーは確認できない。AI から直接呼ぶなら API を叩くスクリプトか、Blender MCP 経由になる。
- 投稿の『free HDRIs + textures』は事実。『luxury = 90% lighting』は意見で、どのアセットを何割使ったかは動画から特定できない。

## 料金

- 無料。全アセット CC0（パブリックドメイン相当）。商用利用可、クレジット不要、再配布可。
- Patreon は任意。API も無料で、API キーは不要。
- 素材を商品に含めて販売することもできるが、Poly Haven のサイト自体には別途利用規約があり、素材ライセンスとは別に適用される。

## 登録の要否

- 不要。アカウントも API キーも不要。ダウンロードして使うだけ。
- Blender から使う場合は、手動でダウンロードして読み込むか、MCP for Blender の Poly Haven 検索・取り込みを使う。
- API 利用時のレート制限は公式に明示を確認していない。大量アクセスは避け、必要なアセットだけ取得する。

## 変更履歴

- 2026-11-09: 初回登録
