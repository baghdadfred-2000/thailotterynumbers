# -*- coding: utf-8 -*-
"""
Article library for the /guides section of thailotterynumbers.com.

Each entry is a fully static guide page rendered by build_seo.py at
/guides/<slug>. To add an article, append a dict here and rerun build_seo.py;
the page, the Guides-index card and the sitemap entry all generate
automatically.

Required keys: slug, title, desc, h1, category, published, updated, body.
Optional keys:
    faq    -> list of (question, answer_html) -> rendered + FAQPage schema
    howto  -> list of (step_name, step_text)  -> HowTo schema

Editorial rules: original, plain-language, factual. Never predictive, never
"numbers to play". Cite official sources (GLO / Revenue Department) for any
claim about money, claiming or tax, and tell readers to verify current figures.
"""

DATE = "2026-06-27"

# ---------------------------------------------------------------------------
# Pillar 3 (flagship) — Understanding the Numbers
# ---------------------------------------------------------------------------
PREDICT = """
      <p class="lead">Hot numbers, &ldquo;due&rdquo; numbers, lucky dreams and paid &ldquo;sure-win&rdquo; systems all promise the same thing: a way to guess the next Thai Government Lottery result. None of them work, and the reason is simple mathematics rather than opinion. Here is the plain-language explanation.</p>

      <h3>Every draw starts from zero</h3>
      <p>The Thai Government Lottery is a game of pure chance. On each draw day the winning numbers are selected at random, and the machine has no memory of any earlier draw. A number that came up last month is neither &ldquo;used up&rdquo; nor &ldquo;warmed up&rdquo; &mdash; it simply has the same chance as every other number, every single time. Statisticians call this <b>independence</b>: each draw is a fresh event, unaffected by the ones before it.</p>
      <p>This is the single most important idea on this page. Once you accept that draws are independent, every prediction system collapses, because they all rely on the past somehow influencing the future. It cannot.</p>

      <h3>The &ldquo;due number&rdquo; trap</h3>
      <p>Suppose a particular last-two-digit number has not appeared for a long time. It feels like it is &ldquo;due&rdquo; &mdash; surely its turn is coming? This feeling is so common that it has a name: the <b>gambler&rsquo;s fallacy</b>. The number is not due. It has exactly the same chance in the next draw as it did in the last one, regardless of how long the gap has been. A coin that lands heads ten times in a row is still a 50/50 coin on the eleventh toss; the coin does not know it &ldquo;owes&rdquo; you a tails.</p>
      <p>The mirror image is just as wrong: believing a recent winner is now &ldquo;hot&rdquo; and likely to repeat. Neither a long absence nor a recent win changes the odds at all.</p>

      <h3>What &ldquo;hot&rdquo; and &ldquo;cold&rdquo; numbers really are</h3>
      <p>Frequency statistics are real and interesting &mdash; they are an honest record of what has already happened. But they describe the past; they do not forecast the future. Over a large number of draws, a fair lottery produces a roughly even spread, with small bumps and dips that are simply normal random variation. The chart below shows how often each last-two-digit number (00&ndash;99) has won the last-two prize across the full archive on this site.</p>
      <figure class="fig">
        <img src="/assets/charts/last2-frequency.svg" alt="Bar chart showing how often each last-two-digit number from 00 to 99 has won the Thai lottery last-two prize; the bars sit close to a flat average line, showing a roughly even, random spread." loading="lazy" width="900" height="380">
        <figcaption>Last-two-digit wins by number across the full archive. The spread is close to flat &mdash; exactly what a fair, random draw produces.</figcaption>
      </figure>
      <p>Notice there is no meaningful pattern: the tallest and shortest bars differ by only a handful of wins out of hundreds of draws, and they are scattered with no structure. A &ldquo;hot&rdquo; number is just one that happens to sit slightly above the average so far. That tells you nothing about the next draw. You can explore the same data yourself on our <a href="/stats/">statistics page</a> and look up any specific number in the <a href="/search/">number search</a>.</p>

      <h3>Your real odds, tier by tier</h3>
      <p>It helps to see the actual numbers. For any single six-digit ticket:</p>
      <ul>
        <li><b>First prize</b> &mdash; your exact six digits must match one specific number out of a million, so the chance is roughly <b>1 in 1,000,000</b>.</li>
        <li><b>Last two digits</b> &mdash; there are 100 possible pairs (00&ndash;99), so about <b>1 in 100</b>. This is why the last-two prize, at &#3647;2,000, is the one most people ever win.</li>
        <li><b>Last three or front three</b> &mdash; each three-digit number is 1 in 1,000; because two numbers are drawn in each of those tiers, your chance of matching one is about <b>1 in 500</b>.</li>
      </ul>
      <p>These odds are fixed by how the draw works. No statistic, system or ritual shifts them by even a fraction. We break every tier down in <a href="/guides/thai-lottery-odds-tier-by-tier/">Understanding Lottery Odds</a>.</p>

      <h3>Why buying more tickets barely moves the needle</h3>
      <p>Buying additional tickets does increase your absolute chance &mdash; but from almost nothing to slightly more than almost nothing. Ten different six-digit numbers raise your first-prize chance to about 10 in 1,000,000, which is still effectively zero, while your spending rises in a straight line. The lottery is designed so that, on average, players receive back less than they put in; that gap is what funds the prize pool and public programmes. Spending more does not change that arithmetic in your favour.</p>

      <h3>Dreams, licence plates and number sellers</h3>
      <p>Choosing numbers from a dream, a monk&rsquo;s blessing, a licence plate or a date is a cherished part of Thai lottery culture, and there is nothing wrong with playing a number that means something to you for fun. Just be clear about what it is: a personal choice, not a method that improves your odds. Any number is as likely as any other.</p>
      <p>Be far more cautious with anyone who <b>sells</b> predictions, &ldquo;leaked&rdquo; numbers or guaranteed systems. They cannot deliver what they promise &mdash; the maths makes that impossible &mdash; and paying for it only guarantees a loss before the draw even happens. If a seller could really predict results, they would have no reason to sell them to you.</p>

      <h3>How to use our statistics the right way</h3>
      <p>So what are the tools on this site good for? Plenty &mdash; as long as you treat them as a record, not a crystal ball. Use the <a href="/results/">results archive</a> to look up past draws, the <a href="/search/">number search</a> to see a number&rsquo;s history, the <a href="/stats/">statistics</a> to satisfy curiosity about the long-term spread, and the <a href="/check/">Did I Win? checker</a> to confirm a ticket you already hold. They make a genuinely random game easy to explore and verify. They do not, and cannot, tell you what is coming next.</p>
      <p>If playing ever stops feeling like harmless fun, please read our <a href="/responsible-play/">Responsible Play</a> guidance, which includes support resources in Thailand.</p>
"""

PREDICT_FAQ = [
    ("Are some Thai lottery numbers luckier than others?",
     "No. Every number has the same chance in every draw. &ldquo;Lucky&rdquo; or &ldquo;hot&rdquo; numbers are simply ones that have appeared slightly more often in the past, which has no effect on future draws."),
    ("If a number hasn&rsquo;t appeared in a long time, is it due?",
     "No. This is the gambler&rsquo;s fallacy. A long gap does not raise a number&rsquo;s chance; each draw is independent and the odds reset completely every time."),
    ("Can anyone predict the Thai lottery?",
     "No one can. The draw is random and independent, so no system, statistic or seller can forecast it. Anyone charging for &ldquo;sure&rdquo; numbers is mistaken or dishonest."),
]

# ---------------------------------------------------------------------------
# Pillar 1 — How the Lottery Works
# ---------------------------------------------------------------------------
HOW_IT_WORKS = """
      <p class="lead">The Thai Government Lottery is one of the country&rsquo;s most familiar institutions, drawn twice a month and sold by vendors on almost every street. This guide explains how it actually works &mdash; who runs it, how tickets are structured, how the draw is conducted, and how the prizes fit together.</p>

      <h3>Who runs the lottery</h3>
      <p>The lottery is administered by the <b>Government Lottery Office (GLO)</b>, a Thai state enterprise. It is one of only two forms of legal gambling in Thailand (the other being horse racing in Bangkok). A share of the proceeds funds the prize pool, with the remainder going to state revenue and public-welfare programmes. You can always verify official results and rules at <a href="https://www.glo.or.th" target="_blank" rel="noopener nofollow">glo.or.th</a>.</p>

      <h3>When the draw happens</h3>
      <p>Draws are held twice a month, on the <b>1st and the 16th</b>, at around 4:00&nbsp;PM Bangkok time (ICT). The draw is televised, with the show running through the afternoon and the headline numbers revealed close to 4:00&nbsp;PM. When a draw date lands on certain public or Buddhist holidays it can be shifted by a day or two, and year-end dates are sometimes moved (for example a 30&nbsp;December draw in place of 1&nbsp;January). Our home page shows a countdown to the next scheduled draw, and the full schedule is covered in <a href="/guides/when-is-thai-lottery-drawn/">When Is the Thai Lottery Drawn?</a></p>

      <h3>How tickets are structured</h3>
      <p>Thai lottery tickets are <b>pre-printed</b>, each carrying a unique six-digit number. They are sold in <b>pairs</b>, and the official price is 80&nbsp;baht per ticket (160&nbsp;baht for the pair). Each printed set contains one million tickets, numbered 000000 to 999999. Because tickets are pre-printed rather than chosen, you are buying whatever numbers a vendor has in stock &mdash; which is why people hunt through vendors&rsquo; books for numbers they like.</p>
      <p>There are two ticket types, printed at the top-left of the ticket: the <b>Thai Government Lottery (TGL)</b> and the occasional <b>Thai Charity Lottery (TCL)</b>. They differ mainly in their first-prize amount and the tax rate on winnings. An official digital ticket is also sold through the government&rsquo;s Pao Tang app, in the same six-digit format.</p>

      <h3>How the draw is conducted</h3>
      <p>On draw day, officials use transparent air-mix machines to select the winning digits live on air, one prize tier at a time. A single six-digit number is drawn for the first prize; separate draws produce the smaller digit prizes. The process is conducted in public view specifically so that anyone can see it is random and unrigged.</p>

      <h3>The prize structure</h3>
      <p>Prizes range from the headline first prize down to a simple two-digit match. The amounts below are per single ticket; because tickets are sold in pairs, holding the matching pair pays double.</p>
      <ul>
        <li><b>First prize</b> &mdash; &#3647;6,000,000 (1 winning number)</li>
        <li><b>Adjacent to first prize</b> (the numbers one above and one below) &mdash; &#3647;100,000 each (2 numbers)</li>
        <li><b>Second prize</b> &mdash; &#3647;200,000 (5 numbers)</li>
        <li><b>Third prize</b> &mdash; &#3647;80,000 (10 numbers)</li>
        <li><b>Fourth prize</b> &mdash; &#3647;40,000 (50 numbers)</li>
        <li><b>Fifth prize</b> &mdash; &#3647;20,000 (100 numbers)</li>
        <li><b>Front three digits</b> &mdash; &#3647;4,000 (2 numbers)</li>
        <li><b>Last three digits</b> &mdash; &#3647;4,000 (2 numbers)</li>
        <li><b>Last two digits</b> &mdash; &#3647;2,000 (1 number)</li>
      </ul>
      <p>The full breakdown of each tier is in <a href="/guides/thai-lottery-prize-tiers-explained/">Prize Tiers Explained</a>. Note that the front-three prize is a relatively recent addition, introduced on 1&nbsp;September 2015.</p>

      <h3>Checking and claiming</h3>
      <p>After a draw you can compare your number against every tier. Our <a href="/check/">Did I Win? checker</a> scans your six digits against 20 years of results in seconds, and the <a href="/results/">results archive</a> holds every official draw. A match here is for your information only &mdash; any real win must be confirmed and paid through the GLO. The full process, including deadlines and what to bring, is in <a href="/guides/how-to-claim-thai-lottery-prize/">How to Claim a Prize</a>.</p>

      <h3>A note on the odds</h3>
      <p>The lottery is popular despite long odds: matching all six digits for the first prize is about a 1-in-a-million chance on any single ticket. The numbers are random and independent, so no past result predicts a future one. If you choose to play, please treat it as entertainment and see our <a href="/responsible-play/">Responsible Play</a> guidance.</p>
"""

PRIZE_TIERS = """
      <p class="lead">The Thai Government Lottery has more prize tiers than many people realise &mdash; nine in total, from the &#3647;6,000,000 first prize down to a &#3647;2,000 two-digit match. This guide explains exactly what each tier pays, how many winning numbers there are, and how the &ldquo;pair&rdquo; system doubles a win.</p>

      <h3>The full prize table</h3>
      <p>All amounts are per single ticket. Tickets are sold in pairs, so if you hold both tickets of a winning pair you receive twice the figure shown.</p>
      <ul>
        <li><b>First prize &mdash; &#3647;6,000,000.</b> One six-digit number. Matching all six digits in order wins the top prize.</li>
        <li><b>Adjacent to the first prize &mdash; &#3647;100,000 each.</b> The two numbers immediately above and below the first-prize number (i.e. first prize &plusmn;1). Two winning numbers in total.</li>
        <li><b>Second prize &mdash; &#3647;200,000.</b> Five separate six-digit numbers.</li>
        <li><b>Third prize &mdash; &#3647;80,000.</b> Ten numbers.</li>
        <li><b>Fourth prize &mdash; &#3647;40,000.</b> Fifty numbers.</li>
        <li><b>Fifth prize &mdash; &#3647;20,000.</b> One hundred numbers.</li>
        <li><b>Front three digits &mdash; &#3647;4,000.</b> Two three-digit numbers; you win if the first three digits of your ticket match either one.</li>
        <li><b>Last three digits &mdash; &#3647;4,000.</b> Two three-digit numbers; you win if the last three digits of your ticket match either one.</li>
        <li><b>Last two digits &mdash; &#3647;2,000.</b> One two-digit number; you win if the last two digits of your ticket match it. This is the most commonly won prize.</li>
      </ul>

      <h3>How the six-digit prizes work</h3>
      <p>The first prize, the adjacent numbers and the second-to-fifth prizes are all matched against your <b>full six-digit number</b>. There is only one first-prize number per draw, but there are 5, 10, 50 and 100 numbers for the second through fifth prizes respectively, so those are the realistic &ldquo;big&rdquo; wins for most full-number holders.</p>

      <h3>How the digit prizes work</h3>
      <p>The front-three, last-three and last-two prizes only look at part of your number, which is why they are far easier to win:</p>
      <ul>
        <li>The <b>front three</b> looks at the first three digits of your ticket.</li>
        <li>The <b>last three</b> looks at the final three digits.</li>
        <li>The <b>last two</b> looks at the final two digits.</li>
      </ul>
      <p>Because two numbers are drawn for each three-digit prize, and one for the two-digit prize, these tiers produce many more winners than the six-digit prizes.</p>

      <h3>The front-three prize is newer</h3>
      <p>If you look at older results you will notice there is no front-three figure before <b>1&nbsp;September 2015</b> &mdash; that prize was introduced on that date, replacing an earlier &ldquo;first-three&rdquo; arrangement. Our <a href="/results/">results archive</a> reflects this: draws before September 2015 show last-three and last-two prizes but no front-three.</p>

      <h3>The pair system</h3>
      <p>Every ticket is part of a pair with an identical number. Vendors often split pairs and sell single tickets, so check whether you are holding one ticket or two. If you hold the full pair and the number wins, every prize amount above is <b>doubled</b> &mdash; a paired first prize, for example, pays &#3647;12,000,000.</p>

      <h3>Check your number</h3>
      <p>To see which tier (if any) a number has matched, enter it in our <a href="/check/">Did I Win? checker</a> or look up its history in the <a href="/search/">number search</a>. As always, confirm any win with the official Government Lottery Office before celebrating &mdash; and remember that past results never predict future ones.</p>
"""

DRAW_DATES = """
      <p class="lead">The Thai Government Lottery runs on a simple, reliable schedule &mdash; twice a month &mdash; but the exact dates and times trip up a lot of people, especially around holidays. Here is everything you need to know about when draws happen.</p>

      <h3>The 1st and the 16th</h3>
      <p>Draws are held <b>twice every month, on the 1st and the 16th</b>. That gives 24 regular draws in a typical year. The schedule is the same in every month, which makes the lottery easy to plan around: buy in the days before the 1st or the 16th, and check results that afternoon.</p>

      <h3>What time is the draw?</h3>
      <p>The draw takes place in the <b>afternoon, Bangkok time (ICT, UTC+7)</b>. It is broadcast live as a programme that runs through the early-to-mid afternoon, with the prize numbers drawn one tier at a time and the headline results revealed close to <b>4:00&nbsp;PM</b>. If you are checking from another time zone, remember Thailand does not observe daylight saving, so the offset from UTC is always +7.</p>

      <h3>Holiday shifts</h3>
      <p>The fixed schedule has a few exceptions. When the 1st or the 16th falls on certain <b>public or major Buddhist holidays</b>, the draw can be moved &mdash; usually by a day or two &mdash; so it is always worth confirming the date around holiday periods rather than assuming. Because these shifts are decided by the GLO, the official site is the place to confirm an exact date.</p>

      <h3>Year-end dates</h3>
      <p>The end of the year is the most common time for a shift. Rather than drawing on 1&nbsp;January, the calendar is often adjusted so that a draw lands on <b>30&nbsp;December</b> instead. You can see this in our own archive: several years record a 30&nbsp;December draw in place of an early-January one. If you are tracking the very start or end of a year, double-check which date applies.</p>

      <h3>How many draws happen in a year?</h3>
      <p>In a normal year there are 24 draws. The total occasionally varies &mdash; for example, draws were disrupted in 2020 &mdash; which is one reason our statistics are based on the actual recorded draws rather than an assumed two-per-month. You can browse every recorded draw, filtered by year, in the <a href="/results/">results archive</a>.</p>

      <h3>Never miss a result</h3>
      <p>The fastest way to stay current is to check back here on the afternoon of the 1st and 16th, or use our <a href="/check/">Did I Win? checker</a> once results are in. Our home page also shows a live countdown to the next scheduled draw. Whatever the date, remember that each draw is independent &mdash; the timing has no bearing on which numbers come up.</p>
"""

# ---------------------------------------------------------------------------
# Pillar 2 — Claiming & Official Process
# ---------------------------------------------------------------------------
CLAIM = """
      <p class="lead">Won something? Congratulations &mdash; but a winning Thai lottery ticket is only worth its prize if you claim it correctly and on time. This guide walks through the process step by step, including where to go, what to bring, and the deadlines that matter. Always confirm the current procedure with the <a href="https://www.glo.or.th" target="_blank" rel="noopener nofollow">Government Lottery Office</a>, as details can change.</p>

      <h3>Step 1: Verify the win</h3>
      <p>First, confirm your number actually matched a prize tier. Check it against the official results &mdash; you can use our <a href="/check/">Did I Win? checker</a> for a quick scan, but treat the official GLO announcement as the final word before doing anything else.</p>

      <h3>Step 2: Sign the back of the ticket</h3>
      <p>As soon as you know you hold a winner, <b>sign your name on the back of the ticket</b>. The Thai lottery ticket is a <b>bearer instrument</b> &mdash; whoever holds it can claim it &mdash; so signing it helps protect against loss or theft. A ticket that is lost, badly torn or destroyed generally cannot be claimed, so keep it safe and intact.</p>

      <h3>Step 3: Choose where to claim, based on the amount</h3>
      <ul>
        <li><b>Small prizes (up to 20,000 baht):</b> You can usually be paid in cash on the spot by an authorised lottery vendor or retailer. Vendors typically take a small commission (often around 1&ndash;2%) for the convenience. Prizes may also be claimed at GLO offices and certain authorised banks.</li>
        <li><b>Larger prizes (over 20,000 baht):</b> You must claim in person at the Government Lottery Office, where a cheque is issued. The main office is in <b>Nonthaburi</b> (near Bangkok); there are also designated GLO offices and a branch at Suvarnabhumi Airport that is convenient for travellers.</li>
      </ul>

      <h3>Step 4: Bring the right documents</h3>
      <ul>
        <li>The <b>original winning ticket</b>, signed and intact.</li>
        <li><b>Valid photo ID</b> &mdash; a Thai national ID card, or a passport for foreign nationals. Anyone, Thai or foreign, can claim a prize; the ticket is what matters.</li>
        <li>For larger prizes you may be asked to <b>complete a claim form</b> and provide a tax identification number.</li>
      </ul>

      <h3>Step 5: Receive payment, minus duty</h3>
      <p>A small <b>stamp duty</b> is deducted at the point of claim &mdash; 0.5% for the standard Government Lottery (1% for the Charity Lottery). That is the only Thai deduction on the prize itself; any vendor commission on a small cash claim is separate. We explain the deductions in detail in <a href="/guides/thai-lottery-taxes-stamp-duty/">Taxes &amp; Stamp Duty</a>.</p>

      <h3>The deadline: two years</h3>
      <p>You have <b>two years from the draw date</b> to claim a prize. After that, an unclaimed prize is forfeited and the money is turned over to the state as public revenue. Don&rsquo;t leave a winning ticket in a drawer &mdash; check and claim promptly.</p>

      <h3>Digital tickets</h3>
      <p>If you bought an official <b>digital ticket through the Pao Tang app</b>, there is no paper ticket to present: a win is recorded against your account and paid out through the platform according to its own process.</p>

      <h3>Avoid claim scams</h3>
      <p>You never have to pay a fee in advance to &ldquo;release&rdquo; a legitimate lottery prize, and no official will ask for your banking passwords. Be wary of anyone who contacts you claiming you have won a lottery you didn&rsquo;t enter. For more, see <a href="/responsible-play/">Responsible Play</a>, and verify everything through official GLO channels.</p>
"""

CLAIM_HOWTO = [
    ("Verify the win", "Confirm your number against the official Government Lottery Office results. You can pre-check it with the Did I Win? tool, then treat the official announcement as final."),
    ("Sign the ticket", "Sign your name on the back of the winning ticket immediately, since it is a bearer instrument and must be kept intact."),
    ("Choose where to claim", "Prizes up to 20,000 baht can be paid in cash by an authorised vendor; prizes over 20,000 baht must be claimed in person at a Government Lottery Office, where a cheque is issued."),
    ("Bring the right documents", "Take the original signed ticket and valid photo ID (Thai ID card or passport). Larger prizes may require a claim form and tax ID number."),
    ("Collect your payment", "Receive your prize minus the stamp duty (0.5% for the Government Lottery). Claim within two years of the draw date or the prize is forfeited."),
]

CLAIM_FAQ = [
    ("How long do I have to claim a Thai lottery prize?",
     "Two years from the draw date. After that the prize is forfeited and the money goes to the state."),
    ("Where do I claim a large prize?",
     "Prizes over 20,000 baht must be claimed in person at a Government Lottery Office (the main office is in Nonthaburi), where a cheque is issued. Smaller prizes can be paid in cash by authorised vendors."),
    ("Can a foreigner claim a Thai lottery prize?",
     "Yes. Anyone holding a valid winning ticket can claim it; bring your passport as identification. The ticket, not nationality, is what matters."),
    ("What if I lose or tear the ticket?",
     "The ticket is a bearer instrument, so a lost ticket generally cannot be claimed and a badly damaged one may be rejected. Keep it safe, flat and intact."),
]

TAXES = """
      <p class="lead">Thai lottery winnings are taxed very lightly compared with many countries, but there are deductions, and they differ between the Government Lottery and the Charity Lottery. This guide explains what comes off a prize and what does not. Tax rules can change, so treat this as general information and confirm current figures with the <a href="https://www.glo.or.th" target="_blank" rel="noopener nofollow">Government Lottery Office</a> or the Thai Revenue Department.</p>

      <h3>The headline: stamp duty</h3>
      <p>The main deduction on a Thai lottery prize is <b>stamp duty</b>, charged on the winnings:</p>
      <ul>
        <li><b>Thai Government Lottery (the standard ticket): 0.5%.</b></li>
        <li><b>Thai Charity Lottery: 1%.</b></li>
      </ul>
      <p>The 0.5% figure is the same thing as the often-quoted rate of <b>1 baht for every 200 baht</b> of prize money. So a &#3647;2,000 last-two-digit win has roughly &#3647;10 of duty deducted, and a &#3647;6,000,000 first prize has about &#3647;30,000 of duty.</p>

      <h3>It applies to every prize</h3>
      <p>The duty is charged on all winnings, including small prizes paid in cash by a vendor. When a vendor pays out a small prize, they are responsible for collecting the duty and passing it on, so you may simply receive the net amount.</p>

      <h3>Vendor commission is not a tax</h3>
      <p>If you cash a small prize with a street vendor, they often keep a <b>commission</b> (commonly around 1&ndash;2%) for the convenience of immediate cash. That is a private service charge, not a government tax, and it is separate from the stamp duty. You can avoid it by claiming through an official GLO office, though that is less convenient for a small amount.</p>

      <h3>Is there income tax on lottery winnings?</h3>
      <p>For the official Thai lotteries, the stamp duty described above is the deduction taken at the point of claim; there is no additional Thai lottery-specific income tax layered on top of it for the standard ticket. However, tax law is detailed and individual circumstances vary, so if a large win could affect your overall tax position you should take professional advice.</p>

      <h3>If you are a foreign winner</h3>
      <p>Foreign nationals can claim Thai prizes on the same terms, with the same stamp duty. The complication is your <b>home country</b>: many countries tax worldwide income or foreign lottery winnings, and you may need to declare the funds when bringing large amounts across a border. Keep the official receipt from the GLO as proof, and check your own country&rsquo;s rules with a local tax adviser.</p>

      <h3>Keep your paperwork</h3>
      <p>When you claim, especially for a larger prize, you receive official documentation of the win and the duty paid. Keep it &mdash; it is your evidence of where the money came from and what was deducted. For the full claiming walkthrough, see <a href="/guides/how-to-claim-thai-lottery-prize/">How to Claim a Prize</a>.</p>
"""

TAXES_FAQ = [
    ("How much tax is deducted from Thai lottery winnings?",
     "A stamp duty of 0.5% on the Government Lottery, or 1% on the Charity Lottery. The 0.5% rate is equivalent to 1 baht per 200 baht of prize money."),
    ("Is the stamp duty taken from small prizes too?",
     "Yes. It applies to all winnings, including small prizes paid in cash by a vendor, who collects and remits it on the winner&rsquo;s behalf."),
    ("Do foreigners pay extra tax on Thai winnings?",
     "No extra Thai tax applies to foreigners &mdash; the stamp duty is the same. But your home country may tax foreign lottery winnings, so check local rules."),
]

# ---------------------------------------------------------------------------
# Pillar 3 — Understanding the Numbers
# ---------------------------------------------------------------------------
HOT_COLD = """
      <p class="lead">&ldquo;Hot&rdquo; and &ldquo;cold&rdquo; numbers are the most popular &mdash; and most misunderstood &mdash; statistics in the lottery world. This guide explains exactly what they are, how we calculate them, and the one thing they absolutely cannot do.</p>

      <h3>What the terms mean</h3>
      <p>A <b>hot number</b> is one that has been drawn more often than average over a chosen period. A <b>cold number</b> is one that has been drawn less often, or not at all. That is the entire definition. It is a description of the past &mdash; a tally &mdash; and nothing more.</p>

      <h3>How we calculate them</h3>
      <p>For each prize category &mdash; last-two, front-three, last-three &mdash; we count how many times every possible number has appeared as a winner across our archive of recorded draws, then rank them. The numbers at the top of the count are &ldquo;hot&rdquo;; those at the bottom are &ldquo;cold&rdquo;. You can see the live ranking, plus a heat grid and per-number trends, on our <a href="/stats/">statistics page</a>.</p>
      <figure class="fig">
        <img src="/assets/charts/last2-frequency.svg" alt="Bar chart of how often each last-two-digit number from 00 to 99 has won, with the bars clustered around a flat average line." loading="lazy" width="900" height="380">
        <figcaption>Last-two-digit win counts across the full archive. &ldquo;Hot&rdquo; numbers are simply the slightly taller bars &mdash; the variation is what randomness looks like.</figcaption>
      </figure>

      <h3>Why the differences are normal randomness</h3>
      <p>Look at the chart and you will see the bars cluster around the average, with some a little higher and some a little lower. Over hundreds of draws, the most-drawn last-two number has appeared only a handful more times than the average, and the spread has no pattern. This is exactly what <b>random variation</b> looks like: in any fair process, some outcomes get slightly ahead and others fall slightly behind, purely by chance. The gaps are noise, not signal.</p>

      <h3>The mistake almost everyone makes</h3>
      <p>The temptation is to treat hot numbers as &ldquo;on a streak&rdquo; (so back them) or cold numbers as &ldquo;due&rdquo; (so back them too). Both are versions of the same error. Because every draw is <b>independent</b>, a number&rsquo;s past frequency has zero influence on the next draw. A hot number is not more likely to come up again, and a cold number is not owed an appearance. We explain the underlying maths in <a href="/guides/why-you-cant-predict-lottery-numbers/">Why You Can&rsquo;t Predict Lottery Numbers</a>.</p>

      <h3>So are the stats useless?</h3>
      <p>Not at all &mdash; they are just for the right job. Frequency stats are genuinely interesting as a record: they let you see how an honest random process plays out over 20 years, settle arguments about which number has actually come up most, and explore the data behind the lottery. They satisfy curiosity. What they cannot do is tell you what is coming next. Use them that way and they are a great tool; use them as a prediction and they will only cost you money.</p>

      <h3>Explore responsibly</h3>
      <p>Dig into the numbers on the <a href="/stats/">statistics page</a> and look up any number&rsquo;s full history in the <a href="/search/">number search</a>. If choosing numbers ever starts to feel like more than fun, our <a href="/responsible-play/">Responsible Play</a> page has guidance and support resources.</p>
"""

ODDS = """
      <p class="lead">Everyone knows the lottery is a long shot, but how long exactly? This guide puts a real number on your chances in each prize tier of the Thai Government Lottery, using the simple fact that every set is one million tickets numbered 000000 to 999999.</p>

      <h3>The key fact: one million numbers</h3>
      <p>Each printed set runs from 000000 to 999999 &mdash; exactly <b>1,000,000</b> possible six-digit numbers. Knowing how many winning numbers there are in each tier, we can state the chance that any single ticket you hold lands that prize. (These are the odds for one specific ticket; buying more tickets adds chances but, as we&rsquo;ll see, barely moves the dial.)</p>

      <h3>Six-digit prizes</h3>
      <ul>
        <li><b>First prize</b> &mdash; 1 winning number out of 1,000,000, so about <b>1 in 1,000,000</b>.</li>
        <li><b>Adjacent to first prize</b> &mdash; 2 numbers, about <b>1 in 500,000</b>.</li>
        <li><b>Second prize</b> &mdash; 5 numbers, about <b>1 in 200,000</b>.</li>
        <li><b>Third prize</b> &mdash; 10 numbers, about <b>1 in 100,000</b>.</li>
        <li><b>Fourth prize</b> &mdash; 50 numbers, about <b>1 in 20,000</b>.</li>
        <li><b>Fifth prize</b> &mdash; 100 numbers, about <b>1 in 10,000</b>.</li>
      </ul>

      <h3>Digit prizes (the realistic ones)</h3>
      <p>The digit prizes only check part of your number, so they are far more attainable:</p>
      <ul>
        <li><b>Last two digits</b> &mdash; 1 number out of 100 possible pairs, so about <b>1 in 100</b>. This is the prize most players actually win at some point.</li>
        <li><b>Last three digits</b> &mdash; 2 numbers out of 1,000, so about <b>1 in 500</b>.</li>
        <li><b>Front three digits</b> &mdash; 2 numbers out of 1,000, so about <b>1 in 500</b>.</li>
      </ul>

      <h3>What this means in plain terms</h3>
      <p>The first prize is roughly as likely as picking one specific second out of eleven-and-a-half days. The last-two prize, at 1 in 100, is the friendly end of the scale &mdash; which is exactly why it pays the smallest amount, &#3647;2,000. The odds and the payouts are designed to balance: the easier a prize is to win, the less it pays.</p>

      <h3>Why more tickets barely helps the top prize</h3>
      <p>Each extra ticket with a different number adds one more chance in a million at the first prize. Ten tickets give you about 10 in 1,000,000 &mdash; still essentially zero &mdash; while costing ten times as much. The overall payout ratio of the lottery is well below the amount staked, which is how it funds prizes and public programmes. In other words, on average it returns less than you put in, by design. That is fine for entertainment; it is not a strategy for making money.</p>

      <h3>The odds never change</h3>
      <p>Crucially, none of these odds shift from draw to draw or because of any number&rsquo;s history. They are fixed by the structure of the game. A number that hasn&rsquo;t appeared in years has the same 1-in-100 (or 1-in-a-million) chance as any other. For why that is, read <a href="/guides/why-you-cant-predict-lottery-numbers/">Why You Can&rsquo;t Predict Lottery Numbers</a>, and to check a number&rsquo;s actual history use our <a href="/search/">number search</a>. Please keep play within your means &mdash; see <a href="/responsible-play/">Responsible Play</a>.</p>
"""

DATA_20Y = """
      <p class="lead">One thing that makes this site useful is depth: an archive of <b>464 recorded Government Lottery draws</b> stretching from December 2006 to mid-2026 &mdash; close to 20 years. This guide looks at what that long-term record actually shows, using our own data. The short version: it looks random, and that is exactly the point.</p>

      <h3>What&rsquo;s in the archive</h3>
      <p>The dataset covers 464 draws across roughly two decades. In a typical year there are 24 draws (two a month), and the chart below shows the count year by year.</p>
      <figure class="fig">
        <img src="/assets/charts/draws-per-year.svg" alt="Bar chart of recorded Thai lottery draws per year from 2006 to 2026, mostly around 24 per year, with 2020 lower at 21 and partial bars for 2006 and 2026." loading="lazy" width="900" height="360">
        <figcaption>Recorded draws per year. Most years hold the steady 24 draws; 2020 is lower at 21, reflecting real-world disruption that year.</figcaption>
      </figure>
      <p>The first and last bars are partial &mdash; the archive begins with a 30&nbsp;December 2006 draw and runs to mid-2026 &mdash; and 2020 dips to 21 draws. We base our statistics on these actual recorded draws rather than assuming a perfect two-per-month, which keeps the frequencies honest.</p>

      <h3>The front-three prize starts in 2015</h3>
      <p>A data quirk worth knowing: the front-three prize only exists from <b>1&nbsp;September 2015</b> onward, so our archive holds front-three results for 256 draws rather than all 464. Last-three and last-two figures, by contrast, run the full span. This is why front-three frequencies are drawn from a smaller sample.</p>

      <h3>What 20 years of last-two digits looks like</h3>
      <p>The last-two-digit prize is the richest part of the record &mdash; one winning pair every draw, for 464 draws. If the lottery is fair, every pair from 00 to 99 should appear roughly the same number of times over a long span, with only chance-driven wobble. That is what we see: across the archive the average pair has won about <b>4&ndash;5 times</b>, the most-drawn pair has appeared around <b>11 times</b>, and at the other extreme some pairs have come up only once. One pair has not appeared as a last-two winner at all in the recorded draws.</p>

      <h3>Doesn&rsquo;t a missing number prove a pattern?</h3>
      <p>It&rsquo;s the opposite. With 100 possible pairs and 464 draws, pure chance guarantees that some numbers race ahead while others lag or get skipped entirely &mdash; that scatter is the signature of randomness, not evidence against it. If every number had appeared exactly the same number of times, <i>that</i> would be suspicious. A number that has never come up is not &ldquo;cold&rdquo; or &ldquo;avoided&rdquo;; it has the same chance as any other in the next draw. We unpack this in <a href="/guides/what-hot-and-cold-numbers-mean/">What Hot and Cold Numbers Really Mean</a>.</p>

      <h3>The honest takeaway</h3>
      <p>Twenty years of data is a wonderful thing to explore, but it does not reveal a system, because there isn&rsquo;t one. The value of a long record is that it lets you <i>see</i> randomness clearly &mdash; the even-ish spread, the meaningless streaks, the gaps &mdash; and understand why no past result predicts a future one. Browse it all in the <a href="/results/">results archive</a> and the <a href="/stats/">statistics page</a>, search any number&rsquo;s history in <a href="/search/">number search</a>, and read how we compile the data on our <a href="/about/">About</a> page.</p>
"""

FAQ_ARTICLE = """
      <p class="lead">A plain-language reference to the questions we&rsquo;re asked most about the Thai Government Lottery &mdash; from draw times and prize amounts to claiming, taxes and whether anyone can predict the numbers. For deeper detail, follow the links into our full guides.</p>

      <h3>The basics</h3>
      <p><b>When is the Thai lottery drawn?</b> Twice a month, on the 1st and the 16th, at around 4:00&nbsp;PM Bangkok time. Some holidays can shift the date; see <a href="/guides/when-is-thai-lottery-drawn/">When Is the Thai Lottery Drawn?</a></p>
      <p><b>How much does a ticket cost?</b> The official price is 80&nbsp;baht per ticket. Tickets are pre-printed, carry a six-digit number, and are sold in pairs (160&nbsp;baht for the pair).</p>
      <p><b>Who runs it?</b> The Government Lottery Office (GLO), a Thai state enterprise. Proceeds help fund prizes and public-welfare programmes.</p>

      <h3>Prizes</h3>
      <p><b>How much is the first prize?</b> &#3647;6,000,000 per ticket. As tickets are sold in pairs, a matching pair pays &#3647;12,000,000.</p>
      <p><b>What do the smaller prizes pay?</b> The last two digits pay &#3647;2,000; the front three and last three pay &#3647;4,000 each; second to fifth prizes pay &#3647;200,000, &#3647;80,000, &#3647;40,000 and &#3647;20,000; and the two numbers adjacent to the first prize pay &#3647;100,000 each. Full detail in <a href="/guides/thai-lottery-prize-tiers-explained/">Prize Tiers Explained</a>.</p>
      <p><b>What are my odds?</b> About 1 in 1,000,000 for the first prize on a single ticket, and about 1 in 100 for the last-two prize. See <a href="/guides/thai-lottery-odds-tier-by-tier/">Understanding the Odds</a>.</p>

      <h3>Checking &amp; claiming</h3>
      <p><b>How do I check my ticket?</b> Enter your six-digit number in our <a href="/check/">Did I Win? checker</a>, which scans every tier across 20 years of draws. Always confirm against the official GLO results before claiming.</p>
      <p><b>How do I claim a prize?</b> Small prizes (up to 20,000 baht) are paid in cash by authorised vendors; larger prizes are claimed in person at a Government Lottery Office with the signed ticket and ID. Full walkthrough in <a href="/guides/how-to-claim-thai-lottery-prize/">How to Claim a Prize</a>.</p>
      <p><b>How long do I have to claim?</b> Two years from the draw date, after which the prize is forfeited to the state.</p>
      <p><b>How much tax is taken?</b> A stamp duty of 0.5% on the Government Lottery (1% on the Charity Lottery). See <a href="/guides/thai-lottery-taxes-stamp-duty/">Taxes &amp; Stamp Duty</a>.</p>

      <h3>Numbers &amp; odds</h3>
      <p><b>Can past results predict future numbers?</b> No. Every draw is independent and random, so frequency history never changes the odds of the next draw. Our statistics are for interest only &mdash; read <a href="/guides/why-you-cant-predict-lottery-numbers/">Why You Can&rsquo;t Predict Lottery Numbers</a>.</p>
      <p><b>What are &ldquo;hot&rdquo; and &ldquo;cold&rdquo; numbers?</b> Simply numbers that have appeared more or less often in the past. Interesting, but not predictive &mdash; see <a href="/guides/what-hot-and-cold-numbers-mean/">What Hot and Cold Numbers Really Mean</a>.</p>
      <p><b>How far back does your data go?</b> Roughly 20 years &mdash;464 recorded draws from 2006 to today, added automatically as results are published.</p>

      <h3>Eligibility</h3>
      <p><b>Can foreigners play and claim?</b> Yes. Anyone can buy tickets from licensed vendors in Thailand, and any holder of a valid winning ticket can claim it &mdash; bring a passport as ID.</p>
      <p>Still have a question? <a href="/contact.html">Contact us</a> and we&rsquo;ll do our best to help. Please also see our <a href="/responsible-play/">Responsible Play</a> guidance.</p>
"""

FAQ_ARTICLE_FAQ = [
    ("When is the Thai lottery drawn?",
     "Twice a month, on the 1st and the 16th, at around 4:00 PM Bangkok time. Some public holidays can shift the date."),
    ("How much is the Thai lottery first prize?",
     "&#3647;6,000,000 per ticket. Because tickets are sold in pairs, a matching pair pays &#3647;12,000,000."),
    ("How much does a Thai lottery ticket cost?",
     "The official price is 80 baht per ticket. Tickets carry a six-digit number and are sold in pairs."),
    ("How long do I have to claim a prize?",
     "Two years from the draw date. After that the prize is forfeited and the money goes to the state."),
    ("How much tax is deducted from winnings?",
     "A stamp duty of 0.5% on the Government Lottery, or 1% on the Charity Lottery."),
    ("Can past results predict future Thai lottery numbers?",
     "No. Every draw is independent and random, so past frequency does not change the odds of any number in the next draw."),
    ("Can foreigners play and claim Thai lottery prizes?",
     "Yes. Anyone can buy tickets from licensed vendors in Thailand, and any holder of a valid winning ticket can claim it with valid ID such as a passport."),
]

CULTURE = """
      <p class="lead">In Thailand, a number is rarely just a number. A phone number, a house address, a car&rsquo;s licence plate or a wedding date can be chosen &mdash; or quietly avoided &mdash; because of what the digits are believed to mean. This guide explains where those beliefs come from, what each single digit signifies, and how lucky sequences are read. One honest caveat up front: however meaningful a number feels, the lottery draw itself is random, and no number is luckier than another when the machines spin.</p>

      <h3>Why numbers carry meaning</h3>
      <p>Thai is a tonal, homophone-rich language, so a spoken number often sounds like an unrelated word &mdash; and can &ldquo;borrow&rdquo; that word&rsquo;s good or bad fortune. Layered on top are Buddhism, older animist beliefs that everything carries a spirit, and a strong Chinese influence from Thailand&rsquo;s large Thai-Chinese community. The result is a culture where the right digits are thought to invite prosperity and the wrong ones to invite misfortune &mdash; which is why businesses pay a premium for an auspicious phone number and buyers haggle over a &ldquo;good&rdquo; address.</p>
      <figure class="fig">
        <img src="/assets/charts/thai-digit-meanings.svg" alt="An infographic showing how the single digits 0 to 9 are viewed in Thai number culture, with 3, 5, 8 and 9 marked lucky, 4 marked as avoided, 6 and 7 mixed, and 0, 1 and 2 neutral." loading="lazy" width="900" height="250">
        <figcaption>A quick guide to how single digits are commonly read in Thai culture. Beliefs vary by region, age and family.</figcaption>
      </figure>

      <h3>The digits, one by one</h3>
      <ul>
        <li><b>1 (&ldquo;neung&rdquo;)</b> &mdash; being first, independence and leadership. Broadly positive, if unremarkable.</li>
        <li><b>2 (&ldquo;song&rdquo;)</b> &mdash; pairs and balance, linked to partnership. Generally neutral-to-good.</li>
        <li><b>3 (&ldquo;saam&rdquo;)</b> &mdash; a classic lucky pick. Odd numbers are widely felt to be luckier than even ones, and three is associated with growth and stability. It also has quiet significance as three times three makes nine.</li>
        <li><b>4 (&ldquo;sii&rdquo;)</b> &mdash; the digit to avoid. Its sound is strongly linked to death &mdash; an association rooted in Chinese culture (where &ldquo;four&rdquo; sounds like the word for death) and carried into everyday Thai life. Many buildings skip a fourth floor, and 444 is especially shunned.</li>
        <li><b>5 (&ldquo;haa&rdquo;)</b> &mdash; playful and lucky. &ldquo;Five&rdquo; is pronounced &ldquo;haa,&rdquo; the sound of laughter, which is why Thais type <b>555</b> to mean &ldquo;hahaha.&rdquo; It carries a sense of fun and happiness.</li>
        <li><b>6 (&ldquo;hok&rdquo;)</b> &mdash; mixed. The word also echoes the verb &ldquo;to spill&rdquo; or &ldquo;to fall,&rdquo; so some treat it cautiously, while others read it positively as smooth movement.</li>
        <li><b>7 (&ldquo;jet&rdquo;)</b> &mdash; views differ. It is often felt to be spiritual or mystical, and lucky in some settings, but treated more warily in others.</li>
        <li><b>8 (&ldquo;paet&rdquo;)</b> &mdash; wealth and prosperity, borrowed from Chinese tradition where eight sounds like &ldquo;to prosper.&rdquo; You will see <b>888</b> in prices and plates almost as often as nines.</li>
        <li><b>9 (&ldquo;kao&rdquo;)</b> &mdash; the king of lucky numbers. It echoes <i>k&acirc;o</i> (&ldquo;to step forward,&rdquo; i.e. progress) and <i>kh&acirc;o</i> (&ldquo;rice,&rdquo; abundance), and carries deep royal resonance &mdash; the late King Bhumibol reigned as Rama IX. Shops open at 9:09, ceremonies invite nine monks, and a licence plate reading 9999 has changed hands for millions of baht.</li>
        <li><b>0 (&ldquo;suun&rdquo;)</b> &mdash; broadly neutral, sometimes read as completeness or a clean start.</li>
      </ul>

      <h3>Sequences and repetition</h3>
      <p>Meaning intensifies when digits repeat or form a pattern:</p>
      <ul>
        <li><b>Repetition amplifies.</b> If nine is lucky, then 99 and 999 are luckier still; the same goes for 888. This is why repeated-digit plates and phone numbers command the highest premiums.</li>
        <li><b>Direction matters.</b> An ascending run such as 123 or <b>789</b> reads as &ldquo;climbing&rdquo; or &ldquo;rising,&rdquo; echoing progress &mdash; so those sequences are prized. A descending run can feel like the opposite.</li>
        <li><b>444</b> stacks the death association three times over and is strongly avoided.</li>
        <li><b>555</b>, by contrast, is just cheerful &mdash; a row of laughter.</li>
      </ul>

      <h3>Lucky numbers and the lottery &mdash; the honest part</h3>
      <p>All of this flows straight into the lottery. Vendors often price tickets carrying lucky digits &mdash; strings of nines and eights, repeated digits, ascending runs, birth dates, or a plate number from a recent stroke of good fortune &mdash; at a premium, and buyers will flip through a vendor&rsquo;s book hunting for the &ldquo;right&rdquo; number. Numbers also arrive from dreams, a monk&rsquo;s blessing, or the news.</p>
      <p>Here is the part we never soften: <b>the draw is random and independent.</b> A &ldquo;lucky&rdquo; 999999 ticket has exactly the same chance as a &ldquo;dreaded&rdquo; 444444 one &mdash; about 1 in 1,000,000 for the first prize, or 1 in 100 for the last two digits. Choosing a number for its meaning is a lovely tradition, but it does not change your odds, and paying extra for a lucky number simply costs more for the same chance. We work through the maths in <a href="/guides/why-you-cant-predict-lottery-numbers/">Why You Can&rsquo;t Predict Lottery Numbers</a>.</p>

      <h3>Enjoy the culture, respect the odds</h3>
      <p>These beliefs are a rich, living part of Thai life, and they deserve curiosity rather than ridicule. Play a number that means something to you, by all means &mdash; for the meaning, the memory or the fun of it. Just hold it lightly, treat any spending as entertainment, and see our <a href="/responsible-play/">Responsible Play</a> guidance if it ever stops being fun. You can look up the real history of any number in our <a href="/search/">number search</a>.</p>
"""

CULTURE_TH = """
      <p class="lead">ในประเทศไทย ตัวเลขไม่ค่อยเป็นเพียงตัวเลข เบอร์โทรศัพท์ บ้านเลขที่ ป้ายทะเบียนรถ หรือฤกษ์แต่งงาน มักถูกเลือก — หรือถูกหลีกเลี่ยงอย่างเงียบ ๆ — เพราะความหมายที่เชื่อกันว่าตัวเลขนั้นมี คู่มือนี้อธิบายที่มาของความเชื่อ ความหมายของแต่ละหลัก และการตีความลำดับเลขมงคล ขอออกตัวอย่างตรงไปตรงมาก่อน ไม่ว่าตัวเลขจะรู้สึกมีความหมายเพียงใด การออกรางวัลสลากนั้นเป็นการสุ่ม และไม่มีเลขใดโชคดีกว่าเลขอื่นเมื่อเครื่องเริ่มหมุน</p>

      <h3>ทำไมตัวเลขจึงมีความหมาย</h3>
      <p>ภาษาไทยมีวรรณยุกต์และคำพ้องเสียงจำนวนมาก ตัวเลขที่ออกเสียงจึงมักไปพ้องกับคำอื่น และ &ldquo;ยืม&rdquo; ความโชคดีหรือโชคร้ายของคำนั้นมา ซ้อนทับด้วยพุทธศาสนา ความเชื่อดั้งเดิมแบบวิญญาณนิยมที่ว่าทุกสิ่งมีจิต และอิทธิพลจีนอันเข้มข้นจากชุมชนไทยเชื้อสายจีน ผลลัพธ์คือวัฒนธรรมที่เชื่อว่าเลขที่ถูกต้องจะเรียกความมั่งคั่ง ส่วนเลขที่ไม่ดีจะเรียกเคราะห์ จึงไม่แปลกที่ธุรกิจยอมจ่ายแพงเพื่อเบอร์มงคล</p>
      <figure class="fig">
        <img src="/assets/charts/thai-digit-meanings.svg" alt="ภาพอธิบายว่าตัวเลข 0 ถึง 9 ถูกมองอย่างไรในวัฒนธรรมไทย โดย 3, 5, 8 และ 9 เป็นเลขมงคล, 4 เป็นเลขที่เลี่ยง, 6 และ 7 ก้ำกึ่ง, ส่วน 0, 1, 2 เป็นกลาง" loading="lazy" width="900" height="250">
        <figcaption>แนวทางคร่าว ๆ ว่าแต่ละหลักถูกมองอย่างไรในวัฒนธรรมไทย ความเชื่ออาจต่างกันตามภูมิภาค วัย และครอบครัว</figcaption>
      </figure>

      <h3>ความหมายทีละหลัก</h3>
      <ul>
        <li><b>1 (&ldquo;หนึ่ง&rdquo;)</b> — การเป็นที่หนึ่ง ความเป็นอิสระ และความเป็นผู้นำ โดยรวมเป็นบวกแต่ไม่โดดเด่นนัก</li>
        <li><b>2 (&ldquo;สอง&rdquo;)</b> — ความเป็นคู่และความสมดุล เชื่อมโยงกับการมีคู่ครอง โดยทั่วไปเป็นกลางถึงดี</li>
        <li><b>3 (&ldquo;สาม&rdquo;)</b> — เลขมงคลคลาสสิก คนไทยมักรู้สึกว่าเลขคี่โชคดีกว่าเลขคู่ และสามผูกกับการเติบโตและความมั่นคง อีกทั้งสามคูณสามได้เก้า</li>
        <li><b>4 (&ldquo;สี่&rdquo;)</b> — หลักที่มักเลี่ยง เสียงของมันผูกแน่นกับความตาย — ความเชื่อที่มีรากจากวัฒนธรรมจีน (ที่คำว่า &ldquo;สี่&rdquo; พ้องกับคำว่าตาย) และซึมเข้าสู่ชีวิตประจำวันของไทย อาคารหลายแห่งข้ามชั้นสี่ และ 444 ถูกเลี่ยงเป็นพิเศษ</li>
        <li><b>5 (&ldquo;ห้า&rdquo;)</b> — สนุกและเป็นมงคล &ldquo;ห้า&rdquo; ออกเสียงเหมือนเสียงหัวเราะ คนไทยจึงพิมพ์ <b>555</b> แทนคำว่า &ldquo;ฮ่าฮ่าฮ่า&rdquo; ให้ความรู้สึกสนุกและมีความสุข</li>
        <li><b>6 (&ldquo;หก&rdquo;)</b> — ก้ำกึ่ง คำนี้พ้องกับกริยา &ldquo;หก&rdquo; (ทำหล่น/ล้ม) บางคนจึงระวัง ขณะที่บางคนตีความเชิงบวกว่าการเคลื่อนที่อย่างราบรื่น</li>
        <li><b>7 (&ldquo;เจ็ด&rdquo;)</b> — ความเห็นต่างกัน หลายคนมองว่าเกี่ยวกับจิตวิญญาณและเป็นมงคลในบางบริบท แต่บางคนก็ระมัดระวัง</li>
        <li><b>8 (&ldquo;แปด&rdquo;)</b> — ความมั่งคั่งและความรุ่งเรือง ยืมมาจากวัฒนธรรมจีนที่เลขแปดพ้องกับคำว่า &ldquo;รวย&rdquo; จะเห็น <b>888</b> ในราคาและป้ายทะเบียนพอ ๆ กับเลขเก้า</li>
        <li><b>9 (&ldquo;เก้า&rdquo;)</b> — ราชาแห่งเลขมงคล พ้องเสียงกับ &ldquo;ก้าว&rdquo; (ก้าวไปข้างหน้า/ความก้าวหน้า) และ &ldquo;ข้าว&rdquo; (ความอุดมสมบูรณ์) ทั้งยังมีความหมายเชิงสถาบันอย่างลึกซึ้ง — ในหลวงรัชกาลที่ 9 ร้านค้าเปิดเวลา 9:09 น. พิธีมงคลนิมนต์พระ 9 รูป และป้ายทะเบียน 9999 เคยซื้อขายกันถึงหลักล้านบาท</li>
        <li><b>0 (&ldquo;ศูนย์&rdquo;)</b> — โดยรวมเป็นกลาง บางครั้งตีความว่าความสมบูรณ์หรือการเริ่มต้นใหม่</li>
      </ul>

      <h3>ลำดับเลขและการซ้ำ</h3>
      <p>ความหมายจะเข้มข้นขึ้นเมื่อเลขซ้ำหรือเรียงเป็นแบบแผน:</p>
      <ul>
        <li><b>การซ้ำขยายความหมาย</b> ถ้าเก้าเป็นมงคล 99 และ 999 ก็ยิ่งมงคล เช่นเดียวกับ 888 จึงเป็นเหตุผลที่ป้ายทะเบียนและเบอร์โทรเลขซ้ำมีราคาแพงที่สุด</li>
        <li><b>ทิศทางก็สำคัญ</b> ลำดับที่ไล่ขึ้นอย่าง 123 หรือ <b>789</b> ถูกอ่านว่า &ldquo;ไต่ขึ้น&rdquo; สื่อถึงความก้าวหน้า จึงเป็นที่นิยม ส่วนลำดับที่ไล่ลงอาจให้ความรู้สึกตรงข้าม</li>
        <li><b>444</b> ซ้อนความหมายเรื่องความตายถึงสามครั้ง จึงถูกเลี่ยงอย่างหนัก</li>
        <li><b>555</b> ในทางกลับกันเป็นเพียงเสียงหัวเราะที่ร่าเริง</li>
      </ul>

      <h3>เลขมงคลกับสลาก — ส่วนที่ต้องพูดตรง ๆ</h3>
      <p>ทั้งหมดนี้ไหลตรงเข้าสู่สลากกินแบ่ง ผู้ขายมักตั้งราคาสลากที่มีเลขมงคล — เลขเก้าและแปดเรียงกัน เลขซ้ำ ลำดับไล่ขึ้น วันเกิด หรือเลขป้ายทะเบียนจากเหตุการณ์โชคดีล่าสุด — สูงกว่าปกติ และผู้ซื้อก็พลิกหาเลข &ldquo;ที่ใช่&rdquo; ในแผงของผู้ขาย เลขยังมาจากความฝัน การให้พรของพระ หรือข่าว</p>
      <p>และนี่คือส่วนที่เราจะไม่พูดให้อ่อนลง <b>การออกรางวัลเป็นการสุ่มและเป็นอิสระ</b> สลากเลข &ldquo;มงคล&rdquo; 999999 มีโอกาสเท่ากันเป๊ะกับเลข &ldquo;ต้องห้าม&rdquo; 444444 — ประมาณ 1 ใน 1,000,000 สำหรับรางวัลที่ 1 หรือ 1 ใน 100 สำหรับเลขท้าย 2 ตัว การเลือกเลขด้วยความหมายเป็นธรรมเนียมที่งดงาม แต่ไม่ได้เปลี่ยนโอกาสของคุณ และการจ่ายแพงขึ้นเพื่อเลขมงคลก็เพียงทำให้เสียเงินมากขึ้นเพื่อโอกาสเท่าเดิม เราอธิบายคณิตศาสตร์ไว้ใน <a href="/guides/why-you-cant-predict-lottery-numbers/">ทำไมจึงทำนายเลขสลากไม่ได้</a></p>

      <h3>เพลิดเพลินกับวัฒนธรรม เคารพความน่าจะเป็น</h3>
      <p>ความเชื่อเหล่านี้เป็นส่วนหนึ่งที่มีชีวิตและงดงามของวัฒนธรรมไทย สมควรได้รับความสนใจมากกว่าการเยาะเย้ย หากอยากเล่นเลขที่มีความหมายกับคุณก็เชิญเลย — เพื่อความหมาย ความทรงจำ หรือความสนุก เพียงถือไว้อย่างเบา ๆ ถือว่าเงินที่ใช้เป็นค่าความบันเทิง และดูแนวทางที่หน้า <a href="/responsible-play/">เล่นอย่างมีสติ</a> หากมันเลิกสนุก คุณค้นประวัติของเลขใด ๆ ได้ที่ <a href="/search/">ค้นหาหมายเลข</a></p>
"""

CULTURE_FAQ = [
    ("Why is 9 considered lucky in Thailand?",
     "Nine (&ldquo;kao&rdquo;) sounds like the Thai words for &ldquo;to step forward&rdquo; (progress) and &ldquo;rice&rdquo; (abundance), and carries royal resonance, so it is seen as the most auspicious digit."),
    ("Why do some Thai buildings skip the 4th floor?",
     "Four (&ldquo;sii&rdquo;) is strongly associated with death, an idea rooted in Chinese culture and common in Thailand, so some buildings omit a fourth floor and many people avoid 4 in addresses and phone numbers."),
    ("Do lucky numbers win the lottery more often?",
     "No. Every draw is random and independent, so a &ldquo;lucky&rdquo; number has exactly the same chance as any other. Lucky numbers are a cultural choice, not a way to improve your odds."),
]

CULTURE_FAQ_TH = [
    ("ทำไมเลข 9 จึงถือเป็นเลขมงคลในไทย?",
     "เลขเก้า (&ldquo;เก้า&rdquo;) พ้องเสียงกับคำว่า &ldquo;ก้าว&rdquo; (ความก้าวหน้า) และ &ldquo;ข้าว&rdquo; (ความอุดมสมบูรณ์) อีกทั้งมีความหมายเชิงสถาบัน จึงถูกมองว่าเป็นเลขที่เป็นมงคลที่สุด"),
    ("ทำไมอาคารบางแห่งในไทยจึงข้ามชั้น 4?",
     "เลขสี่ (&ldquo;สี่&rdquo;) ผูกกับความตายอย่างแน่นแฟ้น ความเชื่อนี้มีรากจากวัฒนธรรมจีนและพบได้ทั่วไปในไทย อาคารบางแห่งจึงข้ามชั้นสี่ และหลายคนเลี่ยงเลข 4 ในที่อยู่และเบอร์โทร"),
    ("เลขมงคลถูกรางวัลบ่อยกว่าจริงไหม?",
     "ไม่จริง ทุกงวดเป็นการสุ่มและเป็นอิสระ เลข &ldquo;มงคล&rdquo; จึงมีโอกาสเท่ากับเลขอื่นทุกประการ เลขมงคลเป็นทางเลือกทางวัฒนธรรม ไม่ใช่วิธีเพิ่มโอกาสถูกรางวัล"),
]

# ---------------------------------------------------------------------------
# Playing as a foreigner
# ---------------------------------------------------------------------------
FOREIGNERS = """
      <p class="lead">Yes &mdash; foreigners can legally buy Thai Government Lottery tickets and claim any prize they win, up to and including the six-million-baht first prize. Whether you are a tourist passing through Bangkok, an expat living in Chiang Mai, or a migrant worker sending money home, the rules are the same: the ticket is what matters, not your passport. This guide explains exactly what you can and cannot do, and how to protect a winning ticket. Always confirm current procedures with the <a href="https://www.glo.or.th" target="_blank" rel="noopener nofollow">Government Lottery Office</a> (GLO), as details can change.</p>

      <h3>Buying a ticket: open to everyone, in person</h3>
      <p>There is no nationality requirement to buy a Thai Government Lottery ticket, and no ID is asked for at the point of sale. You simply buy from a licensed street vendor, market stall or lottery shop anywhere in Thailand. Draws are held twice a month, on the 1st and the 16th, and vendors sell right up until draw day.</p>
      <p>The official face value is <b>80 baht</b> per ticket, each printed with one six-digit number. Vendors often ask more for &ldquo;popular&rdquo; numbers, and tickets are commonly bundled in matching pairs &mdash; which is why winners holding a pair collect twelve million baht instead of six. A small premium is common; several hundred baht for an ordinary ticket is not something you need to accept.</p>

      <h3>What foreigners cannot do: the official digital lottery</h3>
      <p>Thailand also sells official digital tickets through the GLO&rsquo;s online channels and the <b>Paotang app</b>, at a fixed 80 baht. Registration, however, requires e-KYC identity verification with a <b>Thai national ID card</b>, which most foreigners do not hold. Thai citizens can buy digital tickets from their phone; foreigners are limited to paper tickets bought in person.</p>
      <p>The same applies from abroad: there is no official way to buy a Thai lottery ticket over the internet from outside Thailand. Websites selling &ldquo;Thai lottery tickets&rdquo; internationally, or offering Thai results as a betting product, are not part of the official lottery &mdash; and private lottery-style gambling is illegal under Thai law.</p>

      <h3>If you win: your prize is yours</h3>
      <p>Nationality does not affect the right to claim. A Thai lottery ticket is a <b>bearer instrument</b>: whoever presents the physical ticket can claim the prize. That cuts both ways &mdash; it means a foreigner faces no extra hurdle to the money, and it also means a lost or stolen ticket is as good as gone. The moment you buy, and certainly the moment you learn you have won, <b>sign your name on the back of the ticket</b>. For either claim route below, the ID a foreigner presents is the <b>passport used to enter Thailand</b>.</p>

      <h3>Claiming a small prize (up to 20,000 baht): simple, but watch the fee</h3>
      <p>For smaller wins &mdash; last-two-digit, three-digit and similar tiers &mdash; a foreigner can be paid <b>in cash on the spot</b> by an authorised lottery vendor or agent. Show the signed ticket and your passport. The special consideration here is the <b>service fee</b>: vendors typically deduct around 1&ndash;2% for the convenience, and as a visitor you should expect no official receipt from a street payout. If you want the full amount and formal paperwork, you can instead claim at a Government Lottery Office, where only the 0.5% stamp duty is withheld. For a tourist, cash from a vendor is usually the practical choice; for anyone who needs documentation &mdash; for example to satisfy a bank or a home-country tax office &mdash; the GLO route is worth the trip.</p>

      <h3>Claiming a large prize (over 20,000 baht): plan for the cheque</h3>
      <p>Prizes above 20,000 baht, including the six-million-baht first prize, must be claimed <b>in person</b> at the Government Lottery Office &mdash; the head office is at 359 Sanambin Nam Road, Nonthaburi, near Bangkok. You fill out a claim form, staff verify the ticket, duty is withheld, and the prize is paid <b>by cheque</b>, not cash. You may also be asked for a Thai <b>tax identification number</b> for prizes at this level; GLO staff can direct you through this step.</p>
      <p>The cheque is the real special consideration for foreigners. It is drawn through the GLO&rsquo;s partner bank, <b>Krungthai Bank</b>, and the smoothest path is depositing it into a <b>Thai bank account</b> in your own name &mdash; something expats usually have, but short-stay tourists often do not. Reports also indicate that very large amounts (over roughly two million baht) may be transferred only into designated Thai bank accounts. If you have no Thai account, ask the GLO on the day about cashing the cheque at the partner bank; and remember that <b>customs declaration rules</b> apply to large amounts of currency leaving Thailand. The full step-by-step process is in our guide to <a href="/guides/how-to-claim-thai-lottery-prize/">claiming a Thai lottery prize</a>; procedures change, so confirm current requirements with the GLO first.</p>

      <h3>Taxes and deductions</h3>
      <p>Winnings from the Government Lottery carry a <b>0.5% stamp duty</b> (1% for charity draws), deducted when the prize is paid. There is no extra tax for foreigners &mdash; a foreign winner and a Thai winner take home the same amount. Keep the official receipt: your home country may require you to declare foreign lottery winnings, and rules vary widely, so check with your own tax authority. Details are in our <a href="/guides/thai-lottery-taxes-stamp-duty/">taxes and stamp duty guide</a>.</p>

      <h3>Practical tips for foreign players</h3>
      <ul>
        <li><b>Buy in person, from a licensed vendor.</b> Online offers aimed at foreigners are scams or illegal gambling.</li>
        <li><b>Know the real price:</b> 80 baht face value. A modest street premium is common; a large one is not worth paying.</li>
        <li><b>Sign the ticket immediately</b> and photograph both sides.</li>
        <li><b>Check results against official sources</b> &mdash; scan 20 years of draws with our <a href="/check/">Did I Win? checker</a>, then confirm with the GLO.</li>
        <li><b>Claim before you leave.</b> Prizes stay valid for <b>two years</b>, but claiming requires the ticket and your passport in Thailand.</li>
        <li><b>Timing:</b> results are announced from around 4:00 PM Bangkok time on the 1st and 16th of each month.</li>
      </ul>

      <h3>The bottom line</h3>
      <p>Foreigners &mdash; tourists included &mdash; play the Thai lottery on almost equal footing with Thai citizens: buy any paper ticket in person, win any prize, pay the same small stamp duty. The real differences are access (no official online purchase without a Thai ID) and logistics (a big prize means a cheque from a GLO office, easiest with a Thai bank account). Play for fun, buy at a fair price, sign your ticket, and treat every draw as pure chance &mdash; our <a href="/guides/thai-lottery-odds-tier-by-tier/">odds guide</a> shows the honest numbers behind every tier.</p>
"""

FOREIGNERS_FAQ = [
    ("Can a tourist buy a Thai lottery ticket?",
     "Yes. Anyone can buy a paper ticket from a licensed vendor in Thailand — no ID, visa type or residency is required at the point of sale."),
    ("Can foreigners use the Paotang app or buy tickets online?",
     "Generally no. Official digital tickets require e-KYC registration with a Thai national ID card, so most foreigners can only buy paper tickets in person. Sites selling Thai tickets internationally are not official."),
    ("Can a foreigner claim the first prize?",
     "Yes. The ticket is a bearer instrument — whoever holds the winning ticket can claim. Bring the signed original ticket and your passport; prizes over 20,000 baht are claimed at a Government Lottery Office."),
    ("Do foreigners pay extra tax on Thai lottery winnings?",
     "No. The same 0.5% stamp duty (1% for charity draws) applies to everyone. Your home country may separately require you to declare the winnings — check your own tax rules."),
    ("I'm a tourist without a Thai bank account — how do I collect a large prize?",
     "Large prizes are paid by cheque through the GLO's partner bank, Krungthai Bank. Ask the GLO about cashing the cheque at the partner bank on the day; very large amounts may need to go into a designated Thai bank account. Confirm current options with the GLO before visiting."),
    ("How long is a winning ticket valid?",
     "Two years from the draw date. After that the prize is forfeited. If you are visiting, claim before you leave Thailand — the process requires the physical ticket and your passport."),
]

ARTICLES = [
    dict(slug="can-foreigners-play-thai-lottery",
         title="Can Foreigners Play the Thai Lottery? Rules, Buying & Claiming | ThaiLotteryNumbers",
         desc="Yes — foreigners and tourists can legally buy Thai lottery tickets and claim any prize, including first prize. What you need, what it costs, the online restriction, and how claiming works.",
         h1="Can Foreigners Play the Thai Lottery?",
         category="Claiming &amp; Official Process",
         published="2026-07-20", updated="2026-07-20",
         body=FOREIGNERS, faq=FOREIGNERS_FAQ),

    dict(slug="thai-lucky-unlucky-numbers",
         title="Lucky and Unlucky Numbers in Thailand: A Cultural Guide | ThaiLotteryNumbers",
         desc="Why 9 is lucky, why 4 is avoided, and what every digit and sequence like 789 or 444 means in Thai culture \u2014 plus the honest truth about lucky numbers and the lottery.",
         h1="Lucky and Unlucky Numbers in Thailand",
         h1_th="เลขมงคลและเลขอัปมงคลในวัฒนธรรมไทย",
         desc_th="ทำไมเลข 9 จึงมงคล ทำไมเลข 4 จึงถูกเลี่ยง และแต่ละหลักกับลำดับอย่าง 789 หรือ 444 หมายถึงอะไรในวัฒนธรรมไทย พร้อมความจริงเรื่องเลขมงคลกับสลาก",
         category="Culture &amp; Beliefs", category_th="วัฒนธรรม &amp; ความเชื่อ",
         published=DATE, updated=DATE,
         body=CULTURE, body_th=CULTURE_TH, faq=CULTURE_FAQ, faq_th=CULTURE_FAQ_TH),

    dict(slug="why-you-cant-predict-lottery-numbers",
         title="Why You Can't Predict Thai Lottery Numbers (The Math, Explained Simply) | ThaiLotteryNumbers",
         desc="Hot numbers, \u201cdue\u201d numbers and lucky systems can't predict the Thai lottery. Here's the simple math of independent draws, the gambler's fallacy, and your real odds.",
         h1="Why You Can&rsquo;t Predict Thai Lottery Numbers",
         category="Understanding the Numbers",
         published=DATE, updated=DATE, body=PREDICT, faq=PREDICT_FAQ),

    dict(slug="how-thai-government-lottery-works",
         title="How the Thai Government Lottery Works: A Complete Guide | ThaiLotteryNumbers",
         desc="A complete guide to the Thai Government Lottery: who runs it, draw dates and times, how tickets and pairs work, the air-mix draw, and every prize tier explained.",
         h1="How the Thai Government Lottery Works",
         category="How the Lottery Works",
         published=DATE, updated=DATE, body=HOW_IT_WORKS),

    dict(slug="thai-lottery-prize-tiers-explained",
         title="Thai Lottery Prize Tiers Explained: What Each Match Pays | ThaiLotteryNumbers",
         desc="Every Thai lottery prize tier and what it pays, from the 6,000,000 baht first prize to the 2,000 baht last-two digits, plus how the ticket-pair doubling works.",
         h1="Thai Lottery Prize Tiers Explained",
         category="How the Lottery Works",
         published=DATE, updated=DATE, body=PRIZE_TIERS),

    dict(slug="when-is-thai-lottery-drawn",
         title="When Is the Thai Lottery Drawn? Dates, Times & Holiday Shifts | ThaiLotteryNumbers",
         desc="The Thai lottery is drawn on the 1st and 16th at around 4 PM Bangkok time. Learn the schedule, the draw time in ICT, holiday shifts and year-end date changes.",
         h1="When Is the Thai Lottery Drawn?",
         category="How the Lottery Works",
         published=DATE, updated=DATE, body=DRAW_DATES),

    dict(slug="how-to-claim-thai-lottery-prize",
         title="How to Claim a Thai Lottery Prize: Step-by-Step | ThaiLotteryNumbers",
         desc="A step-by-step guide to claiming a Thai lottery prize: verifying the win, signing the ticket, where to go for small vs large prizes, what to bring, and the 2-year deadline.",
         h1="How to Claim a Thai Lottery Prize",
         category="Claiming &amp; Official Process",
         published=DATE, updated=DATE, body=CLAIM, howto=CLAIM_HOWTO, faq=CLAIM_FAQ),

    dict(slug="thai-lottery-taxes-stamp-duty",
         title="Thai Lottery Taxes & Stamp Duty: What Winners Actually Pay | ThaiLotteryNumbers",
         desc="What is deducted from a Thai lottery prize: 0.5% stamp duty on the Government Lottery, 1% on the Charity Lottery, vendor commission, and notes for foreign winners.",
         h1="Thai Lottery Taxes &amp; Stamp Duty",
         category="Claiming &amp; Official Process",
         published=DATE, updated=DATE, body=TAXES, faq=TAXES_FAQ),

    dict(slug="what-hot-and-cold-numbers-mean",
         title="What \"Hot and Cold Numbers\" Really Mean (and Don't) | ThaiLotteryNumbers",
         desc="What hot and cold Thai lottery numbers actually are, how frequency is calculated, why the differences are normal randomness, and why they can't predict the next draw.",
         h1="What &ldquo;Hot and Cold Numbers&rdquo; Really Mean",
         category="Understanding the Numbers",
         published=DATE, updated=DATE, body=HOT_COLD),

    dict(slug="thai-lottery-odds-tier-by-tier",
         title="Understanding Thai Lottery Odds: Your Real Chances Tier by Tier | ThaiLotteryNumbers",
         desc="Your real Thai lottery odds, tier by tier: about 1 in 1,000,000 for the first prize and 1 in 100 for the last two digits, explained in plain language with the math.",
         h1="Understanding Thai Lottery Odds, Tier by Tier",
         category="Understanding the Numbers",
         published=DATE, updated=DATE, body=ODDS),

    dict(slug="20-years-thai-lottery-data",
         title="20 Years of Thai Lottery Data: What the Long-Term Record Shows | ThaiLotteryNumbers",
         desc="A look at 464 Thai lottery draws from 2006 to 2026: draws per year, when the front-three prize began, and why the long-term spread of numbers looks random.",
         h1="20 Years of Thai Lottery Data: What the Record Shows",
         category="Understanding the Numbers",
         published=DATE, updated=DATE, body=DATA_20Y),

    dict(slug="thai-lottery-faq",
         title="Thai Lottery FAQ: Draws, Prizes, Claiming & Odds | ThaiLotteryNumbers",
         desc="Answers to the most common Thai lottery questions: draw times, ticket price, prize amounts, how to check and claim, taxes, odds, and whether results can be predicted.",
         h1="Frequently Asked Questions About the Thai Lottery",
         category="How the Lottery Works",
         published=DATE, updated=DATE, body=FAQ_ARTICLE, faq=FAQ_ARTICLE_FAQ),
]
