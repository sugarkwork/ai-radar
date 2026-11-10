---
name: "librosa"
genre: "other"
repo: "librosa/librosa"
url: "https://github.com/librosa/librosa"
last_release: "1.0.0"
flags: ["unverified"]
risk_notes: "GitHub の latest は 1.0.0 に転送されたが、GitHub 上の公開日は未確認。PyPI の公開日は 2026-08-11。手順は公式資料に基づき、独立した実行・精度測定は行っていない。"
stars: 8830
forks: 1105
open_issues: 47
size_kb: 43867
language: "Python"
created: "2012-10-20"
updated: "2026-11-09"
archived: false
license: "ISC"
commits_30d: 59
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/RealMarvelX/status/2117612832019689696"]
fetched_at: "2026-11-10T09:51:59+00:00"
---

# librosa — 音源のテンポと拍位置を Python で抽出

## 出来ること

- 音源からテンポと拍位置を推定し、拍位置を秒単位で取り出せる。映像編集では、その時刻をカット候補として使える。 [公式リズム解析チュートリアル](https://librosa.org/doc/latest/auto_tutorials/01-intro/06-rhythm.html)

## 目的・背景

- 音楽情報検索向けの音声信号処理ライブラリ。拍追跡では発音の立ち上がりの強さを測り、推定テンポに沿うピーク列を動的計画法で選ぶ。既定では信号全体に一つのテンポを推定するため、テンポが大きく変わる曲には時変テンポを指定できる。 [公式実装](https://librosa.org/doc/main/_modules/librosa/beat.html) [公式の時変テンポ例](https://librosa.org/doc/latest/auto_tutorials/03-advanced/plot_dynamic_beat.html)

## 依存関係

- 主な依存は NumPy、SciPy、Numba、SoundFile、scikit-learn、soxr。 [公式パッケージ設定](https://raw.githubusercontent.com/librosa/librosa/main/pyproject.toml)

## 実行条件

- 1.0.0 は Python 3.12 以上。パッケージは PyPI で公開され、コードは ISC ライセンス。 [PyPI の公式配布ページ](https://pypi.org/project/librosa/)

## 最短手順

- Python 環境で `python -m pip install librosa` を実行する。 [公式 README](https://github.com/librosa/librosa/blob/main/README.md)
- Python で `import librosa`、`y, sr = librosa.load('music.wav')`、`tempo, beats = librosa.beat.beat_track(y=y, sr=sr, units='time')` の順に呼ぶ。Python を実行できる AI エージェントには、この処理をローカル音源に対して実行し、`beats.tolist()` を秒単位の JSON 配列として返すよう指示する。 [公式リズム解析チュートリアル](https://librosa.org/doc/latest/auto_tutorials/01-intro/06-rhythm.html)

## 変更履歴

- 2026-11-10: 初回登録
