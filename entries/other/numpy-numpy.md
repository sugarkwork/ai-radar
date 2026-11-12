---
name: "NumPy"
genre: "other"
url: "https://github.com/numpy/numpy"
repo: "numpy/numpy"
license: "unknown"
stars: 33343
language: "Python"
created: "2010-09-13"
updated: "2026-11-12"
forks: 13099
open_issues: 2249
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 187263
archived: false
flags: ["unverified"]
risk_notes: "ライセンスは取得済みメタデータでunknownのため確認できていない。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-12"
first_seen: "2026-11-12"
sources: ["https://x.com/kursormaxx/status/2118673610722144590"]
fetched_at: "2026-11-12T11:10:36.818769+00:00"
---

# NumPy

## 出来ること

- Pythonで科学計算を行うための基盤パッケージ。N次元配列オブジェクト、ブロードキャスト関数、C/C++・Fortranコードとの連携機能、線形代数・フーリエ変換・乱数機能を提供するとREADMEに記載されている。

## 目的・背景

- NumPyはPython向け科学計算の基盤パッケージとして紹介されている。

## 依存関係

- READMEではテストにpytestが必要とされている。NumPy C APIのテストにはMeson、NumPy Cython APIのテストにはCython、追加のプロパティベーステストにはHypothesisなどが任意で必要と記載されている。

## 実行条件

- READMEには、インストール後にテストを実行する例として `python -c "import numpy, sys; sys.exit(numpy.test() is False)"` が記載されている。

## 最短手順

- READMEのテスト例は、インストール後に `python -c "import numpy, sys; sys.exit(numpy.test() is False)"` を実行する手順。

## 変更履歴

- 2026-11-12: 初回登録
