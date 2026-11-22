---
name: "Open Source Face Recognition SDK"
genre: "other"
url: "https://github.com/Faceplugin-ltd/Open-Source-Face-Recognition-SDK"
repo: "Faceplugin-ltd/Open-Source-Face-Recognition-SDK"
license: "unknown"
language: "Python"
commit_cadence: "monthly"
flags: ["low-quality", "unverified"]
risk_notes: "README заявляет «high accuracy», «real-time» и «completely free», но не приводит измерений точности или скорости; лицензионные условия не указаны. Эти заявления не представлены как независимо проверенные факты. README называет SDK бесплатным и открытым, но API указывает лицензию как unknown. Условия использования и лицензирования не подтверждены. GitHub APIでライセンスを確認できていません。"
stars: 3169
forks: 533
open_issues: 0
size_kb: 55916
created: "2025-01-17"
updated: "2026-10-02"
archived: false
commits_30d: 0
commits_90d: 3
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/bkdgiffug/status/2118888416800542983"]
fetched_at: "2026-11-16T22:00:20Z"
last_release: ""
last_release_at: ""
---

# Open Source Face Recognition SDK

## 出来ること

- READMEによると、画像から顔を検出してバウンディングボックス、顔のランドマーク、特徴量埋め込みを取得できます。2つの埋め込みを比較し、0〜100の類似度スコアを返すAPIも説明されています。対応画像形式としてJPG、PNG、BMP、TIFFが挙げられています。

## 目的・背景

- WindowsおよびLinux上で、アプリケーションに顔認識機能を組み込むためのPython SDKとして紹介されています。READMEは処理がオンプレミスで行われると説明しています。

## 依存関係

- README記載の前提条件はPython 3.9以上です。Anacondaは依存関係管理のための推奨事項として記載されています。依存パッケージはリポジトリのrequirements.txtからインストールする手順です。

## 実行条件

- READMEではWindowsまたはLinuxを対象とし、GPUは任意でCPUのみでも利用できると説明しています。実行時の詳細なハードウェア要件は記載されていません。

## 最短手順

- READMEの手順は、Python 3.9のconda環境を作成して有効化し、`pip install -r requirements.txt`を実行する流れです。基本例では`FaceRecognition`を読み込み、`GetImageInfo(image_path, faceMaxCount=10)`で画像を処理し、`get_similarity(feature1, feature2)`で埋め込みを比較します。

## 変更履歴

- 2026-11-14: 初回登録
