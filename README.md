# Hi, I'm Kevin

Backend engineer, Java first, now building AI applications that run in
production rather than in a notebook.

<p align="center"><a href="https://github.com/zexion7873/perchling"><img src="https://raw.githubusercontent.com/zexion7873/perchling/main/docs/moods.gif" width="600" alt="perchling, a small husky in blue goggles, in its five moods: idle, running at a laptop, waiting, done with a grin, and error with a red cross through each eye."></a></p>

<p align="center"><em><a href="https://github.com/zexion7873/perchling">perchling</a>, a desktop pet that reacts to Claude Code, in its five moods: idle, running, waiting, done, error.</em></p>

## What I build

- **Agent pipelines that run unattended.** Seven scheduled Claude Code agents
  scout GitHub and the AI blogs, enrich what they find and write a weekly
  archive. Every agent's write surface is bounded, and a read-only agent checks
  the data contract every week.
  [How it's built, and what broke →](https://github.com/zexion7873/github-radar-ui/blob/main/docs/case-study.md)
- **RAG with evals in CI.** A Java 25 / Spring AI service that answers questions
  over that archive's trending repos and blog posts, in Chinese or English, with
  citations back to the rows it used. Every pull request is gated by a retrieval
  eval.
- **Tools for working with coding agents**, built because I wanted them.

## Projects

| Project | What it is | Stack |
|---|---|---|
| [radar-rag](https://whyisthistrending.vercel.app/ask) ([repo](https://github.com/zexion7873/radar-rag)) | Cited Q&A over the trending and blog archives, eval-gated in CI | Java 25 · Spring AI · pgvector · ONNX embeddings · Claude · Python evals · Langfuse · Cloud Run |
| [GitHub Radar](https://whyisthistrending.vercel.app) ([repo](https://github.com/zexion7873/github-radar-ui)) | A weekly radar of trending AI repos, each with a one-line summary and a sharp take | Next.js 16 · Notion · Vercel |
| [usage-band](https://github.com/zexion7873/usage-band) | Context fill and rate-limit windows, always on above the Claude Code prompt | Claude Code plugin · TypeScript |
| [perchling](https://github.com/zexion7873/perchling) | A native desktop pet that reacts to what Claude Code is doing | Swift · macOS |

## This week on GitHub Radar

<!-- radar:start -->
<a href="https://whyisthistrending.vercel.app/trending"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/radar-dark.svg"><img src="assets/radar-light.svg" width="100%" alt="GitHub Radar, week of Nov 9, 2026: the top three trending repos"></picture></a>

Picked, summarized and roasted by scheduled agents, with no one in the loop. Summaries and takes are their own words, in Traditional Chinese, unedited. [Full chart →](https://whyisthistrending.vercel.app/trending)

1. **[pingdotgg/t3code](https://github.com/pingdotgg/t3code)** · <img src="assets/meter-1.svg" width="120" height="14" alt="15,379 stars this week, 2.2x its average"> `★ 15,379 / wk` · ×2.2 vs its avg<br>
   Agent harness 的遙控面板：用手機、網頁或 Electron 桌面版操控你本機已登入的 Claude Code、Codex、Cursor、Grok Build、OpenCode 等 coding agent；provider 清單剛擴充到 Grok Build、Antigravity，本週週星第一。

   > README 自己寫「非常早期、可能很多 bug、不收外部貢獻」，一週照樣灌進一萬五千顆星——大家要的不是穩定，是躺在沙發上用手機催 agent 加班。

2. **[mattpocock/skills](https://github.com/mattpocock/skills)** · <img src="assets/meter-2.svg" width="120" height="14" alt="9,635 stars this week, 0.9x its average"> `★ 9,635 / wk`<br>
   從作者個人 agent 目錄整理出來、給資深工程師用的 agent skills 合集，總星已破 31.8 萬，本週週增仍排第二。

   > 31 萬顆星收藏一個私房設定資料夾，GitHub 正式演化成大型「我也要那份 dotfiles」許願池。

3. **[NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology)** · <img src="assets/meter-3.svg" width="120" height="14" alt="9,327 stars this week"> `★ 9,327 / wk`<br>
   NVIDIA 開源的 Python 框架，替 LLM / agent 工作流建一層以圖為基礎的推理層（ontology），改善 context retrieval；總星 10.4k 有九成是本週湧入，等於本週正式出道。

   > RAG 繞了一大圈又走回 ontology，語意網那批老前輩正在角落默默點頭——這次只是多附了一張 GPU 帳單。
<!-- radar:end -->

## How I work

- **Verified means seen working.** Tests are the floor; a change is done when
  I've watched it run on the real surface.
- **Agents get bounded permissions.** Every write an agent can make is named
  in advance, and anything outside that list is out of reach.
- **I write down what broke.** The case study above is mostly failures and what
  each one changed.
