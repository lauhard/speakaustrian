# Content QA (`pnpm qa`)

Checks chapter content against the spec (masterprompt Phase 5 no. 11, `03` Q6/Q8/Q10, `04a` R-T1–R-T3, R-G1, R-K3). Logic: `src/lib/core/qa/checks.ts` (pure, tested in `qa.test.ts`), shell: `scripts/qa/run.ts`. Runs in CI.

```
pnpm qa                        # all chapters, exit 1 on errors
pnpm qa A1-01 --require-pools  # a batch is only done when its chapter has pools and no errors
pnpm qa A1-01 --strict         # warnings fail too: use before the batch goes to review
pnpm qa --file src/lib/core/qa/fixtures/broken.json   # fixture with one defect per check (must fail)
```

Pools of a real chapter go into `src/lib/content/<chapter>-pools.json` = `{ "chapterId", "goals", "pools": { "practice", "test" } }`; `content/index.ts` merges the file if it exists.

| Check | Level (real chapter) | Rule |
|---|---|---|
| `schema` | error | schema, unique ids, `family` = base item of the same pool, goals with title, answer index, ≥ 1 twin |
| `ids.duplicate` | error | item id used in two chapters |
| `pool.size` · `pool.twins` | error | test pool ≥ 60 · every test item ≥ 2 twins (family ≥ 3) |
| `pool.quota` | error | `policy.testComposition` reachable with different twin families per discipline |
| `practice.gate` | error | ≥ 2 readiness blocks without repeats: 2 × quota per discipline |
| `practice.size` | warning | practice part ≈ 40 + 2 blocks = 80 (G-010) |
| `pool.duplicate` | error | same task text twice (practice/test overlap, twin without a new surface) |
| `choice.options` · `test.parts` · `goals.uncovered` | error | duplicate options · test task > 3 parts · chapter goal without item |
| `i18n.blank` · `image.missing` | error | blank `de`/`en`/`tl` · picture file missing |
| `recycling` | error | < 20 % of practice items with `refs`/goals of earlier chapters (first chapter: info, G-011) |
| `vocab.unknown` | warning | word neither in lessons/inventory up to this chapter nor on `src/lib/content/qa-allowlist.json` |
| `variety.de` · `i18n.untranslated` · `pool.family-skill` | warning | German-German form of `03g` · `en`/`tl` equals `de` · twins with different disciplines |

Sandbox chapters (DEMO) get quantity rules and `vocab.unknown` as info only.

## Expected result today (16.11.2026): `0 error(s), 4 warning(s), 31 info`, exit 0
- A1-01: `pools.missing` (info) and 4 × `i18n.untranslated` (verb paradigms repeated in all three languages; fix with the 004b batch).
- DEMO (small on purpose): `pool.size` 12 < 60, 6 × `pool.twins` (1 twin each), `practice.size` 9 < 52, `recycling.na`, 21 × `vocab.unknown` (sandbox texts go beyond A1-01).
- Fixture: 23 errors, 5 warnings, exit 1.
