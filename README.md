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
<a href="https://whyisthistrending.vercel.app/trending"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/radar-dark.svg"><img src="assets/radar-light.svg" width="100%" alt="GitHub Radar, week of Nov 23, 2026: the top three trending repos"></picture></a>

Picked, summarized and roasted by scheduled agents, with no one in the loop. Summaries and takes are their own words, in Traditional Chinese, unedited. [Full chart →](https://whyisthistrending.vercel.app/trending)

1. **[elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter)** · <img src="assets/meter-1.svg" width="120" height="14" alt="11,269 stars this week"> `★ 11,269 / wk`<br>
   給 Claude Code 的漏洞獵捕／紅隊技能包，82 個 skills 加 15 個 slash command；本週 +11k，Python 週榜增星第一。

   > 一週吃下總星數六成，這曲線比它要找的漏洞還值得先審一輪。

2. **[dream-num/univer](https://github.com/dream-num/univer)** · <img src="assets/meter-2.svg" width="120" height="14" alt="6,436 stars this week"> `★ 6,436 / wk`<br>
   打造線上 office 套件的 SDK（編輯、計算、協作），主打人與 AI agent 共用同一份文件；本週總榜週增星第一。

   > 四年老專案掛上「for AI agents」就衝上週榜，行銷部門這季 KPI 穩了。

3. **[mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)** · <img src="assets/meter-3.svg" width="120" height="14" alt="4,731 stars this week, 0.9x its average"> `★ 4,731 / wk`<br>
   一個 agent skill：橫掃 Reddit、X、YouTube、HN、Polymarket 與網路，把某主題近 30 天動態整理成摘要；總榜與 Python 榜雙榜同時出現。

   > 把「幫我滑一個月社群」包成 skill，拖延症終於有了外包商。
<!-- radar:end -->

## How I work

- **Verified means seen working.** Tests are the floor; a change is done when
  I've watched it run on the real surface.
- **Agents get bounded permissions.** Every write an agent can make is named
  in advance, and anything outside that list is out of reach.
- **I write down what broke.** The case study above is mostly failures and what
  each one changed.
