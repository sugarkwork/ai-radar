---
name: "ScaleDown"
genre: "link-service"
url: "https://scaledown.ai/"
author: "ScaleDown AI"
pricing: "paid"
pricing_detail: "従量課金 $0.05/100万入力トークン（画像入力 $0.15/100万）、出力は無料。新規アカウントは100万トークン無料。Enterprise は専用インスタンス／自社ハードへのライセンス（2026-11 時点）"
signup_required: true
type: "link"
added: "2026-11-04"
source_post: "https://x.com/RealMarvelX/status/2117497881108021605"
sources: []
flags: []
risk_notes: "性能・価格優位の数値（467x cheaper 等）はベンダー自身の掲載で、独立した比較検証は確認していない"
---

# ScaleDown

## 目的

分類・抽出・要約・圧縮という単機能に絞った小型モデル（SLM）を API で提供するサービス。フロンティアモデルに頼らず、決まった処理を大量に安く流す用途を狙う。

## 何ができるか

- 4モデル構成: **Classify**（ラベル分類。ラベル体系を自然文で定義）、**Extract**（自然文で指定した項目を JSON で抽出）、**Summarize**（長さ指定の要約）、**Compress**（クエリに関係する事実を残す意味圧縮）。
- 入力はテキスト・画像・スキャン文書で、最大100万トークンの文脈を1コールで扱う（分割・切り捨てなし）。
- Compress は「プロンプト・会話履歴の短縮」向けで、圧縮量に上限がないとしている。エージェントのトークン消費を下げる用途。
- Claude Code のトークン消費を減らす `diet_code` を別途提供（`scaledown.ai/dietcode`）。
- OpenRouter のプロバイダとしても提供されている。
- セキュリティ面は SOC 2 Type 1 / HIPAA / GDPR / ISO 27001 準拠、ゼロデータ保持、学習に使わない、と掲載。Enterprise は専用インスタンスとセルフホスト（ライセンス）に対応。

## 料金

- 従量課金で一律 $0.05/100万入力トークン（画像入力は $0.15/100万）。**出力トークンは無料**。プラン分けなし。
- 新規アカウントに100万トークン分の無料枠。
- Enterprise: 専用インスタンス、自社ハードウェアへのライセンス、SLA 付きサポートを個別見積。
- 「467x cheaper / 200x faster / SOTA accuracy」はトップページの掲載値で、比較条件は明示されていない（独立検証は未確認）。

## 登録の要否

- 必要。`scaledown.ai/auth` でアカウント作成→API キー発行。

## 変更履歴

- 2026-11-04: 初回登録（料金表はトップページの Pricing 節で確認）
