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

EDITORIAL = "By the ThaiLotteryNumbers editorial team · Genext Information Systems"

# Article content lives in article_content.py (one entry per guide page).
from article_content import ARTICLES

def article_canonical(a):
    return f"{SITE}/guides/{a['slug']}"

# Cards for the Guides index, newest first (bilingual; falls back to EN)
def guide_cards(lang):
    cards = []
    for a in sorted(ARTICLES, key=lambda x: x["updated"], reverse=True):
        if lang == "th":
            cat = a.get("category_th", a["category"]); h1 = a.get("h1_th", a["h1"])
            desc = a.get("desc_th", a["desc"]); upd = "ปรับปรุง " + a["updated"]
        else:
            cat = a["category"]; h1 = a["h1"]; desc = a["desc"]; upd = "Updated " + a["updated"]
        cards.append(
            f'<a class="guide-card" href="/guides/{a["slug"]}">'
            f'<span class="gc-cat">{cat}</span>'
            f'<div class="gc-title">{h1}</div>'
            f'<div class="gc-desc">{desc}</div>'
            f'<div class="gc-date">{upd}</div></a>')
    return "\n".join(cards)

EDITORIAL_TH = "โดยทีมบรรณาธิการ ThaiLotteryNumbers · Genext Information Systems"

BLOG_INDEX_TITLE = "Thai Lottery Guides — How It Works, Claiming & Stats | ThaiLotteryNumbers"
BLOG_INDEX_DESC = ("Plain-language guides to the Thai Government Lottery: how draws work, how prizes "
                   "are claimed, how to read the statistics responsibly, and Thai number culture.")

BLOG_INDEX_EN = """      <span class="eyebrow">Guides</span>
      <h1>Thai Lottery Guides</h1>
      <p class="lead">Plain-language guides to how the Thai Government Lottery works, how prizes are claimed, and how to read the statistics responsibly. Everything here is educational — never a prediction of results.</p>
      <h3>How the lottery works</h3>
      <p>Draws take place twice a month, on the 1st and the 16th at around 4:00 PM Bangkok time. Prizes range from the first prize (฿6,000,000 per ticket) down to the last-two digits (฿2,000). Browse every draw in our <a href="/results">results archive</a>.</p>
      <h3>Checking &amp; claiming prizes</h3>
      <p>Small prizes can be paid by authorised vendors, while large prizes are claimed at the Government Lottery Office with photo ID and the original ticket. Check your number first with our <a href="/check">Did I Win? checker</a>, then confirm with the <a href="https://www.glo.or.th" target="_blank" rel="noopener nofollow">GLO</a>.</p>
      <h3>Understanding the numbers</h3>
      <p>Frequency statistics — &ldquo;hot&rdquo; and &ldquo;cold&rdquo; numbers — are interesting but cannot predict results, because every draw is independent and random. Explore our <a href="/stats">statistics</a> and <a href="/search">number search</a>.</p>
      <h3>Playing responsibly</h3>
      <p>The lottery is entertainment, not an investment. Play within your means and always set a limit. If it ever becomes a problem, support is available — read our <a href="/responsible-play">Responsible Play</a> guidance.</p>"""

BLOG_INDEX_TH = """      <span class="eyebrow">คู่มือ</span>
      <h1>คู่มือสลากกินแบ่งรัฐบาล</h1>
      <p class="lead">คู่มือภาษาที่เข้าใจง่ายเกี่ยวกับการทำงานของสลากกินแบ่งรัฐบาล วิธีขึ้นเงินรางวัล และวิธีอ่านสถิติอย่างถูกต้อง เนื้อหาทั้งหมดเพื่อการศึกษา ไม่ใช่การทำนายผลรางวัล</p>
      <h3>วิธีการทำงานของสลาก</h3>
      <p>การออกรางวัลมีเดือนละสองครั้ง คือวันที่ 1 และ 16 เวลาประมาณ 16:00 น. ตามเวลาประเทศไทย รางวัลมีตั้งแต่รางวัลที่ 1 (฿6,000,000 ต่อใบ) ไปจนถึงเลขท้าย 2 ตัว (฿2,000) ดูผลทุกงวดได้ที่ <a href="/results">คลังผลรางวัล</a></p>
      <h3>การตรวจและขึ้นเงินรางวัล</h3>
      <p>รางวัลเล็กขึ้นเงินได้กับตัวแทนจำหน่าย ส่วนรางวัลใหญ่ต้องขึ้นที่สำนักงานสลากกินแบ่งรัฐบาลพร้อมบัตรประชาชนและสลากตัวจริง ตรวจหมายเลขของคุณก่อนได้ที่ <a href="/check">เครื่องตรวจสลาก</a> แล้วยืนยันกับ <a href="https://www.glo.or.th" target="_blank" rel="noopener nofollow">GLO</a></p>
      <h3>ทำความเข้าใจตัวเลข</h3>
      <p>สถิติความถี่ — เลข &ldquo;ร้อน&rdquo; และ &ldquo;เย็น&rdquo; — น่าสนใจแต่ทำนายผลไม่ได้ เพราะทุกงวดเป็นอิสระและสุ่ม สำรวจได้ที่ <a href="/stats">สถิติ</a> และ <a href="/search">ค้นหาหมายเลข</a></p>
      <h3>เล่นอย่างมีสติ</h3>
      <p>สลากคือความบันเทิง ไม่ใช่การลงทุน เล่นเท่าที่ไหวและตั้งวงเงินเสมอ หากเริ่มเป็นปัญหา มีแหล่งช่วยเหลืออยู่ — อ่านแนวทางได้ที่หน้า <a href="/responsible-play">เล่นอย่างมีสติ</a></p>"""

# slug, title, description (<=160), h1, intro paragraph(s), priority, changefreq, flags
PAGES = [
 dict(slug="", title="Thai Lottery Results & Winning Number Statistics | ThaiLotteryNumbers.com",
   desc="Check the latest Thai Government Lottery results, search 20 years of winning numbers, view hot & cold stats, and see if your ticket won. Free, updated every draw.",
   h1="Thai Lottery Results & Winning Number Statistics",
   intro=[
     "ThaiLotteryNumbers.com is a free, independent reference for the Thai Government Lottery (GLO). We publish each official result as soon as it is announced and pair it with roughly 20 years of historical draws — from 2006 to today — so you can look up any past number, study how often it has appeared, and check whether a ticket has ever matched a prize.",
     "The Thai Government Lottery is drawn twice a month, on the 1st and the 16th at around 4:00 PM Bangkok time. The first prize pays 6,000,000 baht per ticket, with further prizes for the adjacent numbers, the second through fifth tiers, and the front-three, last-three and last-two digits. Our tools cover every tier: browse the full results archive, search any 2-, 3-, or 6-digit number, explore frequency statistics, and use the &ldquo;Did I Win?&rdquo; checker.",
     "Everything here is for information and entertainment only. We are not affiliated with the Government Lottery Office, we do not sell tickets, and our statistics are not a prediction — every draw is independent and random, so past frequency never changes future odds. Always verify any result against official GLO sources, and please see our Responsible Play guidance before you take part.",
   ],
   priority="1.0", changefreq="daily"),
 dict(slug="results", title="Thai Lottery Results History — 20 Years of Draws | ThaiLotteryNumbers",
   desc="Browse every Thai Government Lottery draw from 2006 to today. Filter by year, view full prize breakdowns, and export to CSV. Updated every official draw.",
   h1="Thai Lottery Results History (2006–Present)",
   intro=[
     "Browse the complete archive of Thai Government Lottery draws from 2006 to today. Filter results by year and open any draw to see the full prize breakdown — first prize, the two adjacent numbers, the second to fifth prizes, and the front-three, last-three and last-two digits — exactly as announced by the Government Lottery Office.",
     "Each draw record can be exported to CSV for your own analysis, and the archive updates automatically after every official draw on the 1st and 16th of the month. Because the front-three prize was only introduced on 1 September 2015, draws before that date do not list a front-three figure.",
     "Results are compiled from official GLO announcements and reliable public records and are provided for information only. Always confirm a number against the official source before acting on it.",
   ],
   priority="0.9", changefreq="daily"),
 dict(slug="stats", title="Thai Lottery Statistics — Hot & Cold Numbers | ThaiLotteryNumbers",
   desc="Thai lottery statistics from 20 years of draws: frequency charts for 2- and 3-digit numbers, hot and cold numbers, a 00–99 heat grid, and trends over time.",
   h1="Thai Lottery Statistics: Hot & Cold Numbers",
   intro=[
     "Explore Thai lottery statistics drawn from the full 20-year dataset. Compare how often every last-two, front-three and last-three number has been drawn, see the hottest and coldest numbers at a glance, scan the 00–99 heat grid, and chart how any single number's frequency has changed year by year.",
     "These figures are a descriptive record of what has already happened — nothing more. Over a large enough sample the distribution looks essentially random, which is exactly what you would expect from a fair draw. A &ldquo;hot&rdquo; number is simply one that has come up more often in the past; it carries no greater chance of being drawn next time.",
     "We present these statistics for interest and education, never as a prediction system. Every draw is independent: past frequency does not change future odds. If you are new to this idea, our Guides explain the probability behind it in plain language.",
   ],
   priority="0.8", changefreq="weekly"),
 dict(slug="search", title="Thai Lottery Number Search — Check Any Number | ThaiLotteryNumbers",
   desc="Search any 2-, 3-, or 6-digit number across 20 years of Thai lottery draws and see every time it won and in which prize tier. Fast, free and ad-light.",
   h1="Thai Lottery Number Search",
   intro=[
     "Enter any 2-, 3-, or 6-digit number to find every time it has appeared as a winner across 20 years of Thai Government Lottery draws, along with the prize tier it matched and the date of the draw.",
     "Searching a two-digit number checks the last-two-digit prize; a three-digit number checks the front-three and last-three prizes; and a six-digit number is matched against the first prize, the adjacent numbers and the second to fifth prizes. It is a fast way to see the full history behind a number that matters to you.",
     "A number's past appearances are a historical record only and do not make it any more or less likely to be drawn in future. The search is for interest and information; always verify any result with the official Government Lottery Office.",
   ],
   priority="0.8", changefreq="weekly"),
 dict(slug="check", title="Did I Win? Thai Lottery Ticket Checker | ThaiLotteryNumbers.com",
   desc="Enter your 6-digit Thai lottery ticket number to instantly check it against every prize tier across 20 years of Government Lottery draws. Free ticket checker.",
   h1="Did I Win? Thai Lottery Ticket Checker",
   intro=[
     "Type your six-digit Thai Government Lottery ticket number to instantly check it against every prize tier — the first prize, the two adjacent numbers, the second to fifth prizes, and the front-three, last-three and last-two digits — across 20 years of draws.",
     "The checker shows any tier your number has ever matched and on which draw date, so you can see its full prize history in seconds. It runs entirely in your browser; nothing about your ticket is stored or sent anywhere.",
     "This tool is for convenience and information only. A match in our archive is not an official confirmation — always verify a win with the Government Lottery Office, which alone can confirm and pay prizes.",
   ],
   priority="0.8", changefreq="weekly"),
 dict(slug="faq", title="Thai Lottery FAQ — Draw Times, Prizes & Checking | ThaiLotteryNumbers",
   desc="Answers to common Thai lottery questions: when draws happen, how much the first prize and smaller prizes pay, and how to check whether your ticket won.",
   h1="Thai Lottery FAQ",
   intro="Quick, reliable answers to the most common questions about the Thai Government Lottery — when draws take place, how much each prize pays, how to check your ticket, and whether past results can predict future numbers.",
   priority="0.7", changefreq="monthly", faq=True),
 dict(slug="responsible-play", title="Responsible Play — Thai Lottery | ThaiLotteryNumbers.com",
   desc="The Thai lottery is entertainment, not an investment. Understand the odds, play within your means, and find problem-gambling support, including Thailand's DMH 1323 hotline.",
   h1="Responsible Play",
   priority="0.5", changefreq="yearly",
   body="""      <p class="lead">ThaiLotteryNumbers.com is an informational and educational resource. We publish official Government Lottery Office (GLO) results, historical records, and statistics so the public can look up and understand draws that have already happened. We are not a gambling operator, we do not sell tickets, and nothing on this site is a prediction or a recommendation to play.</p>
      <h3>The lottery is entertainment, not an investment</h3>
      <p>The Thai Government Lottery is a game of chance. Every draw is independent and random. No pattern, &ldquo;hot&rdquo; number, or historical frequency changes the odds of any number being drawn next — and anyone claiming to predict winning numbers is mistaken or misleading you. Treat any money spent on tickets as the cost of entertainment, never as a way to make money or solve financial problems.</p>
      <h3>Play within your means</h3>
      <ul>
        <li>Only ever spend money you can comfortably afford to lose.</li>
        <li>Set a personal limit before you buy, and never chase losses.</li>
        <li>Lottery spending should never come before essentials, savings, or family needs.</li>
        <li>Buying more tickets does not meaningfully improve your odds of the top prize.</li>
      </ul>
      <h3>Understanding the odds</h3>
      <p>Matching all six digits for the first prize is extremely unlikely on any single ticket. We explain the real probabilities in plain language in our <a href="/guides">guides</a> so you can make informed, realistic decisions. Understanding the odds is the single best protection against unrealistic expectations.</p>
      <h3>Protecting yourself and others</h3>
      <p>Gambling should stay fun. If it stops being fun — if you feel you can&rsquo;t stop, if you&rsquo;re spending more than you intended, hiding it, or borrowing to play — that is a sign to seek support. These feelings are common and help is available.</p>
      <h3>Where to get help (Thailand)</h3>
      <p>If you or someone you know may have a gambling problem, you can talk to a professional in confidence. In Thailand, the Department of Mental Health hotline <b>1323</b> offers free, 24-hour mental-health support. Your doctor or a local hospital can also refer you to counselling services.</p>
      <p class="muted">(If you are outside Thailand, please seek a local problem-gambling support service in your country.)</p>
      <h3>Minors</h3>
      <p>The lottery is for adults only. This site is not intended for anyone under 18.</p>
      <p class="muted" style="margin-top:18px">For entertainment and informational purposes only. Not affiliated with the Government Lottery Office. Always verify results with official sources.</p>"""),
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
   body="""      <p class="lead">These Terms govern your use of ThaiLotteryNumbers.com. The site is provided for entertainment and information only and is not affiliated with the Government Lottery Office.</p>
      <h3>Entertainment &amp; information only</h3>
      <p>For entertainment and information only. Not affiliated with the Government Lottery Office (GLO) or any Thai government body. Always verify numbers against official sources.</p>
      <h3>Responsible play</h3>
      <p>This site is for entertainment and information only and is intended for adults (18+). Nothing here is gambling advice, a betting strategy, or a prediction of future results. The lottery is a game of chance; past results never influence future draws. If gambling stops being enjoyable, please see our <a href="/responsible-play">Responsible Play</a> page for guidance and support resources.</p>
      <h3>No facilitation of gambling</h3>
      <p>We do not sell lottery tickets, accept payments or wagers, or link to any service that does. Links to the Government Lottery Office are provided solely so you can verify official results.</p>
      <h3>Accuracy and official results</h3>
      <p>We compile results from official GLO announcements and reliable public records and correct errors promptly, but we provide all data &ldquo;as is&rdquo; without warranty. Before claiming any prize, you must verify your numbers against the official Government Lottery Office results. We cannot confirm wins or pay prizes.</p>
      <h3>Limitation of liability</h3>
      <p>To the maximum extent permitted by law, Genext Information Systems is not liable for any loss arising from reliance on information presented here.</p>""",
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

def article_schema(a):
    can = article_canonical(a)
    items = [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
        {"@type": "ListItem", "position": 2, "name": "Guides", "item": f"{SITE}/guides"},
        {"@type": "ListItem", "position": 3, "name": a["h1"], "item": can},
    ]
    webpage = {
        "@type": "WebPage", "@id": can + "#webpage", "url": can,
        "name": a["title"], "description": a["desc"],
        "isPartOf": {"@id": f"{SITE}/#website"}, "inLanguage": "en",
        "dateModified": a["updated"], "publisher": {"@id": f"{SITE}/#org"},
        "breadcrumb": {"@type": "BreadcrumbList", "itemListElement": items},
    }
    article = {
        "@type": "Article", "@id": can + "#article",
        "headline": a["h1"], "description": a["desc"],
        "datePublished": a["published"], "dateModified": a["updated"],
        "author": {"@type": "Organization", "name": "ThaiLotteryNumbers editorial team", "url": SITE},
        "publisher": {"@id": f"{SITE}/#org"},
        "mainEntityOfPage": {"@id": can + "#webpage"},
        "isPartOf": {"@id": f"{SITE}/#website"}, "inLanguage": "en",
    }
    graph = [ORG, WEBSITE, webpage, article]
    if a.get("howto"):
        graph.append({
            "@type": "HowTo", "name": a["h1"], "description": a["desc"],
            "step": [{"@type": "HowToStep", "position": i + 1, "name": nm, "text": tx}
                     for i, (nm, tx) in enumerate(a["howto"])],
        })
    if a.get("faq"):
        graph.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": ans}} for q, ans in a["faq"]]})
    return json.dumps({"@context": "https://schema.org", "@graph": graph},
                      ensure_ascii=False, separators=(",", ":"))

def _article_block(a, lang):
    th = lang == "th"
    h1 = a.get("h1_th", a["h1"]) if th else a["h1"]
    body = a.get("body_th", a["body"]) if th else a["body"]
    faq = a.get("faq_th", a.get("faq")) if th else a.get("faq")
    home, guides_l = ("หน้าแรก", "คู่มือ") if th else ("Home", "Guides")
    editor = EDITORIAL_TH if th else EDITORIAL
    updated_l = "ปรับปรุงล่าสุด" if th else "Last updated"
    faq_head = "คำถามที่พบบ่อย" if th else "Frequently asked questions"
    crumb = ('      <nav class="crumb" aria-label="Breadcrumb">'
             f'<a href="/">{home}</a><span>&rsaquo;</span>'
             f'<a href="/guides">{guides_l}</a><span>&rsaquo;</span>{h1}</nav>')
    head = (f'      <h1>{h1}</h1>\n'
            f'      <p class="byline"><b>{editor}</b><br>{updated_l}: {a["updated"]}</p>')
    faq_html = ""
    if faq:
        items = "\n".join(
            f'        <details class="faq-item"><summary>{q}</summary>'
            f'<div class="faq-a">{ans}</div></details>' for q, ans in faq)
        faq_html = (f'\n      <h3>{faq_head}</h3>\n'
                    f'      <div class="faq-list">\n{items}\n      </div>')
    inner = crumb + "\n" + head + "\n" + body.rstrip() + faq_html
    cls = "lang-th" if th else "lang-en"
    return f'  <div class="{cls}">\n{inner}\n  </div>'

def article_main(a):
    return ('    <section class="section wrap prose">\n'
            + _article_block(a, "en") + "\n"
            + _article_block(a, "th") + "\n"
            + '    </section>')


HEAD = """<!DOCTYPE html>
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
</head>"""

_SPA_BODY = """
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
{main}
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
      <span>© 2026 Genext Information Systems. All rights reserved. · V1.0</span>
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

TEMPLATE = HEAD + _SPA_BODY

_BLOG_BODY = """
<body>
<header class="nav">
  <div class="wrap nav-inner">
    <a class="brand" href="/" aria-label="Thai Lottery Numbers home">
      <span class="logo-slot"><img src="/assets/logo.svg" alt="" width="34" height="34"></span>
      <span class="bn">Thai Lottery<b>Numbers</b><small>.com</small></span>
    </a>
    <button class="burger" aria-label="Menu">☰</button>
    <nav class="nav-links">
      <a href="/"><span class="lang-en">Home</span><span class="lang-th">หน้าแรก</span></a>
      <a href="/results"><span class="lang-en">Results</span><span class="lang-th">ผลรางวัล</span></a>
      <a href="/stats"><span class="lang-en">Statistics</span><span class="lang-th">สถิติ</span></a>
      <a href="/search"><span class="lang-en">Search</span><span class="lang-th">ค้นหา</span></a>
      <a href="/check"><span class="lang-en">Did I Win?</span><span class="lang-th">ฉันถูกไหม?</span></a>
      <a href="/guides" class="active"><span class="lang-en">Guides</span><span class="lang-th">คู่มือ</span></a>
      <a href="/faq"><span class="lang-en">FAQ</span><span class="lang-th">คำถามที่พบบ่อย</span></a>
      <a href="/about"><span class="lang-en">About</span><span class="lang-th">เกี่ยวกับ</span></a>
      <a href="/contact"><span class="lang-en">Contact</span><span class="lang-th">ติดต่อ</span></a>
    </nav>
    <div class="lang-toggle" role="group" aria-label="Language">
      <button data-lang="en" class="on">EN</button>
      <button data-lang="th">ไทย</button>
    </div>
  </div>
</header>

<div class="layout">
  <aside class="ad-rail ad-left" aria-hidden="true">
    <!-- Google AdSense slot (left). Paste your <ins class="adsbygoogle"> code inside. -->
    <div class="ad-slot" data-ad="left" data-label="Advertisement"></div>
  </aside>
  <main id="view">
{main}
  </main>
  <aside class="ad-rail ad-right" aria-hidden="true">
    <!-- Google AdSense slot (right). Paste your <ins class="adsbygoogle"> code inside. -->
    <div class="ad-slot" data-ad="right" data-label="Advertisement"></div>
  </aside>
</div>

<footer class="ft">
  <div class="wrap">
    <div class="ft-grid">
      <div>
        <div class="brand" style="margin-bottom:12px"><img src="/assets/logo.svg" alt="" width="30" height="30"><span class="bn">Thai Lottery<b>Numbers</b></span></div>
        <p class="muted" style="font-size:.86rem"><span class="lang-en">Compiled from official GLO announcements and reliable public records.</span><span class="lang-th">รวบรวมจากประกาศทางการของ GLO และบันทึกสาธารณะที่เชื่อถือได้</span></p>
      </div>
      <div><h4><span class="lang-en">Explore</span><span class="lang-th">สำรวจ</span></h4><a href="/results"><span class="lang-en">Results</span><span class="lang-th">ผลรางวัล</span></a><a href="/stats"><span class="lang-en">Statistics</span><span class="lang-th">สถิติ</span></a><a href="/search"><span class="lang-en">Search</span><span class="lang-th">ค้นหา</span></a><a href="/check"><span class="lang-en">Did I Win?</span><span class="lang-th">ฉันถูกไหม?</span></a></div>
      <div><h4><span class="lang-en">Project</span><span class="lang-th">โครงการ</span></h4><a href="/about"><span class="lang-en">About</span><span class="lang-th">เกี่ยวกับ</span></a><a href="/faq"><span class="lang-en">FAQ</span><span class="lang-th">คำถามที่พบบ่อย</span></a><a href="/contact"><span class="lang-en">Contact</span><span class="lang-th">ติดต่อ</span></a></div>
      <div><h4><span class="lang-en">Legal</span><span class="lang-th">กฎหมาย</span></h4><a href="/privacy"><span class="lang-en">Privacy Policy</span><span class="lang-th">นโยบายความเป็นส่วนตัว</span></a><a href="/cookies"><span class="lang-en">Cookie Policy</span><span class="lang-th">นโยบายคุกกี้</span></a><a href="/terms"><span class="lang-en">Terms & Disclaimer</span><span class="lang-th">ข้อกำหนด & ข้อปฏิเสธ</span></a><a href="/responsible-play"><span class="lang-en">Responsible Play</span><span class="lang-th">เล่นอย่างมีสติ</span></a><a href="/cookie-settings"><span class="lang-en">Cookie Settings</span><span class="lang-th">ตั้งค่าคุกกี้</span></a><a href="/accessibility"><span class="lang-en">Accessibility</span><span class="lang-th">การเข้าถึง</span></a></div>
    </div>
    <div class="flag-rule"><i></i><i></i><i></i><i></i><i></i></div>
    <div class="ft-bottom">
      <span>© 2026 Genext Information Systems. All rights reserved. · V1.0</span>
      <span><span class="lang-en">For entertainment &amp; information only. Not affiliated with the Government Lottery Office (GLO). Always verify numbers against official sources.</span><span class="lang-th">เพื่อความบันเทิงและให้ข้อมูลเท่านั้น ไม่มีส่วนเกี่ยวข้องกับสำนักงานสลากกินแบ่งรัฐบาล (GLO) โปรดตรวจสอบหมายเลขกับแหล่งข้อมูลทางการเสมอ</span></span>
    </div>
  </div>
</footer>

<div id="cookieBanner"></div>
<script src="/assets/blog.js" defer></script>
</body>
</html>
"""

BLOG_TEMPLATE = HEAD + _BLOG_BODY

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True) if os.path.dirname(path) else None
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def render_main(p):
    """Static, crawlable content baked into the shell.

    Content pages (with 'body') ship full static HTML; JS hydrates the
    bilingual version on top. Tool/home pages ship a multi-paragraph intro
    plus a 'Loading…' note; JS replaces it with the interactive UI.
    """
    h1 = f'      <h1>{p["h1"]}</h1>'
    if p.get("body"):
        inner = h1 + "\n" + p["body"]
    else:
        intro = p["intro"]
        paras = intro if isinstance(intro, (list, tuple)) else [intro]
        body = "\n".join(f"      <p>{para}</p>" for para in paras)
        loading = ('      <p class="muted" style="font-size:.85rem;margin-top:18px">'
                   'Loading the interactive tools…</p>')
        inner = f"{h1}\n{body}\n{loading}"
    return f'    <section class="seo-intro wrap">\n{inner}\n    </section>'

def blog_index_schema():
    can = f"{SITE}/guides"
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
             {"@type": "ListItem", "position": 2, "name": "Guides", "item": can}]
    page = {"@type": "CollectionPage", "@id": can + "#webpage", "url": can,
            "name": "Thai Lottery Guides", "description": BLOG_INDEX_DESC,
            "isPartOf": {"@id": f"{SITE}/#website"}, "inLanguage": "en",
            "publisher": {"@id": f"{SITE}/#org"},
            "breadcrumb": {"@type": "BreadcrumbList", "itemListElement": items}}
    return json.dumps({"@context": "https://schema.org", "@graph": [ORG, WEBSITE, page]},
                      ensure_ascii=False, separators=(",", ":"))

def blog_index_main():
    en = (BLOG_INDEX_EN + '\n      <h3>Latest guides</h3>\n'
          '      <div class="guide-list">\n' + guide_cards("en") + '\n      </div>')
    th = (BLOG_INDEX_TH + '\n      <h3>คู่มือล่าสุด</h3>\n'
          '      <div class="guide-list">\n' + guide_cards("th") + '\n      </div>')
    return ('    <section class="section wrap prose">\n'
            f'  <div class="lang-en">\n{en}\n  </div>\n'
            f'  <div class="lang-th">\n{th}\n  </div>\n'
            '    </section>')

def build_blog():
    # Blog index (/guides) — standalone, bilingual, no SPA engine
    html = BLOG_TEMPLATE.format(
        title=BLOG_INDEX_TITLE, desc=BLOG_INDEX_DESC, robots="index, follow",
        canonical=f"{SITE}/guides", site=SITE, schema=blog_index_schema(),
        main=blog_index_main())
    write(os.path.join(HERE, "guides", "index.html"), html)
    print("wrote guides/index.html (blog index)")
    # Articles
    for a in ARTICLES:
        html = BLOG_TEMPLATE.format(
            title=a["title"], desc=a["desc"], robots="index, follow",
            canonical=article_canonical(a), site=SITE, schema=article_schema(a),
            main=article_main(a))
        out = os.path.join(HERE, "guides", a["slug"], "index.html")
        write(out, html)
        print("wrote", os.path.relpath(out, HERE))

def build_pages():
    for p in PAGES:
        robots = "noindex, follow" if p.get("noindex") else "index, follow"
        html = TEMPLATE.format(
            title=p["title"], desc=p["desc"], robots=robots,
            canonical=canonical(p["slug"]), site=SITE, schema=schema_for(p),
            main=render_main(p),
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
    urls.append((f"{SITE}/guides", TODAY, "weekly", "0.7"))   # blog index
    for a in ARTICLES:
        urls.append((article_canonical(a), a["updated"], "monthly", "0.6"))
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
    build_blog()
    build_robots()
    build_sitemap()
    print("\nSEO build complete.")
