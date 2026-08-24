#!/usr/bin/env python3
"""Generate Railway-shaped docs pages with StackBlaze-accurate content."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "src" / "content" / "docs"


def w(rel: str, body: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body.lstrip("\n"), encoding="utf-8")
    print(f"wrote {rel}")


# --- Framework guides (Railway Languages & frameworks tree) ---

FRAMEWORKS = [
    (
        "guides/nextjs.mdx",
        "Next.js",
        "node",
        "package.json",
        "next start",
        "Nixpacks detects Next.js from `package.json` and `next`. Bind to `PORT`. For the App Router, `output: 'standalone'` in `next.config` is a good fit for containers.",
    ),
    (
        "guides/express.mdx",
        "Express",
        "node",
        "package.json",
        "node index.js",
        "Listen on `process.env.PORT`. Keep the process in the foreground — do not daemonize.",
    ),
    (
        "guides/hono.mdx",
        "Hono",
        "node",
        "package.json",
        "node dist/index.js",
        "Works on Node, Bun, or a Dockerfile. Bind the HTTP server to `PORT`.",
    ),
    (
        "guides/fastify.mdx",
        "Fastify",
        "node",
        "package.json",
        "node server.js",
        "Listen on `0.0.0.0` and `process.env.PORT`. Fastify defaults to localhost otherwise, which fails health checks.",
    ),
    (
        "guides/nestjs.mdx",
        "Nest.js",
        "node",
        "package.json",
        "node dist/main.js",
        "Set a build command (`npm run build`) and start `node dist/main.js`. Nest must listen on `PORT`.",
    ),
    (
        "guides/remix.mdx",
        "Remix",
        "node",
        "package.json",
        "remix-serve ./build/server/index.js",
        "Nixpacks runs the start script. Set `PORT`. Attach a database from the canvas if you use Prisma or Drizzle.",
    ),
    (
        "guides/nuxt.mdx",
        "Nuxt",
        "node",
        "package.json",
        "node .output/server/index.mjs",
        "Use Nuxt Nitro's Node preset. The server listens on `PORT` after `nuxt build`.",
    ),
    (
        "guides/astro.mdx",
        "Astro",
        "node",
        "package.json",
        "node ./dist/server/entry.mjs",
        "Static output can be a static service. SSR needs the Node adapter and a start command that binds `PORT`.",
    ),
    (
        "guides/sveltekit.mdx",
        "SvelteKit",
        "node",
        "package.json",
        "node build",
        "Use the Node adapter (`@sveltejs/adapter-node`). Bind to `PORT`.",
    ),
    (
        "guides/bun.mdx",
        "Bun",
        "node",
        "bun.lockb",
        "bun run start",
        "Prefer a `Dockerfile` FROM `oven/bun` if Nixpacks picks Node. Listen on `PORT`.",
    ),
    (
        "guides/react.mdx",
        "React",
        "node",
        "package.json",
        "npx serve -s dist -l $PORT",
        "A Vite/CRA SPA is a static build. Serve the `dist` folder, or put it behind a Node service.",
    ),
    (
        "guides/vue.mdx",
        "Vue",
        "node",
        "package.json",
        "npx serve -s dist -l $PORT",
        "Vite + Vue builds static assets. Serve `dist`, or use Nuxt for SSR.",
    ),
    (
        "guides/angular.mdx",
        "Angular",
        "node",
        "package.json",
        "node dist/*/server/server.mjs",
        "SSR uses the Node server. Client-only builds can be served as static files.",
    ),
    (
        "guides/solid.mdx",
        "Solid",
        "node",
        "package.json",
        "node dist/index.js",
        "SolidStart / Vinxi should listen on `PORT`. A static Solid app is just files.",
    ),
    (
        "guides/sails.mdx",
        "Sails",
        "node",
        "package.json",
        "node app.js",
        "Sails reads `PORT`. Lift in production mode (`NODE_ENV=production`).",
    ),
    (
        "guides/gatsby.mdx",
        "Gatsby",
        "node",
        "package.json",
        "npx gatsby serve --port $PORT",
        "Build produces static HTML. Serve the public folder or `gatsby serve`.",
    ),
    (
        "guides/tanstack-start.mdx",
        "TanStack Start",
        "node",
        "package.json",
        "node .output/server/index.mjs",
        "Vinxi/Nitro output listens on `PORT` after the production build.",
    ),
    (
        "guides/fastapi.mdx",
        "FastAPI",
        "python",
        "requirements.txt or pyproject.toml",
        "uvicorn main:app --host 0.0.0.0 --port $PORT",
        "Nixpacks detects Python. Start Uvicorn/Gunicorn on `0.0.0.0:$PORT`.",
    ),
    (
        "guides/flask.mdx",
        "Flask",
        "python",
        "requirements.txt",
        "gunicorn -b 0.0.0.0:$PORT app:app",
        "Do not use the Flask dev server in production. Gunicorn or Waitress should bind `PORT`.",
    ),
    (
        "guides/django.mdx",
        "Django",
        "python",
        "manage.py",
        "gunicorn myproject.wsgi --bind 0.0.0.0:$PORT",
        "Set `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` to your `*.stackblaze.app` domain. Run migrations as a release command or one-off.",
    ),
    (
        "guides/laravel.mdx",
        "Laravel",
        "php",
        "composer.json",
        "php artisan serve --host=0.0.0.0 --port=$PORT",
        "Prefer php-fpm + nginx via Dockerfile for production. Set `APP_KEY` as a variable. Attach MySQL or Postgres from the canvas.",
    ),
    (
        "guides/symfony.mdx",
        "Symfony",
        "php",
        "composer.json",
        "php -S 0.0.0.0:$PORT -t public",
        "A Dockerfile with php-fpm is more typical. Set `APP_ENV=prod` and `APP_SECRET`.",
    ),
    (
        "guides/rails.mdx",
        "Rails",
        "ruby",
        "Gemfile",
        "bundle exec puma -C config/puma.rb",
        "Puma must bind `PORT`. Set `RAILS_MASTER_KEY`. Attach Postgres from **+ Service → Databases**.",
    ),
    (
        "guides/gin.mdx",
        "Gin",
        "go",
        "go.mod",
        "the compiled binary",
        "Nixpacks builds the Go module. Listen on `os.Getenv(\"PORT\")`.",
    ),
    (
        "guides/go-fiber.mdx",
        "Go Fiber",
        "go",
        "go.mod",
        "the compiled binary",
        "Fiber should `app.Listen(\":\" + os.Getenv(\"PORT\"))`.",
    ),
    (
        "guides/beego.mdx",
        "Beego",
        "go",
        "go.mod",
        "the compiled binary",
        "Set HTTP port from `PORT`. A Dockerfile is fine if Nixpacks misses the entrypoint.",
    ),
    (
        "guides/axum.mdx",
        "Axum",
        "rust",
        "Cargo.toml",
        "the compiled binary",
        "Bind `0.0.0.0:PORT`. Release builds take longer; cache is per service.",
    ),
    (
        "guides/actix-web.mdx",
        "Actix Web",
        "rust",
        "Cargo.toml",
        "the compiled binary",
        "Bind `0.0.0.0:PORT`. Prefer `Dockerfile` if you need extra system libs.",
    ),
    (
        "guides/rocket.mdx",
        "Rocket",
        "rust",
        "Cargo.toml",
        "the compiled binary",
        "Set `ROCKET_ADDRESS=0.0.0.0` and `ROCKET_PORT` from `PORT`.",
    ),
    (
        "guides/spring-boot.mdx",
        "Spring Boot",
        "java",
        "pom.xml or build.gradle",
        "java -jar app.jar",
        "Nixpacks detects Maven/Gradle. `server.port` must be `$PORT`. Heap is the service memory limit.",
    ),
    (
        "guides/ktor.mdx",
        "Ktor",
        "kotlin",
        "build.gradle.kts",
        "the packaged JAR",
        "Engine connector host `0.0.0.0`, port from `PORT`.",
    ),
    (
        "guides/aspnet-core.mdx",
        "ASP.NET Core",
        "csharp",
        "*.csproj",
        "dotnet MyApp.dll",
        "Use a Dockerfile FROM `mcr.microsoft.com/dotnet/aspnet`. Listen on `http://+:$PORT`.",
    ),
    (
        "guides/play.mdx",
        "Play",
        "scala",
        "build.sbt",
        "the staged binary",
        "A Dockerfile is the reliable path. Bind `http.port` to `PORT`.",
    ),
    (
        "guides/phoenix.mdx",
        "Phoenix",
        "elixir",
        "mix.exs",
        "mix phx.server",
        "Set `PHX_HOST` and `PORT`. Release builds via Dockerfile are typical for production.",
    ),
    (
        "guides/phoenix-distillery.mdx",
        "Phoenix + Distillery",
        "elixir",
        "mix.exs",
        "the release binary",
        "Build a Distillery/Elixir release in Docker. The release must read `PORT`.",
    ),
    (
        "guides/luminus.mdx",
        "Luminus",
        "clojure",
        "project.clj or deps.edn",
        "java -jar app.jar",
        "Uberjar in a Dockerfile is the usual path. Bind the HTTP kit/Jetty port to `PORT`.",
    ),
]

for rel, title, runtime, detect, start, note in FRAMEWORKS:
    slug = rel.split("/")[-1].replace(".mdx", "")
    w(
        rel,
        f"""---
title: {title}
description: Deploy {title} on StackBlaze from GitHub or a Dockerfile.
---

Add a service from your {title} repo. Nixpacks detects **{runtime}** from `{detect}`. A `Dockerfile` in the service root always wins.

{note}

## Deploy from GitHub

1. [Dashboard](https://dashboard.stackblaze.cloud) → **New project** (or open an existing canvas).
2. **+ Service → Git repository**. Pick the repo and branch.
3. Review [staged changes](/deploy/staged-changes/) and **Deploy**.
4. Generate a `*.stackblaze.app` domain, or attach a [custom domain](/networking/custom-domains/).

Override install / build / start on the service if detection is wrong. Typical start: `{start}`.

## Docker

If you already have a Dockerfile, StackBlaze uses it. The process must listen on `PORT`.

## Data

**+ Service → Databases** for Postgres, Redis/Valkey, MySQL, and others. Wire `DATABASE_URL` from the service **Variables** tab or `fromDatabase` in [stackblaze.yaml](/blueprint/).

## CLI

```bash
stackblaze login
stackblaze init
stackblaze up
```

See the [CLI](/cli/).
""",
    )


CLI_COMMANDS = [
    ("login", "Login", "Browser or token sign-in. Stores credentials in `~/.config/stackblaze/config.json`.", "stackblaze login"),
    ("logout", "Logout", "Removes the saved token from the local config file.", "stackblaze logout"),
    ("whoami", "Whoami", "Print the authenticated user and how many projects you can see.", "stackblaze whoami"),
    ("init", "Init", "Create a project (pipeline) and link the current directory. Alias: `new`.", "stackblaze init -y --pipeline my-app --phase production --app web"),
    ("link", "Link", "Point this directory at an existing project / environment / service (`.stackblaze/project.json`).", "stackblaze link"),
    ("unlink", "Unlink", "Remove the directory link.", "stackblaze unlink"),
    ("up", "Up", "Deploy the current directory (git build) or `--image` for a registry image. `--ci` streams NDJSON for pipelines.", "stackblaze up --wait"),
    ("down", "Down", "Scale the service to zero (pause). Pass `--yes` in CI.", "stackblaze down -y"),
    ("status", "Status", "Platform and Infrastructure as Code status for the linked project.", "stackblaze status"),
    ("open", "Open", "Print (and open) the dashboard URL for the linked project or service.", "stackblaze open"),
    ("logs", "Logs", "App logs. `-f` streams. `--search` queries the durable index.", "stackblaze logs -f"),
    ("metrics", "Metrics", "CPU and memory snapshot for the service.", "stackblaze metrics"),
    ("run", "Run", "Run a local command with the remote service environment injected.", "stackblaze run -- npm test"),
    ("shell", "Shell", "Interactive subshell with remote env vars.", "stackblaze shell"),
    ("ssh", "SSH", "Interactive shell into the running service (WebSocket console).", "stackblaze ssh"),
    ("connect", "Connect", "Open a database client in the service (for example `stackblaze connect postgres`).", "stackblaze connect postgres"),
    ("variables", "Variables", "`list`, `set KEY=value`, `delete KEY` on the linked service.", "stackblaze variables list"),
    ("env", "Env", "`stackblaze env pull` writes remote variables to `.env.local`.", "stackblaze env pull"),
    ("apps", "Apps", "List, get, create, update, restart, redeploy, scale, delete services (API name: apps).", "stackblaze apps list"),
    ("pipelines", "Pipelines", "List, create, delete projects (API name: pipelines).", "stackblaze pipelines list"),
    ("phases", "Phases", "List, create, delete, and `use` environments (API name: phases).", "stackblaze phases list"),
    ("builds", "Builds", "List, trigger, and stream git build logs.", "stackblaze builds list"),
    ("deployments", "Deployments", "List revisions and `rollback`.", "stackblaze deployments list"),
    ("domain", "Domain", "Add, remove, and check custom domains.", "stackblaze domain add www.example.com"),
    ("templates", "Templates", "Search the catalog and deploy a template onto a project.", "stackblaze templates search n8n"),
    ("addons", "Addons", "List, add, and delete managed databases and other add-ons.", "stackblaze addons list"),
    ("functions", "Functions", "List, get, new, push, invoke, delete Knative functions.", "stackblaze functions list"),
    ("waf", "WAF", "App Shield: status, enable, disable, under-attack mode.", "stackblaze waf status"),
    ("volume", "Volume", "List, add, and delete extra volumes on a service.", "stackblaze volume list"),
    ("snapshots", "Snapshots", "List, create, and restore volume snapshots.", "stackblaze snapshots list"),
    ("files", "Files", "Browse and transfer files on volume mounts.", "stackblaze files mounts"),
    ("apply", "Apply", "Apply `stackblaze.yaml` (IaC must be enabled). Never deletes.", "stackblaze apply ./stackblaze.yaml"),
    ("plan", "Plan", "Diff YAML against live state. No writes.", "stackblaze plan ./stackblaze.yaml"),
    ("export", "Export", "Download live topology as YAML.", "stackblaze export --out ./infra"),
    ("destroy", "Destroy", "Delete resources declared in a YAML path. Confirmation required.", "stackblaze destroy ./stackblaze.yaml"),
    ("agent", "Agent", "CLI agent helper for MCP-oriented workflows.", "stackblaze agent --help"),
    ("mcp", "MCP", "Print MCP connection details. `stackblaze setup mcp` wires Cursor / Claude.", "stackblaze setup mcp"),
    ("skills", "Skills", "Install agent skills. Also `stackblaze setup skills`.", "stackblaze setup skills"),
    ("completion", "Completion", "Shell completion for bash, zsh, or fish.", "stackblaze completion bash"),
    ("upgrade", "Upgrade", "Self-update the CLI binary from GHCR.", "stackblaze upgrade"),
    ("docs", "Docs", "Open this documentation.", "stackblaze docs"),
    ("billing", "Billing", "Plan, usage, and resource breakdown.", "stackblaze billing"),
    ("audit", "Audit", "Who did what, when (org audit log).", "stackblaze audit"),
    ("diagnose", "Diagnose", "Performance findings and hints for the linked service.", "stackblaze diagnose"),
    ("inspect", "Inspect", "Deployment plan from cwd or a public git URL.", "stackblaze inspect"),
    ("wait", "Wait", "Poll until the service and add-ons are running.", "stackblaze wait"),
    ("scale", "Scale", "Set replica count. `0` pauses.", "stackblaze scale --replicas 2"),
    ("restart", "Restart", "Rolling restart without a new build.", "stackblaze restart"),
    ("redeploy", "Redeploy", "Redeploy the current (or `--tag`) image.", "stackblaze redeploy"),
    ("list", "List", "List projects. Alias of `pipelines list`.", "stackblaze list"),
    ("context", "Context", "Show resolved API URL and link scope.", "stackblaze context"),
    ("setup", "Setup", "Wire MCP, skills, or agent into your editor.", "stackblaze setup mcp"),
]

for slug, title, summary, example in CLI_COMMANDS:
    w(
        f"cli/{slug}.mdx",
        f"""---
title: {title}
description: stackblaze {slug}
---

{summary}

```bash
{example}
```

Global flags on most commands: `--pipeline`, `--phase`, `--app`, `--token`, `--api-url`, `--json`.

See [CLI](/cli/) for install and login. Tokens use the `kbr_pat_` prefix (or the token `stackblaze login` stores).
""",
    )


print("done")
