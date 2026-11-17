# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

The adminout.net marketing site plus Lance's resume/portfolio. Nuxt 3 (Vue 3, TypeScript) styled with Bulma 0.9 and SCSS, deployed as a Cloudflare Worker. Despite the repo name, it is not served by GitHub Pages.

## Commands

```bash
npm install        # also runs `nuxt prepare` (postinstall)
npm run dev        # dev server on http://localhost:3000
npm run lint       # ESLint (@nuxtjs/eslint-config-typescript + Prettier) over .ts/.js/.vue
npm run build      # production build into .output/ (Nitro preset: cloudflare-module)
npm run preview    # serve the production build locally
```

There is no test suite. `npm run lint` is the only CI gate, so run it before pushing. Prettier formatting is enforced through ESLint (`plugin:prettier/recommended`), so `npx eslint --fix <file>` fixes formatting.

CI and the deploy pipeline use Node 18.

## Branches and deployment

GitHub Actions, driven by branch name (`.github/workflows/`):

- any branch other than `main`/`staging`: lint only
- `staging`: lint, then deploy to `staging.adminout.net`
- `main`: lint, then deploy to `adminout.net`

The usual flow is feature branch → PR into `staging` → PR `staging` into `main`. Deploys run `wrangler deploy --env <staging|production>` using `wrangler.toml`; the static assets are served from `.output/public` as a Workers site bucket.

`robots.txt` is per environment: the deploy action copies `robots.<env>.txt` into `public/robots.txt` at build time (staging disallows all crawlers). Edit the `robots.*.txt` files at the repo root; `public/robots.txt` is not tracked and is overwritten on deploy.

## Architecture

- `pages/index.vue`: the company landing page (services, clients, contact section). It uses the `default` layout (`NavBar`, `BackToTop`, `AppFooter`).
- `pages/resume/cv.vue` and `pages/resume/portfolio.vue`: the personal resume. Both set `definePageMeta({ layout: "resume" })` and wrap their content in `<NuxtLayout>`. `layouts/resume.vue` renders the profile hero (name, title, bio, photo) and the Resume/Portfolio tabs, then the page content in its slot. The hero bio is shared by both resume pages, so edit it there.
- Content is hard-coded in the templates; there is no CMS or data file. Work-history entries in `cv.vue` and project cards in `portfolio.vue` are repeated Bulma `card` blocks laid out two per `columns` row. Date ranges and durations (for example "2017 to Present (6 years, 4 months)") are literal strings and go stale, so recompute them when touching those entries.
- `app.vue` sets the global `<html lang>`, the `%s | Adminout` title template and the default meta description; each page sets its own `useHead` title and description.
- Styling: `assets/scss/variables.scss` sets the Bulma overrides (`$primary`, `$light`, font family) and is imported before Bulma in `assets/scss/main.scss`, the single global stylesheet registered in `nuxt.config.ts`. Scoped page styles `@import "@/assets/scss/variables"` to reuse those tokens. The `Ming` display font (`assets/font/`) is used via the `.logo-font` class.
- Images live under `assets/img/` (`clients/`, `portfolio/`, `resume/`, `languages/`) and are referenced as `~assets/img/...` so Vite bundles them. Prefer `.webp`, and set explicit `width`/`height` on `<img>`.
- `server/api/contact.post.ts` is a stub that echoes the request body. The contact form on the landing page is not wired to it and sends nothing.
