---
name: "iPhone『削除済み写真173,521件』主張の検証（PhotoData/Thumbnails）"
genre: "article"
url: "https://x.com/Bober_smart/status/2114352296913961208"
published: "2026-10-25"
author: "Bober_smart"
flags: ["unverified", "low-quality"]
risk_notes: "投稿単体では裏取り不能。同一本文内で183,000超と173,521が矛盾し、ほぼ同文の投稿が他アカウントから145,763/147,863/152,000件など異なる数字で出回る（AI-generated engagement baitとのコミュニティノートあり）。PhotoData/Thumbnailsの存在とサムネイル残存は文献で確認できるが、原寸オリジナル4年分という記述と『Spotlight索引』という説明は不正確。『19アプリが自由に読めた』はAppleのサンドボックス仕様および返信者の検証画像（permission denied）と矛盾。引用X記事はログイン壁、添付動画はフレームの文字が判読不能で、手順・プロンプト・実測値はいずれも未確認。"
type: "article"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/Bober_smart/status/2114352296913961208"]
fetched_at: "2026-11-09T16:37:00Z"
---

# iPhoneの『削除済み写真173,521件』は本当か — PhotoData/Thumbnails主張をApple資料で検証

## テーマ

- iPhoneで『完全に削除した』写真・動画が4年分・17万件超残っていたというX投稿（2026-10-25、約10.7万表示）を、Appleの一次資料とフォレンジック文献で分解する。
- 論点は3つ。(1) 削除済みメディアのサムネイルが端末やバックアップに残るのか、(2) 端末上の第三者のアプリがそれを読めるのか、(3) 『Claude Codeで173,521件見つけた』という数値を実測記録として扱えるのか。
- 結論としては、PhotoData/Thumbnailsというパスと『削除後もサムネイルが残り得る』という現象には実体がある一方、件数・『19アプリが自由に読めた』・『Spotlight索引』という説明は支持できない。

## 著者の主張

- MacBookにバックアップし、前回投稿で紹介したClaude Codeの脆弱性スキャンを実行したところ、頼んでいないPhotoData/Thumbnailsが検出され、183,000 items超（本文後半では173,521ファイル）が入っていた。
- 2021〜2024年の写真・動画・スクリーンショットが、撮影直後に消したものやRecently Deletedを手動で空にしたものも含めて残っており、一部は原寸だった、と主張。
- iOSは削除時にギャラリーとゴミ箱から消すだけで、Spotlight検索用の圧縮コピーを保持する。Appleは1ヶ月でも1年でも消さないので『完全削除』は嘘だ、と主張。
- ファイルシステムへのアクセス権を持つアプリが19個あり、天気・QRコードスキャナ・PDFリーダー・2021年に入れた懐中電灯アプリなどが削除済みデータを自由に読めた。5個に減らした、と主張。
- 根拠として、レシピ写真・買い物リスト・バスの時刻表・値札・ミームなど『消したはずの具体例』を列挙し、引用元としてログイン必須のX記事を貼っている。

## 裏取り・注意点

- 【数値の自己矛盾】同じ本文中で『over 183,000 items』と『A total of 173,521 files』が併記され、10,000件近く食い違う。どちらが実測値かは示されていない。
- 【コピペの痕跡】ほぼ同一の文章が複数アカウントから、145,763件・147,863件・152,000件など違う数字で投稿されている。ある投稿には『AI-generated engagement bait text with various random claims of deleted photos or videos on a daily basis』というコミュニティノートが付いている。単一の検証記録ではなく、テンプレートの使い回しと見るのが自然。
- 【パスは実在】PhotoData/ThumbnailsはiOSの写真ライブラリ配下に実在し、バックアップではCameraRollDomainのMedia/PhotoDataに対応する。iTunes/Finderバックアップにithmb形式のサムネイルが含まれることはフォレンジック文献が報告している。
- 【バックアップでの扱い】バックアップのdomain定義では、Thumbnailsは『NotToBackupToService』（iCloudバックアップには含めない扱い）に分類されている。ローカルバックアップでの収録状況はiOSの版によって変わり得るため、『バックアップに必ず4年分入っている』とは言えない。
- 【残存はあり得るが『絶対に消さない』は未確認】Athena Forensicsは『元画像が削除されてもThumbnailsは残る』『削除済みサムネイルを回収できることがある』と記載する。一方、削除後にサムネイルも消えたという検証報告もあり、期間や件数を含めてAppleが保証しているわけではない。
- 【Files and Foldersの誤解】『Files and Folders』はiOSのプライバシー設定に実在する区分だが、生の/var/mobile/Mediaを読む権限ではなく、サンドボックス仕様上も『19アプリが自由に読めた』は説明できない。バックアップをMacに置いた時点でMac上のツールが読めることと、iPhone上の他アプリが読めることは別問題。
- 【Files and Foldersの誤解】『Files and Folders』はiOSのプライバシー設定に実在する区分だが、生の/var/mobile/Mediaを読む権限ではない。19アプリが『自由に読めた』という因果は、Appleのサンドボックス仕様と両立しない。バックアップをMacに置いた時点でMac上のツールが読めることと、iPhone上の他アプリが読めることは別問題。
- 【引用元と動画は未確認】引用X記事はログイン画面へリダイレクトされ、手順・プロンプト・生の出力は取得できなかった。添付動画（22.3秒）は7フレームを抽出したが、端末画面の文字が読めず件数・パス・日付を確認できない。スレッドのもう1枚（LiliH）は、サンドボックス制限とサムネイルの性質を説明する文章のスクリーンショットだったが、一次資料ではない。
- 【年号の不整合】2026年10月の投稿なのに収録年が2021〜2024年で、直近2年分がない。『継続的に保存されていた』という説明とは合わない。
- 【実務的な持ち帰り】端末上の削除は『見えなくする』処理で、サムネイルやバックアップが残り得る。機密写真はバックアップ側も削除し、売却・譲渡前は『すべてのコンテンツと設定を消去』で暗号鍵を破棄する（Appleは鍵の消去でファイルが暗号学的に読めなくなると説明）。設定 > プライバシーとセキュリティ で写真・Files and Foldersの許可を見直すのは妥当だが、この投稿の『19アプリが全部読めた』という説明をそのまま信じる根拠にはならない。

## 出典

- Bober_smart, X投稿（2026-10-25）: https://x.com/Bober_smart/status/2114352296913961208
- 引用元X記事（ログイン必須・本文未取得）: https://x.com/i/article/2078778232250183680
- Apple Platform Security『Security of runtime process in iOS, iPadOS, and visionOS』: https://support.apple.com/guide/security/security-of-runtime-process-sec15bfe098e/web
- Apple Support『Delete photos on your iPhone or iPad』: https://support.apple.com/en-us/104967
- Apple Support『About privacy and Location Services in iOS, iPadOS, and visionOS』: https://support.apple.com/en-us/102515
- Athena Forensics『iPhone Photodata Thumbnails』(2020-02-01): https://athenaforensics.co.uk/iphone-photodata-thumbnails/
- leminlimez『A deep dive into the iOS backup/restore system』(CameraRollDomainのパス対応): https://gist.github.com/leminlimez/c602c067349140fe979410ef69d39c28
- NeuN0madの検証画像: https://pbs.twimg.com/media/HVjrKj5WwAAPnvc.jpg
- coolerwaveの同文面投稿とコミュニティノート: https://x.com/coolerwave/status/2114752518005662114
- Apple Platform Security『Data Protection in Apple devices』: https://support.apple.com/guide/security/data-protection-sece8608431d/web

## 変更履歴

- 2026-11-09: 初回登録
