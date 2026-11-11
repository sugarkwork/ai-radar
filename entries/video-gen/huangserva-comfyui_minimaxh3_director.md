---
name: "ComfyUI MiniMax H3 Director workflows"
genre: "video-gen"
url: "https://github.com/huangserva/ComfyUI_MiniMaxH3_Director"
repo: "huangserva/ComfyUI_MiniMaxH3_Director"
license: "Apache-2.0"
stars: 1485
language: "unknown"
created: "2026-08-04"
updated: "2026-08-04"
forks: 152
open_issues: 2
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 10
archived: false
flags: ["unverified"]
risk_notes: "README报告的已验证环境仅覆盖 RTX 4090、ComfyUI 0.30.0、PyTorch 2.11.0 + CUDA 12.8 和 Ref2VA INT8；该环境下可运行 R2V、V2V、RV2V。T2V、I2V、FL2V 尚需 fl2va 权重。人物身份没有硬锁，README建议检查分段衔接与人物一致性。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/eva_love_1999/status/2118550439440584983"]
fetched_at: "2026-11-11T01:32:13.907626+00:00"
---

# ComfyUI MiniMax H3 Director workflows

## 出来ること

- 仓库保存5份可直接导入 ComfyUI 的 MiniMax H3 Director 工作流，覆盖 T2V 文生音视频、FL2V/I2V 首尾帧或单首帧图生视频、R2V 图片/视频/音频参考生成、V2V 按源视频时间轴分段编辑，以及 RV2V 源视频加参考图或参考音频。README说明导演台支持逐段运行与缓存，音频可选择模型生成、沿用原声或静音。

## 目的・背景

- README称工作流来自 AIMixer/ComfyUI_MiniMaxH3_Director，此仓库保留一套方便下载、复现和测试的副本。

## 依存関係

- 需要 ComfyUI 0.30.0 或更高版本、AIMixer/ComfyUI_MiniMaxH3_Director 上游节点及其 requirements.txt。T2V、I2V、FL2V 使用 minimax_h3_fl2va_pruned_int8_convrot.safetensors；R2V、V2V、RV2V 使用 minimax_h3_ref2va_pruned_int8_convrot.safetensors。共用 Qwen3VL 32B text encoder、视频 VAE 和音频 VAE 文件；CLIP Loader 类型设为 minimax。SageAttention 为可选项。模型权重遵循各自许可条款。

## 実行条件

- README列出的已验证环境为 NVIDIA RTX 4090 48GB、ComfyUI 0.30.0、PyTorch 2.11.0 + CUDA 12.8、MiniMax H3 Ref2VA INT8，并称 MiniMaxH3Director 节点已成功注册。README称该环境只有 Ref2VA，可运行 R2V、V2V、RV2V；T2V、I2V、FL2V 需补齐 fl2va 权重。此为 README 的环境报告。

## 最短手順

- 在 ComfyUI/custom_nodes 安装 AIMixer/ComfyUI_MiniMaxH3_Director，并按 README 所列命令安装 requirements.txt；重启 ComfyUI，将 example_workflows/ 中对应 JSON 拖入页面。RV2V：导入工作流，上传源视频并按镜头切分或智能分割，上传人物参考图（需要声音约束时再加参考音频），逐段填写提示词；先生成5秒并检查脸部、服装、动作和镜头边界，再决定是否扩展。

## 変更履歴

- 2026-11-11: 初回登録
