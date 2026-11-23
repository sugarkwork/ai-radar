---
name: "Harness adapters: Safe RL for efficient agentic development"
genre: "article"
url: "https://huggingface.co/blog/harness-hub/harness-adapters"
published: "2026-11-06"
flags: ["unverified"]
risk_notes: "ツール呼び出しの削減や評価精度、安全性に関する効果は記事の著者らによる報告で、独立した実測としては確認していません。記事ではheld-out評価やsmoke runなどの条件が説明されています。"
type: "article"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/ai_hakase_/status/2119400802389205299"]
fetched_at: "2026-11-20T04:14:24.701741+00:00"
---

# Harness adapters: Safe RL for efficient agentic development

## テーマ

- エージェント・ハーネスごとに小型のLoRAアダプターを用意し、ベースモデルを共有しながら強化学習で調整する手法と、その学習時にツール呼び出しを検査する仕組みを解説する記事。

## 著者の主張

- 著者らは、pi、opencode、hermesの各ハーネス向けにアダプターを学習し、held-out評価ではベースモデルより少ないツール呼び出しで精度を維持または改善したと報告しています。また、safeagentsがツール呼び出しをルールベースで検査し、報酬の不正操作などを試みる呼び出しを遮断すると説明しています。これらは記事内で著者らが述べている結果です。

## 裏取り・注意点

- 記事には学習条件、環境の作成・検証手順、評価条件、safeagentsの検査段階と遮断例が記載されています。報告された性能や安全上の効果は記事の著者らによるもので、ここでは独立に再現・測定していません。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 出典

- [Harness adapters: Safe RL for efficient agentic development](https://huggingface.co/blog/harness-hub/harness-adapters) — Hugging Face Blog。2026-11-06公開。

## 変更履歴

- 2026-11-23: 初回登録
