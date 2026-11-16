# Deploy (D18: Cloudflare Workers)

Config: `wrangler.jsonc` (Worker `speakaustrian`, static assets + SSR worker from `adapter-cloudflare`).

## One-time setup (Andi, ~3 minutes)
1. Cloudflare dashboard → **Workers & Pages** → **Create** → **Import a repository** → `lauhard/speakaustrian`.
2. Build command: `pnpm build` · Deploy command: `npx wrangler deploy` · Production branch: `main`.
3. Save. Every push to `main` deploys; other branches get preview URLs (`preview_urls: true`).

URL after the first deploy: `https://speakaustrian.<account-subdomain>.workers.dev`.

## Manual deploy (optional)
`pnpm deploy` (needs `wrangler login` once).

## Later
KV / D1 / R2 / Workers AI are added as bindings in `wrangler.jsonc`; each needs a spec decision first (D19, G-007).
