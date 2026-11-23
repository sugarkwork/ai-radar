---
name: "antigravity-filter-bypass"
genre: "coding-agent"
url: "https://github.com/v1ktorrr0x/antigravity-filter-bypass"
repo: "v1ktorrr0x/antigravity-filter-bypass"
license: "unknown"
stars: 525
language: "Python"
created: "2026-11-05"
updated: "2026-11-06"
forks: 143
open_issues: 1
commits_30d: 5
commit_cadence: "weekly"
commits_90d: 5
size_kb: 20
archived: false
flags: ["unverified"]
risk_notes: "ライセンスはGitHub APIでunknown。中断検出の精度や継続の効果は独立確認されていない。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/mingzi206/status/2119348019447423476"]
fetched_at: "2026-11-19T13:11:54.307765+00:00"
---

# antigravity-filter-bypass

## 出来ること

- READMEによると、AntigravityのStopイベントを監視し、最新のモデルステップの最終非空行に中断の署名があれば、問題となった語句をより安全な表現に言い換えて続行する指示を注入する。通常のタスク完了時は終了する。

## 目的・背景

- 予期しない停止やフィルターによる中断の後も、エージェントにタスクを続行させる目的として説明されている。これは配布者の説明であり、実際の継続効果は未確認。

## 依存関係

- READMEに明記された依存関係は確認できない。

## 実行条件

- Antigravityのプラグインとして、Windowsでは `%USERPROFILE%\.gemini\config\plugins\antigravity-filter-bypass`、Mac/Linuxでは `~/.gemini/config/plugins/antigravity-filter-bypass` に配置する手順がREADMEに記載されている。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- README記載の方法では、Antigravityのチャットにリポジトリを指定したインストール指示を貼り付ける。または、READMEのOS別コマンドで所定のプラグインディレクトリへcloneする。

## 変更履歴

- 2026-11-23: 初回登録
