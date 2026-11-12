---
name: "無料の動画モーキャプ「RGB MoCap」を試したらすごかった話"
genre: "article"
url: "https://note.com/yosfuku/n/nf844a5ebb48c"
published: "2026-11-07T21:19:00+09:00"
flags: ["unverified"]
risk_notes: "記事で報告される処理時間、メモリ・VRAM使用量、精度や補正効果は著者の特定環境・動画での結果であり、独立した測定や一般的な性能保証ではない。"
type: "article"
added: "2026-11-12"
first_seen: "2026-11-12"
sources: ["https://x.com/luaginga777/status/2119042246637187413"]
fetched_at: "2026-11-12T23:09:02Z"
---

# 無料の動画モーキャプ「RGB MoCap」を試したらすごかった話

## テーマ

- 動画から3Dキャラクター用のモーションを生成するWindowsアプリ「RGB MoCap」の機能と、ブレイクダンス動画を用いた著者の使用記録。

## 著者の主張

- 著者はExMRとFlowHMRを同じ動画で試し、FlowHMRでは床からの浮きが比較的抑えられ、手の接地区間をタイムラインで指定する補正で手の滑りがほぼ止まったと報告。一方、補正後に肘の曲がりが増え、Blenderで追加修正した。5人の動画でも複数人を処理できたと報告している。これらは著者の試用結果であり、独立実測ではない。

## 裏取り・注意点

- 公式READMEは複数人の処理、接地補正、キャラクターへのリターゲット、FBX・BVH・VMD・Blenderプロジェクト等の出力を説明している。記事の具体的な速度、VRAM・メモリ量、精度、手滑りの改善値は著者の環境と素材での報告。記事も推定・補正後に手作業の修正が必要な例を示す。モデルや身体データにはアプリ本体と異なる利用条件があるため、用途に応じ各提供元の条件確認が必要。

## 出典

- 記事本文・公開日: https://note.com/yosfuku/n/nf844a5ebb48c
RGB MoCap公式README（記事内の機能説明の参照先）: https://github.com/toyxyz/toyxyz_RGBMocap

## 変更履歴

- 2026-11-12: 初回登録
