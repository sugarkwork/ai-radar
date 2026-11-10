---
repo: "xinntao/Real-ESRGAN"
name: "Real-ESRGAN"
genre: "image-gen"
url: "https://github.com/xinntao/Real-ESRGAN"
stars: 37430
forks: 4528
open_issues: 648
size_kb: 5514
language: "Python"
created: "2021-07-19"
updated: "2024-08-06"
archived: false
license: "BSD-3-Clause"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
last_release: "v0.3.0"
flags: ["unverified"]
risk_notes: "最新リリースのタグはGitHubの公開ページで確認した。公開日時、現在の依存バージョンでの互換性、実行速度、VRAM使用量、動画フレーム間の一貫性、配布重み固有の利用条件は未確認。画質の記述は著者の報告に基づき、独立した実行・測定は行っていない。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/RealMarvelX/status/2117612832019689696"]
fetched_at: "2026-11-10T09:51:41Z"
---

# Real-ESRGANで低解像度画像を復元・拡大する

## 出来ること

- 一般画像向けの学習済みモデルで画像を4倍に拡大できる。公式リポジトリはアニメ動画向けのモデルも案内している。 [公式README](https://raw.githubusercontent.com/xinntao/Real-ESRGAN/master/README.md)

## 目的・背景

- 入力の劣化過程が未知の画像を対象とする超解像。著者は二段階の劣化モデルで学習用画像を合成し、比較例でアーティファクトの低減とテクスチャの改善を報告した。直線の歪みや不自然な模様が出る例、学習で想定していない劣化が残る例も報告している。 [公式論文](https://arxiv.org/abs/2107.10833)

## 依存関係

- Python版のREADME記載要件はPython 3.7以上とPyTorch 1.7以上。導入手順ではBasicSRと、顔補正用のfacexlibおよびGFPGANを案内している。 [公式README](https://raw.githubusercontent.com/xinntao/Real-ESRGAN/master/README.md)

## 実行条件

- 公式のNCNN/Vulkanポータブル版はWindows、Linux、macOS向けで、CUDAやPyTorchの環境を必要としない。タイル分割により境界で出力が不連続になることがある。 [公式README](https://raw.githubusercontent.com/xinntao/Real-ESRGAN/master/README.md)
- リポジトリのライセンスは親側のAPI測定でBSD-3-Clause。公式READMEはローカル推論を案内している。 [GitHubリポジトリAPI](https://api.github.com/repos/xinntao/Real-ESRGAN) [公式README](https://raw.githubusercontent.com/xinntao/Real-ESRGAN/master/README.md)

## 最短手順

- 公式READMEに従ってPython版の依存関係を導入し、RealESRGAN_x4plusの公開重みを配置する。リポジトリ直下で `python inference_realesrgan.py -n RealESRGAN_x4plus -i input.jpg -o results` を実行し、出力を確認する。 [公式README](https://raw.githubusercontent.com/xinntao/Real-ESRGAN/master/README.md)
- AIエージェントからは、シェル実行機能に同じCLIを渡す。入力画像と出力ディレクトリを明示し、終了コードと生成ファイルを確認する。 [公式README](https://raw.githubusercontent.com/xinntao/Real-ESRGAN/master/README.md)

## 変更履歴

- 2026-11-10: 初回登録
