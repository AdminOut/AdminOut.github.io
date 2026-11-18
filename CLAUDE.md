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
- `pages/resume/cv.vue`, `pages/resume/portfolio.vue` and `pages/resume/print.vue`: the personal resume. All three use the `resume` layout, which renders the profile hero (name, headline, contact line, bio, photo) and the tabs. The print page stacks the CV and portfolio for a single "Save as PDF"; print styles live at the end of `assets/scss/main.scss` (`.no-print`, `.print-page-break`).
- All resume content (profile, skills, roles, projects, earlier career and projects) lives in `data/resume.ts`; the pages render it through the `components/resume/` components. Edit content there, not in templates. Roles are listed newest start date first.
- Dates are `"YYYY-MM"` months; a role with no `end` is current. Durations and the bio's years of experience are calculated at render time (`utils/period.ts`), using a render time shared between server and client (`composables/useNow.ts`) so hydration matches. Never type a duration by hand.
- The contact email is stored only as `profile.emailEncoded` (reversed, then base64) and shown by `components/resume/ProtectedEmail.vue` after a click, or when the page is printed. Never put a plain email address, phone number or `mailto:` link into a template, the data or `public/`: the repo is public and the pages are crawlable.
- Portfolio screenshots must show demo or invented data only, cropped to 16:9 webp under `assets/img/portfolio/`. Clients are named only where the work is already public; otherwise describe them by industry.
- `app.vue` sets the global `<html lang>`, the `%s | Adminout` title template and the default meta description; each page sets its own `useHead` title and description.
- Styling: `assets/scss/variables.scss` sets the Bulma overrides (`$primary`, `$light`, font family) and is imported before Bulma in `assets/scss/main.scss`, the single global stylesheet registered in `nuxt.config.ts`. Scoped page styles `@import "@/assets/scss/variables"` to reuse those tokens. The `Ming` display font (`assets/font/`) is used via the `.logo-font` class.
- Images live under `assets/img/` (`clients/`, `portfolio/`, `resume/`, `languages/`) and are referenced as `~assets/img/...` so Vite bundles them. Prefer `.webp`, and set explicit `width`/`height` on `<img>`.
- `server/api/contact.post.ts` is a stub that echoes the request body. The contact form on the landing page is not wired to it and sends nothing.
