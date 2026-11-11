---
name: "Jetpack Compose for XR 1.0.0-beta02 リリースノート"
genre: "article"
url: "https://developer.android.com/jetpack/androidx/releases/xr-compose?hl=ja#1.0.0-beta02"
published: "2026-10-21"
flags: ["unverified"]
risk_notes: "このバージョンはandroidx.xr.scenecore:1.0.0-rc01に既知のメモリリークを含む依存関係があり、公式資料はSceneCore 1.0.0への明示的な上書きを回避策として示しています。XREAL AURAとの互換性や、投稿にあるエラーの原因はこのページから確認できません。"
type: "article"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/tokufxug/status/2118354543763501510"]
fetched_at: "2026-11-11T22:16:31Z"
---

# Jetpack Compose for XR 1.0.0-beta02 リリースノート

## テーマ

- Android XRの空間UIを宣言的に構築するJetpack Compose for XRの1.0.0-beta02リリース。

## 著者の主張

- 公式リリースノートは、composeおよびcompose-testingの1.0.0-beta02を公開したと記載しています。

## 裏取り・注意点

- 公式資料によると、この版はKotlin 2.2を対象とし、Google Mavenリポジトリの設定と依存関係の追加が必要です。API変更とバグ修正のほか、SceneCore 1.0.0-rc01に既知のメモリリークがあると記載されています。必要に応じてSceneCore 1.0.0を明示的に指定する回避策が案内されています。資料はXREAL AURAの対応状況や投稿にある依存解決エラーの原因を説明していません。

## 出典

- Google Android Developers「XR Compose」リリースノート。https://developer.android.com/jetpack/androidx/releases/xr-compose?hl=ja#1.0.0-beta02

## 変更履歴

- 2026-11-11: 初回登録
