# Comparing the three directions

Ratings are relative to each other, not absolute. ●●●●● is strongest.

| Criterion | 1 · Story Press | 2 · Late Night Table | 3 · The Deck |
|---|---|---|---|
| **Brand distinctiveness** | ●●●●● letterpress + weave is unlike any conversation app | ●●●○○ premium, but "tasteful dark app" is a crowded look | ●●●●● nobody else looks like a felt table |
| **Emotional warmth** | ●●●●● paper, warm ink, italic asides | ●●●○○ intimate but cool; can read as moody | ●●●●○ playful and inviting, slightly more game than gathering |
| **Storytelling suitability** | ●●●●● the question reads like a printed headline | ●●●●○ strong focus, one thing lit | ●●●○○ card framing competes with the words |
| **Cultural authenticity** | ●●●●● strip-weave, kola/indigo/palm, market-print type | ●●○○○ carries none of it in the shell | ●●●○○ carried by the 15 deck backs only |
| **Content readability** | ●●●●● dark ink on warm paper, generous measure | ●●●●○ excellent, but long sessions on OLED at night | ●●●○○ centred serif is the least comfortable for long prompts |
| **Accessibility** | ●●●●● highest contrast, no colour-only meaning | ●●●●○ strong, needs care on amber-on-dark small text | ●●●○○ centred text + rotated index marks need SR handling |
| **Mobile suitability** | ●●●●○ needs the fixed bar to stay thumb-reachable | ●●●●● dock-first design was built for one hand | ●●●●○ stack is lovely, costs vertical space |
| **Ease of implementation** | ●●●●● maps almost 1:1 onto the current DOM | ●●●●○ dock is a new wrapper, otherwise a token swap | ●●○○○ stack, backs and index marks need new markup |
| **Regression risk** | ●●●●● token + CSS only | ●●●●○ control repositioning touches layout | ●●○○○ most new DOM, most chance of breaking `render()` |
| **Maintainability** | ●●●●● small radius/keyline system, few moving parts | ●●●●○ one colour system, two themes | ●●●○○ pattern + hue matrix across 15 decks |
| **Long-term scalability** | ●●●●● rail absorbs new nav; editorial scales to any content | ●●●●○ chip rail scales; dark-only constrains marketing pages | ●●●○○ every new content type must become "a card" |
| **Supports new features** | ●●●●● favourites list, search, filters all fit the rail | ●●●●○ fits, needs a home for secondary nav | ●●○○○ awkward for lists, settings, long-form |
| **Visual uniqueness** | ●●●●● | ●●●○○ | ●●●●● |
| **Fit with current codebase** | ●●●●● one CSS file, same class hooks | ●●●●○ | ●●○○○ |

## Where each one wins

**Story Press** is the only direction that answers *why this app is called Come We Story*. The
identity comes from somewhere specific rather than from a colour picker, and it does it with flat
colour and type — which happens to also be the cheapest and lowest-risk thing to build on top of a
single 15-line stylesheet.

**Late Night Table** is the best pure *reading* environment and the best one-handed design. Its
control dock is genuinely better than the other two, and its instinct about when the app is used is
correct.

**The Deck** has the single best idea in the whole exploration: **15 decks as 15 recognisable card
backs**. It turns a text list into objects you can learn and recognise. It is also the most
expensive to build and the least comfortable for reading long prompts.

## Recommendation

**Story Press**, with two things borrowed:

1. **The control dock from Late Night Table.** Fixed to the bottom on mobile, Next as the widest
   target, DOM order matching visual order. This fixes a real WCAG 2.4.3 problem in the current
   build, where the DOM order is prev → fav → next but the ≤420px visual order is next → prev → fav.
2. **The deck backs from The Deck**, scaled down — not as full portrait cards, but as the woven
   deck-coloured spine and emblem already in Story Press, with the pattern reserved for the deck
   picker. Deck identity without the cost of a card-stack layout.

Story Press's dark theme should also take Late Night Table's warm-white-on-warm-black approach
rather than inverting to grey — pure `#fff` text on `#111` is the one thing the current dark theme
gets slightly wrong.

## First screen to build

**The card reading screen** (`card.html`). It is the screen users spend ~95% of their time on, it
exercises every token in the system (surface, type scale, deck colour, buttons, focus, states), and
it can be restyled without touching a single line of `app-v2.js` — the JS only ever sets
`textContent` and toggles the `hidden` class on elements it finds by ID.
