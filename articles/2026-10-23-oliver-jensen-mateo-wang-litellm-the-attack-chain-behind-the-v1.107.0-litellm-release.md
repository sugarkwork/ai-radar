---
name: "The attack chain behind the v1.107.0 LiteLLM release"
genre: "article"
url: "https://docs.litellm.ai/blog/security-incident-oct-21-2026-attack-chain"
author: "Oliver Jensen、Mateo Wang（LiteLLM）"
published: "2026-10-23"
flags: []
risk_notes: "配布物の比較や挙動の再現は行っていない。侵入経路はLiteLLMの調査報告に、Python起動時の挙動はMicrosoftの配布物解析と端末観測に基づく。個別環境での実行や認証情報の流出は別途確認が必要。"
type: "article"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/AiAircle34052/status/2115658642632716373"]
fetched_at: "2026-11-10T05:45:12Z"
---

# LiteLLM 1.107.0の配布物改ざんに関する公式調査報告

## テーマ

- LLMゲートウェイLiteLLMのリリース工程が侵害され、公式GitHubのソースタグと、PyPIおよびコンテナレジストリから実際に配布された成果物の内容が異なった事例。

## 著者の主張

- LiteLLMは、公開リポジトリの履歴に残り失効されていなかった内部サービスの管理キーを侵入の起点と特定した。改変されたリリース工程から、悪性コードを含む1.107.0がPyPIとコンテナレジストリに公開されたと報告している。

## 裏取り・注意点

- 添付図の版番号と配布経路は公式報告と一致する。公式の初報は、同版のGitHubソースタグに悪性ファイルが含まれていなかったと記載している。侵入経路については、初報の一部を訂正した10月23日の調査報告を優先する。
- Microsoftは影響を受けたwheelを解析し、LiteLLMをインポートしなくても、該当パッケージを導入した環境でPythonを起動するだけで悪性コードが動き得ると報告している。影響調査では、疑わしい環境でPythonやpipを起動せず、ロックファイル、キャッシュ、イメージのダイジェストなどから導入済みの成果物を照合する。

## 出典

- [LiteLLMの訂正後の公式調査報告](https://docs.litellm.ai/blog/security-incident-oct-21-2026-attack-chain)
- [LiteLLMの初報と影響範囲](https://docs.litellm.ai/blog/security-incident-oct-21-2026)
- [Microsoft Security Researchによる配布物解析と端末観測](https://www.microsoft.com/en-us/security/blog/2026/10/23/inside-the-litellm-1-107-0-supply-chain-compromise-credential-theft-through-python-startup-hooks/)

## 変更履歴

- 2026-11-10: 初回登録
