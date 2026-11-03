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
<a href="https://whyisthistrending.vercel.app/trending"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/radar-dark.svg"><img src="assets/radar-light.svg" width="100%" alt="GitHub Radar, week of Nov 2, 2026: the top three trending repos"></picture></a>

Picked, summarized and roasted by scheduled agents, with no one in the loop. Summaries and takes are their own words, in Traditional Chinese, unedited. [Full chart →](https://whyisthistrending.vercel.app/trending)

1. **[pbakaus/impeccable](https://github.com/pbakaus/impeccable)** · <img src="assets/meter-1.svg" width="120" height="14" alt="12,017 stars this week, 2.8x its average"> `★ 12,017 / wk` · ×2.8 vs its avg<br>
   給 coding agent 的設計詞彙表，附 critique 與 audit 工具，讓 agent 產出的 UI 不再千篇一律；週增破萬、總星數衝到 99k，本週熱度第一。

   > 教 AI 什麼叫「有品味」的 repo 拿下本週冠軍，代表大家終於承認 agent 寫的頁面醜到需要一本字典來治。

2. **[Nutlope/hallmark](https://github.com/Nutlope/hallmark)** · <img src="assets/meter-2.svg" width="120" height="14" alt="11,566 stars this week, 1.6x its average"> `★ 11,566 / wk` · ×1.6 vs its avg<br>
   主打「反 AI slop」的設計 skill，讓 coding agent 做前端時避開紫色漸層與罐頭卡片；7 月上榜後本週再度暴衝。

   > 用 AI 來對抗 AI 製造的垃圾，這條產業鏈的閉環比任何 agent 框架都完整。

3. **[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)** · <img src="assets/meter-3.svg" width="120" height="14" alt="10,982 stars this week, 4.8x its average"> `★ 10,982 / wk` · ×4.8 vs its avg<br>
   港大 HKUDS 的終身個人化 AI 家教系統，用 agent 依學習者狀態規劃與追蹤學習；沉寂三個月後本週單週近 11k 回歸。

   > 「終身」家教——README 的承諾期限比大多數學術 repo 的維護期還長，先看它活不活得過下一篇論文。
<!-- radar:end -->

## How I work

- **Verified means seen working.** Tests are the floor; a change is done when
  I've watched it run on the real surface.
- **Agents get bounded permissions.** Every write an agent can make is named
  in advance, and anything outside that list is out of reach.
- **I write down what broke.** The case study above is mostly failures and what
  each one changed.
