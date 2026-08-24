# StackBlaze docs (Astro Starlight)

Content is in `src/content/docs/`. Sidebar IA lives in `astro.config.mjs`.

Write like the product: **project canvas**, **services**, **variables**, **environments**, **staged changes**, **volumes**. Do not lead with Render-style catalogs (web vs worker vs static as separate products) or Heroku dynos. A service is a Git repo, Docker image, template, cron job, or database on the canvas.

Do not invent pipelines, apps, templates, or cluster state. Never tell readers to kubectl. MCP tools are unprefixed (`get_app`, `deploy_app`). Tokens use the `kbr_pat_` prefix. There is no `@stackblaze/cli` on this control plane. Config as code is `stackblaze.yaml`.
