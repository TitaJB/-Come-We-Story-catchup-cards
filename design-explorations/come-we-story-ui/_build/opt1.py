"""Option 1 — "Story Press". Page markup."""

from common import (BRAND, HOME, MODES, DECKS, CARD_UI, CARD, CARD_ALT, CARD_WYR,
                    STATES, icon, page, write)

CSS = ["../shared-assets/fonts.css", "theme.css"]
DIR = "option-1-story-press"


def masthead(theme_icon="moon", crumb=None):
    crumb_html = ""
    if crumb:
        crumb_html = (f'<span class="crumb">{icon(crumb[0])}{crumb[1]}</span>')
    return f"""
<header class="masthead">
  <div class="weave"></div>
  <div class="masthead__inner">
    <a class="skip" href="#main">Skip to content</a>
    <div class="brand">
      <div class="brand__mark">{icon('deck')}</div>
      <div>
        <p class="brand__eyebrow">{BRAND['eyebrow']}</p>
        <h1 class="brand__name">{BRAND['name']}</h1>
        <p class="brand__meaning">{BRAND['meaning']}</p>
      </div>
    </div>
    <div class="masthead__spacer"></div>
    <div class="masthead__nav">
      {crumb_html}
      <button class="iconbtn" aria-label="Switch to dark theme">{icon(theme_icon)}</button>
    </div>
  </div>
</header>"""


def rail(selected=None):
    items = []
    for name, ico, hue in DECKS:
        sel = " is-selected" if name == selected else ""
        items.append(
            f'<li class="rail__item hue-{hue}{sel}">'
            f'<button class="rail__link">{icon(ico)}'
            f'<span class="rail__name">{name}</span>'
            f'<span class="rail__n">50</span></button></li>')
    return f"""
<nav class="rail" aria-label="Decks">
  <div class="rail__head">
    <span class="rail__title">All decks</span>
    <span class="rail__count">15 · 750 prompts</span>
  </div>
  <ul class="rail__list">{''.join(items)}</ul>
</nav>"""


def modes(expanded="deck", hover="smart"):
    out = []
    for i, (key, ico, title, desc) in enumerate(MODES, 1):
        cls = "mode"
        attrs = ""
        if key == hover:
            cls += " is-hover"
        if key == "deck":
            attrs = f' aria-expanded="{"true" if expanded=="deck" else "false"}" aria-controls="deckgrid"'
        out.append(f"""
    <button class="{cls}"{attrs}>
      <span class="mode__num">{i:02d}</span>
      <span class="mode__body">
        <span class="mode__t">{icon(ico)}{title}</span>
        <span class="mode__d">{desc}</span>
      </span>
      <span class="mode__go">{icon('chevron')}</span>
    </button>""")
    return f'<div class="modes">{"".join(out)}</div>'


def deckgrid(selected=None):
    out = []
    for name, ico, hue in DECKS:
        sel = " is-selected" if name == selected else ""
        hov = " is-hover" if name == "London" and not selected else ""
        out.append(f"""
    <button class="deck hue-{hue}{sel}{hov}">
      <span class="deck__ico">{icon(ico)}</span>
      <span class="deck__b">
        <span class="deck__n">{name}</span>
        <span class="deck__c">50 prompts</span>
      </span>
    </button>""")
    return f'<div class="deckgrid" id="deckgrid">{"".join(out)}</div>'


def card(c=CARD, follow_open=True, faved=False):
    follow = ""
    if follow_open:
        follow = f"""
      <p class="follow"><span class="follow__l">Follow-up</span>{c['follow']}</p>"""
    btn_label = CARD_UI["follow_hide"] if follow_open else CARD_UI["follow_show"]
    pct = int(c["n"] / c["total"] * 100) or 2
    fav_cls = "btn btn--fav is-on" if faved else "btn btn--fav"
    fav_txt = CARD_UI["faved"] if faved else CARD_UI["fav"]
    return f"""
<div class="stage hue-{c['hue']}">
  <div class="cardmeta">
    <span class="deckchip">{icon(c['icon'])}<span class="deckchip__t">{c['deck']}</span></span>
    <span class="progress">
      <span class="progress__bar"><span class="progress__fill" style="width:{max(pct,2)}%"></span></span>
      {c['n']} / {c['total']}
    </span>
  </div>

  <article class="card" aria-live="polite">
    <div class="card__spine weave--v"></div>
    <div class="card__body">
      <span class="typemark">{c['type']}</span>
      <h2 class="question">{c['q']}</h2>
      <button class="followbtn">{icon('chevron')}{btn_label}</button>{follow}
      <div class="card__foot">
        <p class="pass">{CARD_UI['pass']}</p>
      </div>
    </div>
  </article>

  <div class="controls">
    <button class="btn">{icon('arrow-left')}{CARD_UI['prev']}</button>
    <button class="{fav_cls}" aria-pressed="{'true' if faved else 'false'}">{icon('heart')}{fav_txt}</button>
    <button class="btn btn--primary btn--lg">{CARD_UI['next']}{icon('arrow-right')}</button>
  </div>
  <div class="subcontrols">
    <button class="btn btn--quiet">{icon('deck')}{CARD_UI['modes']}</button>
    <button class="btn btn--quiet">{icon('refresh')}{CARD_UI['reset']}</button>
  </div>

  <div class="mobilebar">
    <button class="btn" aria-label="{CARD_UI['prev']}">{icon('arrow-left')}</button>
    <button class="{fav_cls}" aria-pressed="{'true' if faved else 'false'}" aria-label="{fav_txt}">{icon('heart')}</button>
    <button class="btn btn--primary">{CARD_UI['next']}{icon('arrow-right')}</button>
  </div>
</div>"""


# ---------------------------------------------------------------- pages ----

def build():
    # ---- home ----
    body = f"""
<div class="app">
{masthead()}
  <main class="main" id="main">
    {rail()}
    <div>
      <div class="pagehead">
        <h1>{HOME['h2']}</h1>
        <p>{HOME['sub']}</p>
      </div>
      {modes(expanded='none', hover='smart')}
      <div class="rulehead"><span class="rulehead__t">Pick up where you left off</span><span class="rulehead__r"></span></div>
      <button class="btn">{icon('refresh')}{HOME['resume']}</button>
    </div>
  </main>
</div>
<div class="note">Option 1 · Story Press · Home</div>"""
    write(f"{DIR}/home.html", page("Come We Story — Home · Story Press", CSS, body))

    # ---- decks ----
    body = f"""
<div class="app">
{masthead()}
  <main class="main" id="main">
    {rail(selected='Black American Culture')}
    <div>
      <div class="pagehead">
        <h1>{HOME['h2']}</h1>
        <p>{HOME['sub']}</p>
      </div>
      {modes(expanded='deck', hover=None)}
      <div class="rulehead"><span class="rulehead__t">Choose a deck · 15 decks · 50 prompts each</span><span class="rulehead__r"></span></div>
      {deckgrid(selected='Black American Culture')}
    </div>
  </main>
</div>
<div class="note">Option 1 · Story Press · Browse by Deck</div>"""
    write(f"{DIR}/decks.html", page("Come We Story — Decks · Story Press", CSS, body))

    # ---- card ----
    body = f"""
<div class="app">
{masthead()}
  <main class="main" id="main">
    {rail(selected='Black American Culture')}
    {card(CARD, follow_open=True, faved=False)}
  </main>
</div>
<div class="note">Option 1 · Story Press · Reading a prompt</div>"""
    write(f"{DIR}/card.html", page("Come We Story — Prompt · Story Press", CSS, body))

    # ---- card, dark ----
    body = f"""
<div class="app">
{masthead('sun')}
  <main class="main" id="main">
    {rail(selected='Memories & Family')}
    {card(CARD_ALT, follow_open=False, faved=True)}
  </main>
</div>
<div class="note">Option 1 · Story Press · Dark theme</div>"""
    write(f"{DIR}/card-dark.html", page("Come We Story — Dark · Story Press", CSS, body,
                                        extra_head='\n  <script>document.documentElement.dataset.theme="dark"</script>'))

    # ---- states ----
    ld_t, ld_b = STATES["loading"]
    er_t, er_b = STATES["error"]
    body = f"""
<div class="app">
{masthead()}
  <main class="main main--single" id="main">
    <div>
      <div class="pagehead"><h1>Interface states</h1>
      <p>Every state the app can actually reach today, plus the three it is currently missing:
      loading, end-of-deck and a confirmation for Favourite.</p></div>

      <div class="rulehead"><span class="rulehead__t">Loading — currently missing</span><span class="rulehead__r"></span></div>
      <div class="state">
        <div class="dealer"><i></i><i></i><i></i><i></i></div>
        <h3>{ld_t}</h3><p>{ld_b}</p>
      </div>

      <div class="rulehead"><span class="rulehead__t">Loading — card skeleton</span><span class="rulehead__r"></span></div>
      <div class="card">
        <div class="card__spine weave--v"></div>
        <div class="card__body">
          <div class="skel" style="width:88px;height:12px"></div>
          <div style="margin-top:12px">
            <div class="skel skel--line" style="width:96%;height:26px"></div>
            <div class="skel skel--line" style="width:88%;height:26px"></div>
            <div class="skel skel--line" style="width:54%;height:26px"></div>
          </div>
          <div class="skel" style="width:150px;height:14px;margin-top:10px"></div>
        </div>
      </div>

      <div class="rulehead"><span class="rulehead__t">Error — the app's real message</span><span class="rulehead__r"></span></div>
      <div class="state state--error">
        <div class="state__ico">{icon('alert')}</div>
        <h3>{er_t}</h3><p>{er_b}</p>
        <div class="state__actions">
          <button class="btn btn--primary">{icon('refresh')}Try again</button>
          <button class="btn">Use the two offline decks</button>
        </div>
      </div>

      <div class="rulehead"><span class="rulehead__t">Inline alert</span><span class="rulehead__r"></span></div>
      <div class="alert">{icon('alert')}<p><strong>Showing 100 prompts, not 750.</strong>
      The full deck could not be loaded, so Light &amp; Funny and Catch-up are being used.</p></div>

      <div class="rulehead"><span class="rulehead__t">End of deck — currently missing</span><span class="rulehead__r"></span></div>
      <div class="state state--end">
        <div class="state__ico">{icon('check')}</div>
        <h3>{STATES['end_title']}</h3><p>{STATES['end_body']}</p>
        <div class="state__actions">
          <button class="btn btn--primary">{icon('refresh')}Reshuffle</button>
          <button class="btn">{icon('deck')}Choose another deck</button>
        </div>
      </div>

      <div class="rulehead"><span class="rulehead__t">Success confirmation</span><span class="rulehead__r"></span></div>
      <div class="toast">{icon('heart')}{STATES['saved']}</div>

      <div class="rulehead"><span class="rulehead__t">Button states</span><span class="rulehead__r"></span></div>
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

      <div class="rulehead"><span class="rulehead__t">Deck row states</span><span class="rulehead__r"></span></div>
      <div class="deckgrid" style="grid-template-columns:repeat(3,1fr)">
        <button class="deck hue-indigo">{'<span class="deck__ico">'+icon('london')+'</span>'}<span class="deck__b"><span class="deck__n">London</span><span class="deck__c">Default</span></span></button>
        <button class="deck hue-kola is-hover">{'<span class="deck__ico">'+icon('hot-takes')+'</span>'}<span class="deck__b"><span class="deck__n">Hot Takes</span><span class="deck__c">Hover</span></span></button>
        <button class="deck hue-green is-selected">{'<span class="deck__ico">'+icon('cameroon')+'</span>'}<span class="deck__b"><span class="deck__n">Cameroon</span><span class="deck__c">Selected</span></span></button>
      </div>
    </div>
  </main>
</div>
<div class="note">Option 1 · Story Press · States</div>"""
    write(f"{DIR}/states.html", page("Come We Story — States · Story Press", CSS, body))

    # ---- index / specimen ----
    swatches = "".join(
        f'<div style="flex:1;min-width:104px"><div style="height:64px;background:{hexv};'
        f'border:1px solid var(--rule);border-radius:var(--r-sm)"></div>'
        f'<div style="font-size:11px;margin-top:6px;font-weight:600">{nm}</div>'
        f'<div style="font-size:11px;color:var(--ink-2);font-family:ui-monospace,monospace">{hexv}</div></div>'
        for nm, hexv in [("Paper", "#F2EAD9"), ("Paper raised", "#FBF6EC"), ("Ink", "#1A1714"),
                         ("Indigo", "#2B4A7D"), ("Kola", "#B02A16"), ("Palm gold", "#C88A2E"),
                         ("Rule", "#D6C9AE")])
    body = f"""
<div class="app">
{masthead()}
  <main class="main main--single" id="main">
    <div>
      <div class="pagehead"><h1>Story Press</h1>
      <p>West African market-print and letterpress editorial. Flat ink on paper, keylines instead of
      shadows, and type carrying the emotion. The woven strip is the only ornament, and it is
      functional — it identifies the deck.</p></div>

      <div class="rulehead"><span class="rulehead__t">Screens</span><span class="rulehead__r"></span></div>
      <div class="modes">
        <a class="mode" href="home.html"><span class="mode__num">01</span><span class="mode__body"><span class="mode__t">Home</span><span class="mode__d">Mode chooser + persistent deck rail</span></span><span class="mode__go">{icon('chevron')}</span></a>
        <a class="mode" href="decks.html"><span class="mode__num">02</span><span class="mode__body"><span class="mode__t">Browse by Deck</span><span class="mode__d">All 15 decks, expanded</span></span><span class="mode__go">{icon('chevron')}</span></a>
        <a class="mode" href="card.html"><span class="mode__num">03</span><span class="mode__body"><span class="mode__t">Reading a prompt</span><span class="mode__d">Follow-up revealed</span></span><span class="mode__go">{icon('chevron')}</span></a>
        <a class="mode" href="card-dark.html"><span class="mode__num">04</span><span class="mode__body"><span class="mode__t">Dark theme</span><span class="mode__d">Favourited state</span></span><span class="mode__go">{icon('chevron')}</span></a>
        <a class="mode" href="states.html"><span class="mode__num">05</span><span class="mode__body"><span class="mode__t">States</span><span class="mode__d">Loading, error, end of deck, buttons</span></span><span class="mode__go">{icon('chevron')}</span></a>
      </div>

      <div class="rulehead"><span class="rulehead__t">Palette</span><span class="rulehead__r"></span></div>
      <div style="display:flex;gap:10px;flex-wrap:wrap">{swatches}</div>

      <div class="rulehead"><span class="rulehead__t">Type specimen</span><span class="rulehead__r"></span></div>
      <p style="font-family:var(--display);font-weight:800;font-size:3rem;line-height:1.05;
        font-variation-settings:'opsz' 144;letter-spacing:-.025em;max-width:18ch">
        Which Black American sports moment had the greatest cultural significance?</p>
      <p style="margin-top:16px;color:var(--ink-2);max-width:52ch">
        Fraunces 800 for questions and headings. Inter for interface and metadata.
        Fraunces italic at small optical size for the tagline and the pass line.</p>

      <div class="rulehead"><span class="rulehead__t">Deck iconography — replaces emoji</span><span class="rulehead__r"></span></div>
      <div style="display:flex;gap:18px;flex-wrap:wrap">
        {''.join(f'<span class="deck__ico hue-{h}" title="{n}">{icon(i)}</span>' for n,i,h in DECKS)}
      </div>
    </div>
  </main>
</div>"""
    write(f"{DIR}/index.html", page("Story Press — Option 1", CSS, body))
