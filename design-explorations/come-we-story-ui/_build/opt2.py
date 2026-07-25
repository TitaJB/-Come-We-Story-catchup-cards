"""Option 2 — "Late Night Table". Page markup."""

from common import (BRAND, HOME, MODES, DECKS, CARD_UI, CARD, CARD_ALT,
                    STATES, icon, page, write)

CSS = ["../shared-assets/fonts.css", "theme.css"]
DIR = "option-2-late-night-table"

# transit-map style deck colours for this direction
HUE = {
    "Light & Funny": "amber", "Catch-up": "rust", "Memories & Family": "plum",
    "Would You Rather": "sky", "Remove One": "lamp", "Hot Takes": "clay",
    "London": "sky", "Black British Culture": "clay", "Black American Culture": "rust",
    "Cameroon": "sage", "West African & Sub-Saharan African Culture": "amber",
    "Relationships & Family": "plum", "Career & Money": "sage",
    "Football & Sport": "lime", "Philosophy & Future": "lamp",
}


def topbar(theme_icon="sun", narrow=False):
    cls = "topbar topbar--narrow" if narrow else "topbar"
    return f"""
<header class="{cls}">
  <a class="skip" href="#main">Skip to content</a>
  <div class="brand">
    <div class="brand__mark">{icon('deck')}</div>
    <div>
      <p class="brand__eyebrow">{BRAND['eyebrow']}</p>
      <h1 class="brand__name">{BRAND['name']}</h1>
      <p class="brand__meaning">{BRAND['meaning']}</p>
    </div>
  </div>
  <div class="topbar__spacer"></div>
  <button class="iconbtn" aria-label="Switch to light theme">{icon(theme_icon)}</button>
</header>"""


def chiprail(selected=None, hover=None):
    out = ['<div class="chiprail" role="tablist" aria-label="Decks">']
    out.append(f'<button class="chip hue-lamp{" is-selected" if selected is None else ""}" '
               f'role="tab" aria-selected="{str(selected is None).lower()}">All 750</button>')
    for name, ico, _ in DECKS:
        cls = "chip hue-" + HUE[name]
        if name == selected:
            cls += " is-selected"
        if name == hover:
            cls += " is-hover"
        out.append(f'<button class="{cls}" role="tab" aria-selected="{str(name==selected).lower()}">'
                   f'<span class="chip__dot"></span>{name}</button>')
    out.append("</div>")
    return "".join(out)


def modes(expanded=None, hover="smart"):
    out = []
    for key, ico, title, desc in MODES:
        cls = "mode"
        attrs = ""
        if key == hover:
            cls += " is-hover"
        if key == "deck":
            attrs = f' aria-expanded="{"true" if expanded=="deck" else "false"}" aria-controls="deckgrid"'
        out.append(f"""
    <button class="{cls}"{attrs}>
      <span class="mode__t">{icon(ico)}{title}</span>
      <span class="mode__d">{desc}</span>
    </button>""")
    return f'<div class="modes">{"".join(out)}</div>'


def deckgrid(selected=None):
    out = []
    for name, ico, _ in DECKS:
        cls = f"deck hue-{HUE[name]}"
        if name == selected:
            cls += " is-selected"
        elif name == "London":
            cls += " is-hover"
        out.append(f"""
    <button class="{cls}">
      <span class="deck__ico">{icon(ico)}</span>
      <span>
        <span class="deck__n">{name}</span>
        <span class="deck__c">50 prompts</span>
      </span>
    </button>""")
    return f'<div class="deckgrid" id="deckgrid">{"".join(out)}</div>'


def card(c=CARD, follow_open=True, faved=False):
    hue = HUE[c["deck"]]
    follow = ""
    if follow_open:
        follow = f'<div class="follow"><span class="follow__l">Follow-up</span>{c["follow"]}</div>'
    btn = CARD_UI["follow_hide"] if follow_open else CARD_UI["follow_show"]
    pct = max(int(c["n"] / c["total"] * 100), 2)
    fav_cls = "btn btn--fav is-on" if faved else "btn btn--fav"
    fav_txt = CARD_UI["faved"] if faved else CARD_UI["fav"]
    return f"""
<div class="stage hue-{hue}">
  <div class="cardmeta">
    <span class="deckchip">{icon(c['icon'])}<span class="deckchip__t">{c['deck']}</span></span>
    <span class="progress">
      <span class="progress__bar"><span class="progress__fill" style="width:{pct}%"></span></span>
      {c['n']} / {c['total']}
    </span>
  </div>

  <article class="card" aria-live="polite">
    <span class="typemark">{c['type']}</span>
    <h2 class="question">{c['q']}</h2>
    <button class="followbtn">{icon('chevron')}{btn}</button>
    {follow}
    <p class="pass">{CARD_UI['pass']}</p>
  </article>

  <div class="dock">
    <div class="dock__row">
      <button class="btn" aria-label="{CARD_UI['prev']}">{icon('arrow-left')}</button>
      <button class="{fav_cls}" aria-pressed="{'true' if faved else 'false'}" aria-label="{fav_txt}">{icon('heart')}</button>
      <button class="btn btn--primary btn--lg">{CARD_UI['next']}{icon('arrow-right')}</button>
    </div>
    <div class="subcontrols">
      <button class="btn btn--quiet">{icon('deck')}{CARD_UI['modes']}</button>
      <button class="btn btn--quiet">{icon('refresh')}{CARD_UI['reset']}</button>
    </div>
  </div>
</div>"""


def build():
    # ---- home ----
    body = f"""
<div class="app">
{topbar()}
  <main class="main" id="main">
    {chiprail(hover='London')}
    <div class="pagehead">
      <h1>{HOME['h2']}</h1>
      <p>{HOME['sub']}</p>
    </div>
    {modes(hover='smart')}
    <p class="sectionlabel">Pick up where you left off</p>
    <button class="btn">{icon('refresh')}{HOME['resume']}</button>
  </main>
</div>
<div class="note">Option 2 · Late Night Table · Home</div>"""
    write(f"{DIR}/home.html", page("Come We Story — Home · Late Night Table", CSS, body))

    # ---- decks ----
    body = f"""
<div class="app">
{topbar()}
  <main class="main" id="main">
    {chiprail(selected='Cameroon')}
    <div class="pagehead">
      <h1>{HOME['h2']}</h1>
      <p>{HOME['sub']}</p>
    </div>
    {modes(expanded='deck', hover=None)}
    <p class="sectionlabel">Choose a deck · 15 decks · 50 prompts each</p>
    {deckgrid(selected='Cameroon')}
  </main>
</div>
<div class="note">Option 2 · Late Night Table · Browse by Deck</div>"""
    write(f"{DIR}/decks.html", page("Come We Story — Decks · Late Night Table", CSS, body))

    # ---- card ----
    body = f"""
<div class="app">
{topbar(narrow=True)}
  <main class="main main--narrow" id="main">
    {card(CARD, follow_open=True, faved=False)}
  </main>
</div>
<div class="note">Option 2 · Late Night Table · Reading a prompt</div>"""
    write(f"{DIR}/card.html", page("Come We Story — Prompt · Late Night Table", CSS, body))

    # ---- light theme ----
    body = f"""
<div class="app">
{topbar('moon', narrow=True)}
  <main class="main main--narrow" id="main">
    {card(CARD_ALT, follow_open=False, faved=True)}
  </main>
</div>
<div class="note">Option 2 · Late Night Table · Light theme</div>"""
    write(f"{DIR}/card-dark.html", page("Come We Story — Light · Late Night Table", CSS, body,
                                        extra_head='\n  <script>document.documentElement.dataset.theme="light"</script>'))

    # ---- states ----
    ld_t, ld_b = STATES["loading"]
    er_t, er_b = STATES["error"]
    body = f"""
<div class="app">
{topbar(narrow=True)}
  <main class="main main--narrow" id="main">
    <div class="pagehead"><h1>Interface states</h1>
    <p>Every state the app can reach today, plus the three it is missing: loading,
    end-of-deck and a confirmation for Favourite.</p></div>

    <p class="sectionlabel">Loading — currently missing</p>
    <div class="state">
      <div class="dealer"><i></i><i></i><i></i><i></i></div>
      <h3>{ld_t}</h3><p>{ld_b}</p>
    </div>

    <p class="sectionlabel">Loading — card skeleton</p>
    <div class="card">
      <div class="skel" style="width:96px;height:26px;border-radius:999px"></div>
      <div style="margin-top:6px">
        <div class="skel skel--line" style="width:94%;height:28px"></div>
        <div class="skel skel--line" style="width:86%;height:28px"></div>
        <div class="skel skel--line" style="width:48%;height:28px"></div>
      </div>
      <div class="skel" style="width:160px;height:15px"></div>
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
    <div class="toast">{icon('heart')}{STATES['saved']}</div>

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

    <p class="sectionlabel">Deck chip states</p>
    <div style="display:flex;gap:8px;flex-wrap:wrap">
      <button class="chip hue-sky"><span class="chip__dot"></span>London</button>
      <button class="chip hue-clay is-hover"><span class="chip__dot"></span>Hot Takes</button>
      <button class="chip hue-sage is-selected"><span class="chip__dot"></span>Cameroon</button>
      <button class="chip hue-plum is-focus"><span class="chip__dot"></span>Memories &amp; Family</button>
    </div>
  </main>
</div>
<div class="note">Option 2 · Late Night Table · States</div>"""
    write(f"{DIR}/states.html", page("Come We Story — States · Late Night Table", CSS, body))

    # ---- index ----
    sw = "".join(
        f'<div style="flex:1;min-width:104px"><div style="height:64px;background:{h};'
        f'border-radius:8px;border:1px solid var(--edge)"></div>'
        f'<div style="font-size:11px;margin-top:6px;font-weight:600">{n}</div>'
        f'<div style="font-size:11px;color:var(--lamp-3);font-family:ui-monospace,monospace">{h}</div></div>'
        for n, h in [("Night", "#12100E"), ("Table", "#1D1A17"), ("Lamp", "#F5E6C8"),
                     ("Amber", "#E8A33D"), ("Clay", "#C9553D"), ("Sage", "#7FA07A"),
                     ("Dim", "#8C837A")])
    body = f"""
<div class="app">
{topbar(narrow=True)}
  <main class="main main--narrow" id="main">
    <div class="pagehead"><h1>Late Night Table</h1>
    <p>Dark first, because the deck gets played in the evening. The room is dark; one warm
    lamp falls on the card in front of you. High contrast, no ornament, everything else out of
    the way.</p></div>

    <p class="sectionlabel">Screens</p>
    <div class="modes">
      <a class="mode" href="home.html"><span class="mode__t">{icon('smart')}Home</span><span class="mode__d">Mode chooser + deck chip rail</span></a>
      <a class="mode" href="decks.html"><span class="mode__t">{icon('deck')}Browse by Deck</span><span class="mode__d">All 15 decks, expanded</span></a>
      <a class="mode" href="card.html"><span class="mode__t">{icon('journey')}Reading a prompt</span><span class="mode__d">Follow-up revealed</span></a>
      <a class="mode" href="card-dark.html"><span class="mode__t">{icon('sun')}Light theme</span><span class="mode__d">Favourited state</span></a>
      <a class="mode" href="states.html"><span class="mode__t">{icon('alert')}States</span><span class="mode__d">Loading, error, end of deck, buttons</span></a>
    </div>

    <p class="sectionlabel">Palette</p>
    <div style="display:flex;gap:10px;flex-wrap:wrap">{sw}</div>

    <p class="sectionlabel">Type specimen</p>
    <p style="font-family:var(--display);font-weight:700;font-size:2.75rem;line-height:1.07;
      letter-spacing:-.04em;font-variation-settings:'wdth' 86;max-width:17ch">
      Which Black American sports moment had the greatest cultural significance?</p>
    <p style="margin-top:16px;color:var(--lamp-2);max-width:52ch">
      Archivo at width 86–92 for questions and headings — a grotesk squeezed just enough to fit
      long prompts on a phone without shrinking the type. Inter for interface and metadata.</p>

    <p class="sectionlabel">Deck iconography — replaces emoji</p>
    <div style="display:flex;gap:14px;flex-wrap:wrap">
      {''.join(f'<span class="deck__ico hue-{HUE[n]}" title="{n}">{icon(i)}</span>' for n,i,_ in DECKS)}
    </div>
  </main>
</div>"""
    write(f"{DIR}/index.html", page("Late Night Table — Option 2", CSS, body))
