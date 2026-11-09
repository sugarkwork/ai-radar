---
name: "PDF skill (anthropics/skills)"
genre: "other"
url: "https://github.com/anthropics/skills/tree/main/skills/pdf"
pricing: "free"
pricing_detail: "GitHubで無償公開。skills/pdf/LICENSE.txt は Apache License 2.0（11,357 bytes）。親リポジトリ anthropics/skills にはリポジトリレベルのLICENSEがないため、許諾範囲は各スキル配下のLICENSEに従う。"
signup_required: false
author: "Anthropic"
license: "Apache-2.0"
source_post: "https://x.com/Y0urDumble/status/2114428470168334365"
sources: ["https://github.com/anthropics/skills/tree/main/skills/pdf", "https://raw.githubusercontent.com/anthropics/skills/main/skills/pdf/LICENSE.txt", "https://raw.githubusercontent.com/anthropics/skills/main/skills/pdf/SKILL.md", "https://x.com/Y0urDumble/status/2114428470168334365"]
flags: []
risk_notes: "親リポジトリ anthropics/skills にはリポジトリレベルのLICENSEがなく（GitHub APIのlicenseは404）、許諾は skills/pdf/LICENSE.txt（Apache-2.0）単位で判断する必要がある。OCR・フォーム入力は追加の依存（pytesseract/poppler、pdf-lib等）と外部ツールに依存する。投稿の『契約書PDFを自動生成して閉める』工程のうち、このSkillが担うのはPDFの読み書き・フォーム・生成のみで、提案内容や契約条件の作成は行わない。投稿の『48 leads / 12 pitches / 1 signed』『$3,000–6,000』『0 employees』などの営業実績は著者の主張で、第三者検証がなく未検証。"
fetched_at: "2026-11-09T20:14:56Z"
type: "link"
added: "2026-11-09"
first_seen: "2026-11-09"
---

# PDF skill — PDFの読み書き・フォーム・生成を扱うAgent Skill

## 目的

- PDFのテキスト・表抽出、結合・分割、回転、透かし、新規作成、フォーム入力、暗号化・復号、画像抽出、スキャンPDFのOCRを扱うための手順とコード集。
- 投稿では『提案書・契約書のPDFを作る』工程に置かれているが、Skillが担うのはPDF操作であり、文面や契約条件の作成は別の工程。

## 何ができるか

- SKILL.md（8,058 bytes）に加えて forms.md（フォーム入力）、reference.md（JSライブラリ・上級編）、scripts/ を同梱する。
- Pythonは pypdf（結合・分割・回転・暗号化・メタデータ）、pdfplumber（テキスト・表抽出）、reportlab（生成）を中心に、必要に応じて pytesseract / pdf2image / pandas を使う。
- コマンドラインツールとして pdftotext / pdfimages（poppler-utils）、qpdf（結合・分割・回転・復号）、pdftk の例も収録する。請求書や表紙のような生成物をコードで組み立てられる。

## 料金

- 無料。skills/pdf/LICENSE.txt は Apache License 2.0。
- 利用するPythonライブラリやOCRツールはそれぞれのライセンス・従量課金に従う。

## 登録の要否

- 閲覧・取得に登録は不要。スキルフォルダをエージェントのskillsディレクトリに置く。
- OCRやフォーム入力を使う場合は、Tesseract・poppler等の外部ツールとPythonパッケージの導入が別途必要。

## 変更履歴

- 2026-11-09: 初回登録
