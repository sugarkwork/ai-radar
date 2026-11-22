---
name: "Cinematic Skill"
genre: "coding-agent"
url: "https://github.com/Moh4696/cinematic-skill"
repo: "Moh4696/cinematic-skill"
license: "MIT"
stars: 633
language: "Python"
created: "2026-11-09"
updated: "2026-11-09"
forks: 91
open_issues: 1
commits_30d: 3
commit_cadence: "monthly"
commits_90d: 3
size_kb: 1989
archived: false
flags: ["unverified"]
risk_notes: "無料の下書き音声としてmacOSのsayまたはespeak-ngを使用し、最終音声は任意のTTSまたは録音音声と記載。Wikimedia Commonsから素材を取得する手順がある。最終音声サービスの料金・利用条件はREADMEに記載なし。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/GitTrend0x/status/2121566394286248121"]
fetched_at: "2026-11-16T21:46:08Z"
last_release: ""
last_release_at: ""
---

# Cinematic Skill

## 出来ること

- コーディングエージェントが、調査・台本作成、ナレーションに合わせたタイミング調整、画像や文書などの配置、カメラ移動、音響、字幕を含む映像をコードから構築する。映像はSkia（Python）で描画するとREADMEに記載。Wikimedia Commonsの画像検索・取得とライセンス記録、独自画像やAI生成静止画の利用にも対応すると説明されている。出典: https://github.com/Moh4696/cinematic-skill

## 目的・背景

- READMEによると、エージェントで制作した5分のアル・カポネのドキュメンタリーを元に、任意の題材に使えるよう開発された。映像生成ではなくコードでフレームを描画する設計で、同じ入力では同じ映像をレンダリングし、ナレーションの変更に合わせて映像のタイミングを調整すると説明されている。出典: https://github.com/Moh4696/cinematic-skill

## 依存関係

- README記載のPythonパッケージはskia-python、numpy、pillowで、scipyは任意。ffmpegをPATHに通す必要がある。インストーラー利用にはNode 22.20以降が必要。下書き音声にはmacOSのsayまたはespeak-ngを利用する。最終音声は任意のTTSまたは録音音声を使うとされる。出典: https://github.com/Moh4696/cinematic-skill

## 実行条件

- READMEは16 GBのノートPCで92秒の映像を1080pで約6分でレンダリングすると報告している。これはREADME記載の作者側の目安で、独立した実測値ではない。利用にはPython依存パッケージとffmpegが必要。出典: https://github.com/Moh4696/cinematic-skill

## 最短手順

- README記載の導入例は `npx skills add Moh4696/cinematic-skill`。Nodeなしの場合はシェルインストーラーも案内されている。導入後、`pip install -r requirements.txt` で依存を入れ、ffmpegをPATHに用意する。作例はプロジェクト作成、Commons素材取得、地図と素材準備、音声生成・分割・構築、最後にrender.pyでレンダリングする手順。出典: https://github.com/Moh4696/cinematic-skill

## 変更履歴

- 2026-11-14: 初回登録
