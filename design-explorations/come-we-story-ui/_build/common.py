"""Shared content + iconography for the Come We Story design explorations.

Every string in CONTENT is taken verbatim from the working app (index.html,
app-v2.js) or from data/questions.json. Nothing here invents a feature, a
screen or a label that the application does not already have.

The three option modules import from here so that all three directions render
*identical copy* — the only thing that differs between them is the design.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# --------------------------------------------------------------------------
# Copy — verbatim from the working app
# --------------------------------------------------------------------------

BRAND = {
    "eyebrow": "OFFLINE CONVERSATION DECK",     # index.html:19
    "name": "Come We Story",                    # index.html:20
    "meaning": "Hey, let's catch up!",          # index.html:21
}

HOME = {
    "h2": "Choose how the conversation flows",  # index.html:29
    "sub": "Pass the phone, follow a tangent, and let the stories unfold.",
    "resume": "Resume previous session",        # index.html:39
}

# index.html:33-36 — data-mode values are the app's real contract
MODES = [
    ("smart",   "smart",   "Smart Shuffle",         "Varied, but avoids emotional whiplash."),
    ("random",  "dice",    "Pure Random",           "All 750 prompts, fully shuffled."),
    ("journey", "journey", "Conversation Journey",  "Starts light and gradually deepens."),
    ("deck",    "deck",    "Browse by Deck",        "Choose one theme and shuffle within it."),
]

# app-v2.js:2 — the 15 real categories, in dataset order. 50 prompts each.
# icon = the drawn replacement for the current emoji; hue = deck colour token.
DECKS = [
    ("Light & Funny",                              "light-funny",    "sun"),
    ("Catch-up",                                   "catch-up",       "clay"),
    ("Memories & Family",                          "memories",       "rose"),
    ("Would You Rather",                           "wyr",            "indigo"),
    ("Remove One",                                 "remove-one",     "slate"),
    ("Hot Takes",                                  "hot-takes",      "kola"),
    ("London",                                     "london",         "indigo"),
    ("Black British Culture",                      "black-british",  "kola"),
    ("Black American Culture",                     "black-american", "clay"),
    ("Cameroon",                                   "cameroon",       "green"),
    ("West African & Sub-Saharan African Culture", "west-african",   "gold"),
    ("Relationships & Family",                     "relationships",  "rose"),
    ("Career & Money",                             "career",         "green"),
    ("Football & Sport",                           "football",       "green"),
    ("Philosophy & Future",                        "philosophy",     "slate"),
]

CARD_UI = {
    "follow_show": "Reveal follow-up",          # index.html:50
    "follow_hide": "Hide follow-up",            # app-v2.js:32
    "pass": "You can always pass without explaining.",   # index.html:52
    "prev": "Previous",                         # index.html:55
    "fav": "Favourite",                         # index.html:56
    "faved": "Favourited",                      # app-v2.js:9
    "next": "Next",                             # index.html:57
    "modes": "Modes",                           # index.html:60
    "reset": "Reset",                           # index.html:61
}

# Real prompts from data/questions.json.
CARD = {
    "deck": "Black American Culture",
    "icon": "black-american",
    "hue": "clay",
    "type": "question",
    "q": "Which Black American sports moment had the greatest cultural significance?",
    "follow": "What would the world look like without it?",
    "n": 1,
    "total": 750,
}

CARD_ALT = {
    "deck": "Memories & Family",
    "icon": "memories",
    "hue": "rose",
    "type": "story",
    "q": "What childhood meal immediately feels like home?",
    "follow": "Who made the best version?",
    "n": 14,
    "total": 50,
}

CARD_WYR = {
    "deck": "Would You Rather",
    "icon": "wyr",
    "hue": "indigo",
    "type": "would you rather",
    "q": "Would you rather take one first-class trip every five years, or two economy "
         "trips every year—with the same total holiday time?",
    "follow": "Do you value comfort, frequency, or the memories created?",
    "n": 7,
    "total": 50,
}

CARD_CMR = {
    "deck": "Cameroon",
    "icon": "cameroon",
    "hue": "green",
    "type": "question",
    "q": "Which Cameroonian dish deserves the widest global recognition?",
    "follow": "What would make it accessible without diluting it?",
    "n": 3,
    "total": 50,
}

# States. The loading/end-of-deck copy is *proposed* (the app has none today);
# the error copy is the app's real string from app-v2.js:30.
STATES = {
    "loading": ("Shuffling 750 prompts…", "One moment — this only happens once, then it works offline."),
    "error": ("The question deck could not be loaded.", "Please refresh while online once."),
    "end_title": "That's the whole deck.",
    "end_body": "You reached prompt 750 of 750. Reshuffle, switch decks, or keep talking — "
                "the best conversations usually carry on without the cards.",
    "saved": "Saved to your favourites",
}


# --------------------------------------------------------------------------
# Icon system — replaces the platform-dependent emoji in app-v2.js:2
# 24x24 grid, 1.6 stroke, currentColor, no fills except where noted.
# --------------------------------------------------------------------------

_P = {
    # deck icons
    "light-funny":    '<circle cx="12" cy="12" r="8.6"/><path d="M7.6 13.4a4.9 4.9 0 0 0 8.8 0"/>'
                      '<path d="M8.7 9.3h.01M15.3 9.3h.01" stroke-width="2.4"/>',
    "catch-up":       '<path d="M4.6 9.9h11.2v5.2a4.2 4.2 0 0 1-4.2 4.2H8.8a4.2 4.2 0 0 1-4.2-4.2z"/>'
                      '<path d="M15.8 11.2h1.6a2.4 2.4 0 0 1 0 4.8h-1.6"/>'
                      '<path d="M8.2 6.9c0-1.1 1.1-1.3 1.1-2.4M11.9 6.9c0-1.1 1.1-1.3 1.1-2.4"/>',
    "memories":       '<rect x="3.4" y="4.6" width="17.2" height="14.8" rx="1.8"/>'
                      '<path d="M3.4 15.6l4.3-4.2 3.4 3.4 3.1-3 6.4 6.2"/><circle cx="8.4" cy="9" r="1.4"/>',
    "wyr":            '<path d="M12 20.2v-4.8"/><path d="M12 15.4L7.1 10.5V5.4M12 15.4l4.9-4.9V5.4"/>'
                      '<path d="M5.1 7.4l2-2 2 2M14.9 7.4l2-2 2 2"/>',
    "remove-one":     '<rect x="3.8" y="3.8" width="6.6" height="6.6" rx="1.3"/>'
                      '<rect x="13.6" y="3.8" width="6.6" height="6.6" rx="1.3"/>'
                      '<rect x="3.8" y="13.6" width="6.6" height="6.6" rx="1.3"/>'
                      '<path d="M14.6 14.6l4.6 4.6M19.2 14.6l-4.6 4.6"/>',
    "hot-takes":      '<path d="M12 20.8c3.5 0 5.9-2.3 5.9-5.5 0-3.6-2.7-5.6-3.7-8.9-.2-.7-1.1-.8-1.4-.1-.8 1.8-2 2.7-3.4 4.1-1.6 1.6-3.3 3-3.3 4.9 0 3.2 2.4 5.5 5.9 5.5z"/>'
                      '<path d="M12 20.8c1.7 0 2.9-1.1 2.9-2.7 0-1.7-1.4-2.6-1.9-4-.7 1-2.9 2-2.9 4 0 1.6.8 2.7 1.9 2.7z"/>',
    "london":         '<circle cx="12" cy="12" r="6.9"/><path d="M2.9 12h18.2"/>',
    "black-british":  '<rect x="5.2" y="3.4" width="13.6" height="17.2" rx="1.8"/>'
                      '<circle cx="12" cy="9.2" r="2.9"/><circle cx="12" cy="16.2" r="1.7"/>',
    "black-american": '<circle cx="12" cy="12" r="8.6"/><circle cx="12" cy="12" r="2.7"/>'
                      '<path d="M12 11.9h.01" stroke-width="2.2"/>',
    "cameroon":       '<path d="M12 3.4l2.5 5.1 5.6.8-4.1 4 1 5.6L12 16.2l-5 2.7 1-5.6-4.1-4 5.6-.8z"/>',
    "west-african":   '<path d="M3.6 20V15h5v-5h5V5h5.8"/><path d="M3.6 20h4M19.4 5v4.4"/>',
    "relationships":  '<circle cx="9.1" cy="12" r="5.3"/><circle cx="14.9" cy="12" r="5.3"/>',
    "career":         '<rect x="2.9" y="7.3" width="18.2" height="12.3" rx="2"/>'
                      '<path d="M8.9 7.3V5.8a2 2 0 0 1 2-2h2.2a2 2 0 0 1 2 2v1.5"/><path d="M2.9 13h18.2"/>',
    "football":       '<circle cx="12" cy="12" r="8.6"/><path d="M12 7.1l3.5 2.6-1.4 4.2H9.9L8.5 9.7z"/>'
                      '<path d="M12 3.4v3.7M20.2 9.9l-4.7-.2M3.8 9.9l4.7-.2M14.4 14l2.6 3.3M9.6 14L7 17.3"/>',
    "philosophy":     '<circle cx="12" cy="12" r="4.1"/>'
                      '<ellipse cx="12" cy="12" rx="9.6" ry="4.1" transform="rotate(-24 12 12)"/>',
    # mode icons
    "smart":          '<path d="M3.4 7.6h3.3c1.5 0 2.3.9 3 2.2l2.9 5.4c.7 1.3 1.5 2.2 3 2.2h3.6"/>'
                      '<path d="M17.2 15l3 2.4-3 2.4"/><path d="M3.4 17.4h3.3c1.3 0 2-.6 2.7-1.6"/>'
                      '<path d="M14 9.8c.7-1.3 1.5-2.2 3-2.2h3.2"/><path d="M17.2 5.2l3 2.4-3 2.4"/>',
    "dice":           '<rect x="3.6" y="3.6" width="16.8" height="16.8" rx="3.6"/>'
                      '<path d="M8.6 8.6h.01M12 12h.01M15.4 15.4h.01" stroke-width="2.6"/>',
    "journey":        '<path d="M3.4 19c4.4 0 4.1-3.6 8.2-3.6S15.4 6.6 20.4 6.6"/>'
                      '<path d="M17.4 4.2l3 2.4-3 2.4"/>',
    "deck":           '<rect x="8.2" y="3.6" width="12.2" height="16.8" rx="2.2"/>'
                      '<path d="M4.6 6.8v11.6a2.4 2.4 0 0 0 2.4 2.4h9"/>',
    # ui icons
    "moon":           '<path d="M20.4 14.8A8.8 8.8 0 1 1 9.4 3.6a7.1 7.1 0 0 0 11 11.2z"/>',
    "sun":            '<circle cx="12" cy="12" r="4.2"/>'
                      '<path d="M12 2.4v2.6M12 19v2.6M2.4 12h2.6M19 12h2.6M5.2 5.2l1.9 1.9M16.9 16.9l1.9 1.9M18.8 5.2l-1.9 1.9M7.1 16.9l-1.9 1.9"/>',
    "heart":          '<path d="M12 20.4S3.6 15.6 3.6 9.9a4.6 4.6 0 0 1 8.4-2.6 4.6 4.6 0 0 1 8.4 2.6c0 5.7-8.4 10.5-8.4 10.5z"/>',
    "arrow-left":     '<path d="M19 12H5"/><path d="M10.6 5.6L4.2 12l6.4 6.4"/>',
    "arrow-right":    '<path d="M5 12h14"/><path d="M13.4 5.6L19.8 12l-6.4 6.4"/>',
    "refresh":        '<path d="M20.2 12a8.2 8.2 0 1 1-2.6-6"/><path d="M20.4 4.2v5h-5"/>',
    "alert":          '<path d="M12 3.8L21.4 20H2.6z"/><path d="M12 10v4.4M12 17.4h.01" stroke-width="2.2"/>',
    "check":          '<circle cx="12" cy="12" r="8.8"/><path d="M8 12.2l2.8 2.8L16.4 9.4"/>',
    "close":          '<path d="M5.6 5.6l12.8 12.8M18.4 5.6L5.6 18.4"/>',
    "chevron":        '<path d="M8.6 4.6L16 12l-7.4 7.4"/>',
    "search":         '<circle cx="10.8" cy="10.8" r="6.6"/><path d="M15.6 15.6l4.6 4.6"/>',
}


def sprite() -> str:
    """One inline SVG sprite per page — inlined rather than referenced so the
    prototypes work from file:// with zero network requests."""
    syms = "".join(
        f'<symbol id="i-{k}" viewBox="0 0 24 24">{v}</symbol>' for k, v in _P.items()
    )
    return (
        '<svg class="sprite" aria-hidden="true" focusable="false" width="0" height="0" '
        'style="position:absolute" fill="none" stroke="currentColor" stroke-width="1.6" '
        f'stroke-linecap="round" stroke-linejoin="round">{syms}</svg>'
    )


def icon(name: str, cls: str = "") -> str:
    c = f' class="ico {cls}"' if cls else ' class="ico"'
    return f'<svg{c} aria-hidden="true"><use href="#i-{name}"/></svg>'


# --------------------------------------------------------------------------
# Page scaffolding
# --------------------------------------------------------------------------

def page(title: str, css_files, body: str, body_class: str = "", extra_head: str = "") -> str:
    links = "\n  ".join(f'<link rel="stylesheet" href="{c}">' for c in css_files)
    bc = f' class="{body_class}"' if body_class else ""
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
  <title>{title}</title>
  {links}{extra_head}
</head>
<body{bc}>
{sprite()}
{body}
</body>
</html>
"""


def deck_count(name: str) -> int:
    return 50  # every deck in data/questions.json holds exactly 50 prompts


def write(rel: str, text: str) -> None:
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    print(f"  wrote {rel} ({len(text)/1024:.1f} KB)")
