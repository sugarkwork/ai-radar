---
name: "Arnis"
genre: "other"
url: "https://github.com/louis-e/arnis"
repo: "louis-e/arnis"
license: "Apache-2.0"
stars: 18725
language: "Rust"
created: "2022-09-10"
updated: "2026-11-19"
forks: 1588
open_issues: 70
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 152606
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 依存関係。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/dextune/status/2119346686933778690"]
fetched_at: "2026-11-19T13:09:40.062352+00:00"
---

# Arnis

## 出来ること

- OpenStreetMapの地理データと標高データを処理して、実世界の地形や建築を反映したワールドを生成する。READMEではMinecraft Java Edition（1.21.4以降）、Bedrock Edition、Luanti（Minetest）、Hytaleに対応すると説明されている。範囲を地図上で選択し、Start Generationを押して生成するGUIがあり、ワールドの縮尺、スポーン地点、建物の内部生成などを設定できる。

## 目的・背景

- 実世界の地理データを大規模に扱い、町や都市、自然景観をMinecraftなどのワールドとして生成することを目的とする。READMEはモジュール性、性能、包括的な文書、使いやすさ、Windows・macOS・Linux対応をプロジェクトの目標に挙げている。

## 依存関係

- READMEでは、OpenStreetMapの地理データと標高データを利用すると説明している。個別の取得元や依存ライブラリの詳細は、リンクされたGitHub Wikiの文書を参照。

## 実行条件

- README記載の対応環境の目標はWindows、macOS、Linux。リリース版をダウンロードするか、RustのCargoでビルドして実行する。Minecraft向けCLIの例は `cargo run --release --no-default-features -- --output-dir="C:/YOUR_PATH/.minecraft/saves" --bbox="min_lat,min_lng,max_lat,max_lng"`。Nixを使う場合の実行例もREADMEにある。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- READMEの案内に従い、公式GitHub Releasesから最新リリースを入手する。GUIでは地図上で対象範囲を矩形選択し、Start Generationをクリックする。CLIではビルド後に出力先と緯度・経度の範囲を指定する。READMEは配布元として公式サイトまたはGitHubのみを案内している。

## 変更履歴

- 2026-11-23: 初回登録
