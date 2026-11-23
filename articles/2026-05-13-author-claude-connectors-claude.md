---
name: "Claude Connectors：Claudeを外部アプリに接続する方法"
genre: "article"
url: "https://ruben.substack.com/p/claude-connectors"
published: "2026-05-13"
flags: ["unverified"]
risk_notes: "記事中の「200以上」というコネクター数、個別アプリの利用例や効果、独自コネクターの構築所要時間は記事の記述であり、独立確認していません。利用できるコネクターやプラン条件は変わる可能性があります。Anthropicの案内では、リモートコネクターは有料プラン向けで、カスタムコネクターはAnthropic未検証のサービスにも接続できるため、接続先と権限の確認が必要です。"
type: "article"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/okapi_fukugyo/status/2119299912882123032"]
fetched_at: "2026-11-18T21:12:02.365005+00:00"
---

# Claude Connectors：Claudeを外部アプリに接続する方法

## テーマ

- Claudeのコネクターを使い、Gmail、Slack、Notionなどの外部アプリの情報をClaudeから参照する方法と、独自のリモートMCPコネクターを追加する手順を紹介する記事です。

## 著者の主張

- 著者は、チャット欄の「+」からコネクターを追加し、会話ごとに有効化して使う方法を説明しています。Gmail、Slack、Granolaなどを使った例を挙げ、用途のないコネクターは無効にすること、書き込み権限を与える前に読み取り用途から試すことを勧めています。独自コネクターについては、リモートMCPサーバーを用意してClaudeの設定にURLを登録する手順を示しています。これらの利用例や効果は著者の説明です。

## 裏取り・注意点

- Anthropic公式ヘルプは、設定の「Connectors」からコネクターを追加し、認証・権限を設定して使う手順を案内しています。また、カスタムコネクターでは未検証のサービスに接続でき、権限に応じてデータの読み取りや変更などが可能なため、信頼できる接続先を選び、要求された権限やツール操作を確認するよう注意しています。記事のコネクター数、個々のアプリでの動作例、効果、構築時間は独立確認していません。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 出典

- 記事本文・公開日：[Claude Connectors — Ruben Hassid](https://ruben.substack.com/p/claude-connectors)

公式資料：[Getting Started with Custom Connectors Using Remote MCP — Anthropic Help Center](https://support.anthropic.com/en/articles/11175166-about-custom-integrations-using-remote-mcp)

公式資料：[Pre-built Web Connectors Using Remote MCP — Anthropic Help Center](https://support.anthropic.com/en/articles/11176164-pre-built-connectors-using-remote-mcp)

## 変更履歴

- 2026-11-23: 初回登録
