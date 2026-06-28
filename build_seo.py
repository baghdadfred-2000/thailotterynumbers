#!/usr/bin/env python3
"""
Generate SEO-optimised static HTML pages (one real URL per route), plus
robots.txt and sitemap.xml, for thailotterynumbers.com.

Each page ships a unique <title>, meta description, canonical, Open Graph /
Twitter tags and JSON-LD structured data, with crawlable pre-rendered intro
content. The same app.js then hydrates the interactive UI on top.

Run after changing page copy or adding draws:
    python build_seo.py
(The output is committed to the repo, so visitors never need to run anything.)
"""
import os, json, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://thailotterynumbers.com"
TODAY = datetime.date.today().isoformat()

# try to use the real latest-draw date for lastmod on dynamic pages
try:
    draws = json.load(open(os.path.join(HERE, "assets", "data", "draws.json")))
    LATEST = draws[0]["date"]
except Exception:
    LATEST = TODAY

ORG = {
    "@type": "Organization", "@id": f"{SITE}/#org",
    "name": "Genext Information Systems",
    "url": SITE,
    "logo": {"@type": "ImageObject", "url": f"{SITE}/assets/logo.svg"},
}
WEBSITE = {
    "@type": "WebSite", "@id": f"{SITE}/#website",
    "url": f"{SITE}/", "name": "Thai Lottery Numbers",
    "publisher": {"@id": f"{SITE}/#org"},
    "inLanguage": ["en", "th"],
    "potentialAction": {
        "@type": "SearchAction",
        "target": {"@type": "EntryPoint", "urlTemplate": f"{SITE}/search?q={{search_term_string}}"},
        "query-input": "required name=search_term_string",
    },
}

# slug, title, description (<=160), h1, intro paragraph(s), priority, changefreq, flags
PAGES = [
 dict(slug="", title="Thai Lottery Results & Winning Number Statistics | ThaiLotteryNumbers.com",
   desc="Check the latest Thai Government Lottery results, search 20 years of winning numbers, view hot & cold stats, and see if your ticket won. Free, updated every draw.",
   h1="Thai Lottery Results & Winning Number Statistics",
   intro="See the latest Thai Government Lottery (GLO) results as soon as they are published, then explore 20 years of winning numbers. Search any 2-, 3-, or 6-digit number, study hot and cold statistics, and check whether your ticket has ever won — all free and updated automatically every draw.",
   priority="1.0", changefreq="daily"),
 dict(slug="results", title="Thai Lottery Results History — 20 Years of Draws | ThaiLotteryNumbers",
   desc="Browse every Thai Government Lottery draw from 2006 to today. Filter by year, view full prize breakdowns, and export to CSV. Updated every official draw.",
   h1="Thai Lottery Results History (2006–Present)",
   intro="Browse the complete archive of Thai Government Lottery draws from 2006 to today. Filter results by year, open any draw to see the full prize breakdown — first prize, adjacent numbers, second to fifth prizes, front three, last three and last two digits — and export the data to CSV.",
   priority="0.9", changefreq="daily"),
 dict(slug="stats", title="Thai Lottery Statistics — Hot & Cold Numbers | ThaiLotteryNumbers",
   desc="Thai lottery statistics from 20 years of draws: frequency charts for 2- and 3-digit numbers, hot and cold numbers, a 00–99 heat grid, and trends over time.",
   h1="Thai Lottery Statistics: Hot & Cold Numbers",
   intro="Explore Thai lottery statistics drawn from the full 20-year dataset. Compare how often every last-two, front-three and last-three number has been drawn, see the hottest and coldest numbers, scan the 00–99 heat grid, and chart how any number's frequency has changed over time.",
   priority="0.8", changefreq="weekly"),
 dict(slug="search", title="Thai Lottery Number Search — Check Any Number | ThaiLotteryNumbers",
   desc="Search any 2-, 3-, or 6-digit number across 20 years of Thai lottery draws and see every time it won and in which prize tier. Fast, free and ad-light.",
   h1="Thai Lottery Number Search",
   intro="Enter any 2-, 3-, or 6-digit number to find every time it has appeared as a winner across 20 years of Thai Government Lottery draws, together with the prize tier it matched and the draw date.",
   priority="0.8", changefreq="weekly"),
 dict(slug="check", title="Did I Win? Thai Lottery Ticket Checker | ThaiLotteryNumbers.com",
   desc="Enter your 6-digit Thai lottery ticket number to instantly check it against every prize tier across 20 years of Government Lottery draws. Free ticket checker.",
   h1="Did I Win? Thai Lottery Ticket Checker",
   intro="Type your six-digit Thai Government Lottery ticket number to instantly check it against every prize tier — first prize, adjacent numbers, second to fifth prizes, and the front-three, last-three and last-two digits — across 20 years of draws. Always confirm any win with the official Government Lottery Office before claiming.",
   priority="0.8", changefreq="weekly"),
 dict(slug="faq", title="Thai Lottery FAQ — Draw Times, Prizes & Checking | ThaiLotteryNumbers",
   desc="Answers to common Thai lottery questions: when draws happen, how much the first prize and smaller prizes pay, and how to check whether your ticket won.",
   h1="Thai Lottery FAQ",
   intro="Quick, reliable answers to the most common questions about the Thai Government Lottery — when draws take place, how much each prize pays, how to check your ticket, and whether past results can predict future numbers.",
   priority="0.7", changefreq="monthly", faq=True),
 dict(slug="about", title="About ThaiLotteryNumbers.com — Data Sources & Methodology",
   desc="How ThaiLotteryNumbers.com compiles 20 years of Thai Government Lottery results, our data sources and methodology, and why statistics are for entertainment only.",
   h1="About ThaiLotteryNumbers.com",
   intro="ThaiLotteryNumbers.com compiles roughly 20 years of official Thai Government Lottery results into fast, searchable tools and statistics. Learn where our data comes from, how it is kept current, and why frequency statistics are presented for interest and entertainment rather than prediction.",
   priority="0.5", changefreq="monthly"),
 dict(slug="privacy", title="Privacy Policy | ThaiLotteryNumbers.com",
   desc="How ThaiLotteryNumbers.com handles your data. We use only essential local storage for language and consent — no accounts, no tracking, no selling of data.",
   h1="Privacy Policy", intro="This Privacy Policy explains the limited information ThaiLotteryNumbers.com handles when you visit, how it is used, and the choices you have.",
   priority="0.3", changefreq="yearly"),
 dict(slug="cookies", title="Cookie Policy | ThaiLotteryNumbers.com",
   desc="ThaiLotteryNumbers.com uses only essential cookies and local storage to remember your language and consent choice. No advertising or tracking cookies.",
   h1="Cookie Policy", intro="This Cookie Policy describes the small number of essential local-storage values ThaiLotteryNumbers.com uses and how you can manage them.",
   priority="0.3", changefreq="yearly"),
 dict(slug="terms", title="Terms & Disclaimer | ThaiLotteryNumbers.com",
   desc="Terms of use for ThaiLotteryNumbers.com. This site is for entertainment and information only and is not affiliated with the Government Lottery Office (GLO).",
   h1="Terms & Disclaimer", intro="These Terms govern your use of ThaiLotteryNumbers.com. The site is provided for entertainment and information only and is not affiliated with the Government Lottery Office.",
   priority="0.3", changefreq="yearly"),
 dict(slug="accessibility", title="Accessibility Statement | ThaiLotteryNumbers.com",
   desc="Our commitment to accessibility at ThaiLotteryNumbers.com, including WCAG 2.1 AA goals, keyboard navigation, contrast, and reduced-motion support.",
   h1="Accessibility Statement", intro="ThaiLotteryNumbers.com aims to be usable by everyone and to meet WCAG 2.1 AA guidance. This statement outlines what we do and how to give feedback.",
   priority="0.3", changefreq="yearly"),
 dict(slug="cookie-settings", title="Cookie Settings | ThaiLotteryNumbers.com",
   desc="Review and clear the essential preferences ThaiLotteryNumbers.com stores in your browser.",
   h1="Cookie Settings", intro="Review or clear the essential preferences this site stores in your browser.",
   noindex=True),
]

def canonical(slug):
    return f"{SITE}/" if slug == "" else f"{SITE}/{slug}"

def breadcrumb(slug, h1):
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"}]
    if slug:
        items.append({"@type": "ListItem", "position": 2, "name": h1, "item": canonical(slug)})
    return {"@type": "BreadcrumbList", "itemListElement": items}

def faq_schema():
    qa = [
      ("When is the Thai lottery drawn?",
       "The Thai Government Lottery is drawn twice a month, on the 1st and the 16th, at around 4:00 PM Bangkok time. Some public holidays can shift the date."),
      ("How much is the Thai lottery first prize?",
       "The first prize for matching all six digits is 6,000,000 baht per ticket. As tickets are sold in pairs, a matching pair pays 12,000,000 baht."),
      ("How much do the smaller Thai lottery prizes pay?",
       "The last two digits pay 2,000 baht, the front three and last three digits pay 4,000 baht each, and the second to fifth prizes pay 200,000, 80,000, 40,000 and 20,000 baht. Numbers adjacent to the first prize pay 100,000 baht each."),
      ("How do I check if my Thai lottery ticket won?",
       "Enter your six-digit ticket number in the Did I Win? checker, which scans every prize tier across 20 years of draws. Always confirm against the official Government Lottery Office results before claiming."),
      ("Can past results predict future winning numbers?",
       "No. Every draw is independent and random, so frequency history does not change the odds of any number in the next draw. The statistics are for interest and entertainment only."),
      ("How far back does the data go?",
       "The archive covers roughly 20 years of draws, from 2006 to the present, and new results are added automatically as they are published."),
    ]
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qa]}

def schema_for(p):
    slug, h1 = p["slug"], p["h1"]
    webpage = {
        "@type": "WebPage", "@id": canonical(slug) + "#webpage",
        "url": canonical(slug), "name": p["title"],
        "description": p["desc"], "isPartOf": {"@id": f"{SITE}/#website"},
        "inLanguage": "en", "dateModified": LATEST if slug in ("", "results", "stats") else TODAY,
        "publisher": {"@id": f"{SITE}/#org"},
        "breadcrumb": breadcrumb(slug, h1),
    }
    graph = [ORG, WEBSITE, webpage]
    if p.get("faq"):
        graph.append(faq_schema())
    return json.dumps({"@context": "https://schema.org", "@graph": graph},
                      ensure_ascii=False, separators=(",", ":"))

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#0B1026">
<link rel="icon" href="/assets/logo.svg" type="image/svg+xml">
<meta property="og:site_name" content="Thai Lottery Numbers">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{site}/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_US">
<meta property="og:locale:alternate" content="th_TH">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{site}/assets/og-image.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Kanit:wght@400;500;600;700&family=Sarabun:wght@300;400;500;600&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/styles.css">
<script type="application/ld+json">{schema}</script>
</head>
<body>
<header class="nav">
  <div class="wrap nav-inner">
    <a class="brand" href="/" aria-label="Thai Lottery Numbers home">
      <span class="logo-slot"></span>
      <span class="bn">Thai Lottery<b>Numbers</b><small>.com</small></span>
    </a>
    <button class="burger" aria-label="Menu" onclick="document.querySelector('.nav-links').classList.toggle('open')">☰</button>
    <nav class="nav-links" id="navLinks"></nav>
    <div class="lang-toggle" role="group" aria-label="Language">
      <button data-lang="en" class="on">EN</button>
      <button data-lang="th">ไทย</button>
    </div>
  </div>
</header>

<div class="layout">
  <aside class="ad-rail ad-left" aria-hidden="true">
    <!-- Google AdSense slot (left). Paste your <ins class="adsbygoogle"> code inside. -->
    <div class="ad-slot" data-ad="left"></div>
  </aside>
  <main id="view" aria-live="polite">
    <section class="seo-intro wrap">
      <h1>{h1}</h1>
      <p>{intro}</p>
      <p class="muted" style="font-size:.85rem;margin-top:18px">Loading the interactive tools…</p>
    </section>
  </main>
  <aside class="ad-rail ad-right" aria-hidden="true">
    <!-- Google AdSense slot (right). Paste your <ins class="adsbygoogle"> code inside. -->
    <div class="ad-slot" data-ad="right"></div>
  </aside>
</div>

<footer class="ft">
  <div class="wrap">
    <div class="ft-grid" id="footerGrid"></div>
    <div class="flag-rule"><i></i><i></i><i></i><i></i><i></i></div>
    <div class="ft-bottom">
      <span>© 2026 Genext Information Systems. All rights reserved.</span>
      <span id="ftDisclaimerShort"></span>
    </div>
  </div>
</footer>

<div id="cookieBanner"></div>
<div id="toast" class="toast" style="display:none"></div>

<script src="/assets/chart.umd.js" defer></script>
<script src="/assets/i18n.js" defer></script>
<script src="/assets/app.js" defer></script>
</body>
</html>
"""

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True) if os.path.dirname(path) else None
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def build_pages():
    for p in PAGES:
        robots = "noindex, follow" if p.get("noindex") else "index, follow"
        html = TEMPLATE.format(
            title=p["title"], desc=p["desc"], robots=robots,
            canonical=canonical(p["slug"]), site=SITE, schema=schema_for(p),
            h1=p["h1"], intro=p["intro"],
        )
        out = os.path.join(HERE, "index.html") if p["slug"] == "" \
            else os.path.join(HERE, p["slug"], "index.html")
        write(out, html)
        print("wrote", os.path.relpath(out, HERE))
    # SPA fallback for dynamic URLs (e.g. /results/2026-06-01) on GitHub Pages
    write(os.path.join(HERE, "404.html"),
          open(os.path.join(HERE, "index.html"), encoding="utf-8").read())
    print("wrote 404.html (SPA fallback)")
    # Netlify SPA fallback
    write(os.path.join(HERE, "_redirects"), "/*    /index.html    200\n")
    print("wrote _redirects (Netlify fallback)")

def build_robots():
    txt = f"""# robots.txt for thailotterynumbers.com
User-agent: *
Allow: /
Disallow: /cookie-settings

# Let Google render everything it needs
User-agent: Googlebot
Allow: /
Allow: /assets/

# AI / answer engines (helps visibility in AI Overviews & citations)
User-agent: Google-Extended
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: ChatGPT-User
Allow: /

Sitemap: {SITE}/sitemap.xml
"""
    write(os.path.join(HERE, "robots.txt"), txt)
    print("wrote robots.txt")

def build_sitemap():
    urls = []
    for p in PAGES:
        if p.get("noindex"):
            continue
        lm = LATEST if p["slug"] in ("", "results", "stats") else TODAY
        urls.append((canonical(p["slug"]), lm, p["changefreq"], p["priority"]))
    body = "\n".join(
        f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{lm}</lastmod>\n"
        f"    <changefreq>{cf}</changefreq>\n    <priority>{pr}</priority>\n  </url>"
        for u, lm, cf, pr in urls)
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           f"{body}\n</urlset>\n")
    write(os.path.join(HERE, "sitemap.xml"), xml)
    print("wrote sitemap.xml")

if __name__ == "__main__":
    build_pages()
    build_robots()
    build_sitemap()
    print("\nSEO build complete.")
