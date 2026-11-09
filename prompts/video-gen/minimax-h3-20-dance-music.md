---
type: "prompt"
name: "MiniMax H3：20種のダンスと音楽指定"
genre: "video-gen"
url: "https://x.com/i/status/2119247871341998536"
target: "MiniMax H3"
transcribed_from: "X投稿本文"
prompt_sha1: "3fd546e8aae5bf149eadcce12f10328709402f29"
author: "EndFolding79421"
added: "2026-11-09"
fetched_at: "2026-11-09T04:03:33Z"
flags: ["unverified"]
risk_notes: "投稿本文を原文のまま収録。生成品質や参照画像の一致、音楽と動作の同期は未検証。元投稿には再配布・商用利用条件の明記を確認できていない。ローカルH3の生成物を商用利用するには別途ライセンスが必要。"
sources: ["https://x.com/i/status/2119247871341998536", "https://docs.comfy.org/tutorials/video/minimax/minimax-h3", "https://docs.comfy.org/tutorials/partner-nodes/minimax/minimax-h3"]
---

# MiniMax H3：20種のダンスと音楽指定

## 目的

キャラクターシートを参照し、6秒間の全身ダンスと音楽・環境音を指示するための投稿者のテンプレート。ダンス20種類の音楽指定例を含む。

## 前提

MiniMax H3の参照画像対応ワークフローとキャラクターシートが必要。作者の音楽記述は指示であり、指定通りの振り付け・同期・人物の一致を保証しない。

## プロンプト本文

```text
subject_definitions:
<Subject 1> is the single female character shown across all views in <Picture 1>. Preserve her exact face, hair, body proportions, skin tone, and full outfit from the character sheet.

summary:
[reference generation] A continuous 6-second full-body dance performance of <Subject 1> performing [DANCE] in a clean studio. She dances solo with clear, energetic, style-correct movement.

retention_analysis:
<Subject 1> (appears in [Shot 1]): fully_preserved - face, hair, body, and outfit remain identical to the character sheet.

detailed_description:
Realistic live-action, cinematic lighting.
[Shot 1] Full-body framing of <Subject 1> centered. She performs clear [DANCE] with authentic footwork, arms, posture, and energy. Mostly static camera or slow push-in. Continuous motion, full body visible, no cuts, no extra people.

overall_soundscape:
Soft foot contact, fabric movement, and light room ambience matching the motion.

non_diegetic_music:
[MUSIC]

***Ready-to-use versions for all 20 dances. Just  swap only the dance + music lines.***

1. Flamenco
non_diegetic_music: Passionate Spanish guitar with sharp rhythmic accents, castanets, and dramatic hand claps at a moderate-fast tempo.

2. Tap Dance
non_diegetic_music: Bright swing jazz piano and light percussion with clear rhythmic space for the tapping sounds.

3. Hip Hop
non_diegetic_music: Hard boom-bap hip-hop beat with punchy drums, deep bass, and sparse melodic samples at around 90 BPM.

4. Freestyle
non_diegetic_music: Energetic modern electronic dance track with a driving beat and open space for improvisation.

5. Ballet
non_diegetic_music: Soft classical orchestral piece with flowing strings and gentle piano at a moderate tempo.

6. Jazz
non_diegetic_music: Cool swing jazz with upright bass, brushed drums, and a light saxophone melody.

7. Contemporary
non_diegetic_music: Atmospheric modern instrumental with soft electronic textures, piano, and subtle rhythmic pulse.

8. Breakdancing
non_diegetic_music: Classic funk breakbeat with heavy bass, crisp drums, and 70s/80s electro flavor.

9. Salsa
non_diegetic_music: Lively salsa track with piano montuno, brass stabs, congas, and a strong clave rhythm.

10. Ballroom (Waltz)
non_diegetic_music: Elegant orchestral waltz in clear 3/4 time with sweeping strings.

11. Swing
non_diegetic_music: Upbeat big-band swing with driving rhythm section and bright brass.

12. Belly Dance
non_diegetic_music: Middle Eastern percussion featuring doumbek and frame drum with a steady rhythmic groove and subtle oud.

13. Modern Dance
non_diegetic_music: Minimalist contemporary score with soft piano and ambient electronic layers.

14. Lyrical
non_diegetic_music: Emotional piano-led instrumental with soft strings and a gentle, flowing tempo.

15. Cha-Cha
non_diegetic_music: Bright Latin cha-cha rhythm with piano, percussion, and light brass accents.

16. Tango
non_diegetic_music: Dramatic Argentine tango with bandoneon, piano, and a strong, passionate pulse.

17. Irish Step Dance
non_diegetic_music: Fast traditional Irish tune with fiddle, tin whistle, and bodhrán drum at a lively tempo.

18. Popping
non_diegetic_music: Electro-funk track with crisp synth stabs, punchy drums, and robotic rhythmic accents.

19. Locking
non_diegetic_music: Funky disco/P-Funk groove with tight bass, clap-heavy drums, and bright synths.

20. Waltz
non_diegetic_music: Classic romantic orchestral waltz with flowing strings in clear 3/4 time.
```

## 使い方

キャラクターシートをPicture 1として参照させ、テンプレート内の`[DANCE]`と`[MUSIC]`を使いたいスタイルと対応する音楽説明へ置き換える。20項目は生成時に同時に渡す指示ではなく、選択肢として使う。

## 注意点

生成品質・音楽と動きの同期・音源や人物の権利は未検証。投稿本文の再配布・商用利用条件は確認できていない。ComfyUIのローカルH3生成物の商用利用には別途ライセンスが必要で、クラウド／APIは料金とサービス規約が別。第三者の画像を参照する場合は権利と本人の同意に注意する。
