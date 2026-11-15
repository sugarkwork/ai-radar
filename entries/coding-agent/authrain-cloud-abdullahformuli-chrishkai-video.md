---
name: "ChrisHKAI-Video"
genre: "coding-agent"
url: "https://github.com/authrain-cloud-abdullahformuli/ChrisHKAI-Video"
repo: "authrain-cloud-abdullahformuli/ChrisHKAI-Video"
stars: 0
forks: 0
open_issues: 0
size_kb: 1008
language: "JavaScript"
created: "2026-11-07"
updated: "2026-11-07"
archived: false
license: "MIT"
commits_30d: 1
commits_90d: 1
commit_cadence: "monthly"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/abdullahformuli/status/2118982549833949493"]
fetched_at: "2026-11-15T03:13:09.290106+00:00"
---

# ChrisHKAI-Video

## 出来ること

- README описывает skill для coding agents, который по ссылке на X-профиль создает короткий ролик с автором в виде 3D vinyl toy. Этапы включают разбор публикаций и достижений, сборку персонажа, раскадровку, звук и рендер видео в Blender Cycles. Это описание возможностей из README, не независимая проверка результата.

## 目的・背景

- Проект предназначен для создания персонального intro-фильма на основе публикаций, временных меток, метрик и визуального оформления профиля автора. README указывает, что фильм строится кодом, без black-box video generation models и stock footage.

## 依存関係

- README перечисляет Blender 5.2+, Node.js 22+, Python 3.9+ с NumPy и Pillow, ffmpeg и headless Chrome. Для рендера рекомендуется GPU acceleration в Blender Cycles.

## 実行条件

- README заявляет экспериментальную поддержку Codex и Claude Code и сообщает о тестировании на macOS Apple Silicon и Linux с Blender Cycles. Для описанного процесса также нужны перечисленные зависимости и доступ к материалам профиля X. Независимая проверка этих условий не проводилась.

## 最短手順

- Для Codex README предлагает клонировать репозиторий, перейти в каталог и выполнить `python3 scripts/install-codex.py`; затем открыть Codex в доступной для записи папке и вызвать `$creator-toy-intro Make a self-intro film for https://x.com/abdullahformuli`. Для Claude Code описаны установка плагина через marketplace либо запуск с `--plugin-dir`.

## 変更履歴

- 2026-11-15: 初回登録
