---
name: "Coding Agents Copy Your Secrets to a Hidden File. Thousands Are on GitHub"
genre: "article"
url: "https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again"
author: "Apiiro"
published: "2026-11-05"
flags: ["unverified"]
risk_notes: "集計と挙動の再現はApiiroによる報告。調査対象の認証情報の有効性や、Claude Codeのバージョンごとの挙動は独立に検証していない。"
type: "article"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/Nursing_DX/status/2119274934631555421"]
fetched_at: "2026-11-10T06:17:57.030Z"
---

# Claude Codeの承認ルールに残る認証情報とGitでの漏えい対策

## テーマ

- Claude Codeのコマンド承認ルールに認証情報が残り、プロジェクトのローカル設定ファイルがGitで公開される経路を扱う。

## 著者の主張

- Apiiroは、公開GitHub上で調べたローカル設定ファイル104,185件のうち、1,122ファイルに認証情報が含まれていたと報告した。
- Apiiroは、ローカル設定ファイルをGitの追跡対象から外してリポジトリの.gitignoreに追加し、公開済みの認証情報をローテーションするよう勧めている。

## 裏取り・注意点

- Claude Code公式ドキュメントは、継続承認がプロジェクトのローカル設定に保存され、Claude CodeがGitリポジトリ内で初めて設定ファイルを書き込む際には、既存の除外設定がなければグローバル除外に追加すると説明している。手動作成時は.gitignoreへの追加を案内している。
- 1,122は認証情報を含むファイル数。Apiiroの集計は同社の判定基準に基づき、調査では認証情報を使った有効性のテストを行っていない。

## 出典

- https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again
- https://code.claude.com/docs/en/settings?_rsc=vr6dg

## 変更履歴

- 2026-11-10: 初回登録
