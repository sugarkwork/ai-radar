---
name: "「どのAIに何を入れたっけ？」をもう探さない。原本1つの自分のSkillsを、Grok Bot・dots・ChatGPT・Claudeから自在に呼び出す方法"
genre: "article"
url: "https://x.com/i/article/2119227796903940096"
published: "2026-11-08"
flags: ["unverified"]
risk_notes: "Cloudflare無料枠の料金・上限や、各AIとの接続条件は記事公開時の著者の説明。現在の適用条件は未確認。複数AIでの動作・負荷測定は著者による報告であり、独立検証ではない。"
type: "article"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/tetumemo/status/2119324068478582948"]
fetched_at: "2026-11-19T05:14:03.298350+00:00"
---

# 「どのAIに何を入れたっけ？」をもう探さない。原本1つの自分のSkillsを、Grok Bot・dots・ChatGPT・Claudeから自在に呼び出す方法

## テーマ

- GitHubに保存したSkillsを原本として管理し、Cloudflare上のMCPサーバーからChatGPT、Claude、dots、Grok Botなど複数のAIに提供する方法。記事には構築キット、Googleドライブを使う簡易案、接続トラブルの記録も含まれる。

## 著者の主張

- 著者は、SkillsをGitHubに集約し、読み取り専用のMCP受付をCloudflareに置くことで、各AIへコピーし直さずに同じSkillsを呼び出せると説明している。記事では、dots・ChatGPT・Claudeで同じ依頼を試したことや、Googleドライブ経由とMCP経由での呼び出し時間・回数の比較も報告している。これらは著者自身の実践・測定報告。

## 裏取り・注意点

- 著者の公開記事では、MCP受付がSkillsの一覧・検索・本文・付属資料を読む用途に限られ、原本の書き換えやスクリプト実行はできない構成と説明されている。また、ChatGPTで本文が空になる問題を応答フィールド名の変更で修正した経緯や、Grok Botの登録時に生じた問題も記載されている。複数AIでの動作や測定結果は独立実測ではない。Cloudflareの無料枠の現行条件は別途確認が必要。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 出典

- 著者の公開記事（本文・公開日）：https://note.com/tetumemo/n/nc68796cef6c7
対象として指定されたX記事：https://x.com/i/article/2119227796903940096

## 変更履歴

- 2026-11-23: 初回登録
