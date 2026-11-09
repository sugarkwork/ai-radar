---
type: "link"
name: "TailorRig Dataset"
genre: "3d-motion"
url: "https://huggingface.co/datasets/tencent/TailorRig"
author: "Tencent"
pricing: "free"
pricing_detail: "データセットは無償公開。カードは学術研究専用と記載。"
signup_required: false
flags: ["unverified"]
risk_notes: "カードは学術研究専用・商用および製品用途不可と記載。添付LICENSEのTailorRigの定義はコード・重みであり、データへの適用範囲や第三者由来素材の条件は配布元に確認。データ内容やダウンロード後の動作は未検証。"
sources: ["https://x.com/i/status/2119469707267031161", "https://huggingface.co/datasets/tencent/TailorRig", "https://huggingface.co/datasets/tencent/TailorRig/raw/main/LICENSE", "https://xxxx0601.github.io/trig/"]
---

# TailorRig Dataset — リグ付き人体メッシュ研究データ

## 目的

キャラクターの骨格生成・スキニング重み推定などの研究向けデータセット。

## 何ができるか

配布カードは39,073体のメッシュ・関節・親子関係・スキニング重みをNPZに収録と説明。rignet・humanrig・articulation_xlv2・vroidの4種類のZIPがあり、Hugging Face上のファイル一覧で各アーカイブの存在を確認。中身は未取得。論文プロジェクトページのHuman-Mix 38,088体との違いは未確認。

## 料金

データは無償公開。カードは学術研究のみを許し、商用・製品利用を禁止している。

## 登録の要否

公開ページとファイル一覧はログインせず閲覧可能。利用時のアクセス条件は配布元を確認。

## 注意点

添付LICENSEの「TailorRig」はコード・パラメータ・重みに言及する一方、データカードはデータに研究専用条件を適用すると説明する。範囲や第三者由来データの権利が不明な場合は配布元へ確認すること。`np.load(..., allow_pickle=True)`は信頼しないファイルで実行しない。推論用モデルや動作するアプリの配布を意味しない。
