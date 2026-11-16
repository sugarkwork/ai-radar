---
name: "大模型推理案头手册（开源版）"
genre: "other"
url: "https://github.com/shtjww/llm-inference-capacity-handbook"
repo: "shtjww/llm-inference-capacity-handbook"
license: "unknown"
flags: ["unverified"]
risk_notes: "README说明此版本是完整版的开源节选，未包含常数锚定的详细方法、部分 MoE 算例及规划报告模板等内容。 GitHub APIでライセンスを確認できていません。"
stars: 186
forks: 0
open_issues: 0
size_kb: 727
language: "unknown"
created: "2026-09-02"
updated: "2026-09-20"
archived: false
commits_30d: 0
commits_90d: 13
commit_cadence: "monthly"
type: "repo"
added: "2026-11-16"
first_seen: "2026-11-16"
sources: ["https://x.com/Ryrenz/status/2119069615401714093"]
fetched_at: "2026-11-16T16:26:36.108817+00:00"
---

# 大模型推理案头手册（开源版）

## 出来ること

- 手册介绍如何按物理上限、单节点系统瓶颈与排队延迟分层进行推理服务容量规划，涵盖 QPS、TTFT、TPOT、P95、KV Cache、压测及采购规划。README将这些内容描述为手册方法与算例，并非本次独立实测结论。

## 目的・背景

- README指出，手册面向从 GPU 算力推算服务容量、延迟与资源需求的容量规划问题；适合推理平台、SRE、容量规划工程师、技术管理者、售前交付及性能仿真研究者。手册声明不覆盖 CUDA 或算子级调优，也不提供可直接照搬的常数表。

## 依存関係

- README未说明软件依赖；内容定位为技术手册。

## 実行条件

- README未说明软件运行条件；本仓库README描述的是阅读和使用规划方法、公式及 SOP。

## 最短手順

- 按任务选择阅读路径：采购或汇报决策读第 0 章后接第 7 章；压测前读第 6 章；首次做容量规划则顺序阅读并用第 7 章算例练习。

## 変更履歴

- 2026-11-16: 初回登録
