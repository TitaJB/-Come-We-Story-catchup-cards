"""Option 3 — "The Deck". Page markup."""

from common import (BRAND, HOME, MODES, DECKS, CARD_UI, CARD, CARD_ALT,
                    STATES, icon, page, write)

CSS = ["../shared-assets/fonts.css", "theme.css"]
DIR = "option-3-the-deck"

MODE_HUE = ["kola", "slate", "green", "gold"]


def topbar(theme_icon="moon"):
    return f"""
<header class="topbar">
  <a class="skip" href="#main">Skip to content</a>
  <div class="brand">
    <div class="brand__mark back hue-kola">{icon('deck')}</div>
    <div>
      <p class="brand__eyebrow">{BRAND['eyebrow']}</p>
      <h1 class="brand__name">{BRAND['name']}</h1>
    </div>
  </div>
  <div class="topbar__spacer"></div>
  <p class="brand__meaning">{BRAND['meaning']}</p>
  <button class="iconbtn" aria-label="Switch to dark theme">{icon(theme_icon)}</button>
</header>"""


def modes(expanded=None, hover="smart"):
    out = []
    for i, (key, ico, title, desc) in enumerate(MODES):
        cls = f"mode hue-{MODE_HUE[i]}"
        attrs = ""
        if key == hover:
            cls += " is-hover"
        if key == "deck":
            attrs = f' aria-expanded="{"true" if expanded=="deck" else "false"}" aria-controls="deckgrid"'
        out.append(f"""
    <button class="{cls}"{attrs}>
      <span class="mode__pip">{icon(ico)}</span>
      <span class="mode__idx">{i+1}</span>
      <span class="mode__t">{title}</span>
      <span class="mode__rule"></span>
      <span class="mode__d">{desc}</span>
    </button>""")
    return f'<div class="modes">{"".join(out)}</div>'


def deckgrid(selected=None, hover="London"):
    out = []
    for name, ico, hue in DECKS:
        cls = f"deck hue-{hue}"
        if name == selected:
            cls += " is-selected"
        elif name == hover:
            cls += " is-hover"
        out.append(f"""
    <button class="{cls}">
      <span class="deck__back back"><span class="deck__emblem">{icon(ico)}</span></span>
      <span class="deck__n">{name}</span>
      <span class="deck__c">50 prompts</span>
    </button>""")
    return f'<div class="deckgrid" id="deckgrid">{"".join(out)}</div>'


def card(c=CARD, follow_open=True, faved=False):
    follow = ""
    if follow_open:
        follow = f'<p class="follow">{c["follow"]}</p><span class="hairline"></span>'
    btn = CARD_UI["follow_hide"] if follow_open else CARD_UI["follow_show"]
    pct = max(int(c["n"] / c["total"] * 100), 2)
    fav_cls = "btn btn--fav is-on" if faved else "btn btn--fav"
    fav_txt = CARD_UI["faved"] if faved else CARD_UI["fav"]
    idx = f'<span class="index__n">{c["n"]}</span>{icon(c["icon"])}'
    return f"""
<div class="hue-{c['hue']}">
  <div class="cardmeta">
    <span class="deckchip">{icon(c['icon'])}{c['deck']}</span>
    <span class="progress">
      <span class="progress__bar"><span class="progress__fill" style="width:{pct}%"></span></span>
      {c['n']} / {c['total']}
    </span>
  </div>

  <div class="stack">
    <div class="stack__under stack__under--2" aria-hidden="true"></div>
    <div class="stack__under stack__under--1" aria-hidden="true"></div>
    <article class="card" aria-live="polite">
      <span class="index index--tl" aria-hidden="true">{idx}</span>
      <span class="index index--br" aria-hidden="true">{idx}</span>
      <div class="card__inner">
        <span class="typemark">{c['type']}</span>
        <h2 class="question">{c['q']}</h2>
        <span class="hairline"></span>
        <button class="followbtn">{icon('refresh')}{btn}</button>
        {follow}
        <p class="pass">{CARD_UI['pass']}</p>
      </div>
    </article>
  </div>

  <div class="controls">
    <button class="btn" aria-label="{CARD_UI['prev']}">{icon('arrow-left')}</button>
    <button class="{fav_cls}" aria-pressed="{'true' if faved else 'false'}" aria-label="{fav_txt}">{icon('heart')}</button>
    <button class="btn btn--primary btn--lg">{CARD_UI['next']}{icon('arrow-right')}</button>
  </div>
  <div class="subcontrols">
    <button class="btn btn--quiet">{icon('deck')}{CARD_UI['modes']}</button>
    <button class="btn btn--quiet">{icon('refresh')}{CARD_UI['reset']}</button>
  </div>
</div>"""


def build():
    # ---- home ----
    body = f"""
<div class="app">
{topbar()}
  <main class="main" id="main">
    <div class="pagehead">
      <h1>{HOME['h2']}</h1>
      <p>{HOME['sub']}</p>
    </div>
    {modes(hover='smart')}
    <p class="sectionlabel">Pick up where you left off</p>
    <button class="btn">{icon('refresh')}{HOME['resume']}</button>
  </main>
</div>
<div class="note">Option 3 · The Deck · Home</div>"""
    write(f"{DIR}/home.html", page("Come We Story — Home · The Deck", CSS, body))

    # ---- decks ----
    body = f"""
<div class="app">
{topbar()}
  <main class="main" id="main">
    <div class="pagehead">
      <h1>{HOME['h2']}</h1>
      <p>{HOME['sub']}</p>
    </div>
    {modes(expanded='deck', hover=None)}
    <p class="sectionlabel">Choose a deck · 15 decks · 50 prompts each</p>
    {deckgrid(selected='Cameroon', hover='London')}
  </main>
</div>
<div class="note">Option 3 · The Deck · Browse by Deck</div>"""
    write(f"{DIR}/decks.html", page("Come We Story — Decks · The Deck", CSS, body))

    # ---- card ----
    body = f"""
<div class="app">
{topbar()}
  <main class="main main--narrow main--stage" id="main">
    {card(CARD, follow_open=True, faved=False)}
  </main>
</div>
<div class="note">Option 3 · The Deck · Reading a prompt</div>"""
    write(f"{DIR}/card.html", page("Come We Story — Prompt · The Deck", CSS, body))

    # ---- dark ----
    body = f"""
<div class="app">
{topbar('sun')}
  <main class="main main--narrow main--stage" id="main">
    {card(CARD_ALT, follow_open=False, faved=True)}
  </main>
</div>
<div class="note">Option 3 · The Deck · Dark theme</div>"""
    write(f"{DIR}/card-dark.html", page("Come We Story — Dark · The Deck", CSS, body,
                                        extra_head='\n  <script>document.documentElement.dataset.theme="dark"</script>'))

    # ---- states ----
    ld_t, ld_b = STATES["loading"]
    er_t, er_b = STATES["error"]
    body = f"""
<div class="app">
{topbar()}
  <main class="main main--narrow" id="main">
    <div class="pagehead"><h1>Interface states</h1>
    <p>Every state the app can reach today, plus the three it is missing: loading,
    end-of-deck and a confirmation for Favourite.</p></div>

    <p class="sectionlabel">Loading — currently missing</p>
    <div class="state">
      <div class="dealer"><i class="back hue-kola"></i><i class="back hue-indigo"></i><i class="back hue-green"></i><i class="back hue-gold"></i></div>
      <h3>{ld_t}</h3><p>{ld_b}</p>
    </div>

    <p class="sectionlabel">Loading — card skeleton</p>
    <div class="state" style="gap:14px">
      <div class="skel" style="width:88px;height:12px"></div>
      <div style="width:100%">
        <div class="skel skel--line" style="width:82%;height:26px"></div>
        <div class="skel skel--line" style="width:66%;height:26px"></div>
        <div class="skel skel--line" style="width:44%;height:26px"></div>
      </div>
      <div class="skel" style="width:140px;height:14px"></div>
    </div>

    <p class="sectionlabel">Error — the app's real message</p>
    <div class="state state--error">
      <div class="state__ico">{icon('alert')}</div>
      <h3>{er_t}</h3><p>{er_b}</p>
      <div class="state__actions">
        <button class="btn btn--primary">{icon('refresh')}Try again</button>
        <button class="btn">Use the two offline decks</button>
      </div>
    </div>

    <p class="sectionlabel">Inline alert</p>
    <div class="alert">{icon('alert')}<p><strong>Showing 100 prompts, not 750.</strong>
    The full deck could not be loaded, so Light &amp; Funny and Catch-up are being used.</p></div>

    <p class="sectionlabel">End of deck — currently missing</p>
    <div class="state state--end">
      <div class="state__ico">{icon('check')}</div>
      <h3>{STATES['end_title']}</h3><p>{STATES['end_body']}</p>
      <div class="state__actions">
        <button class="btn btn--primary">{icon('refresh')}Reshuffle</button>
        <button class="btn">{icon('deck')}Choose another deck</button>
      </div>
    </div>

    <p class="sectionlabel">Success confirmation</p>
    <div style="text-align:center"><span class="toast">{icon('heart')}{STATES['saved']}</span></div>

    <p class="sectionlabel">Button states</p>
    <div style="display:flex;gap:12px;flex-wrap:wrap;align-items:center">
      <button class="btn btn--primary">Default</button>
      <button class="btn btn--primary is-hover">Hover</button>
      <button class="btn btn--primary is-focus">Focus</button>
      <button class="btn">Secondary</button>
      <button class="btn is-hover">Hover</button>
      <button class="btn is-focus">Focus</button>
      <button class="btn is-disabled">Disabled</button>
      <button class="btn btn--fav is-on" aria-pressed="true">{icon('heart')}Favourited</button>
      <button class="btn btn--quiet">Quiet</button>
    </div>

    <p class="sectionlabel">Deck card-back states</p>
    <div class="deckgrid" style="grid-template-columns:repeat(4,1fr)">
      <button class="deck hue-indigo"><span class="deck__back back"><span class="deck__emblem">{icon('london')}</span></span><span class="deck__n">London</span><span class="deck__c">Default</span></button>
      <button class="deck hue-kola is-hover"><span class="deck__back back"><span class="deck__emblem">{icon('hot-takes')}</span></span><span class="deck__n">Hot Takes</span><span class="deck__c">Hover</span></button>
      <button class="deck hue-green is-selected"><span class="deck__back back"><span class="deck__emblem">{icon('cameroon')}</span></span><span class="deck__n">Cameroon</span><span class="deck__c">Selected</span></button>
      <button class="deck hue-rose"><span class="deck__back back is-focus"><span class="deck__emblem">{icon('memories')}</span></span><span class="deck__n">Memories &amp; Family</span><span class="deck__c">Focus</span></button>
    </div>
  </main>
</div>
<div class="note">Option 3 · The Deck · States</div>"""
    write(f"{DIR}/states.html", page("Come We Story — States · The Deck", CSS, body))

    # ---- index ----
    sw = "".join(
        f'<div style="flex:1;min-width:104px"><div style="height:64px;background:{h};'
        f'border-radius:8px;border:1px solid rgba(255,255,255,.2)"></div>'
        f'<div style="font-size:11px;margin-top:6px;font-weight:600">{n}</div>'
        f'<div style="font-size:11px;color:var(--onfelt-2);font-family:ui-monospace,monospace">{h}</div></div>'
        for n, h in [("Felt", "#1F4739"), ("Card face", "#FCFAF4"), ("Card edge", "#E3DACA"),
                     ("Ink", "#171514"), ("Suit red", "#C0341F"), ("Suit black", "#22201E"),
                     ("Foil", "#D9A441")])
    body = f"""
<div class="app">
{topbar()}
  <main class="main main--narrow" id="main">
    <div class="pagehead"><h1>The Deck</h1>
    <p>It is a deck of cards, so build it like one. A felt table, a stack with visible depth,
    portrait cards with corner index marks, and a woven back per deck so all fifteen become
    recognisable objects rather than fifteen rows of text.</p></div>

    <p class="sectionlabel">Screens</p>
    {modes(hover=None)}
    <div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:20px">
      <a class="btn" href="home.html">Home</a>
      <a class="btn" href="decks.html">Browse by Deck</a>
      <a class="btn" href="card.html">Reading a prompt</a>
      <a class="btn" href="card-dark.html">Dark theme</a>
      <a class="btn" href="states.html">States</a>
    </div>

    <p class="sectionlabel">Palette</p>
    <div style="display:flex;gap:10px;flex-wrap:wrap">{sw}</div>

    <p class="sectionlabel">Type specimen</p>
    <p style="font-family:var(--display);font-size:3rem;line-height:1.06;max-width:16ch;color:var(--face)">
      Which Black American sports moment had the greatest cultural significance?</p>
    <p style="margin-top:16px;color:var(--onfelt-2);max-width:52ch">
      Instrument Serif for the prompt itself — a high-contrast display serif that reads like
      something printed on card stock rather than rendered in an app. Inter for interface,
      metadata and controls.</p>

    <p class="sectionlabel">The fifteen decks</p>
    {deckgrid(selected=None, hover=None)}
  </main>
</div>"""
    write(f"{DIR}/index.html", page("The Deck — Option 3", CSS, body))
