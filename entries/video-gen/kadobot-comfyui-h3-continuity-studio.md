---
repo: KadoBOT/ComfyUI-H3-Continuity-Studio
name: H3 Continuity Studio
genre: video-gen
url: https://github.com/KadoBOT/ComfyUI-H3-Continuity-Studio
license: MIT
stars: 147
language: Python
created: 2026-11-02
updated: 2026-11-06
added: 2026-11-03
sources:
  - https://x.com/superfang119/status/2117545628398162003
  - https://x.com/superfang119/status/2117634030393040927
forks: 16
open_issues: 1
commits_30d: 100
commits_90d: 100
commit_cadence: daily
size_kb: 6590
archived: false
fetched_at: "2026-11-06T22:51:59Z"
last_release: v0.18.0
last_release_at: 2026-11-06
---

# H3 Continuity Studio

## 出来ること

- MiniMax H3 で複数ショットの連続映像を作るための ComfyUI カスタムノード群。**Timeline** でクリップを並べ、連続するクリップ間でコンテキストを引き継ぐ。
- **Visual Memory**: 前のクリップの任意の瞬間を選び、後のショット（別カメラアングル、屋外シーンを挟んだ後でも）へ持ち込める。これが本リポジトリの中心機能。
- **H3 Story**: OpenAI 互換エンドポイント（ローカル／クラウド）に接続し、Timeline の計画とプロンプト記述を書かせる。任意機能。
- **Studio**: story / reference / timeline の編集 UI。加えて、保存済みセグメント、スチル、H3 コンテキストウィンドウ用のノードを含む。
- **編集履歴**: Timeline の編集を元に戻す／やり直す。直近100件の名前付き状態から任意の時点へ移動できる（プロジェクトやワークフローの変更、再読み込みまで）。
- **長い参照動画の分割再生成**: 1本の動画をクリップごとの区間に分けて持たせ（`video_slices`）、未描画のクリップが残る間は描画済み部分と元動画のフレーム・音声を合わせた `_partial.mp4` を書き出す。
- **ガイドと FLF2VA**: 任意のフレームにガイド画像を置け、REF2VA のクリップを First/Last フレーム＋キャッシュ済み RefMods（FLF2VA）へ変換できる。音声付きクリップも変換でき、H3 audio VAE の接続が必要。
- **台詞キューと録音の固定**: 録音の各時点の台詞（話者、画面内／ナレーション）をキューとして持ち、クリップに喋らせる。録音はシーケンス時計に固定でき、ブリッジで尺が動かない。
- 継続性チェック用のリファレンス（`docs/CONTINUITY-CHECK.md`）と、外部 Timeline 連携（`docs/EXTERNAL-TIMELINE.md`）の資料を同梱。
- **音声をボックスに固定**（v0.18.0）: 録音の各区間をタイムラインのボックスに紐づけ、尺の変更・並べ替え・挿入をしても割り当てが崩れない。ボックスを伸ばすと無音が入り、縮めると末尾が隠れて戻すと復元される（既定オフ、解除で元の連続配置に戻る）。
- **第1パスを残して第2パスだけ描き直す**（v0.16.0）: `H3 Disk Cache` ノードが第1パスの結果をディスクに保存し、`H3 Save Segment` の `guide_frames` で続きのクリップを「描画済みの最終フレーム」から案内する。`codec` で H.264 / HEVC（HDR は Main10）を選べる。
- **編集とプレビュー**（v0.13〜0.15）: 描画後に設定が変わったクリップを *outdated* としてサムネイル・動画を保ったまま表示、尺や形式の違うクリップの連結、波形表示とビート検出／スナップ、プレイヘッド、名前付きチェックポイントと自動保存。

## 目的・背景

MiniMax H3 で長尺・多ショットの物語映像を作ると、ショット間で人物・小道具・空間がずれる。その連続性を ComfyUI 内で扱うために作られたノードパック。作者は KadoBOT、MIT。2026-11-02 作成と極めて新しく、v0.1.0 時点でデモ動画（2分弱のコンテスト版とフル版）を Releases で配布している。ドキュメントサイトは GitHub Pages（kadobot.github.io/ComfyUI-H3-Continuity-Studio/）。

## 依存関係

- 稼働する ComfyUI（MiniMax H3 対応版）と H3 のモデル一式（diffusion モデル、text encoder、video VAE、audio VAE、任意で LoRA）。
- `requirements.txt` を **ComfyUI と同じ Python 環境**で入れる。Windows ポータブル版は `python_embeded/python.exe` を使う。
- Story 機能は別途 OpenAI 互換の言語モデルエンドポイント設定が必要。
- Context Windows 機能はコアに MiniMax H3 Context Windows ノードを含む ComfyUI バージョンが必要。
- モデル重みとプロバイダ認証情報は同梱されない（自動ダウンロードもしない）。

## 実行条件

- GPU と H3 用モデルファイルが必須。必要 VRAM は選ぶ H3 モデル次第で、ノードパック側は規定していない。
- **MiniMax H3 のプロンプトガイド（`base-en.txt` / `ref-en.txt`）は公開リリースに含まれない**。正規に入手済みの場合は `h3_continuity/h3_guide/` に置くと有効化される。無い場合も動作はするが、同梱の instruction bundle がガイド欠落を報告する。
- H3 モデルとガイドは MiniMax の利用条件（地域制限を含む）に従う。
- 既存インストールと並置すると同一ノード／ルートが二重登録されるため、上書き設置は禁止（README 明記）。
- ソースは CPU のみの ComfyUI で起動確認済み。生成には GPU が要る。

## 最短手順

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/KadoBOT/ComfyUI-H3-Continuity-Studio
cd ComfyUI-H3-Continuity-Studio
python -m pip install -r requirements.txt   # ComfyUI と同じ Python で
# ComfyUI を再起動し、examples/h3_story_studio.json を読み込む
# ローダーノードで手元の H3 モデル／VAE／text encoder を選択して Timeline を追加
```

## 変更履歴

- 2026-11-03: 初回登録（star 64 / pushed 2026-11-03 / v0.1.0）
- 2026-11-04: 編集履歴・部分書き出し・台詞キュー等の追加を反映（v0.10.1）
- 2026-11-06: 音声のボックス固定（v0.18.0）、H3 Disk Cache と guide_frames（v0.16.0）、outdated クリップ表示・波形・ビートスナップ・チェックポイント（v0.13〜0.15）
