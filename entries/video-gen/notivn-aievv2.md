---
name: "AIEV - AI Edit Video"
genre: "video-gen"
url: "https://github.com/notivn/AIEVv2"
repo: "notivn/AIEVv2"
stars: 143
forks: 66
open_issues: 5
size_kb: 15302
language: "TypeScript"
created: "2026-10-26"
updated: "2026-11-13"
archived: false
license: "MIT"
commits_30d: 14
commits_90d: 14
commit_cadence: "weekly"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・依存関係。"
type: "repo"
added: "2026-11-16"
first_seen: "2026-11-16"
sources: ["https://x.com/Ryrenz/status/2119039413329993878"]
fetched_at: "2026-11-16T07:16:17.575410+00:00"
---

# AIEV - AI Edit Video

## 出来ること

- AI-монтаж видео: Claude анализирует исходник, создает сцены HyperFrames на HTML и GSAP, собирает таймлайн в Remotion и экспортирует MP4. Встроенный редактор позволяет просматривать и изменять сцены, субтитры, звуковые эффекты и музыку. Также описаны преобразование текста или URL в видео с озвучкой, нарезка длинных видео на короткие и перевод видео с субтитрами и/или дубляжом. Источник: README проекта — https://github.com/notivn/AIEVv2.

## 目的・背景

- README представляет AIEV как систему автоматического AI-монтажа видео, где Claude выступает режиссером, а пользователь контролирует работу через веб-панель. В описании заявлены черновой монтаж и проверка каждого кадра; это описание автора, а не независимая проверка. Источник: https://github.com/notivn/AIEVv2.

## 依存関係

- README перечисляет Node.js 24 LTS (также указаны версии 22.23.4+ и 26.12.1+), FFmpeg и Google Chrome. Для функций Claude требуется вход в Claude Code или ANTHROPIC_API_KEY; для генерации изображений, Gemini TTS и перевода — GEMINI_API_KEY. Python 3.11–3.14 указан как необязательный для субтитров faster-whisper и офлайн-голосов VieNeu-TTS; необязательные шлюзы изображений требуют Python 3.13 или 3.14. Источник: https://github.com/notivn/AIEVv2.

## 実行条件

- README сообщает, что запускной скрипт проверяет окружение и предлагает установить доступные компоненты. Указаны отдельные сценарии запуска для Windows, macOS и Linux; для ручного запуска разработки приведены `npm install` и `npm run dev`. Для рендеринга HyperFrames и Remotion используют headless Chromium. Источник: https://github.com/notivn/AIEVv2.

## 最短手順

- README предлагает получить репозиторий командами `git clone https://github.com/notivn/AIEVv2.git` и `cd AIEVv2`, затем запустить `start\start.bat` в Windows, `start/start.command` в macOS или `./start/start.sh` в Linux. README говорит, что скрипт проверяет окружение, выполняет `npm install` при первом запуске, собирает проект, создает `.env` и запускает сервер и веб-интерфейс. Источник: https://github.com/notivn/AIEVv2.

## 変更履歴

- 2026-11-16: 初回登録
