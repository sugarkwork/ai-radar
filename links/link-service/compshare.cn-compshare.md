---
type: "link"
name: "CompShare（優云智算）"
genre: "link-service"
url: "https://www.compshare.cn/"
author: "UCloud（优刻得科技）"
pricing: "paid"
pricing_detail: "GPU 従量/包日/包月/抢占の4方式。RTX4090 24G（1*GPU 14C32G）従量 1.92元/h・包月 1,154.64元、RTX4090 48G（16C96G）3.80元/h・包月 2,280.00元、RTX3080Ti 12G 0.74元/h、A100 80G 10.75元/h。GPU の無料枠は確認できず、云硬盘 50GB と公共モデル库 30TB が無料（2026-11 時点、すべて税抜表示かは未確認）"
signup_required: true
added: "2026-11-06"
first_seen: "2026-11-06"
sources: ["https://x.com/wquguru/status/2117202562160238691"]
flags: ["unverified"]
risk_notes: "GPU の無料枠・トライアルの有無、本人確認（実名認証）の要否、表示価格の税込/税抜は未確認。対象URLには referral_code と ytag のアフィリエイト用パラメータが付いており、エントリでは正規URL（https://www.compshare.cn/）を使う。コミュニティイメージは作成者が乌兰察布(cn-wlcb-01)の RTX4090 のみで検証済みと明記。210GB のイメージ取得とストレージ課金が別途発生する。"
fetched_at: "2026-11-06T21:06:07Z"
---

# CompShare（優云智算）— Agent が CLI/API で GPU を借りて解放まで回せる GPU クラウド

## 目的

- UCloud（优刻得）系の GPU クラウド。AI の学習・推論・画像生成用に GPU インスタンスを時間・日・月単位で借りる。
- 公式 CLI・REST API・Agent Skill が揃っており、人間がコンソールを触らなくても AI エージェントが在庫確認→見積→起動→実行→解放まで完結できる点を売りにしている。

## 何ができるか

- CLI: `pip install compshare-cli` で入る `compshare` コマンド。`config`（認証プロファイル）/`doctor`（設定・認証・SSH 診断）/`instance`（検索・作成・一覧・SSH）/`image`/`storage`/`bandwidth`/`minimax`/`team` のサブコマンドを持つ。
- エージェント向け: 全コマンドが `--json` で単一の JSON を返す。`instance create --dry-run` で価格と影響を先に見積もり、承認後に `--yes` で実行する運用。
- 公式 Agent Skill: `npx skills add compshare-cn/compshare-cli --skill compshare-cli`。Codex / Claude Code / Cursor 等に入り、SKILL.md 側で「変更前に必ず dry-run」「秘匿情報をログに出さない」「タイムアウト後は再試行前に状態確認」といった手順を規定している。
- REST API: `https://api.compshare.cn`。GPU インスタンスの作成・起動・停止・削除・再インストール・課金方式変更・価格照会・在庫確認（CheckCompShareResourceCapacity）・イメージ/ディスク/CFS/チーム管理までエンドポイントが公開されている。認証は公開鍵/秘密鍵。
- 実用例: コミュニティイメージをそのまま起動できる。対象URLの「Shisei线稿转白模深度法线」（210GB、ComfyUI + Qwen-Image-Edit-2511、Depth Anything V2、Marigold Normals）は起動すると ComfyUI が 8188 番で立ち上がり、`/root/pilot/run.sh` で線画→白模/深度/法線をバッチ生成する。
- MiniMax H3 の動画・画像・音声タスクも同じ CLI から投げられる。SSH 接続・ファイル転送・常駐ジョブ・定时关机にも対応。

## 料金

- GPU は「従量 / 包日 / 包月 / 抢占（スポット）」の4方式。価格ページ（https://www.compshare.cn/price-list）に卡型・CPU/メモリ構成ごとの数値が公開されている。
- RTX4090 24G・1*GPU 14C32G: 従量 1.92元/h、包日 42.33元、包月 1,154.64元、抢占 1.31元/h。
- RTX4090 48G（高顕存型）・1*GPU 16C96G: 従量 3.80元/h、包日 83.60元、包月 2,280.00元。抢占の設定は「/」で提供なし。
- RTX3080Ti 12G・1*GPU 12C32G: 0.74元/h。A100 80G・1*GPU 16C64G: 10.75元/h、包月 6,452.40元。
- ストレージ: 云硬盘はインスタンス併設で 50GB まで無料、超過 0.01元/GB/日。云存储 0.004元/GB/日、イメージ保存 0.008元/GB/日、公共モデル库は 30TB まで無料。
- GPU の無料枠・トライアルは価格ページに記載が見当たらず未確認。Coding Plan（モデル API の定額プラン、49〜999元/月）は別 product。
- 料金はすべて人民元建て。税込/税抜の別と可用区による差は未確認。

## 登録の要否

- 要。インスタンス作成・課金・API キー発行にはアカウント作成とコンソール（console.compshare.cn）ログインが必須。
- API キーはコンソールのアカウントセンター → API 密钥で公開鍵/秘密鍵のペアを発行し、`compshare config` か環境変数 `COMPSHARE_PUBLIC_KEY` / `COMPSHARE_PRIVATE_KEY` で渡す。
- CLI のインストール自体と `--help` / 構造化ヘルプの表示は認証なしで可能。実際の検索・作成・課金にはキーが要る。
- 本人確認（実名認証）の要否は未確認。

## 変更履歴

- 2026-11-06: 初回登録
