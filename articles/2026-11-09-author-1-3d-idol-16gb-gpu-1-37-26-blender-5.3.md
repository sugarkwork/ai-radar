---
name: "画像1枚から3Dの「Idol」を16GB GPUで動かした——キャラシート正面1枚が37秒で26万粒のガウシアンスプラットに。Blender 5.3はアドオンなしで読んで撮れた"
genre: "article"
url: "https://make-profit.net/2026/11/09/genai-lab-68-idol-image-to-3d-gaussian-splat-16gb-measured-37s-blender-53-no-addon-turntable/"
published: "2026-11-09"
flags: ["unverified"]
risk_notes: "H3の参照動画に使った場合の改善効果は未検証。記事中の生成時間・VRAM値は作者環境での報告で、異なる環境や入力での性能を保証しない。"
type: "article"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/Phantom_202601/status/2120249912118186495"]
fetched_at: "2026-11-11T01:21:05Z"
---

# 画像1枚から3Dの「Idol」を16GB GPUで動かした——キャラシート正面1枚が37秒で26万粒のガウシアンスプラットに。Blender 5.3はアドオンなしで読んで撮れた

## テーマ

- 正面画像1枚からIdolで3Dガウシアンスプラットを生成し、Blender 5.3で読み込んで撮影する手順と、作者環境での結果を紹介する記事。

## 著者の主張

- 記事の報告では、ComfyUI 0.44.0上で公式モデルを配置し、正面画像から262,144粒のPLYを生成。作者環境のRTX 5060 Ti 16GBでは再測定36.7秒、GPUピーク約4.7GBだった。Blender 5.3 Release Candidateの標準PLY読み込みでガウシアンスプラットとして認識し、正面・側面・背面およびターンテーブル映像を作成できたとしている。

## 裏取り・注意点

- 生成速度やメモリ値は記事著者の環境での報告で、独立実測ではない。背面・靴裏などは1枚の入力からの推定であり、記事自身も形状の歪みや細部の不安定さを記載。出力は編集可能なメッシュやリグ付きモデルではなく、H3の参照動画として使った際の改善は未検証。

## 出典

- 記事本文（公開日: 2026-11-09）: https://make-profit.net/2026/11/09/genai-lab-68-idol-image-to-3d-gaussian-splat-16gb-measured-37s-blender-53-no-addon-turntable/

## 変更履歴

- 2026-11-11: 初回登録
