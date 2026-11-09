---
name: "Opus Edit Machine"
genre: "link-inspiration"
url: "https://opus-edit-machine.vercel.app/"
pricing: "free"
pricing_detail: "無料。ページ内に料金表示・課金導線・アカウント機能はなく、three.js の静的サイトとして配信されている（2026-11-09 時点）。"
signup_required: false
author: "Dumble (@Y0urDumble)"
flags: ["unverified"]
risk_notes: "ページ自身が『The footage, timings and counts are a simulation for teaching, not a benchmark.』と明記しており、40:12 → 00:58 は画面内の固定値であって実測ではない。動作するのは3Dデスクの操作と、工程ごとのプロンプトのコピーまで。プロンプトを Claude に渡して実際に58秒の編集が出るかは未検証。投稿の『Opus 5.5 が After Effects を代替した』も投稿者の主張で、Anthropic 公式に動画編集向け pre-built skill はない（文書系4種のみ）。なお Claude Opus 5.5 自体の存在は Anthropic 公式で確認できる（2026-09-22 公開、$4/$20 per MTok）。"
type: "link"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/Y0urDumble/status/2113730624989102489"]
fetched_at: "2026-11-09T07:41:05Z"
---

# Opus Edit Machine — 8工程の動画編集パイプラインを触って壊せる3D教材

## 目的

- 「40分の生素材が58秒の縦動画になるまで」を、8つの工程（station）に分解して体感するためのブラウザ教材。実際に動画を編集するツールではなく、各工程で何を判断しているか・どこを間違えやすいかを3Dデスク上で再現する。制作者は映像編集者・モーションデザイナーで、AI 編集パイプラインの工程分解を示す目的で作られている。

## 何ができるか

- 8ステーション: Ingest（40分の素材と文字起こし）→ Find the hook（58秒に値する箇所の選定）→ Cut（無音・フィラー除去）→ Reframe 9:16（顔追従の縦切り）→ Captions（1〜3語のカード）→ Motion（キーフレームとカーブ）→ Sound（声優先のダッキング）→ Render（MP4 書き出し）。順に実行するとタイムラインと進捗（0/8 → 8/8）が組み上がる。
- 各工程に「壊す」ボタンがあり、文字起こしなしの取り込み、中央固定クロップ、リニアキーフレーム、声を埋もれさせるミックスなどを意図的に試して、失敗がどこに出るかを見られる。
- 各工程の『Copy prompt』で、そのまま Claude に貼れるプロンプトを取得できる。例（Ingest）: 「Transcribe raw.mp4 with word-level timestamps. Save it as transcript.json, then list the 5 longest pauses and every filler word (um, uh, like) with its timecode.」Cut は無音0.35秒超とフィラーの除去、0.15秒の呼吸を残す編集判断リストを ffmpeg の concat スクリプトとして出させる内容。
- 工程ごとに「What happens here」「Editor's note」「Check yourself（理解度クイズ）」が付き、用語の暗記ではなく判断の理由を確認できる。
- 3D ビューはドラッグで回転・スクロールでズーム。被写界深度、ラベル表示、BGM、画質の切り替えがある。

## 料金

- 無料。ページ内に料金表・サブスク導線・従量課金の表示はない。
- サイト自体は静的な three.js アプリで、外部 API の呼び出しや API キーの入力は求められない。プロンプトの実行は自分の Claude（Claude Code など）側の契約・利用料で行う。

## 登録の要否

- 不要。ログインもサインアップもなく、URL を開けばそのまま操作できる。
- WebGL が動くブラウザが必要。プロンプトを使う段になって初めて、自分の Claude 環境（Claude Code / claude.ai など）と素材（raw.mp4、transcript.json）を用意する。

## 変更履歴

- 2026-11-09: 初回登録
