---
name: "モーショントランスファー用プロンプト（Kling Motion Control など）"
genre: "prompt-other"
url: "https://x.com/Y0urDumble/status/2109342020921659784"
prompt_sha1: "5d1a7ab60f2a9ed063b56569dc7294bac134a471"
target: "ChatGPT などのテキスト/画像生成LLM、および Kling Motion Control 等の image-to-video"
transcribed_from: "text"
flags: []
risk_notes: "実在の人物・有名人・他者のキャラクターに寄せると権利侵害になり得る。効果（再生数・収益）は著者の主張で未検証。"
type: "prompt"
added: "2026-11-08"
first_seen: "2026-11-08"
sources: ["https://x.com/Y0urDumble/status/2109342020921659784"]
fetched_at: "2026-11-07T15:42:23Z"
---

# モーショントランスファー用プロンプト（Kling Motion Control など）

## 目的

- Genjutsu 以外の image-to-video motion control ツール（記事は Kling Motion Control を例示）で、参照動画の動きを静止画キャラクターに演じさせるための指示文。

## 前提

- 参照動画と、キャラクターの全身・顔が分かる画像。記事の推奨は1人・固定カメラ・手が隠れない8〜15秒のクリップ。公式の入力条件は3〜30秒・1カット。

## プロンプト本文

```
My character from the image performs the exact movements from the reference video. 

Keep the face, hair and outfit identical to the image. Match the original timing and camera angle. Realistic skin, natural hands, handheld phone footage look. One person, no text.
```

## 使い方

- Motion Control 系のUIで「キャラクター画像＋参照動画＋このプロンプト」を入力して生成する。
- 1080p で3〜4テイク回し、顔・手・服をフレーム単位で確認して最良を残す。

## 注意点

- 参照画像の背景や照明が動画に漏れる（reference bleed）、元映像の背景・ロゴは残る、元音声の権利は別問題、という限界がある。人物の差し替えであって背景の権利処理ではない。

## 変更履歴

- 2026-11-08: 初回登録
