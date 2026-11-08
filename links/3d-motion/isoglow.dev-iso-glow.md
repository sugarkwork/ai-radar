---
name: "ISO-GLOW"
genre: "3d-motion"
url: "https://isoglow.dev/"
pricing: "free"
pricing_detail: "スキル本体は無料（MIT）。zip / tar.gz / .skill を直接ダウンロード。姉妹の Iso UI（500点パック）は別売り。"
signup_required: false
flags: ["unverified"]
risk_notes: "3D実装（three.js 0.160.0、OrbitControls、正射影のIso view、.glb取り込み、3D作例12点）は配布zip内のSKILL.mdとgallery-3d.html、および投稿動画のフレームで確認した。ただしClaude上で実際に図を生成する再現テストは未実施で、出力品質や.glbの仕上がりは未検証。バージョン番号・変更履歴は公開されておらず、「更新版」の版を特定できない。配布物は14ファイル約455KBで、サイトの「Six text files, about 300 KB」という説明とは一致しない（機能面への影響は不明）。公式GitHubリポジトリは無く、配布はisoglow.devのzip/tar.gz/.skillのみ。"
type: "link"
added: "2026-11-08"
first_seen: "2026-11-08"
sources: ["https://x.com/sumika45379/status/2112019659679740164"]
fetched_at: "2026-11-08T11:50:15Z"
---

# ISO-GLOW（3D対応）— 等角図を生成するClaudeスキル

## 目的

- テキストで指示した物体・デバイス・建物を、細線の等角投影（アイソメトリック）イラスト1枚のHTMLとして生成するClaudeスキル。点灯している部分だけが発光し、押せる部品は実際に反応する。3Dを指定すると同じ見た目をthree.jsで構築し、視点を回せるようにする。

## 何ができるか

- 2D: 説明文から単一HTMLの等角図を生成。ライト/ダーク、アクセントカラーの選択、Ember/Cityなどのパレット、複数図を並べるギャラリーに対応。

3D: ドラッグでオービット、スクロールでズーム。「Iso view」で正射影の真の等角表示にワンクリックでスナップし、再押下で同じ角度の透視表示に戻る。Revolve（自動回転）、図ごとのボタンパネル、読み取り表示、効果音ヘルパーも同梱。

.glb/.gltf: 手持ちの3Dモデルをbase64でHTMLに埋め込み、サイズを正規化したうえで、ダークなボディ・シルエット・折り目線のハーフラインに描き直す。

3D作例12点: タイプライター、ドラムマシン、カセットデッキ、キッチンタイマー、自販機、コンピュータ、ランプ、ロジックボード、サーバーラック、システムスタック、ターンテーブル、インスタントカメラ。

導入手順（Claude Code）: `mkdir -p ~/.claude/skills && curl -fsSL https://iso-glow.vercel.app/iso-glow.tar.gz | tar -xz -C ~/.claude/skills` を実行し、Claude Codeを再起動して `/iso-glow` と入力する。Claude.aiでは iso-glow.skill をスキル設定にアップロード、Windows/macOS/Linuxの手動配置は iso-glow.zip を使う。

AIからの呼び方: Claudeのスキルとして `/iso-glow` または自然文で起動。API/MCP/CLIは提供されていない。3Dページの生成にはPython 3（同梱の組み立て用ワンライナー）とブラウザがあればよく、Nodeは任意。

## 料金

- 無料。MITライセンスで、クレジット（ISO-GLOW / isoglow.dev、および土台のiso-figure by Tolga Cohce）を保持すれば改変・再配布・商用利用が可能。サイトに料金ページや決済導線は無く、zip / tar.gz / .skill を直接ダウンロードする。姉妹の Iso UI（500点のイラストパック）は別売りだが、本スキルの利用に購入は不要。

## 登録の要否

- 不要。isoglow.dev のダウンロードにアカウント登録は無い。ただしClaude.aiでスキルとして使う場合はスキル機能を含むプランが必要（サイト記載: 「Skills need a plan that includes them」）。Claude Codeはローカルの ~/.claude/skills に展開するだけでよい。

## 変更履歴

- 2026-11-08: 初回登録
