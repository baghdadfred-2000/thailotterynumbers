# ThaiLotteryNumbers.com

A fast, bilingual (English / ไทย), dark-themed website presenting **20 years of Thai
Government Lottery (GLO) results** with search, statistics, frequency charts, a heat
grid, trend graphs, and a "Did I Win?" ticket checker.

Built as a **static site** — plain HTML, CSS, and JavaScript with the data baked in as
JSON. No server, database, or build step is required, so you can publish it to almost
any host in minutes.

---

## 1. Preview it locally

The site now uses real URLs (e.g. `/results`, `/stats`) instead of `#` links, and it
loads data with `fetch`, so it must be served over HTTP from the project root — not
opened as a `file://` page. Run a tiny local server:

```bash
cd thailotterynumbers
python -m http.server 8000
# then open http://localhost:8000 in your browser
```

Any static server that serves `index.html` from each folder works
(`npx serve`, VS Code "Live Server", etc.).

---

## 2. Publish it to the web

Pick whichever is easiest for you — the site is just a folder of files.

**Netlify (drag & drop, free):** go to app.netlify.com → "Add new site" → "Deploy
manually" → drag the whole `thailotterynumbers` folder onto the page. Done. Point your
`thailotterynumbers.com` domain at it in Site settings → Domain management.

**Vercel:** `npm i -g vercel`, then run `vercel` inside the folder and follow the prompts.

**GitHub Pages:** push the folder to a repo, then Settings → Pages → deploy from the
`main` branch root. (The site uses hash routing, so Pages needs no extra config.)

**Cloudflare Pages / any web host / S3:** upload the folder's contents to your web
root. That's it.

---

## 3. Add a new draw (twice a month)

Results come out on the 1st and 16th. To add one, run the helper and answer the prompts:

```bash
cd thailotterynumbers
python add_draw.py
```

Or do it in one line:

```bash
python add_draw.py --date 2026-06-16 \
  --first 123456 --front3 111 222 --last3 333 444 --last2 55 \
  --near 123455 123457
```

You can also add the lower tiers if you want the checker/search to cover them:
`--second 6-digit... --third ... --fourth ... --fifth ...`

The script writes the draw into `data_src/` and automatically rebuilds the site's data.
Then **re-upload the site** (or just the `assets/data/` folder) to your host and the new
result appears — latest-draw card, countdown, archive, stats, search, and checker all
update automatically.

> No coding needed beyond running that one command. If you'd rather not use the script,
> you can hand-edit a copy of any file in `data_src/` and run `python build_data.py`.

---

## 4. Folder structure

```
thailotterynumbers/
├── index.html              ← homepage (generated, SEO-optimised)
├── results/index.html      ← one real URL per route (generated)
├── stats/index.html
├── search/index.html
├── check/index.html
├── faq/index.html
├── about/index.html
├── privacy/  cookies/  terms/  accessibility/  cookie-settings/   (generated)
├── 404.html                ← SPA fallback for GitHub Pages
├── _redirects              ← SPA fallback for Netlify
├── robots.txt              ← generated
├── sitemap.xml             ← generated
├── assets/
│   ├── styles.css          ← full design system
│   ├── app.js              ← router, views, charts, search, checker, countdown, live update
│   ├── i18n.js             ← English + Thai text
│   ├── chart.umd.js        ← Chart.js (bundled — no CDN needed)
│   ├── logo.svg            ← brand mark
│   ├── og-image.png        ← 1200×630 social/link-preview image
│   └── data/
│       ├── draws.json      ← every draw (generated)
│       └── stats.json      ← precomputed frequencies (generated)
├── data_src/               ← raw source, one .txt per draw (the "database")
├── build_data.py           ← regenerates assets/data/*.json from data_src/
├── build_seo.py            ← regenerates all HTML pages, robots.txt, sitemap.xml
├── add_draw.py             ← add a new draw + rebuild everything (admin tool)
└── README.md
```

> The HTML pages, `robots.txt`, and `sitemap.xml` are produced by `build_seo.py`. Don't
> hand-edit the generated `index.html` files; change the copy/metadata in `build_seo.py`
> (or the views in `assets/app.js`) and re-run it.

---

## 5. Features

- **Latest draw** card with full prize breakdown, the **payout for each match**
  (฿6,000,000 first prize down to ฿2,000 for the last-2), and a live **countdown** to
  the next official draw (1st & 16th, 4:00 PM Bangkok time).
- **Live auto-update.** Every time the page loads it quietly checks the public results
  archive for any draw newer than the data bundled with the site, fetches it, and merges
  it in — so the site is never a stale static page. If nothing newer exists yet, or the
  visitor is offline, it simply shows the bundled data. (See section 8.)
- **"What each match pays"** — the full official GLO prize table.
- **Last 10 draws**, each clickable to a detail page with all prize tiers.
- **Results archive** — every draw, filterable by year, paginated, CSV export.
- **Number search** — enter a 2-, 3-, or 6-digit number to see every winning appearance
  and which prize tier it hit.
- **Did I Win?** — enter a 6-digit ticket to scan first prize, adjacent, 2nd–5th, and
  front-3 / last-3 / last-2 matches across all draws.
- **Statistics hub** — frequency charts for last-2, front-3, and last-3 numbers, a
  hot/cold panel, a 00–99 heat grid, and a per-number **trend-over-time** graph, all
  filterable by year range.
- **Side ad slots** ready for Google AdSense (see section 9).
- **Bilingual** English / Thai toggle (with Buddhist-era dates in Thai).
- Premium dark theme, responsive to mobile, keyboard-accessible, reduced-motion aware.
- Legal pages: Privacy, Cookie Policy, Terms & Disclaimer, Cookie Settings,
  Accessibility. A discreet disclaimer sits in the footer of every page.

---

## 6. Design system

- **Base** midnight indigo `#0B1026` · **panels** `#141A38`
- **Temple gold** `#F2C14E` (winning numbers) · **flag red** `#EF3340` (live/alerts) ·
  **jade** `#2BB7A3` (chart accent) · white text `#F5F7FA`
- **Type** Kanit (display) · Sarabun (body — the Thai government's document typeface) ·
  Space Mono (numbers)
- **Signature** the Thai flag's five-stripe motif recurs as section rules and the
  draw-card accent bar, paired with a gold *kanok* ornamental flourish.

To rebrand colors, edit the `:root` variables at the top of `assets/styles.css`.

---

## 8. How live auto-updating works

On load, the site computes which draw dates *should* exist after its bundled data (the
1st and 16th of each month up to today) and fetches just those files directly from the
public archive
(`raw.githubusercontent.com/vicha-w/thai-lotto-archive`). Anything found is merged in and
all statistics recompute in the browser. No server or API key is involved, and it never
asks for a draw that hasn't happened yet.

This means a freshly published draw can appear on your live site **without you doing
anything**. Two practical notes:

- It depends on that public archive being kept current by its maintainer. If you want a
  guarantee, use `add_draw.py` (section 3) to bundle the official numbers yourself — that
  always wins and is what visitors see instantly.
- To point at a different source, change the `ARCHIVE` constant near the bottom of
  `assets/app.js`.

---

## 9. Google ad slots

The layout reserves a 160-px ad rail on each side of the content (visible on screens
wider than ~1380 px; hidden on tablet/mobile). To turn them into live Google AdSense
units:

1. Add your AdSense loader once in `index.html`, just before `</head>`:
   ```html
   <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXXXXXXXX" crossorigin="anonymous"></script>
   ```
2. In `index.html`, replace the contents of each `<div class="ad-slot" ...>` with your
   ad unit, e.g.:
   ```html
   <ins class="adsbygoogle" style="display:block;width:160px;height:600px"
        data-ad-client="ca-pub-XXXXXXXXXXXXXXXX" data-ad-slot="0000000000"></ins>
   <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
   ```

Until then they show neutral "Advertisement" placeholders. You can also drop an in-content
banner anywhere by adding your own `<ins class="adsbygoogle">` block. (Note: AdSense
approval and a privacy/cookie disclosure are your responsibility — the Cookie Policy page
is written for an ad-free baseline, so update it if you enable personalised ads.)

---

## 10. SEO (Google-first)

The site is built for Google: every route is a **real, crawlable URL** with its own
optimised `<head>`, not a `#` fragment.

What's included:

- **Real URLs + static pages.** Each route (`/`, `/results`, `/stats`, `/search`,
  `/check`, `/faq`, `/about`, and the legal pages) is a physical `folder/index.html`
  with a unique `<title>`, meta description, canonical tag, Open Graph + Twitter cards,
  and crawlable pre-rendered intro text. The app then hydrates the interactive UI on top.
  Direct loads and Google crawling both work with no server config on Netlify, GitHub
  Pages, Vercel, or Cloudflare Pages.
- **Structured data (JSON-LD)** on every page: `Organization`, `WebSite` (with a
  `SearchAction` for sitelinks search), `WebPage`, and `BreadcrumbList`. The **FAQ page**
  also emits `FAQPage` schema — strong for rich results and Google AI Overviews.
- **One H1 per page**, logical heading order, and a new **FAQ page** answering the
  highest-intent questions (draw times, prize amounts, how to check).
- **`robots.txt`** (allows Google + major AI answer engines, points to the sitemap) and
  **`sitemap.xml`** (all indexable URLs with priorities and lastmod).
- **`og-image.png`** (1200×630) for link previews.
- **Core Web Vitals touches:** scripts deferred, fonts preconnected with `display=swap`,
  Chart.js bundled locally (no render-blocking CDN), and the logo as inline SVG.
- **E-E-A-T:** named publisher (Genext Information Systems), last-updated dates in schema,
  and an authoritative outbound link to the official GLO site on the About page.

**Regenerate after copy/page changes:** `python build_seo.py` rewrites every page,
`robots.txt`, and `sitemap.xml`. (Output is committed, so visitors never run anything.)

**One-time Google Search Console steps after you deploy:**

1. Verify the property for `https://thailotterynumbers.com` (DNS or HTML tag).
2. In GSC → Sitemaps, submit `https://thailotterynumbers.com/sitemap.xml`.
3. Use URL Inspection → Request indexing for the homepage and each key page.
4. Watch the Pages (coverage), Core Web Vitals, and Rich Results reports.
5. Run the homepage and `/faq` through the Rich Results Test and PageSpeed Insights.
6. Link Google Analytics 4 to Search Console for query/traffic data.

> Heads-up: because the bilingual EN/Thai switch happens in-browser on the same URL,
> there are no separate Thai URLs to declare with `hreflang`. If Thai-language search
> traffic becomes a priority later, the cleanest upgrade is separate `/th/...` pages —
> ask and I can generate them.

---

## 11. Data & disclaimer

Draw data is compiled from official GLO announcements and reliable public records. The
**front-3-digit prize only exists from 1 September 2015 onward**; before that each draw
had four last-3-digit winners. The site handles both formats.

This site is **for entertainment and information only**. It is **not affiliated with the
Government Lottery Office (GLO)** or any Thai government body. Every draw is independent —
historical frequency does not change future odds. Always verify numbers with official
sources.

© 2026 Genext Information Systems. All rights reserved.
