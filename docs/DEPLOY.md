# Deploy (D18: Cloudflare Workers)

Config: `wrangler.jsonc` (Worker `speakaustrian`, static assets + SSR worker from `adapter-cloudflare`).

## One-time setup (Andi, ~2 minutes)
1. Cloudflare dashboard → **Workers & Pages** → **Create** → **Import a repository** → `lauhard/speakaustrian`.
2. Leave every field at its default and save. No build command is needed: `wrangler deploy` (the default deploy command) builds the app itself via `build.command` in `wrangler.jsonc`. Production branch is the repo default, `main`.

Every push to `main` deploys; other branches get preview URLs (`preview_urls: true`).

URL after the first deploy: `https://speakaustrian.<account-subdomain>.workers.dev`.

## Manual deploy (optional)
`pnpm run deploy` (needs `wrangler login` once).

## Later
KV / D1 / R2 / Workers AI are added as bindings in `wrangler.jsonc`; each needs a spec decision first (D19, G-007).
