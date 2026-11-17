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
<a href="https://whyisthistrending.vercel.app/trending"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/radar-dark.svg"><img src="assets/radar-light.svg" width="100%" alt="GitHub Radar, week of Nov 16, 2026: the top three trending repos"></picture></a>

Picked, summarized and roasted by scheduled agents, with no one in the loop. Summaries and takes are their own words, in Traditional Chinese, unedited. [Full chart →](https://whyisthistrending.vercel.app/trending)

1. **[meta/astryx](https://github.com/meta/astryx)** · <img src="assets/meter-1.svg" width="120" height="14" alt="13,501 stars this week"> `★ 13,501 / wk`<br>
   Meta 開源的 React 19 + StyleX design system：150+ 無障礙元件、7 套主題，repo 自帶 AGENTS.md、CLAUDE.md 與 Claude plugin，主打「人和 coding agent 讀同一份文件、寫出同一套 UI」；仍掛 beta，本週直接拿下總榜第一。

   > 一個還在 beta 的元件庫靠「agent ready」四個字奪下全站週冠軍——2026 年的設計系統要先討好的是 LLM，人類設計師請抽號碼牌。

2. **[sherlock-project/sherlock](https://github.com/sherlock-project/sherlock)** · <img src="assets/meter-2.svg" width="120" height="14" alt="10,412 stars this week"> `★ 10,412 / wk`<br>
   老牌 OSINT 工具：輸入 username，跨數百個社群網站找出同名帳號；2018 年的專案本週突然回暖，Python 週榜同場還有 soxoj/maigret，整個帳號情蒐類一起升溫。

   > 七歲的工具一週暴衝一萬星，沒有新版本撐腰，純粹是全網集體想起了「肉搜」這個需求。

3. **[pingdotgg/t3code](https://github.com/pingdotgg/t3code)** · <img src="assets/meter-3.svg" width="120" height="14" alt="9,260 stars this week, 0.8x its average"> `★ 9,260 / wk`<br>
   從任何電腦或手機遙控 Claude Code、Codex 等 coding agent 的介面；第三度上榜，本週仍是 TypeScript 週榜星數最高的 agent 工具。

   > 寫程式的終極形態：躺在床上用手機按 approve。生產力工具卷到最後，賣點是不用起床。
<!-- radar:end -->

## How I work

- **Verified means seen working.** Tests are the floor; a change is done when
  I've watched it run on the real surface.
- **Agents get bounded permissions.** Every write an agent can make is named
  in advance, and anything outside that list is out of reach.
- **I write down what broke.** The case study above is mostly failures and what
  each one changed.
