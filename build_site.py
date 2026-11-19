#!/usr/bin/env python3
"""Cortés Painting Inc — template-v2 T2 site generator (2026-11-19, cohort B).
Identity: 'forest & limestone' — deep green on limestone, brass accents,
bristle-tick strips. Zero third-party JS.
Verified facts (card t_d5622672): CCB #213757 ACTIVE RGC regis 2017-02-10,
LBPR re-registered 2026-05-21, $25K bond + $1M ins, 14318 SE Johnson Rd
Milwaukie OR 97267, phone 503-476-5120 exact, RMI Edgar Cortes Martinez,
email info@ecortespaintinginc.com (live MX), FB cortespaintinginc."""
import json, os

SLUG   = "cortes-painting"
ORIGIN = "https://cortes-painting-demo.up.railway.app"
SITE   = "Cortés Painting Inc"
BRAND  = "Cortés Painting"
PHONE  = "(503) 476-5120"
TEL    = "tel:+15034765120"
EMAIL  = "info@ecortespaintinginc.com"
STREET = "14318 SE Johnson Rd"
CITY, ST, ZIP = "Milwaukie", "OR", "97267"
CITY_FULL = "Milwaukie, Oregon"
FB = "https://www.facebook.com/cortespaintinginc/"
MAPQ = "https://www.google.com/maps?q=14318+SE+Johnson+Rd,+Milwaukie,+OR+97267&amp;output=embed"
BUILT = "<!-- BUILT-2026-11-19 -->\n"

def head(title, desc, path, util=False):
    url = ORIGIN + ("/" if path == "/" else path)
    h = ['<!DOCTYPE html>', '<html lang="en">', '<head>',
    '<meta charset="utf-8">',
    '<meta name="viewport" content="width=device-width, initial-scale=1">',
    f'<title>{title}</title>',
    f'<meta name="description" content="{desc}">',
    '<meta name="robots" content="noindex, nofollow">',
    f'<link rel="canonical" href="{url}">']
    if not util:
        h += [
        f'<meta property="og:title" content="{title}">',
        f'<meta property="og:description" content="{desc}">',
        f'<meta property="og:url" content="{url}">',
        '<meta property="og:type" content="website">',
        f'<meta property="og:site_name" content="{SITE}">',
        '<meta property="og:locale" content="en_US">',
        f'<meta property="og:image" content="{ORIGIN}/og.png">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{title}">',
        f'<meta name="twitter:description" content="{desc}">',
        f'<meta name="twitter:image" content="{ORIGIN}/og.png">']
    h += ['<link rel="icon" type="image/svg+xml" href="/favicon.svg">',
    '<link rel="stylesheet" href="/style.css">', '</head>', '<body>',
    '<a class="skip" href="#main">Skip to content</a>']
    return "\n".join(h)

NAV = ('<header class="top"><div class="wrap headrow"><a class="brand" href="/">Cortés <span>Painting</span></a>'
       '<nav class="links"><a href="/services">Services</a><a href="/interior-painting">Interior</a>'
       '<a href="/exterior-painting">Exterior</a><a href="/contact">Contact</a></nav></div></header>')
BRISTLE = '<div class="bristle" aria-hidden="true"></div>'

FOOTER = f'''<footer>
  <div class="wrap footgrid">
    <div class="footid">
      <span class="brand">Cortés <span>Painting</span></span>
      <p class="footline">Interior &amp; exterior painting — lead-safe certified, registered &amp; insured.</p>
      <p class="footline muted">{STREET}, {CITY}, {ST} {ZIP} &middot; <a href="{TEL}">{PHONE}</a> &middot; <a href="mailto:{EMAIL}">{EMAIL}</a> &middot; <a href="{FB}">Facebook</a></p>
    </div>
    <nav class="footlinks" aria-label="Footer">
      <a href="/services">Services</a><a href="/interior-painting">Interior</a><a href="/exterior-painting">Exterior</a><a href="/contact">Contact</a>
    </nav>
    <p class="copy">© 2026 {SITE} &middot; {CITY}, {ST}</p>
  </div>
</footer>'''

def crumbs(trail):
    parts = ['<a href="/">Home</a>']
    for label, href in trail[:-1]:
        parts.append(f'<a href="{href}">{label}</a>')
    parts.append(trail[-1][0])
    return '<p class="crumbs">' + ' › '.join(parts) + '</p>'

def ld_block(data):
    return '<script type="application/ld+json">\n' + json.dumps(data, ensure_ascii=False, indent=1) + '\n</script>'

def breadcrumb_ld(trail):
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": ORIGIN + "/"}]
    for i, (label, href) in enumerate(trail, start=2):
        items.append({"@type": "ListItem", "position": i, "name": label,
                      "item": ORIGIN + ("/" if href == "/" else href)})
    return ld_block({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items})

CTA = f'''<section class="quote">
  <div class="wrap quotain">
    <h2>Registered, bonded, insured, lead-safe.</h2>
    <p class="deck">Oregon CCB #213757 (RGC) &middot; LBPR lead-safe registration &middot; Milwaukie, {ST}.</p>
    <div class="cta-row">
      <a class="btn fill" href="/contact">Get a quote</a>
      <a class="btn line" href="{TEL}">Call {PHONE}</a>
    </div>
  </div>
</section>'''

MAP = (f'<iframe title="Map — {SITE}, {STREET}, {CITY}, {ST} {ZIP}" src="{MAPQ}" loading="lazy"></iframe>')

STATS = '''<section class="stats">
  <div class="wrap statgrid">
    <div class="stat"><p><b>2017</b><span>CCB-registered painter since</span></p></div>
    <div class="stat"><p><b>#213757</b><span>CCB RGC &middot; $25K bond &middot; $1M insurance</span></p></div>
    <div class="stat"><p><b>LBPR</b><span>lead-based paint renovation registered</span></p></div>
  </div>
</section>'''

LEADSAFE = '''<section class="block">
  <div class="wrap leadband">
    <div class="leadtext">
      <p class="eyebrow">Pre-1978 houses</p>
      <h2>Certified for the dust older homes kick up</h2>
      <p class="deck">If a house was built before 1978, sanding and scraping before repainting is lead-regulated work. Cortés Painting carries Oregon lead-based paint renovation registration (LBPR, current through 2027) on top of its CCB painting license — containment, certified cleanup, the whole protocol.</p>
    </div>
    <div class="leadbadge" aria-hidden="true"><span class="lbnum">LBPR</span><span class="lbcap">registered &middot; thru 2027</span></div>
  </div>
</section>'''

PROCESS = '''<section class="block">
  <div class="wrap">
    <p class="eyebrow">How a job runs</p>
    <h2>Clean scope, cleaner edges</h2>
    <div class="steps">
      <div class="step"><p class="num">1</p><h3>Scope</h3><p>Call or send the form — surfaces, prep and price agreed before a brush comes out.</p></div>
      <div class="step"><p class="num">2</p><h3>Prep</h3><p>Masking, patching, sanding, priming — with lead-safe protocol where the house is old enough to need it.</p></div>
      <div class="step"><p class="num">3</p><h3>Paint</h3><p>Hand cut-ins, even coats, room by room so daily life in the house keeps moving.</p></div>
      <div class="step"><p class="num">4</p><h3>Walk</h3><p>Final walkthrough with you, touch-ups found and fixed, tape pulled, floors wiped.</p></div>
    </div>
  </div>
</section>'''

def faq(items):
    body = ''.join(f'<div class="qa"><h3>{q}</h3><p>{a}</p></div>' for q, a in items)
    return f'<section class="block"><div class="wrap"><p class="eyebrow">Good questions</p><h2>Before you call</h2><div class="fa grid2">{body}</div></div></section>'

def faq_ld(items):
    return ld_block({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]})

def service_ld(name, desc):
    return ld_block([
        {"@context": "https://schema.org", "@type": "Service", "name": name, "description": desc,
         "areaServed": {"@type": "Place", "name": CITY_FULL}, "provider": {"@id": ORIGIN + "/#business"}}])

PAGES = {}

# ---------------------------------------------------------------- home
home_ld = ld_block({
 "@context": "https://schema.org", "@type": "HousePainter", "@id": ORIGIN + "/#business",
 "name": SITE, "alternateName": "Cortes Painting Inc",
 "telephone": "+1-503-476-5120", "email": EMAIL,
 "address": {"@type": "PostalAddress", "streetAddress": STREET, "addressLocality": CITY,
             "addressRegion": ST, "postalCode": ZIP, "addressCountry": "US"},
 "url": ORIGIN + "/", "logo": ORIGIN + "/og.png", "image": ORIGIN + "/og.png",
 "sameAs": [FB], "areaServed": CITY_FULL,
 "hasCredential": "Oregon CCB License #213757 (RGC) registered since 2017, bonded & insured; LBPR lead-based paint renovation certification"})

PAGES["/index.html"] = head(
 "Interior &amp; Exterior Painting — Cortés Painting Inc, Milwaukie OR",
 "Cortés Painting Inc — interior and exterior painting in Milwaukie, Oregon. CCB #213757, bonded, insured, lead-safe certified (LBPR). (503) 476-5120.", "/") + f'''
{NAV}
{BRISTLE}
<main id="main">

<section class="hero">
  <div class="wrap herogrid">
    <div>
      <p class="eyebrow">Painting contractors &middot; {CITY_FULL}</p>
      <h1>A certified crew for every coat.</h1>
      <p class="deck">Cortés Painting Inc does interior and exterior paint work out of {CITY_FULL} — registered, bonded, insured and lead-safe certified, with the paperwork to prove all four.</p>
      <div class="cta-row">
        <a class="btn fill" href="/contact">Get a quote</a>
        <a class="btn line" href="{TEL}">Call {PHONE}</a>
      </div>
      <p class="telhint">Or put the job details on the <a href="/contact">quote page</a> — straight to the business.</p>
    </div>
    <div class="credstack" aria-hidden="true">
      <div class="cred"><b>CCB</b><span>#213757 RGC</span></div>
      <div class="cred"><b>LBPR</b><span>lead-safe registered</span></div>
      <div class="cred"><b>$1M</b><span>insurance on file</span></div>
    </div>
  </div>
</section>

{STATS}

<section class="block">
  <div class="wrap">
    <p class="eyebrow">What we paint</p>
    <h2>Inside, outside — old houses included</h2>
    <p class="lead">A licensed painting company for homes in and around {CITY_FULL} — rooms and trim, siding and shell, pre-1978 houses handled with lead-safe protocol.</p>
    <div class="cards">
      <div class="card">
        <span class="tick" aria-hidden="true"></span>
        <h3>Interior painting</h3>
        <p>Rooms, hallways, ceilings, trim and doors — patched, primed and rolled, with cut lines you can stand next to.</p>
        <a class="go" href="/interior-painting">Interior details &rarr;</a>
      </div>
      <div class="card">
        <span class="tick" aria-hidden="true"></span>
        <h3>Exterior painting</h3>
        <p>Siding, trim, fascia and doors — cleaned, scraped and caulked before the finish coats, lead-safe where it applies.</p>
        <a class="go" href="/exterior-painting">Exterior details &rarr;</a>
      </div>
      <div class="card">
        <span class="tick" aria-hidden="true"></span>
        <h3>Older homes, done right</h3>
        <p>Pre-1978 surfaces get the certified handling they need — containment and cleanup per Oregon LBPR rules, no shortcuts.</p>
        <a class="go" href="/contact">Ask about your house &rarr;</a>
      </div>
    </div>
  </div>
</section>

{LEADSAFE}
{PROCESS}
{CTA}

</main>
{BRISTLE}
{FOOTER}
{home_ld}
</body>
</html>
'''

# ---------------------------------------------------------------- services
svc_ld = ld_block({"@context": "https://schema.org", "@graph": [
 {"@type": "Service", "name": "Interior painting", "areaServed": {"@type": "Place", "name": CITY_FULL}, "provider": {"@id": ORIGIN + "/#business"}},
 {"@type": "Service", "name": "Exterior painting", "areaServed": {"@type": "Place", "name": CITY_FULL}, "provider": {"@id": ORIGIN + "/#business"}},
 {"@type": "Service", "name": "Lead-safe renovation painting", "areaServed": {"@type": "Place", "name": CITY_FULL}, "provider": {"@id": ORIGIN + "/#business"}}]})
PAGES["/services.html"] = head(
 "Painting Services — Cortés Painting Inc, Milwaukie OR",
 "Interior, exterior and lead-safe painting services in Milwaukie, Oregon. CCB #213757, LBPR registered. See scopes and get a quote.", "/services") + f'''
{NAV}
{BRISTLE}
<main id="main">

<section class="pagehero">
  <div class="wrap">
    {crumbs([("Services", "/services")])}
    <p class="eyebrow">Services</p>
    <h1>Paint work with the credentials attached</h1>
    <p class="deck">Every quote is scoped to the surfaces — including whether they predate 1978, which changes how the prep has to go.</p>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <div class="cards">
      <div class="card">
        <span class="tick" aria-hidden="true"></span>
        <h3>Interior painting</h3>
        <p>Full rooms and partial refreshes: walls, ceilings, trim, baseboards, doors, closets and hallways. Patch, sand, prime, coat — in that order.</p>
        <a class="go" href="/interior-painting">Interior details &rarr;</a>
      </div>
      <div class="card">
        <span class="tick" aria-hidden="true"></span>
        <h3>Exterior painting</h3>
        <p>Siding, trim, fascia, soffits, doors and porch surfaces. Prep starts with cleaning, ends with caulk — paint last.</p>
        <a class="go" href="/exterior-painting">Exterior details &rarr;</a>
      </div>
      <div class="card">
        <span class="tick" aria-hidden="true"></span>
        <h3>Lead-safe renovation work</h3>
        <p>Disturbing paint on pre-1978 surfaces is regulated. LBPR registration covers the containment, protocol and certified cleanup.</p>
        <a class="go" href="/contact">Scope an older home &rarr;</a>
      </div>
    </div>
  </div>
</section>

{LEADSAFE}
{CTA}

</main>
{BRISTLE}
{FOOTER}
{svc_ld}
{breadcrumb_ld([("Services", "/services")])}
</body>
</html>
'''

# ---------------------------------------------------------------- interior
int_faq = [
 ("What surfaces does an interior job cover?",
  "Room walls and ceilings, hallways, closets, trim, baseboards and doors — the full envelope of the rooms in scope, not just the big flat walls."),
 ("Is patching and prep included?",
  "It comes first: nail pops and patches filled, sanding smooth, dust killed, priming where bare or repaired. That is the half of the job cheap quotes skip."),
 ("My house is older — does that change the inside work?",
  "If surfaces predate 1978 and prep will sand through old paint, the job follows the lead-safe renovation protocol — registered, contained, cleaned certified."),
 ("How does pricing work?",
  f"By scope, not by guess. Call {PHONE} or send the contact form — surfaces and prep set the price, and you see it before work starts.")]
PAGES["/interior-painting.html"] = head(
 "Interior Painting — Cortés Painting Inc, Milwaukie OR",
 "Interior house painting in Milwaukie, Oregon — rooms, ceilings, trim and doors, prepped and primed before the finish coats. CCB #213757.", "/interior-painting") + f'''
{NAV}
{BRISTLE}
<main id="main">

<section class="pagehero">
  <div class="wrap">
    {crumbs([("Services", "/services"), ("Interior painting", "/interior-painting")])}
    <p class="eyebrow">Service &middot; Interior</p>
    <h1>Interior paint that survives real life</h1>
    <p class="deck">Hall scuffs, kitchen grease, closet-door edges — interior paint fails at the prep, not the color. The prep gets fixed first, then the coat goes on.</p>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <p class="eyebrow">What gets covered</p>
    <h2>The usual scope</h2>
    <div class="specs">
      <div class="spec"><h3>Walls &amp; ceilings</h3><p>Full rooms or accent walls — roller coverage on walls, brush work where the roller can&#39;t reach.</p></div>
      <div class="spec"><h3>Trim, base &amp; doors</h3><p>Cut lines at ceiling and base, gloss on trim and doors so every edge reads sharp.</p></div>
      <div class="spec"><h3>Hallways &amp; stairs</h3><p>Worn high-touch walls and banisters, worked section by section so the house keeps functioning.</p></div>
      <div class="spec"><h3>Closets &amp; bonus rooms</h3><p>The cheap fast rooms too — primed and coated, not left as an afterthought.</p></div>
    </div>
  </div>
</section>

{PROCESS}
{faq(int_faq)}
{CTA}

</main>
{BRISTLE}
{FOOTER}
{service_ld("Interior painting", "Interior house painting in Milwaukie, Oregon — walls, ceilings, trim and doors, fully prepped before finish coats.")}
{faq_ld(int_faq)}
{breadcrumb_ld([("Services", "/services"), ("Interior painting", "/interior-painting")])}
</body>
</html>
'''

# ---------------------------------------------------------------- exterior
ext_faq = [
 ("What surfaces does an exterior job cover?",
  "Siding, trim, fascia, soffits, doors and porch surfaces — the shell of the house, painted as one system, not one wall at a time."),
 ("Is the outside cleaned before painting?",
  "Exterior prep starts with cleaning, then scraping and caulking, before any new coat goes on. Paint over dirt or open gaps peels right back off."),
 ("What about lead paint on an older exterior?",
  "Scraping pre-1978 siding is exactly the regulated kind of work — containment, certified cleaning and disposal are part of the scope, billed openly, not hidden in a daily rate."),
 ("Can this be combined with an interior job?",
  "Interior and exterior are commonly scoped together — one crew, one schedule, one walkthrough at the end.")]
PAGES["/exterior-painting.html"] = head(
 "Exterior Painting — Cortés Painting Inc, Milwaukie OR",
 "Exterior house painting in Milwaukie, Oregon — siding, trim, doors and porches cleaned, caulked and coated. Lead-safe certified crew. CCB #213757.", "/exterior-painting") + f'''
{NAV}
{BRISTLE}
<main id="main">

<section class="pagehero">
  <div class="wrap">
    {crumbs([("Services", "/services"), ("Exterior painting", "/exterior-painting")])}
    <p class="eyebrow">Service &middot; Exterior</p>
    <h1>A paint job built for west-side weather</h1>
    <p class="deck">Rain, sun and freeze-thaw attack the outside from every direction at once. Exterior paint earns its years in the prep — cleaning, scraping, caulking — before the finish coats.</p>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <p class="eyebrow">What gets covered</p>
    <h2>The usual scope</h2>
    <div class="specs">
      <div class="spec"><h3>Siding</h3><p>Washed, scraped, spot-primed and coated — lap siding and flat surfaces, worked so the lap lines stay clean.</p></div>
      <div class="spec"><h3>Trim, fascia &amp; soffits</h3><p>The edges that decide how the house reads — caulked tight and painted smooth.</p></div>
      <div class="spec"><h3>Doors &amp; porch surfaces</h3><p>Entry doors, porch rails and columns get the same finish system as the rest of the shell.</p></div>
      <div class="spec"><h3>Gutter &amp; downspout color</h3><p>Coordinated or contrast — decided in the scope so the hardware matches the plan.</p></div>
    </div>
  </div>
</section>

{LEADSAFE}
{faq(ext_faq)}
{CTA}

</main>
{BRISTLE}
{FOOTER}
{service_ld("Exterior painting", "Exterior house painting in Milwaukie, Oregon — siding, trim, doors and porches cleaned, caulked and coated; lead-safe protocol for pre-1978 surfaces.")}
{faq_ld(ext_faq)}
{breadcrumb_ld([("Services", "/services"), ("Exterior painting", "/exterior-painting")])}
</body>
</html>
'''

# ---------------------------------------------------------------- contact
PAGES["/contact.html"] = head(
 "Contact &amp; Quotes — Cortés Painting Inc, Milwaukie OR",
 "Get a painting quote in Milwaukie, Oregon — call (503) 476-5120 or send the form. CCB #213757, bonded, insured, lead-safe certified.", "/contact") + f'''
{NAV}
{BRISTLE}
<main id="main">

<section class="pagehero">
  <div class="wrap">
    {crumbs([("Contact", "/contact")])}
    <p class="eyebrow">Contact</p>
    <h1>Tell us about the surfaces</h1>
    <p class="deck">Rooms, siding, an older house due for a repaint — describe it and we&#39;ll scope it and price it back to you.</p>
  </div>
</section>

<section class="block">
  <div class="wrap cgrid">
    <form class="form" method="post" action="/contact">
      <label for="f-name">Your name<input id="f-name" name="name" type="text" maxlength="120" required></label>
      <label for="f-phone">Phone (optional)<input id="f-phone" name="phone" type="tel" maxlength="60"></label>
      <label for="f-email">Email<input id="f-email" name="email" type="email" maxlength="120"></label>
      <label for="f-msg">What needs painting<textarea id="f-msg" name="message" rows="6" maxlength="4000" required></textarea></label>
      <button class="btn fill" type="submit">Send the details</button>
      <p class="formnote">The form goes straight to the business — no middleman, no mailing list.</p>
    </form>
    <aside class="cinfo">
      <div class="callbox">
        <p class="eyebrow">Phone</p>
        <p class="bignum"><a href="{TEL}">{PHONE}</a></p>
        <p class="muted">Email: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
      <div class="addr">
        <p class="eyebrow">Where</p>
        <p>{STREET}<br>{CITY}, {ST} {ZIP}</p>
      </div>
      <div class="mapwrap">{MAP}</div>
    </aside>
  </div>
</section>

</main>
{BRISTLE}
{FOOTER}
{breadcrumb_ld([("Contact", "/contact")])}
</body>
</html>
'''

# ---------------------------------------------------------------- privacy
PAGES["/privacy.html"] = head(
 "Privacy — Cortés Painting Inc, Milwaukie OR",
 "How this site handles the contact form: no cookies, no third-party trackers, nothing served from other companies' servers.", "/privacy") + f'''
{NAV}
{BRISTLE}
<main id="main">

<section class="pagehero">
  <div class="wrap">
    {crumbs([("Privacy", "/privacy")])}
    <p class="eyebrow">Privacy</p>
    <h1>What this site knows about you</h1>
    <p class="deck">Very little, on purpose.</p>
  </div>
</section>

<section class="prose">
  <div class="wrap narrow">
    <h2>The contact form</h2>
    <p>When you send the contact form, {SITE} receives your name, message, and any phone number or email you add — used only to answer you and quote the job. Messages are delivered by email and kept no longer than needed to follow up.</p>
    <h2>No trackers</h2>
    <p>This site loads no third-party scripts and sets no advertising or analytics cookies. The stylesheet, fonts and images are all served from this site itself. Nothing about your visit is assembled into a profile.</p>
    <h2>Questions</h2>
    <p>Want something kept or removed from the email trail? Call {PHONE} or write {EMAIL} and say the word.</p>
  </div>
</section>

</main>
{BRISTLE}
{FOOTER}
{breadcrumb_ld([("Privacy", "/privacy")])}
</body>
</html>
'''

# ---------------------------------------------------------------- thanks
PAGES["/thanks.html"] = head(
 "Thanks — Cortés Painting Inc",
 "Your message is on its way to Cortés Painting Inc, Milwaukie Oregon.", "/thanks", util=True) + f'''
{NAV}
{BRISTLE}
<main id="main">

<section class="pagehero">
  <div class="wrap">
    <p class="eyebrow">Sent</p>
    <h1>Your message is on its way</h1>
    <p class="deck">It landed with {BRAND} — watch for the reply.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="cta-row" style="justify-content:flex-start">
      <a class="btn fill" href="/">Back to home</a>
      <a class="btn line dark" href="/services">Browse services</a>
    </div>
  </div>
</section>

</main>
{BRISTLE}
{FOOTER}
</body>
</html>
'''

# ---------------------------------------------------------------- 404
PAGES["/404.html"] = head(
 "Page not found — Cortés Painting Inc",
 "That page is not here. Start over at Cortés Painting Inc, Milwaukie Oregon.", "/404", util=True) + f'''
{NAV}
{BRISTLE}
<main id="main">

<section class="pagehero">
  <div class="wrap">
    <p class="eyebrow">404</p>
    <h1>That page took a wrong turn</h1>
    <p class="deck">The paint is down the hall. Try one of these:</p>
    <div class="cta-row" style="justify-content:flex-start">
      <a class="btn fill" href="/">Home</a>
      <a class="btn line dark" href="/services">Services</a>
      <a class="btn line dark" href="/contact">Contact</a>
    </div>
  </div>
</section>

</main>
{BRISTLE}
{FOOTER}
</body>
</html>
'''

# ---------------------------------------------------------------- robots + sitemap
robots = f"""User-agent: *
Allow: /

Sitemap: {ORIGIN}/sitemap.xml
"""
sitemap_pages = ["/", "/services", "/interior-painting", "/exterior-painting", "/contact", "/privacy"]
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
    "".join(f"  <url><loc>{ORIGIN}{p}</loc></url>\n" for p in sitemap_pages) + "</urlset>\n"

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public")
for path, html in PAGES.items():
    p = os.path.join(out, path.lstrip("/"))
    os.makedirs(os.path.dirname(p) or out, exist_ok=True)
    body = BUILT + html
    open(p, "w", encoding="utf8").write(body)
    print(f"{len(body):>7}  {path}")
open(os.path.join(out, "robots.txt"), "w").write(robots); print(f"{len(robots):>7}  /robots.txt")
open(os.path.join(out, "sitemap.xml"), "w").write(sitemap); print(f"{len(sitemap):>7}  /sitemap.xml")
print("pages:", len(PAGES))
