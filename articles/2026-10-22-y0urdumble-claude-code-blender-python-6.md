---
name: "Claude Code に Blender シーンを Python で書かせ、ヘッドレスで回す6段階"
genre: "article"
url: "https://x.com/Y0urDumble/status/2113374545302200732"
published: "2026-10-22"
author: "@Y0urDumble"
source_post: "https://x.com/Y0urDumble/status/2113374545302200732"
article_url: "https://x.com/i/article/2109318233866006528"
sources: ["https://x.com/Y0urDumble/status/2113374545302200732", "https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html", "https://docs.blender.org/manual/en/latest/advanced/command_line/render.html", "https://docs.blender.org/manual/en/latest/render/eevee/index.html", "https://www.blender.org/download/", "https://www.anthropic.com/pricing", "https://platform.claude.com/docs/en/about-claude/pricing", "https://github.com/arjun988/blender-skills"]
first_seen: "2026-10-22"
added: "2026-11-08"
flags: ["unverified", "low-quality"]
risk_notes: "主張: 719 voxels・12 joints・16秒/120bpm・音楽も Python 合成・参考画像1枚で修正・『Opus 5.5 が無料でやった』『Blender を一度も開いていない』。確認できた: blender -b（UIなし）と -P（スクリプト実行）は公式引数で、-f によるフレーム単位レンダーも公式。EEVEE は実在しラスタライズ方式。Blender 5.2.3 LTS は投稿当日の 2026-10-22 リリースで無料（GPL）。動画は実測 16.04 秒で『16 sec』と一致。確認できず: 719 voxels / 12 joints / 120bpm / 音楽合成のいずれも投稿と動画キャプション以外の裏付けがなく、再現スクリプトも第三者検証もない。手順3の t.co は scene.py が URL と誤認されたもので資料ではない。誤り・誇張: Free プランに Claude Code は含まれず『無料』は不正確（Pro 月20ドル、Opus 5.5 API は $4/$20 per MTok）。動画のオーバーレイは『CLAUDE OPUS 5.5 x BLENDER MCP』『mcp.connect(blender)』で、ヘッドレス実行とも『一度も開いていない』とも食い違う。『28 beats . 120 bpm』は14秒、ログの beats=12 は6秒で、16秒と整合しない。配布物 arjun988/blender-skills は MCP 前提の 94 skills で、headless/719/120bpm/12 joints の記述は0件——投稿の主張と配布物の実体は別物。『3Dはドリフトしない』は形状のみで、ライティング・フレーミング・アニメーションで印象は変わる（返信で同旨の指摘、著者も同意）。記事本文はログイン必須で未取得のため、記事内の詳細・コード・プロンプトは未確認。"
fetched_at: "2026-11-08T20:52:35Z"
type: "article"
---

# Claude Code に Blender シーンを Python で書かせ、ヘッドレスで回す6段階

## テーマ

- コーディングエージェント（Claude Code 等）に Blender のシーンを Python スクリプトとして書かせ、GUI を開かずにモデリング→リグ→アニメーションまで組み立てる技法。2026-10-22 の @Y0urDumble の投稿が、ボクセル調キャラクターを踊らせた例として6ステップで紹介した。
- 投稿の文脈は「AIインフルエンサーの顔ドリフト対策」。生成モデルで毎回作り直すのではなく、3D アセットを自前で持つという発想。手順の全文は X の記事（ログイン必須）にあるとされるが、本文は取得できていない。
- 同じ投稿が紹介する配布物（arjun988/blender-skills の /voxel-style、typingmind の /scenario-blender-animation）は別項目で扱う。ここでは手順そのものを扱う。

## 著者の主張

- 手順1: Blender 5.2（無料）と Claude Code を入れる。手順2: キャラクターの説明と参考画像1枚（例「voxel toy style, white sticker outline, bright background」）。
- 手順3: Claude が Python スクリプトを書き、blender -b -P scene.py でヘッドレス実行する。手順4: 本番前に4〜5フレームだけレンダーして自分で見て、壊れた箇所を直す。
- 手順5: mesh → rig → animation の順に段階を分ける（リグは同じプロンプトで頼む）。手順6: 最後に EEVEE で本番レンダー、普通のPCで足りる。
- 成果として 719 voxels、12 joints と T-pose テスト、16秒・120bpm のダンス、音楽も Python で合成、サンプル素材はゼロと主張。
- 「Opus 5.5 が無料でやった」「Blender は一度も開いていない」「3Dモデルはドリフトしない」という主張を添えている。

## 裏取り・注意点

- 公式と一致: -b/--background は「Run in background (often used for UI-less rendering)」、-P/--python は「Run the given Python script file」。引数は順序依存で「Always position -f or -a as the last arguments」なので、レンダー系のフラグは最後に置く。
- -P が取るのはローカルのファイルパス。URL を渡す引数ではない。例外時に非ゼロで落としたいなら --python-exit-code を併用する（既定は無効）。
- 手順3の t.co リンクは資料ではない。転送先は https://scene.py/ で DNS 解決不可。X がファイル名 scene.py の .py（パラグアイの ccTLD）を URL と誤認して自動リンク化したもので、コマンド例の実体は blender -b -P scene.py。
- 4〜5フレームのプレビューは -f で実装できる。ただし「エージェントが画像を見て自己修正する」部分は Blender 側の機能ではなく、画像を読めるエージェント側に依存する。公式に定められた自己修正ループはない。
- EEVEE は公式に「realtime render engine focused on speed and interactivity」「based on rasterization and is not a path tracer」。通常PCのプレビューや最終レンダーに向くが、物理的な正確さでは Cycles に劣る。
- Blender 5.2.3 LTS は 2026-10-22 リリース（投稿と同日）。「Blender 5.2 は無料」は正しい（GPL）。バージョン指定としては妥当。
- 数値は未検証: 719 voxels / 12 joints / 120bpm / 音楽も Python 合成は、投稿本文と動画の焼き込みキャプション以外に裏付けがない。動画は実測 16.04 秒で「16 sec」は一致するが、オーバーレイの「28 beats . 120 bpm」は14秒、ログの anim.dance(bpm=120, beats=12) は6秒で、16秒と噛み合わない。
- 動画のオーバーレイは「CLAUDE OPUS 5.5 x BLENDER MCP」「mcp.connect('blender') ok 5.2.3」。実演は GUI の Blender に MCP アドオンで繋ぐ方式で、blender -b のヘッドレスとも「一度も開いていない」とも食い違う。ログは演出として描かれた HUD で、実ログではない。
- 配布物との差: arjun988/blender-skills の README（実測 stars 2,237 / forks 193 / MIT / 94 skills）に headless・blender -b・719・120bpm・12 joints の記述は0件。実行方式は「Every skill executes directly in Blender via MCP」で GUI 前提。投稿の主張と配布物の実体は別物。
- 「無料」は不正確: Anthropic の料金ページで Free プランは Claude Code 非対応。Claude Code は Pro（月20ドル、年払い17ドル）以上。API の Opus 5.5 は入力 $4/MTok・出力 $20/MTok。無料で回した証拠はない。
- 「3Dはドリフトしない」は形状についてのみ。ライティング・フレーミング・アニメーションでキャラクターの印象は変わる（返信で同旨の指摘があり、著者も同意している）。
- 記事本文（https://x.com/i/article/2109318233866006528）はログイン必須。HTTP 200 だがログイン画面へリダイレクトされ、本文・コード・プロンプトは未確認。記事の中身は推測しない。

## 出典

- 投稿: @Y0urDumble「You paid a sh*t ton of money per generation for your AI influencer...」2026-10-22 20:58 UTC — https://x.com/Y0urDumble/status/2113374545302200732
- 記事（ログイン必須・本文未取得）: https://x.com/i/article/2109318233866006528
- Blender 5.2 Manual: Command Line Arguments / Rendering From The Command Line / EEVEE — https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html , https://docs.blender.org/manual/en/latest/advanced/command_line/render.html , https://docs.blender.org/manual/en/latest/render/eevee/index.html
- Blender ダウンロード（5.2.3 LTS, 2026-10-22 リリース）: https://www.blender.org/download/
- Anthropic 料金（Free/Pro/Max と Claude Code の可否）: https://www.anthropic.com/pricing
- Claude モデル料金（Opus 5.5 の $4/$20 per MTok）: https://platform.claude.com/docs/en/about-claude/pricing
- 配布物の実体確認: https://github.com/arjun988/blender-skills

## 変更履歴

- 2026-11-09: 初回登録
