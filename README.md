# Hi, I'm Kevin

Backend engineer, Java first, now building AI applications that run in
production rather than in a notebook.

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

<a href="https://github.com/zexion7873/perchling"><img src="https://raw.githubusercontent.com/zexion7873/perchling/main/docs/moods.gif" width="480" alt="perchling, a small husky in blue goggles, in its five moods: idle, running at a laptop, waiting, done with a grin, and error with a red cross through each eye."></a>

*perchling's five moods, one per Claude Code state: idle, running, waiting, done, error.*

## This week on GitHub Radar

<!-- radar:start -->
<sub>Week of 2026-10-26. Picked, summarized and roasted by the radar's scheduled agents, in Traditional Chinese, with no one in the loop. [Full chart →](https://whyisthistrending.vercel.app/trending)</sub>

1. **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** · ★ 15,072 this week<br>
   Cloudflare 出的 coding-agent 安全稽核 skill：多階段審查，每條 finding 都獨立驗證、輸出機器可讀格式。本週週增星數全榜第一。<br>
   <i>讓 agent 寫完漏洞再請 agent 來抓漏洞，安全產業終於找到永動機。</i>
2. **[debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio)** · ★ 11,837 this week<br>
   完全本機跑的開源 ElevenLabs 替代品：聲音複製、配音、聽寫、轉錄、有聲書一條龍，號稱支援 646 種語言。<br>
   <i>646 種語言，其中大概有 600 種連 README 作者自己都沒聽過——但星星不用聽得懂。</i>
3. **[stablyai/orca](https://github.com/stablyai/orca)** · ★ 9,622 this week<br>
   管理一整支 coding agent 艦隊的工作台（Claude Code 等），用自己的訂閱在桌機、手機、遠端 runtime 上跑任意 agent。<br>
   <i>第七週上榜，一個人管不好一個 agent，所以解法是給你一整支艦隊。</i>
<!-- radar:end -->

## How I work

- **Verified means seen working.** Tests are the floor; a change is done when
  I've watched it run on the real surface.
- **Agents get bounded permissions.** Every write an agent can make is named
  in advance, and anything outside that list is out of reach.
- **I write down what broke.** The case study above is mostly failures and what
  each one changed.
