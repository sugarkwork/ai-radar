---
name: "JavRanking 浏览器扩展"
genre: "other"
url: "https://github.com/javranking/javranking-extension"
repo: "javranking/javranking-extension"
license: "MIT"
stars: 1043
language: "TypeScript"
created: "2026-09-07"
updated: "2026-10-27"
forks: 70
open_issues: 0
commits_30d: 4
commit_cadence: "weekly"
commits_90d: 15
size_kb: 833
archived: false
flags: ["unverified"]
risk_notes: "Chrome/Edge installation uses a manually loaded unpacked extension and updates are manual. Firefox is only available for temporary development loading; persistent installation requires a Mozilla-signed XPI, which is not yet available."
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/ruyi3699/status/2118735409052004744"]
fetched_at: "2026-11-13T22:10:04.709587+00:00"
---

# JavRanking 浏览器扩展

## 出来ること

- 用户主动点击浏览器工具栏图标后，扩展会识别当前页面中的影片番号，并展示可对应的 JavRanking 榜单资料。README 还说明，扩展读取 JavRanking 已发布的静态搜索索引来查找匹配项。

## 目的・背景

- 为浏览器当前页面提供影片番号识别和对应榜单资料查看功能。README 未说明更广泛的产品目标。

## 依存関係

- 从源代码验证和构建需要 Node.js 20.19 或更高版本。README 未列出浏览器扩展运行时的其他依赖。

## 実行条件

- Chrome 或 Edge 可通过加载解压后的 Chromium ZIP 安装。Firefox 仅支持临时开发加载；持久安装需要目前尚未提供的 Mozilla 签名 XPI。README 称页面 URL、页面文字、DOM 内容和浏览记录不会上传；绑定冲码后，用户标记的影片番号、标记状态与时间会同步至 JavRanking API。

## 最短手順

- Chrome/Edge：从 GitHub Releases 下载 Chromium ZIP，解压到本地文件夹，打开 chrome://extensions 或 edge://extensions，启用 Developer mode，选择 Load unpacked 并选取含 manifest.json 的文件夹。更新需下载并解压新版，再 Reload 扩展或加载新文件夹。

## 変更履歴

- 2026-11-14: 初回登録
