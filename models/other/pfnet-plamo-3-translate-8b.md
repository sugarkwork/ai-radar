---
type: "model"
name: "PLaMo 3 Translate 8B"
genre: "other"
url: "https://huggingface.co/pfnet/plamo-3-translate-8b"
author: "Preferred Networks"
pricing: "free"
pricing_detail: "非商用（個人・学習・趣味・学術）は無償・登録不要。商用は直近事業年度の売上高が10億円以下なら申請フォームで登録すれば無償、10億円超は個別ライセンス契約が必要。"
signup_required: false
model: "pfnet/plamo-3-translate-8b"
license: "plamo-community-license"
downloads: 89
likes: 12
format: "safetensors"
size: "17.06 GB (BF16, 4 shards)"
base_model: ["pfnet/plamo-3-nict-8b-base"]
created: "2026-10-27"
updated: "2026-11-04"
added: "2026-11-06"
first_seen: "2026-11-06"
sources: ["https://x.com/naka_1717/status/2118548329286242602", "https://x.com/gosrum/status/2119048949831188578?a=KptX01pXwqs_GDFSUaI&s=46", "https://x.com/gosrum/status/2119048949831188578", "https://x.com/gosrum/status/2119048311328116860", "https://huggingface.co/api/models?search=plamo-3-translate", "https://x.com/gosrum/status/2118173790840729980"]
flags: ["unverified"]
risk_notes: "weights は PLaMo Community License（OSI 認証のオープンソースライセンスではない）。商用利用は売上高10億円で条件が分岐するため、業務利用前に条件確認が必要。custom_code モデルのため trust_remote_code=True でリポジトリ内 modeling_plamo.py を実行する点に注意（コード自体のライセンスは未確認）。base_model はカード表記が「PLaMo 3 NICT」で正確な repo id は明記されておらず、同サイズの pfnet/plamo-3-nict-8b-base をサイズから対応付けた推測。"
fetched_at: "2026-11-06T08:15:50Z"
license_name: "plamo-community-license"
source_post: "https://x.com/gosrum/status/2119048949831188578"
amplifiers: []
---

# PLaMo 3 Translate 8B — 53言語対応の翻訳特化LLM（8.5B, BF16/量子化版あり）

## 出来ること

- 日本語↔英語を含む53言語（カード記載）間の翻訳をローカルで実行する（pipeline_tag: translation）
- 文脈（context）と用語集（glossary）を渡して、訳語や曖昧語の解釈を固定する
- 日本語出力の文体を常体（plain）／敬体（polite）から選ぶ
- 直前までの訳文ペアを履歴として渡し、段落ごとの翻訳で用語・文体を引き継ぐ
- 入力+出力で最大32,768トークンを1リクエストで扱う（長文は分割推奨）
- vLLM の OpenAI 互換 Chat Completions API 経由で、エージェントやアプリから HTTP で呼ぶ

## 目的・背景

- PFN（Preferred Networks）が2026-11-05に重みを公開した翻訳特化LLM。0.8B / 2B / 8B / 31B の4サイズ展開で、本項目はその8B BF16版。
- ベースは PFN と NICT の共同研究による事前学習モデル PLaMo 3 NICT。翻訳特化データを数百億トークン規模で追加学習している（カード記載: tens of billions of tokens）。
- 公式ブログは「最小の0.8Bモデルでも、日英および日本語↔多言語で30倍以上大きな既存の翻訳特化LLMを上回る」と主張しており、この主張はブログ本文で確認できる。数値の独立再現はしていない。
- 8B BF16 のカード掲載スコア: PFTB(En↔Ja) 0.6119 / SaaS(En→Ja) 0.5750 / WMT24++ COMET-22(En→Ja) 0.8805 / FLORES+ chrF++(Ja↔多言語) 37.45 / FLORES+ chrF++(En↔多言語) 56.22。
- 翻訳専用のプロンプト形式 PFML3 を採用し、汎用チャットモデルとしての対話用途は想定されていない。

## 収録ファイル

- model-00001〜00004-of-00004.safetensors（合計 17,063,540,224 bytes = 17.06 GB、BF16）
- model.safetensors.index.json / config.json / generation_config.json
- modeling_plamo.py（Plamo3ForCausalLM のカスタム実装）/ tokenization_plamo.py / tokenizer.jsonl / tokenizer_config.json / special_tokens_map.json
- chat_template.jinja（source_lang / target_lang / context / glossary / form を PFML3 に変換するテンプレート）
- README.md（英語）/ README_ja.md（日本語）/ LICENSE/en・LICENSE/ja（PLaMo Community License 全文）/ figures/benchmark_en.png・benchmark_ja.png

## 実行条件

- BF16 の重みが 17.06 GB あるため、GPU メモリはモデル分＋KV キャッシュで 20GB 超を見込む（量子化版は別リポジトリ）
- Transformers 実行は torch / transformers / accelerate / numba、custom_code のため trust_remote_code=True が必須
- vLLM 実行は vllm / openai / numba、起動時も --trust-remote-code が必要
- 軽量環境向けに同一orgから FP8 / W4A16 / W4AFP8 / NVFP4 / GGUF / MLX-4bit の変換版が公開されている（例: pfnet/plamo-3-translate-8b-GGUF、Q4_K_M で 5.28 GB）
- ライセンス: 非商用は登録不要で無償。商用は売上高10億円以下なら登録フォーム、超過は個別契約

## 使い方

```bash
pip install -U huggingface_hub
hf download pfnet/plamo-3-translate-8b --local-dir plamo-3-translate-8b
cd plamo-3-translate-8b
pip install -U torch transformers accelerate numba
```

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(".", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    ".", trust_remote_code=True, dtype="bfloat16", device_map="auto",
)

inputs = tokenizer.apply_chat_template(
    [{"role": "user", "content": "会議は来週の月曜日に変更されました。"}],
    target_lang="en",
    add_generation_prompt=True,
    return_dict=True, return_tensors="pt",
).to(model.device)

output = model.generate(**inputs, do_sample=False, max_new_tokens=512)
print(tokenizer.decode(output[0, inputs["input_ids"].shape[1]:], skip_special_tokens=True))
```

- 用語集と文脈を固定する場合（カードの引数はすべて apply_chat_template に渡す。system メッセージは非対応）:
```python
inputs = tokenizer.apply_chat_template(
    [{"role": "user", "content": "プロジェクトの管理画面を開いてください。"}],
    source_lang="ja", target_lang="en",
    context="プロジェクト管理ツールのヘルプページです。",
    glossary=[{"source": "管理画面", "target": "dashboard"}],
    form=None,
    add_generation_prompt=True,
    return_dict=True, return_tensors="pt",
).to(model.device)
```
- エージェントから呼ぶ場合は vLLM で OpenAI 互換サーバを立てる:
```bash
pip install -U vllm openai numba
vllm serve . --trust-remote-code \
  --served-model-name plamo-3-translate \
  --max-model-len 16384 --max-num-seqs 4
```
```bash
curl http://localhost:8000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "plamo-3-translate",
    "messages": [{"role": "user", "content": "こんにちは。"}],
    "chat_template_kwargs": {"source_lang": "ja", "target_lang": "en"},
    "temperature": 0,
    "max_tokens": 512,
    "stop": ["<|plamo:tag|>", "<|plamo:bos|>"]
  }'
```
- メモ: 生成テキストの末尾に <|plamo:tag|> や <|plamo:bos|> が残る場合は stop 指定で除去する。max_tokens は訳文の長さに合わせて調整し、入力（履歴・文脈・用語集含む）+出力が 32,768 トークン以内に収める。

## 変更履歴

- 2026-11-06: 初回登録

## 追加出典・確認範囲（2026-11-09）

PLaMo3 Translate8Bを使ったWebGPU拡張の事例に関する追加出典。

モデル本体と個人制作のChrome拡張は別物。拡張は配布未確認。

別サイズ・量子化の利用体験を8B本体の公式対応や実測としない。

対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:31:08.831716+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

### 今回取得した公式メタ情報

既存フロントマターの過去値は維持し、今回の取得値を下に併記する。どちらも実行・性能の追試ではない。

| 項目 | 値 |
|---|---|
| model | pfnet/plamo-3-translate-8b |
| url | https://huggingface.co/pfnet/plamo-3-translate-8b |
| license | other |
| base_model | [] |
| downloads | 569 |
| likes | 18 |
| format | safetensors |
| size | 配布中の重みファイル 4本・合計17,063,540,224 bytes（複数形式・量子化・派生を含む。必要メモリではない） |
| created | 2026-10-27 |
| updated | 2026-11-08 |
| fetched_at | 2026-11-09T00:31:08.831716+00:00 |
| pricing | free |
| pricing_detail | 重みのダウンロードに利用料金の表示なし。ライセンス・用途・地域・商用許諾と実行費用は別途確認。 |
| signup_required | False |
| license_name | plamo-community-license |


- @gosrum: https://x.com/gosrum/status/2119048949831188578
- 対象資料: https://huggingface.co/pfnet/plamo-3-translate-8b
- 参照: https://x.com/gosrum/status/2119048311328116860
- 参照: https://x.com/gosrum/status/2118173790840729980

- 2026-11-09: 関連出典と確認範囲を追記。既存の記述・過去の数値・原文プロンプトは維持。今回の実行確認なし。
