---
name: "Lawyer with too many GPUs, part 4: DeepSeek-V4.1-Flash on eight V100s"
genre: "article"
url: "https://reddit.com/r/LocalLLaMA/comments/1xoubyo/lawyer_with_too_many_gpus_part_4_deepseekv41flash"
published: "2026-11-05"
flags: ["unverified"]
risk_notes: "性能値、品質評価、運用結果は投稿者が自身の環境で測定したと述べる数値で、独立した再現確認はしていない。測定条件は記事内に記載されているが、別環境での再現性は不明。"
type: "article"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/ai_hakase_/status/2119384922762674183"]
fetched_at: "2026-11-19T23:09:22.683766+00:00"
---

# Lawyer with too many GPUs, part 4: DeepSeek-V4.1-Flash on eight V100s

## テーマ

- 投稿者が、DeepSeek-V4.1-Flash-1017を8枚のTesla V100-SXM2-32GBで動かした構成と調整内容を報告する記事。GGUFの2-bit量子化モデルを使用し、PP2×TP4で分割したと説明している。

## 著者の主張

- 投稿者の記載では、コード生成の速度は1K入力時215 tok/s、256K入力時160 tok/s。128K入力でのprefillは約2,200 tok/s、リクエストあたりのコンテキスト上限は524,288 tokens。測定はthinking off、greedy、出力1,024 tokens、各セル2回の平均とされる。投稿者は、GPU構成、ソフトウェア、調整前後の比較、ベンチマーク結果、失敗した調整案を公開したと述べている。

## 裏取り・注意点

- 記事本文で確認できるのは投稿者による構成・手順・測定条件と報告値であり、ここでは測定の独立再現や品質評価の妥当性を確認していない。投稿者自身が、110 GBのEngramテーブルはシステムRAMに置かれ、全重みがVRAMにあるという当初の説明は誤りだったと訂正している。また実運用は1リクエストずつで、複数ストリームの性能値は予測段階と記載されている。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 出典

- 記事本文・表示公開日: https://www.reddit.com/r/LocalLLaMA/comments/1xoubyo/lawyer_with_too_many_gpus_part_4_deepseekv41flash/ 。記事中で配布・実装資料として案内されているリポジトリ: https://github.com/ProprietaryLegal/Volta-sPLIt-DeepSeek-V4.1-Flash-1017-8xV100-SXM2-PP2xTP4 。

## 変更履歴

- 2026-11-23: 初回登録
