---
name: "MiniMax H3の8秒カメラ接近をBlenderの白素体で設計し、縦じまを比較した記録"
genre: "video-gen"
url: "https://make-profit.net/2026/11/08/genai-lab-61-minimax-h3-drone-approach-8s-rear-camera-blender-12step-sky-stripes/"
published: "2026-11-08"
flags: ["unverified"]
risk_notes: "生成時間と縦じまの変化は記事著者の報告で、独立した再測定はない。記事も1組の比較のみで、縞が減った原因をステップ数だけとは断定していない。"
type: "article"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/Phantom_202601/status/2119200865865306464"]
fetched_at: "2026-11-19T04:09:48.111744+00:00"
---

# MiniMax H3の8秒カメラ接近をBlenderの白素体で設計し、縦じまを比較した記録

## テーマ

- Blenderで作成した白素体のカメラ軌道を使い、MiniMax H3で走る人物を後方上空から8秒追う動画を生成した記録。

## 著者の主張

- 著者は、カメラの高さ・後方距離・俯角を始点と終点で指定し、smoothstepで補間した白素体を参照に使ったと報告。8秒版ではカメラ高を6.5mから3.4m、後方距離を11mから6.3mへ移動させ、全コマで人物全身が画面内の余白に収まるか検査してから書き出したという。著者の比較では、同じseedなどの条件で10から12ステップに変更した結果、空の赤・黄系の縦じまが比較コマで目立たなくなった。

## 裏取り・注意点

- MiniMaxの公式モデル資料では、H3は動画と音声を生成し、出力時間は4〜15秒、標準フレームレートは24fpsとされる。日本語は安定対応する対話言語11言語の一つ。記事の具体的なカメラ制御法、所要時間、画質比較は著者の実験報告であり、公式資料による再現確認や独立測定ではない。記事自身も比較は1組で、ステップ数だけが縞の原因とは言えず、15・20ステップは未検証としている。

対応言語: MiniMax H3公式資料は、安定対応する対話言語としてアラビア語、中国語、英語、フランス語、ドイツ語、イタリア語、日本語、韓国語、ポルトガル語、ロシア語、スペイン語を列挙。その他の言語も程度の差はあるが対応すると記載。（出典: https://huggingface.co/MiniMaxAI/MiniMax-H3）
日本語対応: 対話言語は日本語に安定対応。記事の動画生成で日本語プロンプトを使った場合の品質や条件は、この記事では確認されていない。（出典: https://huggingface.co/MiniMaxAI/MiniMax-H3）

## 出典

- 記事本文・公開日: https://make-profit.net/2026/11/08/genai-lab-61-minimax-h3-drone-approach-8s-rear-camera-blender-12step-sky-stripes/
MiniMax H3公式モデル資料: https://huggingface.co/MiniMaxAI/MiniMax-H3

## 変更履歴

- 2026-11-23: 初回登録
