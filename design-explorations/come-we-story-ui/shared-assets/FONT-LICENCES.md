# Fonts used in the design explorations

All four are licensed under the **SIL Open Font License 1.1**, which permits embedding,
self-hosting and commercial use. No licensing cost, no per-domain restriction.

| Family | Role | Used by | Designer / foundry |
|---|---|---|---|
| **Fraunces** | display — questions, headings | Option 1 (Story Press) | Undercase Type (Phaedra Charles, Flavia Zimbardi) |
| **Archivo** | display — questions, headings | Option 2 (Late Night Table) | Omnibus-Type |
| **Instrument Serif** | display — questions, headings | Option 3 (The Deck) | Instrument |
| **Inter** | interface, body, metadata | all three | Rasmus Andersson |

## How they are embedded here

`fonts.css` contains one `@font-face` per face with the woff2 inlined as a `data:` URI, **latin
subset only** (243 KB raw across all five faces). This is a prototyping choice, not a
recommendation: data URIs mean the prototypes render from `file://` with zero network requests, so
the mockups look identical on any machine with no server and no internet.

## How they would ship, if adopted

Not as data URIs. In the real app they would be:

1. Downloaded as `.woff2`, latin subset, and committed under something like `fonts/`.
2. Declared with `@font-face` + `font-display:swap` and a system fallback in the same stack.
3. **Added to the `ASSETS` array in `sw-v2.js`** — this is the step that is easy to forget and
   would silently break offline use, which is the whole point of the app.
4. Cache-busted by bumping the `CACHE` constant in `sw-v2.js`, exactly as the existing
   `come-we-story-v6-ui-refresh` string does.

Budget: one variable display face plus Inter, latin subset, is roughly 110–150 KB — against a
`data/questions.json` that is already 184 KB. It roughly doubles the precache, which is worth
confirming before committing to it.
