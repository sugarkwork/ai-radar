---
repo: agronholm/apscheduler
name: APScheduler
genre: other
url: https://github.com/agronholm/apscheduler
license: MIT
stars: 7685
language: Python
created: 2016-03-27
updated: 2026-10-26
added: 2026-11-05
first_seen: 2026-11-05
source_post: https://x.com/roundtablespace/status/2118172700757889191
sources:
  - https://apscheduler.readthedocs.io
flags: []
risk_notes: ""
forks: 819
open_issues: 86
commits_30d: 7
commits_90d: 21
commit_cadence: weekly
size_kb: 6069
archived: false
fetched_at: "2026-11-05T22:09:56Z"
last_release: 3.11.3
last_release_at: 2026-06-28
---

# APScheduler

## 出来ること

- Python のコードを**後で1回**、または**周期的に**実行するスケジューラ。アプリ内に埋め込んで使う。
- 3種類のトリガー: **cron形式**（開始・終了時刻の指定可）、**interval**（一定間隔）、**date**（指定日時に1回）。
- ジョブをDBに保存すれば、**プロセス再起動をまたいで状態を保持**し、停止中に実行すべきだったジョブを再開後に走らせる。
- ジョブの追加・削除を実行中に行える。実行器（executor）はスレッド／プロセス／asyncio から選べる。
- ジョブストアはメモリ、SQLAlchemy（SQLite/PostgreSQL/MySQL）、MongoDB、Redis などに対応。

## 目的・背景

cron や Windows タスクスケジューラの代わりに、**アプリケーション固有のスケジュールをコード内で管理する**ためのライブラリ。APScheduler 自体はデーモンでもサービスでもなく、CLIも持たない。常駐プロセスの中に組み込むか、専用プロセスの部品として使う。

## 依存関係

- Python 3.8 以上（3.x系）。
- `pip install apscheduler`。永続化する場合は `apscheduler[sqlalchemy]` など extras。
- asyncio 用のスケジューラ（`AsyncIOScheduler`）はイベントループ内で使う。

## 実行条件

- **デーモンではない**。プロセスが落ちればスケジューラも止まる。常時実行したいなら supervisor／systemd／コンテナ側でプロセスを維持する。
- ジョブストアをメモリにすると再起動で消える。永続化が必要ならDBを指定する。
- 分散環境で同じジョブを二重実行しないためには、1プロセスだけスケジューラを動かすか、ジョブストアのロックを設計する。
- ★7,685・直近30日で7コミット。v3.11.3 が安定版で、4.x 系が別途開発中。

## 最短手順

```bash
pip install apscheduler
```

```python
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

sched = BlockingScheduler(
    jobstores={"default": SQLAlchemyJobStore(url="sqlite:///jobs.sqlite")},
    timezone="Asia/Tokyo",
)

@sched.scheduled_job("cron", hour=9, minute=0, id="daily_report")
def daily_report():
    print("run")

sched.start()   # Ctrl+C で停止
```

## 変更履歴

- 2026-11-05: 初回登録（★7,685 / pushed 2026-10-26 / MIT / 3.11.3）
