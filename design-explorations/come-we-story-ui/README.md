# Come We Story — UI design explorations

Three visual directions for the existing app, built as **isolated static prototypes**.

> **Nothing in here is wired into the application.** No file outside
> `design-explorations/` was created, edited, renamed or deleted. The app is served as static
> files from the repository root, so this folder cannot affect the build, the routing or the
> service-worker cache (`sw-v2.js` precaches an explicit `ASSETS` list — this folder is not on it).

## Look at it

Open any of these directly in a browser — no server, no build, no dependencies:

```
option-1-story-press/index.html
option-2-late-night-table/index.html
option-3-the-deck/index.html
```

Or start with the side-by-side comparison images in `shared-assets/screens/`.

## The three directions

| | Concept | Core idea |
|---|---|---|
| **Option 1** | [Story Press](option-1-story-press/index.html) | West African market-print / letterpress editorial. Flat ink on paper, keylines instead of shadows, a woven strip as the brand signature and a solid deck-coloured spine on each card. Desktop gets a persistent deck rail. |
| **Option 2** | [Late Night Table](option-2-late-night-table/index.html) | Dark-first. The deck is played in the evening, so the interface is a dark room with one warm lamp on the card. Colour-coded deck chips, a fixed control dock, Archivo set tight. |
| **Option 3** | [The Deck](option-3-the-deck/index.html) | It *is* a deck of cards. Felt table, a stack with visible depth, portrait cards with corner index marks, and a woven card back per deck so all fifteen become recognisable objects. |

Each direction contains the same five pages so they can be compared fairly:

- `home.html` — mode chooser (Smart Shuffle / Pure Random / Conversation Journey / Browse by Deck)
- `decks.html` — Browse by Deck expanded, all 15 decks
- `card.html` — reading a prompt, follow-up revealed
- `card-dark.html` — the opposite theme, plus the Favourited state
- `states.html` — loading, error, end-of-deck, alert, toast, and every button/deck interaction state
- `index.html` — palette, type specimen, deck iconography, links to the above

## What is real and what is proposed

Everything is grounded in the current app. Specifically:

**Taken verbatim from the codebase** — the brand line "OFFLINE CONVERSATION DECK", the name, the
tagline "Hey, let's catch up!", the heading "Choose how the conversation flows", all four mode
titles and descriptions, all 15 deck names, "Reveal follow-up" / "Hide follow-up", "You can always
pass without explaining.", Previous / Favourite / Next / Modes / Reset, "Resume previous session",
and the error message. Sources are cited inline in `_build/common.py`.

**Prompts** are real records from `data/questions.json` (`q0401` and others) — no placeholder copy.

**Proposed, and labelled as such** — the loading state, the end-of-deck state and the Favourite
confirmation toast. The app has none of these today; they are shown because the review recommends
adding them, not because they exist.

**Deliberately not shown** — there is no story-creation, submission, editing, search, profile,
authentication or settings screen in this repository, so none was invented. The deck picker is the
only selection surface the app has, and it is mocked as-is.

## Iconography

The current app uses emoji as deck icons (`app-v2.js:2`). Emoji render differently on every
platform and are the loudest "unstyled" signal in the interface. All three directions replace them
with a drawn 24×24 stroke set, defined once in `_build/common.py` and inlined per page as an SVG
sprite. Four of the marks are specific rather than generic: Black British Culture is a sound-system
speaker stack, Black American Culture a vinyl record, Cameroon the five-pointed star from the flag,
and West African & Sub-Saharan African a stepped Nkyinkyim meander.

## Fonts

`shared-assets/fonts.css` embeds four open-licence faces as base64 data URIs, latin subset only
(243 KB raw). Data URIs are used so the prototypes render from `file://` with **zero network
requests** — verified on every render. See `shared-assets/FONT-LICENCES.md`.

If these were adopted in the app they would be self-hosted `.woff2` files added to the `ASSETS`
array in `sw-v2.js`, not data URIs.

## Rebuilding

The HTML is generated so that all three directions share identical copy — the only difference
between them is the design.

```bash
python3 _build/build.py        # all three
python3 _build/build.py 1 3    # just options 1 and 3
```

Requires nothing but Python 3. The CSS in each `option-*/theme.css` is hand-written and is the
actual deliverable; `_build/` only assembles the markup around it.

Screenshots were captured with the Chromium already present in this environment at
**1440×900** (desktop), **834×1112** (tablet) and **390×844** (mobile).

## Files

```
design-explorations/come-we-story-ui/
├── README.md                     this file
├── comparison.md                 scored comparison + recommendation
├── _build/
│   ├── common.py                 shared copy, deck data, icon sprite, page scaffold
│   ├── build.py                  generator entry point
│   └── opt1.py / opt2.py / opt3.py
├── shared-assets/
│   ├── fonts.css                 embedded open-licence faces
│   ├── FONT-LICENCES.md
│   └── screens/                  rendered comparison sheets
├── option-1-story-press/         theme.css + 6 pages
├── option-2-late-night-table/    theme.css + 6 pages
└── option-3-the-deck/            theme.css + 6 pages
```
