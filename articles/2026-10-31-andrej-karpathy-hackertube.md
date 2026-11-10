---
name: "HackerTube"
genre: "coding-agent"
url: "https://karpathy.bearblog.dev/hacker-tube/"
author: "Andrej Karpathy"
published: "2026-10-31"
flags: ["unverified"]
risk_notes: "所要時間とデプロイ時のセキュリティ対策は著者の報告に基づく。推薦の選別精度、Mediumと他の設定の比較、実際の費用、エクスポートデータの再利用条件は未確認。"
type: "article"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/eng_khairallah1/status/2116930007134249237"]
fetched_at: "2026-11-10T06:30:15+00:00"
---

# HackerTube — Claude CodeでHacker Newsの動画推薦を集約した開発事例

## テーマ

- Hacker Newsのコメントから推薦されたYouTube動画を抽出し、閲覧サイトにまとめた事例。著者は別バージョンを作るためにエージェントに渡せるデータのエクスポートも案内している。

## 著者の主張

- Mac版Claude Code DesktopでOpus 5.5をMedium effortに設定。コメントの選別にはClaude CodeのWorkflowでSonnetを使い、最終的に6,454本の動画を抽出したと述べている。
- 著者はYouTubeの動画メタデータ取得用APIキーの発行、VPSの起動、ドメイン購入を担当し、実装とデプロイをClaudeに任せたと記している。

## 裏取り・注意点

- 添付画像にある設定と作業分担は本人記事の追記と一致する。約2時間という所要時間はこの事例の自己報告で、Mediumの比較評価や公開環境の安全性は独立に検証されていない。

## 出典

- [Andrej Karpathy本人の記事『HackerTube』](https://karpathy.bearblog.dev/hacker-tube/) 

## 変更履歴

- 2026-11-10: 初回登録
