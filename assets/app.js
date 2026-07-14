/* ============================================================
   Thai Lottery Numbers — application
   Vanilla JS · hash router · no build step
   ============================================================ */
(() => {
"use strict";

const S = { lang: localStorage.getItem("tln_lang") || "en", draws: [], stats: null, cd: null };
const $ = (s, r=document) => r.querySelector(s);
const t = k => (window.I18N[S.lang][k] ?? window.I18N.en[k] ?? k);
const tn = (k, n) => t(k).replace("{n}", n);
const esc = s => String(s).replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));

const LOGO = `<svg viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
<defs><clipPath id="r"><circle cx="32" cy="32" r="25"/></clipPath>
<linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F7D778"/><stop offset=".5" stop-color="#F2C14E"/><stop offset="1" stop-color="#C8901F"/></linearGradient></defs>
<circle cx="32" cy="32" r="30" fill="url(#g)"/><circle cx="32" cy="32" r="26.5" fill="#0B1026"/>
<g clip-path="url(#r)"><rect x="7" y="7" width="50" height="50" fill="#EF3340"/><rect x="7" y="15" width="50" height="34" fill="#F5F7FA"/><rect x="7" y="22" width="50" height="20" fill="#241E4E"/><rect x="7" y="15" width="50" height="7" fill="#F5F7FA"/><rect x="7" y="42" width="50" height="7" fill="#F5F7FA"/></g>
<circle cx="32" cy="32" r="25" fill="none" stroke="url(#g)" stroke-width="2.5"/>
<text x="32" y="38" text-anchor="middle" font-family="monospace" font-weight="700" font-size="15" fill="#F2C14E" stroke="#0B1026" stroke-width=".6">88</text></svg>`;

const KANOK = `<svg class="kanok" viewBox="0 0 100 100" fill="none" stroke="#F2C14E" stroke-width="2"><path d="M50 5 C70 25 70 45 50 60 C30 45 30 25 50 5 Z M50 95 C30 75 30 55 50 40 C70 55 70 75 50 95 Z"/><circle cx="50" cy="50" r="6"/></svg>`;

const ROUTES = ["", "results", "stats", "search", "check", "about", "contact",
  "faq", "guides", "responsible-play", "privacy", "cookies", "terms", "cookie-settings", "accessibility"];

/* official GLO prize amounts (baht, per single ticket) */
const PRIZES = { first:6000000, near:100000, second:200000, third:80000,
  fourth:40000, fifth:20000, front3:4000, last3:4000, last2:2000 };
const baht = n => "฿" + n.toLocaleString("en-US");

/* ---------- date helpers ---------- */
const PRIZE_KEYS = ["second","third","fourth","fifth"];
function fmtDate(iso){
  const [y,m,d] = iso.split("-").map(Number);
  const months = S.lang==="th"
    ? ["ม.ค.","ก.พ.","มี.ค.","เม.ย.","พ.ค.","มิ.ย.","ก.ค.","ส.ค.","ก.ย.","ต.ค.","พ.ย.","ธ.ค."]
    : ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
  const yr = S.lang==="th" ? y+543 : y;
  return `${d} ${months[m-1]} ${yr}`;
}

/* next official draw: 1st & 16th, 16:00 Asia/Bangkok (=09:00 UTC) */
function nextDraw(){
  const now = Date.now();
  const cand = [];
  const d = new Date();
  for (let i=0;i<3;i++){
    const y=d.getUTCFullYear(), m=d.getUTCMonth();
    cand.push(Date.UTC(y,m,1,9,0,0), Date.UTC(y,m,16,9,0,0));
    d.setUTCMonth(m+1);
  }
  return cand.filter(x=>x>now).sort((a,b)=>a-b)[0];
}

/* ============================================================ shell */
function buildShell(){
  $(".logo-slot").innerHTML = LOGO;
  // nav
  const nav = [["","nav_home"],["results","nav_results"],["stats","nav_stats"],
    ["search","nav_search"],["check","nav_check"],["guides","nav_guides"],["faq","nav_faq"],["about","nav_about"],["contact","nav_contact"]];
  $("#navLinks").innerHTML = nav.map(([r,k]) =>
    `<a href="${r==='contact'?'/contact.html':'/'+r}" data-route="${r==='contact'?'contact.html':r}">${t(k)}</a>`).join("");
  // footer
  $("#footerGrid").innerHTML = `
    <div>
      <div class="brand" style="margin-bottom:12px">${LOGO}<span class="bn">Thai Lottery<b>Numbers</b></span></div>
      <p class="muted" style="font-size:.86rem">${t("data_note")}</p>
    </div>
    <div><h4>${t("ft_explore")}</h4>
      <a href="/results">${t("nav_results")}</a><a href="/stats">${t("nav_stats")}</a>
      <a href="/search">${t("nav_search")}</a><a href="/check">${t("nav_check")}</a></div>
    <div><h4>${t("ft_about")}</h4>
      <a href="/about">${t("nav_about")}</a><a href="/faq">${t("nav_faq")}</a><a href="/contact.html">${t("nav_contact")}</a></div>
    <div><h4>${t("ft_legal")}</h4>
      <a href="/privacy">${t("legal_privacy")}</a><a href="/cookies">${t("legal_cookie")}</a>
      <a href="/terms">${t("legal_terms")}</a><a href="/responsible-play">${t("legal_responsible")}</a>
      <a href="/cookie-settings">${t("legal_cookie_set")}</a>
      <a href="/accessibility">${t("legal_access")}</a></div>`;
  $("#ftDisclaimerShort").textContent = t("disclaimer");
  document.querySelectorAll(".ad-slot").forEach(s=>s.setAttribute("data-label", t("ad_label")));
  // lang toggle
  document.querySelectorAll(".lang-toggle button").forEach(b=>{
    b.classList.toggle("on", b.dataset.lang===S.lang);
    b.onclick = () => { S.lang=b.dataset.lang; localStorage.setItem("tln_lang",S.lang);
      document.documentElement.lang=S.lang; buildShell(); render(); };
  });
  cookieBanner();
}

function cookieBanner(){
  const el = $("#cookieBanner");
  if (localStorage.getItem("tln_cookie")==="1"){ el.innerHTML=""; return; }
  el.innerHTML = `<div class="cookie">
    <p>${t("cookie_text")}</p>
    <a class="btn btn-ghost" href="/cookie-settings">${t("cookie_settings")}</a>
    <button class="btn btn-gold" id="ckOk">${t("cookie_accept")}</button></div>`;
  $("#ckOk").onclick = ()=>{ localStorage.setItem("tln_cookie","1"); el.innerHTML=""; };
}

function toast(msg){
  const el=$("#toast"); el.textContent=msg; el.style.display="block";
  clearTimeout(el._t); el._t=setTimeout(()=>el.style.display="none",1800);
}

function disclaimerBox(){ return ""; }

/* ============================================================ router */
function parsePath(){
  let p = location.pathname.replace(/\/+$/,"");          // strip trailing slash
  if (p.startsWith("/")) p = p.slice(1);                 // strip leading slash
  const seg = p.split("/").filter(Boolean);
  return [seg[0]||"", seg[1]||""];                       // [route, param]
}

function navigate(url){
  history.pushState({}, "", url);
  render();
}

function render(keepScroll){
  const [route, param] = parsePath();
  document.querySelectorAll("#navLinks a").forEach(a=>
    a.classList.toggle("active", a.dataset.route===route));
  $(".nav-links").classList.remove("open");
  const v = $("#view");
  if(!keepScroll) window.scrollTo(0,0);

  if (route==="results" && param) return drawDetail(param);
  if (route==="guides") return;   // /guides and /guides/* are static HTML; leave baked content
  if (route==="contact") return;  // /contact is static baked HTML (contact form); leave baked content
  switch(route){
    case "": return home();
    case "results": return results();
    case "stats": return stats();
    case "search": return search();
    case "check": return checker();
    case "about": return about();
    case "contact": return contact();
    case "faq": return faq();
    case "responsible-play": return responsiblePlay();
    case "privacy": return legalPrivacy();
    case "cookies": return legalCookies();
    case "terms": return legalTerms();
    case "cookie-settings": return cookieSettings();
    case "accessibility": return legalAccess();
    default: return notFound();
  }
}

/* ============================================================ views */
function ballRow(arr, n=5, sm=false){
  return arr.slice(0,n).map(x=>`<div class="ball${sm?' sm':''}"><b>${x.n}</b><span>${tn("drawn_x",x.c)}</span></div>`).join("");
}

function home(){
  const d = S.draws[0];
  const recent = S.draws.slice(0,10);
  $("#view").innerHTML = `
  <section class="hero wrap">
    ${KANOK}
    <div class="hero-grid">
      <div>
        <h1>${t("hero_title_a")}<br><span class="g">${t("hero_title_b")}</span></h1>
        <p class="sub">${t("hero_sub")}</p>
        <div class="hero-cta">
          <a class="btn btn-gold" href="/search">${t("cta_search")}</a>
          <a class="btn btn-ghost" href="/check">${t("nav_check")}</a>
        </div>
      </div>
      <div class="draw-card">
        <div class="top"><span class="tag-live"><span class="dot"></span>${t("live")}</span>
          <span class="muted">${fmtDate(d.date)}</span></div>
        <div class="first-prize"><div class="lbl">${t("first_prize")}</div>
          <div class="num">${d.first}</div>
          <div class="payout-pill">${t("prize_sixdigit")} · <b>${baht(PRIZES.first)}</b></div></div>
        <div class="prize-row">
          <div class="prize-cell"><div class="lbl">${t("front3")}</div><div class="v">${d.front3.join(" ")||"—"}</div><div class="pay">${baht(PRIZES.front3)}</div></div>
          <div class="prize-cell"><div class="lbl">${t("last3")}</div><div class="v">${d.last3.slice(0,2).join(" ")}</div><div class="pay">${baht(PRIZES.last3)}</div></div>
          <div class="prize-cell"><div class="lbl">${t("last2")}</div><div class="v two">${d.last2}</div><div class="pay">${baht(PRIZES.last2)}</div></div>
        </div>
        <div class="spacer"></div>
        <div class="lbl muted center" style="font-size:.74rem;letter-spacing:.1em;text-transform:uppercase">${t("next_draw")}</div>
        <div class="countdown" id="cd"></div>
      </div>
    </div>
  </section>

  <section class="section wrap" style="padding-top:0">
    <span class="eyebrow">${t("prizes_title")}</span>
    <h2>${t("prizes_title")}</h2><p class="lead">${t("prizes_sub")}</p>
    <div class="spacer"></div>
    <div class="payout-grid">
      <div class="payout-card hi"><div class="pc-lbl">${t("prize_sixdigit")}</div><div class="pc-amt">${baht(PRIZES.first)}</div></div>
      <div class="payout-card"><div class="pc-lbl">${t("prize_near")}</div><div class="pc-amt">${baht(PRIZES.near)}</div></div>
      <div class="payout-card"><div class="pc-lbl">${t("prize_second")}</div><div class="pc-amt">${baht(PRIZES.second)}</div></div>
      <div class="payout-card"><div class="pc-lbl">${t("prize_third")}</div><div class="pc-amt">${baht(PRIZES.third)}</div></div>
      <div class="payout-card"><div class="pc-lbl">${t("prize_fourth")}</div><div class="pc-amt">${baht(PRIZES.fourth)}</div></div>
      <div class="payout-card"><div class="pc-lbl">${t("prize_fifth")}</div><div class="pc-amt">${baht(PRIZES.fifth)}</div></div>
      <div class="payout-card"><div class="pc-lbl">${t("prize_front3")}</div><div class="pc-amt">${baht(PRIZES.front3)}</div></div>
      <div class="payout-card"><div class="pc-lbl">${t("prize_last3")}</div><div class="pc-amt">${baht(PRIZES.last3)}</div></div>
      <div class="payout-card hi2"><div class="pc-lbl">${t("prize_last2")}</div><div class="pc-amt">${baht(PRIZES.last2)}</div></div>
    </div>
    <p class="muted" style="font-size:.82rem;margin-top:12px">${t("pair_note")}</p>
  </section>

  <section class="section wrap" style="padding-top:0">
    <span class="eyebrow">${t("hot_title")}</span>
    <h2>${t("hot_title")}</h2><p class="lead">${t("hot_sub")}</p>
    <div class="spacer"></div>
    <div class="cards g3">
      <div class="card"><h4 class="gold" style="margin-bottom:14px">${t("hot2")}</h4><div class="hot-row">${ballRow(S.stats.last2,5)}</div></div>
      <div class="card"><h4 class="gold" style="margin-bottom:14px">${t("hot3f")}</h4><div class="hot-row">${ballRow(S.stats.front3,4,true)}</div></div>
      <div class="card"><h4 class="gold" style="margin-bottom:14px">${t("hot3l")}</h4><div class="hot-row">${ballRow(S.stats.last3,4,true)}</div></div>
    </div>
  </section>

  <section class="section wrap" style="padding-top:0">
    <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px">
      <div><span class="eyebrow">${t("recent")}</span><h2>${t("recent")}</h2></div>
      <a class="btn btn-ghost" href="/results">${t("view_all")}</a>
    </div>
    <div class="spacer"></div>
    <div class="cards" style="gap:10px">
      ${recent.map(x=>`<a class="mini" href="/results/${x.date}">
        <span class="d">${fmtDate(x.date)}</span>
        <span class="vals"><span class="a mono">${x.first}</span>
        <span class="mono muted">${t("last3")}: ${x.last3.slice(0,2).join("/")}</span>
        <span class="a mono">${t("last2")}: ${x.last2}</span></span></a>`).join("")}
    </div>
  </section>`;
  startCountdown();
}

function startCountdown(){
  if (S.cd) clearInterval(S.cd);
  const target = nextDraw();
  const tick = () => {
    const box = $("#cd"); if(!box){ clearInterval(S.cd); return; }
    let diff = Math.max(0, target - Date.now());
    const dd = Math.floor(diff/864e5); diff-=dd*864e5;
    const hh = Math.floor(diff/36e5); diff-=hh*36e5;
    const mm = Math.floor(diff/6e4); diff-=mm*6e4;
    const ss = Math.floor(diff/1e3);
    const cell=(v,l)=>`<div class="cd-box"><b>${String(v).padStart(2,"0")}</b><span>${l}</span></div>`;
    box.innerHTML = cell(dd,t("days"))+cell(hh,t("hrs"))+cell(mm,t("min"))+cell(ss,t("sec"));
  };
  tick(); S.cd=setInterval(tick,1000);
}

function results(){
  const years = [...new Set(S.draws.map(d=>d.date.slice(0,4)))];
  let year="all", page=0; const PER=20;
  const head = `<section class="section wrap">
    <span class="eyebrow">${t("nav_results")}</span><h1>${t("results_title")}</h1>
    <p class="lead">${t("results_sub")}</p><div class="spacer"></div>
    <div class="toolbar">
      <div class="field"><label class="fl">${t("filter_year")}</label>
        <select id="yr"><option value="all">${t("all_years")}</option>
        ${years.map(y=>`<option value="${y}">${S.lang==="th"?+y+543:y}</option>`).join("")}</select></div>
      <button class="btn btn-ghost" id="exp">${t("export_csv")}</button>
    </div>
    <div id="tbl"></div><div class="pager" id="pg"></div>
    <div class="spacer-lg"></div>${disclaimerBox()}</section>`;
  $("#view").innerHTML = head;

  const draw = () => {
    let rows = year==="all" ? S.draws : S.draws.filter(d=>d.date.startsWith(year));
    const pages = Math.ceil(rows.length/PER);
    const slice = rows.slice(page*PER,(page+1)*PER);
    $("#tbl").innerHTML = `<div class="tbl-wrap"><table>
      <thead><tr><th>${t("col_date")}</th><th>${t("col_first")}</th><th>${t("col_front3")}</th>
      <th>${t("col_last3")}</th><th>${t("col_last2")}</th><th></th></tr></thead><tbody>
      ${slice.map(d=>`<tr>
        <td>${fmtDate(d.date)}</td><td class="m gold">${d.first}</td>
        <td class="m">${d.front3.join(" ")||"—"}</td><td class="m">${d.last3.slice(0,2).join(" ")}</td>
        <td class="m gold">${d.last2}</td>
        <td><a class="badge b-muted" href="/results/${d.date}">${t("view")} →</a></td></tr>`).join("")}
      </tbody></table></div>`;
    $("#pg").innerHTML = pages>1 ? `
      <button ${page===0?"disabled":""} id="prev">←</button>
      <span class="muted" style="align-self:center">${page+1} / ${pages}</span>
      <button ${page>=pages-1?"disabled":""} id="next">→</button>`:"";
    if($("#prev"))$("#prev").onclick=()=>{page--;draw();};
    if($("#next"))$("#next").onclick=()=>{page++;draw();};
  };
  $("#yr").onchange = e => { year=e.target.value; page=0; draw(); };
  $("#exp").onclick = () => exportCSV(year==="all"?S.draws:S.draws.filter(d=>d.date.startsWith(year)));
  draw();
}

function drawDetail(date){
  const d = S.draws.find(x=>x.date===date);
  if(!d) return notFound();
  const tier = (label, arr, cls="") => arr.length ? `
    <div class="card" style="margin-top:14px"><h4 class="${cls}" style="margin-bottom:10px">${label}
      <span class="muted" style="font-family:var(--body);font-weight:400">· ${arr.length}</span></h4>
      <div class="mono" style="display:flex;flex-wrap:wrap;gap:8px 18px">
        ${arr.map(n=>`<span>${n}</span>`).join("")}</div></div>`:"";
  $("#view").innerHTML = `<section class="section wrap">
    <a class="badge b-muted" href="/results">← ${t("back")}</a>
    <div class="spacer"></div>
    <span class="eyebrow">${t("draw_detail")} · ${d.date}</span>
    <h1>${fmtDate(d.date)}</h1>
    <button class="btn btn-ghost" style="margin-top:10px" id="share">🔗 ${t("share")}</button>
    <div class="spacer"></div>
    <div class="draw-card" style="max-width:540px">
      <div class="first-prize"><div class="lbl">${t("first_prize")}</div><div class="num">${d.first}</div></div>
      <div class="prize-row">
        <div class="prize-cell"><div class="lbl">${t("front3")}</div><div class="v">${d.front3.join(" ")||"—"}</div></div>
        <div class="prize-cell"><div class="lbl">${t("last3")}</div><div class="v">${d.last3.slice(0,2).join(" ")}</div></div>
        <div class="prize-cell"><div class="lbl">${t("last2")}</div><div class="v two">${d.last2}</div></div>
      </div>
      ${d.near.length?`<div class="spacer"></div><div class="center muted" style="font-size:.84rem">${t("near")}: <span class="mono gold">${d.near.join(" · ")}</span></div>`:""}
    </div>
    ${tier(t("prize_second"), d.second, "gold")}
    ${tier(t("prize_third"), d.third)}
    ${tier(t("prize_fourth"), d.fourth)}
    ${tier(t("prize_fifth"), d.fifth)}
    <div class="spacer-lg"></div>${disclaimerBox()}</section>`;
  $("#share").onclick = () => { navigator.clipboard?.writeText(location.href); toast(t("copied")); };
}

/* ---------------- statistics ---------------- */
function stats(){
  const years = [...new Set(S.draws.map(d=>d.date.slice(0,4)))].sort();
  const yrLabel = y => S.lang==="th" ? +y+543 : y;
  $("#view").innerHTML = `<section class="section wrap">
    <span class="eyebrow">${t("nav_stats")}</span><h1>${t("stats_title")}</h1>
    <p class="lead">${t("stats_sub")}</p>
    <div class="spacer"></div>
    <span class="badge b-gold">${t("full_dataset")} · ${yrLabel(years[0])}–${yrLabel(years[years.length-1])}</span>
    <div class="spacer"></div>
    <div class="cards g2">
      <div class="chart-box"><h3>${t("freq2")}</h3><div class="cap">Top 20</div><canvas id="c2" height="200"></canvas></div>
      <div class="chart-box"><h3>${t("hotcold")}</h3><div class="cap">${t("hottest")} / ${t("coldest")}</div><div id="hc"></div></div>
    </div>
    <div class="spacer"></div>
    <div class="cards g2">
      <div class="chart-box"><h3>${t("freq3f")}</h3><div class="cap">Top 20 · ${S.lang==="th"?"ตั้งแต่ ก.ย. 2558":"since Sep 2015"}</div><canvas id="c3f" height="200"></canvas></div>
      <div class="chart-box"><h3>${t("freq3l")}</h3><div class="cap">Top 20</div><canvas id="c3l" height="200"></canvas></div>
    </div>
    <div class="spacer"></div>
    <div class="chart-box"><h3>${t("heat_title")}</h3><div class="cap">${t("heat_sub")}</div><div class="heat" id="heat"></div></div>
    <div class="spacer"></div>
    <div class="chart-box"><h3>${t("trend_title")}</h3><div class="cap">${t("trend_sub")}</div>
      <div class="toolbar" style="margin:12px 0">
        <div class="field"><label class="fl">&nbsp;</label>
          <div class="seg" id="tcat">
            <button data-cat="last2" data-len="2" class="on">${t("last2")}</button>
            <button data-cat="front3" data-len="3">${t("front3")}</button>
            <button data-cat="last3" data-len="3">${t("last3")}</button>
          </div></div>
        <div class="field"><label class="fl">${t("trend_input")}</label>
          <input id="tnum" type="text" inputmode="numeric" maxlength="2" placeholder="77" style="width:120px"></div>
        <button class="btn btn-gold" id="tgo">${t("show_trend")}</button>
      </div><canvas id="ctrend" height="160"></canvas></div>
    <div class="spacer-lg"></div>
    <p class="muted center" style="margin-top:14px;font-size:.84rem">${t("every_draw")}</p>
  </section>`;

  const charts = {};
  const GOLD="#F2C14E", JADE="#2BB7A3", RED="#EF3340", GRID="#262F5C", MUT="#9AA3C7";
  const CAT_COLOR = { last2:GOLD, front3:JADE, last3:RED };
  Chart.defaults.color=MUT; Chart.defaults.font.family="'Sarabun',sans-serif";
  const barOpts = {responsive:true,plugins:{legend:{display:false}},
    scales:{x:{grid:{display:false},ticks:{maxRotation:90,minRotation:90,font:{size:9}}},
      y:{grid:{color:GRID},beginAtZero:true,ticks:{precision:0}}}};

  // full-dataset frequency tables
  const c2={}, c3f={}, c3l={};
  for(let i=0;i<100;i++) c2[String(i).padStart(2,"0")]=0;
  S.draws.forEach(d=>{ if(d.last2)c2[d.last2]=(c2[d.last2]||0)+1;
    d.front3.forEach(n=>c3f[n]=(c3f[n]||0)+1);
    d.last3.forEach(n=>c3l[n]=(c3l[n]||0)+1); });
  const top = (obj,n)=>Object.entries(obj).sort((a,b)=>b[1]-a[1]).slice(0,n);

  const mk=(id,data,color)=>{ const e=top(data,20);
    charts[id]=new Chart($("#"+id),{type:"bar",data:{labels:e.map(x=>x[0]),
      datasets:[{data:e.map(x=>x[1]),backgroundColor:color,borderRadius:4}]},options:barOpts}); };
  mk("c2",c2,GOLD); mk("c3f",c3f,JADE); mk("c3l",c3l,RED);

  // hot / cold (last-2)
  const ranked=Object.entries(c2).sort((a,b)=>b[1]-a[1]);
  const hot=ranked.slice(0,5), cold=ranked.slice(-5).reverse();
  $("#hc").innerHTML=`<div style="margin-bottom:14px"><div class="badge b-red" style="margin-bottom:10px">${t("hottest")}</div>
    <div class="hot-row">${hot.map(([n,c])=>`<div class="ball sm"><b>${n}</b><span>${c}×</span></div>`).join("")}</div></div>
    <div><div class="badge b-jade" style="margin-bottom:10px">${t("coldest")}</div>
    <div class="hot-row">${cold.map(([n,c])=>`<div class="ball sm" style="border-color:#2BB7A3"><b style="color:#2BB7A3">${n}</b><span>${c}×</span></div>`).join("")}</div></div>`;

  // heatmap
  const max=Math.max(...Object.values(c2));
  $("#heat").innerHTML=Array.from({length:100},(_,i)=>{
    const n=String(i).padStart(2,"0"), v=c2[n], a=max?v/max:0;
    const bg=`rgba(242,193,78,${(0.08+a*0.92).toFixed(2)})`;
    const col=a>0.5?"#0B1026":"#F5F7FA";
    return `<div class="cell" style="background:${bg};color:${col}" title="${n}: ${v}×">${n}</div>`;
  }).join("");

  // ---- trend: 2-digit (last-2) or 3-digit (front-3 / last-3) ----
  let tcat="last2";
  const catLabel = { last2:t("last2"), front3:t("front3"), last3:t("last3") };
  const trend = num => {
    const len = tcat==="last2" ? 2 : 3;
    if(!new RegExp(`^\\d{1,${len}}$`).test(num)) return;
    num = num.padStart(len,"0");
    const byYear={}; years.forEach(y=>byYear[y]=0);
    S.draws.forEach(d=>{
      const y=d.date.slice(0,4);
      if(tcat==="last2"){ if(d.last2===num) byYear[y]++; }
      else if(tcat==="front3"){ if(d.front3.includes(num)) byYear[y]++; }
      else { if(d.last3.includes(num)) byYear[y]++; }
    });
    const color=CAT_COLOR[tcat];
    const rgba=tcat==="last2"?"rgba(242,193,78,.15)":tcat==="front3"?"rgba(43,183,163,.15)":"rgba(239,51,64,.15)";
    if(charts.ctrend)charts.ctrend.destroy();
    charts.ctrend=new Chart($("#ctrend"),{type:"line",
      data:{labels:years.map(yrLabel),
        datasets:[{data:years.map(y=>byYear[y]),borderColor:color,backgroundColor:rgba,
          fill:true,tension:.3,pointRadius:3,pointBackgroundColor:color}]},
      options:{responsive:true,plugins:{legend:{display:false},title:{display:true,
        text:`${catLabel[tcat]} · ${num}`,color}},
        scales:{x:{grid:{display:false}},y:{grid:{color:GRID},beginAtZero:true,ticks:{precision:0}}}}});
  };

  $("#tcat").querySelectorAll("button").forEach(btn=>{
    btn.onclick=()=>{
      $("#tcat").querySelectorAll("button").forEach(b=>b.classList.remove("on"));
      btn.classList.add("on");
      tcat=btn.dataset.cat;
      const inp=$("#tnum"); inp.maxLength=+btn.dataset.len;
      inp.placeholder = tcat==="last2" ? "77" : "123";
      inp.value=""; inp.focus();
    };
  });
  $("#tgo").onclick=()=>trend($("#tnum").value);
  $("#tnum").addEventListener("keyup",e=>{if(e.key==="Enter")trend($("#tnum").value);});
  trend("77");
}

/* ---------------- search ---------------- */
function search(){
  $("#view").innerHTML = `<section class="section wrap">
    <span class="eyebrow">${t("nav_search")}</span><h1>${t("search_title")}</h1>
    <p class="lead">${t("search_sub")}</p><div class="spacer"></div>
    <div class="toolbar">
      <div class="field" style="flex:1;min-width:240px"><input id="q" type="text" inputmode="numeric"
        placeholder="${t("search_ph")}" maxlength="6"></div>
      <button class="btn btn-gold" id="go">${t("search_btn")}</button>
    </div>
    <div id="out"></div><div class="spacer-lg"></div>${disclaimerBox()}</section>`;
  const run = () => {
    const q=($("#q").value||"").replace(/\D/g,"");
    if(!q) return;
    const hits=[];
    S.draws.forEach(d=>{
      if(q.length===2){
        if(d.last2===q) hits.push([d,t("prize_last2"),q]);
        if(d.first.slice(-2)===q) hits.push([d,t("prize_first")+" ("+t("last2")+")",d.first]);
      } else if(q.length===3){
        d.front3.forEach(n=>{if(n===q)hits.push([d,t("prize_front3"),n]);});
        d.last3.forEach(n=>{if(n===q)hits.push([d,t("prize_last3"),n]);});
      } else {
        // full 6-digit ticket: check every prize tier, including the
        // partial-match tiers (front-3, last-3, last-2) so a ticket like
        // 500062 is correctly reported as a last-2 winner.
        const f3=q.slice(0,3), l3=q.slice(-3), l2=q.slice(-2);
        if(d.first===q) hits.push([d,t("prize_first"),q]);
        d.near.forEach(n=>{if(n===q)hits.push([d,t("prize_near"),n]);});
        [["second","prize_second"],["third","prize_third"],["fourth","prize_fourth"],["fifth","prize_fifth"]]
          .forEach(([k,lbl])=>d[k].forEach(n=>{if(n===q)hits.push([d,t(lbl),n]);}));
        d.front3.forEach(n=>{if(n===f3)hits.push([d,t("prize_front3"),n]);});
        d.last3.forEach(n=>{if(n===l3)hits.push([d,t("prize_last3"),n]);});
        if(d.last2===l2) hits.push([d,t("prize_last2"),d.last2]);
      }
    });
    $("#out").innerHTML = hits.length ? `
      <div class="spacer"></div>
      <p class="muted"><b class="gold mono">${hits.length}</b> ${t("appearances")} · ${t("matches_for")} <b class="mono">${q}</b></p>
      <div class="spacer"></div>
      <div class="card" style="padding:0">${hits.map(([d,lbl,n])=>`
        <a class="result-line" href="/results/${d.date}">
          <span><b class="mono gold">${n}</b> &nbsp;<span class="badge b-gold">${lbl}</span></span>
          <span class="muted">${fmtDate(d.date)} →</span></a>`).join("")}</div>`
      : `<div class="empty">${t("no_matches")} <b class="mono gold">${q}</b>.</div>`;
  };
  $("#go").onclick=run;
  $("#q").addEventListener("keyup",e=>{if(e.key==="Enter")run();});
  // deep-link ?q
  const pre=new URLSearchParams(location.search).get("q");
  if(pre){ $("#q").value=pre; run(); }
}

/* ---------------- did I win ---------------- */
/* shared matching engine: returns [ [draw, tierLabel, badgeClass], ... ] for one 6-digit ticket */
function scanTicket(q){
  const f3=q.slice(0,3), l3=q.slice(-3), l2=q.slice(-2);
  const hits=[];
  S.draws.forEach(d=>{
    if(d.first===q) hits.push([d,t("prize_first"),"b-gold"]);
    d.near.forEach(n=>{if(n===q)hits.push([d,t("prize_near"),"b-gold"]);});
    [["second","prize_second"],["third","prize_third"],["fourth","prize_fourth"],["fifth","prize_fifth"]]
      .forEach(([k,lbl])=>{ if(d[k].includes(q)) hits.push([d,t(lbl),"b-jade"]); });
    if(d.front3.includes(f3)) hits.push([d,t("prize_front3"),"b-muted"]);
    if(d.last3.includes(l3)) hits.push([d,t("prize_last3"),"b-muted"]);
    if(d.last2===l2) hits.push([d,t("prize_last2"),"b-muted"]);
  });
  return hits;
}

function hitLines(hits){
  return `<div class="card" style="padding:0">${hits.map(([d,lbl,cls])=>`
    <a class="result-line" href="/results/${d.date}">
      <span class="badge ${cls}">${lbl}</span>
      <span class="muted">${fmtDate(d.date)} →</span></a>`).join("")}</div>`;
}

function checker(){
  const BULK_MAX = 25;
  $("#view").innerHTML = `<section class="section wrap">
    <span class="eyebrow">${t("nav_check")}</span><h1>${t("check_title")}</h1>
    <p class="lead">${t("check_sub")}</p><div class="spacer"></div>
    <div class="toolbar">
      <div class="field" style="flex:1;min-width:240px"><input id="tk" type="text" inputmode="numeric"
        placeholder="${t("check_ph")}" maxlength="6"></div>
      <button class="btn btn-gold" id="go">${t("check_btn")}</button>
    </div>
    <div id="out"></div>

    <div class="spacer-lg"></div>
    <span class="eyebrow">${t("bulk_title")}</span><h2>${t("bulk_title")}</h2>
    <p class="lead">${t("bulk_sub")}</p><div class="spacer"></div>
    <div class="field"><textarea id="bulk" rows="6" inputmode="numeric" spellcheck="false"
      style="font-family:var(--mono)" placeholder="${t("bulk_ph")}"></textarea></div>
    <div class="spacer"></div>
    <button class="btn btn-gold" id="goBulk">${t("bulk_btn")}</button>
    <div id="bulkOut"></div>

    <div class="spacer-lg"></div>${disclaimerBox()}</section>`;

  /* single-ticket checker */
  const run = () => {
    const q=($("#tk").value||"").replace(/\D/g,"");
    if(q.length!==6) return;
    const hits=scanTicket(q);
    $("#out").innerHTML = hits.length ? `
      <div class="spacer"></div>
      <p><span class="badge b-red">★ ${t("check_win")}</span> &nbsp;<b class="mono">${q}</b> · ${hits.length} ${t("appearances")}</p>
      <div class="spacer"></div>
      ${hitLines(hits)}`
      : `<div class="empty">${t("check_none")} <b class="mono gold">${q}</b>.</div>`;
  };
  $("#go").onclick=run;
  $("#tk").addEventListener("keyup",e=>{if(e.key==="Enter")run();});

  /* bulk checker — accepts only digits, spaces, commas and new lines */
  const bulkEl=$("#bulk");
  const clean=s=>s.replace(/[^\d ,\n]/g,"");
  bulkEl.addEventListener("input",()=>{
    const c=clean(bulkEl.value);
    if(c!==bulkEl.value){
      const p=Math.max(0,bulkEl.selectionStart-1);
      bulkEl.value=c;
      bulkEl.setSelectionRange(p,p);
    }
  });
  const runBulk = () => {
    const tokens=clean(bulkEl.value).split(/[\s,]+/).filter(Boolean);
    const seen=new Set(), uniq=[];
    tokens.forEach(tok=>{ if(/^\d{6}$/.test(tok) && !seen.has(tok)){ seen.add(tok); uniq.push(tok); } });
    const capped=uniq.slice(0,BULK_MAX);
    if(!capped.length){
      $("#bulkOut").innerHTML=`<div class="spacer"></div><div class="empty">${t("bulk_invalid")}</div>`;
      return;
    }
    let winners=0;
    const items=capped.map(q=>{
      const hits=scanTicket(q);
      if(hits.length) winners++;
      const head = hits.length
        ? `<p><span class="badge b-red">★ ${t("bulk_win")}</span> &nbsp;<b class="mono">${q}</b> · ${hits.length} ${t("appearances")}</p>`
        : `<p><b class="mono muted">${q}</b></p>`;
      const body = hits.length
        ? `<div class="spacer"></div>${hitLines(hits)}`
        : `<div class="empty" style="padding:16px">${t("bulk_none")}</div>`;
      return `<div>${head}${body}</div>`;
    }).join(`<div class="spacer-lg"></div>`);
    const note = uniq.length>BULK_MAX
      ? `<p class="muted" style="font-size:.85rem;margin-top:6px">${t("bulk_limit")}</p>` : ``;
    $("#bulkOut").innerHTML=`
      <div class="spacer"></div>
      <p><b>${capped.length}</b> ${t("bulk_checked")} · <b class="gold">${winners}</b> ${t("bulk_with_matches")}</p>
      ${note}<div class="spacer-lg"></div>${items}`;
  };
  $("#goBulk").onclick=runBulk;
}

/* ---------------- static pages ---------------- */
function about(){
  const th = S.lang==="th";
  $("#view").innerHTML = `<section class="section wrap prose">
    <span class="eyebrow">${t("nav_about")}</span><h1>${t("about_title")}</h1>
    <p>${th
      ? "Thai Lottery Numbers คือคลังข้อมูลอิสระที่รวบรวมผลออกรางวัลสลากกินแบ่งรัฐบาล (GLO) ย้อนหลังประมาณ 20 ปี ตั้งแต่ปี 2549 ถึงปัจจุบัน เราเปลี่ยนผลรางวัลที่กระจัดกระจายให้กลายเป็นเครื่องมือค้นหา สถิติ และตัวตรวจผลที่ใช้งานได้รวดเร็วและฟรีทั้งหมด"
      : "Thai Lottery Numbers is an independent reference archive of official Government Lottery Office (GLO) results, covering roughly 20 years of draws from 2006 to the present. We turn scattered draw records into fast, free tools: a number search, frequency statistics, and a ticket checker."}</p>

    <h3>${th?"ใครเป็นผู้ดูแลเว็บไซต์นี้":"Who runs this site"}</h3>
    <p>${th
      ? "เว็บไซต์นี้สร้างและดูแลโดย Genext Information Systems ซึ่งเป็นผู้พัฒนาเครื่องมืออ้างอิงและยูทิลิตี้ออนไลน์ที่ตั้งอยู่ในประเทศไทย ทีมงานมีพื้นฐานด้านไอทีและการจัดการข้อมูล โครงการนี้เริ่มต้นจากความต้องการส่วนตัวในการค้นหาผลรางวัลย้อนหลังที่เชื่อถือได้และค้นหาง่าย ซึ่งหาได้ยากในที่เดียว"
      : "This site is built and maintained by Genext Information Systems, an independent developer of online reference and utility tools based in Thailand. Our background is in IT and data handling. The project began from a practical need: a single, reliable, easy-to-search archive of historical Thai lottery results, which was surprisingly hard to find in one place."}</p>

    <h3>${th?"แหล่งข้อมูลและวิธีการรวบรวม":"Data sources & methodology"}</h3>
    <p>${t("data_note")} ${th
      ? "ข้อมูลครอบคลุมรางวัลที่ 1, เลขข้างเคียง, รางวัลที่ 2–5, เลขหน้า 3 ตัว, เลขท้าย 3 ตัว และเลขท้าย 2 ตัว หมายเหตุ: รางวัลเลขหน้า 3 ตัวเริ่มมีตั้งแต่วันที่ 1 กันยายน 2558 เป็นต้นไป ผลแต่ละงวดจะถูกตรวจสอบกับประกาศทางการก่อนเผยแพร่ และมีการแก้ไขทันทีหากพบความคลาดเคลื่อน"
      : "The dataset covers the first prize, adjacent numbers, second through fifth prizes, front-3, last-3, and last-2 digits. Note: the front-3 prize only exists from 1 September 2015 onward. Each draw is checked against the official announcement before publication, and corrections are made promptly if a discrepancy is found."}
      ${th
      ? "โปรดตรวจสอบผลทางการได้ที่ "
      : "Always verify official results at the "}<a class="gold" href="https://www.glo.or.th" target="_blank" rel="noopener nofollow">${th?"สำนักงานสลากกินแบ่งรัฐบาล (glo.or.th)":"Government Lottery Office (glo.or.th)"}</a>.</p>

    <h3>${th?"ความเป็นอิสระและความน่าเชื่อถือ":"Independence & trust"}</h3>
    <p>${th
      ? "เราไม่มีส่วนเกี่ยวข้องกับสำนักงานสลากกินแบ่งรัฐบาลหรือหน่วยงานรัฐใด ๆ เราไม่ขายสลาก ไม่รับพนัน และไม่มีลิงก์ไปยังการซื้อสลากหรือการเดิมพันใด ๆ เว็บไซต์นี้ให้บริการข้อมูลเพื่อการอ้างอิงเท่านั้น"
      : "We are not affiliated with the Government Lottery Office or any government body. We do not sell lottery tickets, take wagers, or link to ticket purchase or betting of any kind. This site is purely an informational reference."}</p>

    <h3>${th?"ความถี่ ≠ การทำนาย":"Frequency ≠ prediction"}</h3>
    <p>${t("every_draw")} ${th
      ? "สถิติที่แสดงมีไว้เพื่อความสนใจและความบันเทิงเท่านั้น ไม่ใช่คำแนะนำในการเล่นหรือการทำนายผลในอนาคต"
      : "The statistics shown are for interest and entertainment only — they are not playing advice or a prediction of future outcomes."}</p>

    <p class="muted">${th?"มีคำถามหรือพบข้อผิดพลาด? ":"Questions or spotted an error? "}<a class="gold" href="/contact.html">${t("nav_contact")}</a>.</p>
    <div class="spacer"></div>${disclaimerBox()}</section>`;
}

/* ---------- Contact ---------- */
function contact(){
  const th = S.lang==="th";
  const email = "hello@thailotterynumbers.com";
  $("#view").innerHTML = `<section class="section wrap prose">
    <span class="eyebrow">${t("nav_contact")}</span><h1>${t("contact_title")}</h1>
    <p class="lead">${th
      ? "ยินดีรับฟังทุกความคิดเห็น เราอ่านทุกข้อความและพยายามตอบกลับภายใน 2–3 วันทำการ"
      : "We would love to hear from you. We read every message and aim to reply within 2–3 business days."}</p>

    <h3>${th?"อีเมล":"Email us"}</h3>
    <p>${th
      ? "วิธีที่เร็วที่สุดในการติดต่อเราคือทางอีเมล: "
      : "The fastest way to reach us is by email: "}<a class="gold" href="mailto:${email}">${email}</a></p>

    <h3>${th?"เรื่องที่ติดต่อได้":"What you can write about"}</h3>
    <ul>
      <li>${th?"แจ้งแก้ไขผลรางวัลหรือข้อมูลที่คลาดเคลื่อน — โปรดระบุวันที่งวดและรายละเอียด":"Corrections to a result or data error — please include the draw date and details."}</li>
      <li>${th?"ข้อเสนอแนะเกี่ยวกับฟีเจอร์หรือเครื่องมือใหม่":"Suggestions for features or new tools."}</li>
      <li>${th?"คำถามเกี่ยวกับวิธีการรวบรวมข้อมูลหรือนโยบายความเป็นส่วนตัวของเรา":"Questions about our methodology or privacy practices."}</li>
      <li>${th?"การสอบถามด้านสื่อหรือความร่วมมือ":"Media or partnership enquiries."}</li>
    </ul>
    <p class="muted">${th
      ? "หากต้องการแจ้งแก้ไขข้อมูล โปรดแนบวันที่งวดและหมายเลขที่เกี่ยวข้อง เพื่อให้เราตรวจสอบกับประกาศทางการได้รวดเร็วขึ้น"
      : "For a correction, including the draw date and the numbers involved helps us verify against the official announcement faster."}</p>

    <h3>${th?"ผู้ดูแลเว็บไซต์":"Site operator"}</h3>
    <p>Genext Information Systems${th?" — ผู้พัฒนาเครื่องมืออ้างอิงออนไลน์ ประเทศไทย":" — independent online reference tools, Thailand."}</p>
    <p class="muted">${th
      ? "โปรดทราบ: เราไม่สามารถจ่ายรางวัล ยืนยันการถูกรางวัลอย่างเป็นทางการ หรือขายสลากได้ การถูกรางวัลทุกครั้งต้องตรวจสอบและขึ้นเงินกับ "
      : "Please note: we cannot pay prizes, officially confirm a win, or sell tickets. All wins must be verified and claimed through the "}<a class="gold" href="https://www.glo.or.th" target="_blank" rel="noopener nofollow">${th?"สำนักงานสลากกินแบ่งรัฐบาล":"Government Lottery Office"}</a>.</p>
    <div class="spacer"></div>${disclaimerBox()}</section>`;
}

/* ---------- FAQ ---------- */
function faq(){
  const qa = [1,2,3,4,5,6].map(i=>[t("faq_q"+i), t("faq_a"+i)]);
  $("#view").innerHTML = `<section class="section wrap prose">
    <span class="eyebrow">${t("nav_faq")}</span><h1>${t("faq_title")}</h1>
    <p class="lead">${t("faq_sub")}</p>
    <div class="spacer"></div>
    <div class="faq-list">
      ${qa.map(([q,a])=>`<details class="faq-item">
        <summary>${q}</summary><div class="faq-a">${a}</div></details>`).join("")}
    </div>
    <div class="spacer"></div>
    <p class="muted">${t("faq_more")}: <a class="gold" href="/search">${t("nav_search")}</a> ·
      <a class="gold" href="/check">${t("nav_check")}</a> ·
      <a class="gold" href="/stats">${t("nav_stats")}</a> ·
      <a class="gold" href="/results">${t("nav_results")}</a></p>
  </section>`;
}

/* ---------- Responsible Play ---------- */
function responsiblePlay(){
  const th = S.lang==="th";
  $("#view").innerHTML = `<section class="section wrap prose">
    <span class="eyebrow">${t("legal_responsible")}</span>
    <h1>${th?"เล่นอย่างมีสติ":"Responsible Play"}</h1>
    <p class="lead">${th
      ? "ThaiLotteryNumbers.com เป็นแหล่งข้อมูลและการศึกษา เราเผยแพร่ผลรางวัล สถิติ และบันทึกย้อนหลังของสำนักงานสลากกินแบ่งรัฐบาล (GLO) เพื่อให้ประชาชนค้นหาและทำความเข้าใจงวดที่ออกไปแล้ว เราไม่ใช่ผู้ให้บริการการพนัน ไม่ขายสลาก และไม่มีสิ่งใดในเว็บไซต์นี้ที่เป็นการทำนายหรือการแนะนำให้เล่น"
      : "ThaiLotteryNumbers.com is an informational and educational resource. We publish official Government Lottery Office (GLO) results, historical records, and statistics so the public can look up and understand draws that have already happened. We are not a gambling operator, we do not sell tickets, and nothing on this site is a prediction or a recommendation to play."}</p>

    <h3>${th?"สลากคือความบันเทิง ไม่ใช่การลงทุน":"The lottery is entertainment, not an investment"}</h3>
    <p>${th
      ? "สลากกินแบ่งรัฐบาลเป็นเกมเสี่ยงโชค ทุกงวดเป็นอิสระและสุ่ม ไม่มีรูปแบบ เลข ‘ร้อน’ หรือความถี่ในอดีตใดที่เปลี่ยนโอกาสของเลขที่จะออกงวดถัดไป ผู้ใดก็ตามที่อ้างว่าทำนายเลขที่จะถูกได้นั้นเข้าใจผิดหรือกำลังหลอกลวงคุณ จงถือว่าเงินที่ใช้ซื้อสลากเป็นค่าความบันเทิง ไม่ใช่หนทางหาเงินหรือแก้ปัญหาการเงิน"
      : "The Thai Government Lottery is a game of chance. Every draw is independent and random. No pattern, \u201chot\u201d number, or historical frequency changes the odds of any number being drawn next \u2014 and anyone claiming to predict winning numbers is mistaken or misleading you. Treat any money spent on tickets as the cost of entertainment, never as a way to make money or solve financial problems."}</p>

    <h3>${th?"เล่นเท่าที่ไหว":"Play within your means"}</h3>
    <ul>
      <li>${th?"ใช้เฉพาะเงินที่คุณยอมเสียได้โดยไม่เดือดร้อน":"Only ever spend money you can comfortably afford to lose."}</li>
      <li>${th?"ตั้งวงเงินส่วนตัวก่อนซื้อ และอย่าไล่ตามเงินที่เสียไป":"Set a personal limit before you buy, and never chase losses."}</li>
      <li>${th?"การซื้อสลากต้องไม่มาก่อนค่าใช้จ่ายจำเป็น เงินออม หรือความต้องการของครอบครัว":"Lottery spending should never come before essentials, savings, or family needs."}</li>
      <li>${th?"การซื้อสลากมากขึ้นไม่ได้เพิ่มโอกาสถูกรางวัลที่ 1 อย่างมีนัยสำคัญ":"Buying more tickets does not meaningfully improve your odds of the top prize."}</li>
    </ul>

    <h3>${th?"เข้าใจความน่าจะเป็น":"Understanding the odds"}</h3>
    <p>${th
      ? "การถูกครบทั้งหกหลักเพื่อรับรางวัลที่ 1 นั้นมีโอกาสน้อยมากสำหรับสลากใบเดียว เราอธิบายความน่าจะเป็นจริงด้วยภาษาที่เข้าใจง่ายในคู่มือของเรา เพื่อให้คุณตัดสินใจได้อย่างมีข้อมูลและสมจริง การเข้าใจความน่าจะเป็นคือเกราะป้องกันที่ดีที่สุดจากความคาดหวังเกินจริง"
      : "Matching all six digits for the first prize is extremely unlikely on any single ticket. We explain the real probabilities in plain language in our guides so you can make informed, realistic decisions. Understanding the odds is the single best protection against unrealistic expectations."}</p>

    <h3>${th?"ดูแลตัวเองและคนรอบข้าง":"Protecting yourself and others"}</h3>
    <p>${th
      ? "การเล่นควรเป็นเรื่องสนุก หากมันเลิกสนุก — หากคุณรู้สึกว่าหยุดไม่ได้ ใช้เงินมากกว่าที่ตั้งใจ ปิดบัง หรือกู้ยืมมาเล่น — นั่นคือสัญญาณให้ขอความช่วยเหลือ ความรู้สึกเหล่านี้พบได้บ่อยและมีคนพร้อมช่วยเสมอ"
      : "Gambling should stay fun. If it stops being fun \u2014 if you feel you can\u2019t stop, if you\u2019re spending more than you intended, hiding it, or borrowing to play \u2014 that is a sign to seek support. These feelings are common and help is available."}</p>

    <h3>${th?"ขอความช่วยเหลือได้ที่ไหน (ประเทศไทย)":"Where to get help (Thailand)"}</h3>
    <p>${th
      ? "หากคุณหรือคนที่คุณรู้จักอาจมีปัญหาการพนัน สามารถปรึกษาผู้เชี่ยวชาญได้อย่างเป็นความลับ สายด่วนสุขภาพจิต กรมสุขภาพจิต โทร "
      : "If you or someone you know may have a gambling problem, you can talk to a professional in confidence. In Thailand, the Department of Mental Health hotline "}<b>1323</b>${th
      ? " ให้บริการฟรีตลอด 24 ชั่วโมง แพทย์หรือโรงพยาบาลใกล้บ้านสามารถส่งต่อไปยังบริการให้คำปรึกษาได้เช่นกัน"
      : " offers free, 24-hour mental-health support. Your doctor or a local hospital can also refer you to counselling services."}</p>
    <p class="muted">${th
      ? "(หากคุณอยู่นอกประเทศไทย โปรดติดต่อบริการช่วยเหลือผู้มีปัญหาการพนันในประเทศของคุณ)"
      : "(If you are outside Thailand, please seek a local problem-gambling support service in your country.)"}</p>

    <h3>${th?"ผู้เยาว์":"Minors"}</h3>
    <p>${th
      ? "สลากกินแบ่งมีไว้สำหรับผู้ใหญ่เท่านั้น เว็บไซต์นี้ไม่ได้มีไว้สำหรับผู้ที่มีอายุต่ำกว่า 18 ปี"
      : "The lottery is for adults only. This site is not intended for anyone under 18."}</p>

    <p class="muted">${th
      ? "เพื่อความบันเทิงและให้ข้อมูลเท่านั้น ไม่มีส่วนเกี่ยวข้องกับสำนักงานสลากกินแบ่งรัฐบาล โปรดตรวจสอบผลกับแหล่งข้อมูลทางการเสมอ อ่านเพิ่มเติมเกี่ยวกับ"
      : "For entertainment and informational purposes only. Not affiliated with the Government Lottery Office. Always verify results with official sources. Read more about "}<a class="gold" href="/stats">${t("nav_stats")}</a> ${th?"และ":"and "}<a class="gold" href="/faq">${t("nav_faq")}</a>.</p>
    <div class="spacer"></div>${disclaimerBox()}</section>`;
}

/* ---------- legal ---------- */
function prose(eyebrow, title, body){
  $("#view").innerHTML = `<section class="section wrap prose">
    <span class="eyebrow">${eyebrow}</span><h1>${title}</h1>
    <p class="upd">${S.lang==="th"?"ปรับปรุงล่าสุด":"Last updated"}: 1 ${S.lang==="th"?"มิถุนายน 2569":"June 2026"}</p>
    ${body}<div class="spacer-lg"></div>${disclaimerBox()}</section>`;
}
function legalPrivacy(){
  prose(t("ft_legal"), t("legal_privacy"), `
    <p>Genext Information Systems ("we", "us") operates ThaiLotteryNumbers.com. This policy explains what limited information we handle when you visit, and how our advertising partner uses cookies.</p>
    <h3>Information we collect directly</h3>
    <p>We do not require accounts and we do not sell personal data. We store two preferences locally in your browser: your chosen language and your cookie-consent choice. These never leave your device.</p>
    <p>If you contact us by email, we receive the information you choose to send (such as your name, email address, and message) solely to respond to you.</p>
    <h3>Advertising &amp; cookies</h3>
    <p>This site is supported by advertising served through Google AdSense. Third-party vendors, including Google, use cookies to serve ads based on your prior visits to this and other websites.</p>
    <ul>
      <li>Google's use of advertising cookies enables it and its partners to serve ads to you based on your visit to this site and/or other sites on the internet.</li>
      <li>You may opt out of personalised advertising by visiting <a href="https://www.google.com/settings/ads" target="_blank" rel="noopener">Google Ads Settings</a>. You can also opt out of a third party vendor's use of cookies for personalised advertising by visiting <a href="https://www.aboutads.info/choices/" target="_blank" rel="noopener">www.aboutads.info</a>.</li>
      <li>Where required by law, ads are shown to you in a non-personalised form unless you provide consent.</li>
    </ul>
    <p>For more detail on how Google uses data when you use our partners' sites or apps, see <a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener">policies.google.com/technologies/partner-sites</a>.</p>
    <h3>Analytics</h3>
    <p>Any aggregate, anonymised traffic measurement we use cannot identify you individually.</p>
    <h3>Your choices &amp; rights</h3>
    <p>You may clear locally stored preferences and cookies at any time through your browser settings or our <a href="/cookie-settings">${t("legal_cookie_set")}</a> page. You may request deletion of any email correspondence by writing to us.</p>
    <h3>Contact</h3>
    <p>Questions about this policy: <a href="mailto:hello@thailotterynumbers.com">hello@thailotterynumbers.com</a>, or via our <a href="/contact.html">${t("nav_contact")}</a> page.</p>`);
}
function legalCookies(){
  prose(t("ft_legal"), t("legal_cookie"), `
    <p>Cookies and similar local-storage technologies are small pieces of data saved by your browser. We keep our own use minimal, but our advertising partner sets additional cookies as described below.</p>
    <h3>Essential cookies we set</h3>
    <ul>
      <li><b>Language preference.</b> Remembers whether you chose English or Thai.</li>
      <li><b>Consent state.</b> Remembers that you dismissed the cookie notice so it doesn't reappear.</li>
    </ul>
    <h3>Advertising cookies (third party)</h3>
    <p>This site uses Google AdSense. Google and its partners set cookies to deliver and measure ads, and to serve personalised ads based on your visits to this and other sites. You can review or disable these via <a href="https://www.google.com/settings/ads" target="_blank" rel="noopener">Google Ads Settings</a> and <a href="https://www.aboutads.info/choices/" target="_blank" rel="noopener">www.aboutads.info</a>. See our <a href="/privacy">${t("legal_privacy")}</a> for full detail.</p>
    <h3>Managing cookies</h3>
    <p>Use our <a href="/cookie-settings">${t("legal_cookie_set")}</a> page or your browser controls to review or clear stored values. Clearing essential cookies simply resets the site to its defaults; clearing advertising cookies may make the ads you see less relevant.</p>`);
}
function legalTerms(){
  prose(t("ft_legal"), t("legal_terms"), `
    <h3>Acceptance</h3>
    <p>By using ThaiLotteryNumbers.com you agree to these terms. If you do not agree, please do not use the site.</p>
    <h3>Entertainment & information only</h3>
    <p>${t("disclaimer")}</p>
    <h3>No guarantee of accuracy</h3>
    <p>Results are compiled from public records and provided "as is" without warranty of any kind. ${t("every_draw")} Nothing here is gambling advice or a prediction of future outcomes.</p>
    <h3>Responsible play</h3>
    <p>This site is for entertainment and information only and is intended for adults (18+). Nothing here is gambling advice, a betting strategy, or a prediction of future results. The lottery is a game of chance; past results never influence future draws. If gambling stops being enjoyable, please see our <a href="/responsible-play">${t("legal_responsible")}</a> page for guidance and support resources.</p>
    <h3>No facilitation of gambling</h3>
    <p>We do not sell lottery tickets, accept payments or wagers, or link to any service that does. Links to the Government Lottery Office are provided solely so you can verify official results.</p>
    <h3>Accuracy and official results</h3>
    <p>We compile results from official GLO announcements and reliable public records and correct errors promptly, but we provide all data "as is" without warranty. Before claiming any prize, you must verify your numbers against the official Government Lottery Office results. We cannot confirm wins or pay prizes.</p>
    <h3>Limitation of liability</h3>
    <p>To the maximum extent permitted by law, Genext Information Systems is not liable for any loss arising from reliance on information presented here. Always verify numbers with the official Government Lottery Office before acting on them.</p>
    <h3>Intellectual property</h3>
    <p>The site design, text, and compiled presentation are © 2026 Genext Information Systems. Underlying draw results are factual public records.</p>
    <h3>Changes</h3>
    <p>We may update these terms; continued use after changes constitutes acceptance.</p>`);
}
function cookieSettings(){
  const lang=localStorage.getItem("tln_lang")||"en", ck=localStorage.getItem("tln_cookie")==="1";
  prose(t("ft_legal"), t("legal_cookie_set"), `
    <p>${t("cookie_text")}</p>
    <div class="card" style="margin-top:16px">
      <p><b>${S.lang==="th"?"ภาษา":"Language preference"}:</b> <span class="gold mono">${lang}</span></p>
      <p style="margin-top:8px"><b>${S.lang==="th"?"สถานะการยินยอม":"Consent state"}:</b> <span class="gold mono">${ck?"accepted":"not set"}</span></p>
      <div class="spacer"></div>
      <button class="btn btn-ghost" id="clear">${S.lang==="th"?"ล้างค่าที่บันทึกไว้":"Clear stored preferences"}</button>
    </div>`);
  $("#clear").onclick=()=>{ localStorage.removeItem("tln_cookie"); toast(t("copied").replace(/.*/,S.lang==="th"?"ล้างแล้ว":"Cleared")); setTimeout(()=>location.reload(),600); };
}
function legalAccess(){
  prose(t("ft_legal"), t("legal_access"), `
    <p>We want ThaiLotteryNumbers.com to be usable by everyone, and we aim to meet WCAG 2.1 AA guidance.</p>
    <h3>What we do</h3>
    <ul>
      <li>High-contrast white text on a dark background, tested for readability.</li>
      <li>Full keyboard navigation with visible focus outlines.</li>
      <li>Respect for the "reduce motion" system setting — animations are disabled when requested.</li>
      <li>Semantic structure and descriptive labels for assistive technology.</li>
      <li>Responsive layouts from mobile to desktop.</li>
    </ul>
    <h3>Feedback</h3>
    <p>If you encounter a barrier, please tell us at <a href="mailto:hello@thailotterynumbers.com">hello@thailotterynumbers.com</a> and we will work to fix it.</p>`);
}

function notFound(){
  $("#view").innerHTML = `<section class="section wrap center">
    <h2 style="font-size:3rem">404</h2><p class="muted">${t("not_found")}</p>
    <div class="spacer"></div><a class="btn btn-gold" href="/">${t("go_home")}</a></section>`;
}

/* ---------- CSV export ---------- */
function exportCSV(rows){
  const head=["date","first","front3","last3","last2","near","second","third","fourth","fifth"];
  const lines=[head.join(",")].concat(rows.map(d=>head.map(k=>{
    const v=d[k]; return Array.isArray(v)?`"${v.join(" ")}"`:v;
  }).join(",")));
  const blob=new Blob([lines.join("\n")],{type:"text/csv"});
  const a=document.createElement("a"); a.href=URL.createObjectURL(blob);
  a.download="thai-lottery-results.csv"; a.click(); URL.revokeObjectURL(a.href);
  toast(t("export_csv")+" ✓");
}

/* ============================================================ live auto-update
   On every load, look for draws newer than the bundled data and merge them in.
   Source: public GLO archive (raw GitHub). Fails silently when offline or when
   no newer draw has been published yet, falling back to the bundled data. */
const ARCHIVE = "https://raw.githubusercontent.com/vicha-w/thai-lotto-archive/master/lottonumbers/";

function parseDrawText(text, date){
  const d={date,first:"",near:[],front3:[],last3:[],last2:"",second:[],third:[],fourth:[],fifth:[]};
  text.split(/\r?\n/).forEach(line=>{
    const p=line.trim().split(/\s+/);
    if(!p[0] || !/^[A-Z_]+$/.test(p[0])) return;
    const k=p[0], v=p.slice(1);
    if(k==="FIRST"&&v[0])d.first=v[0];
    else if(k==="THREE_FIRST")d.front3=v;
    else if(k==="THREE_LAST"||k==="THREE")d.last3=v;
    else if(k==="TWO"&&v[0])d.last2=v[0];
    else if(k==="NEAR_FIRST")d.near=v;
    else if(k==="SECOND")d.second=v;
    else if(k==="THIRD")d.third=v;
    else if(k==="FOURTH")d.fourth=v;
    else if(k==="FIFTH")d.fifth=v;
  });
  return d.first?d:null;
}

function computeStats(draws){
  const last2={},front3={},last3={};
  for(let i=0;i<100;i++) last2[String(i).padStart(2,"0")]=0;
  let l3slots=0;
  draws.forEach(d=>{
    if(d.last2)last2[d.last2]=(last2[d.last2]||0)+1;
    d.front3.forEach(n=>front3[n]=(front3[n]||0)+1);
    d.last3.forEach(n=>{last3[n]=(last3[n]||0)+1;l3slots++;});
  });
  const f3dates=draws.filter(d=>d.front3.length).map(d=>d.date).sort();
  const rank=o=>Object.entries(o).sort((a,b)=>b[1]-a[1]||(a[0]<b[0]?-1:1)).map(([n,c])=>({n,c}));
  return {
    totalDraws:draws.length, dateRange:[draws[draws.length-1].date, draws[0].date],
    front3Draws:f3dates.length, front3Since:f3dates[0]||null, last3Slots:l3slots,
    grid:Array.from({length:100},(_,i)=>{const n=String(i).padStart(2,"0");return{n,c:last2[n]};}),
    last2:rank(last2), front3:rank(front3), last3:rank(last3),
  };
}

/* expected draw dates (1st & 16th, 16:00 ICT) after `afterISO`, up to now */
function candidateDates(afterISO){
  const out=[]; let [y,m]=afterISO.split("-").map(Number); const now=Date.now();
  for(let guard=0;guard<240;guard++){
    for(const day of [1,16]){
      const iso=`${y}-${String(m).padStart(2,"0")}-${String(day).padStart(2,"0")}`;
      const ts=Date.UTC(y,m-1,day,9,0,0);
      if(iso>afterISO && ts<=now) out.push(iso);
    }
    if(Date.UTC(y,m-1,1,9,0,0)>now) break;
    m++; if(m>12){m=1;y++;}
  }
  return out;
}

async function autoUpdate(){
  const cands = candidateDates(S.draws[0].date);
  if(!cands.length) return;
  const fresh=[];
  for(const date of cands){
    try{
      const r=await fetch(ARCHIVE+date+".txt",{cache:"no-store"});
      if(!r.ok) continue;
      const dr=parseDrawText(await r.text(), date);
      if(dr) fresh.push(dr);
    }catch(e){ /* offline / not yet published — ignore */ }
  }
  if(!fresh.length) return;
  const seen=new Set(S.draws.map(d=>d.date));
  fresh.forEach(d=>{ if(!seen.has(d.date)){ S.draws.push(d); seen.add(d.date); } });
  S.draws.sort((a,b)=>a.date<b.date?1:-1);
  S.stats=computeStats(S.draws);
  render(true);
  toast(t("updated_toast"));
}

/* ============================================================ boot */
function interceptLinks(){
  document.addEventListener("click", e=>{
    const a = e.target.closest("a");
    if(!a) return;
    const href = a.getAttribute("href");
    if(!href || !href.startsWith("/")) return;          // ignore external / mailto / anchors
    if(href === "/guides" || href.startsWith("/guides/")) return;  // static blog: real navigation
    if(href === "/contact.html") return;  // static contact page: real navigation
    if(a.target==="_blank" || e.metaKey || e.ctrlKey || e.shiftKey) return;
    e.preventDefault();
    if(href !== location.pathname + location.search) navigate(href);
  });
  window.addEventListener("popstate", ()=>render());
}

async function boot(){
  document.documentElement.lang = S.lang;
  try{
    const [draws, stats] = await Promise.all([
      fetch("/assets/data/draws.json").then(r=>r.json()),
      fetch("/assets/data/stats.json").then(r=>r.json()),
    ]);
    S.draws = draws; S.stats = stats;
  }catch(e){
    $("#view").innerHTML = `<section class="section wrap center"><h2>⚠️</h2>
      <p class="muted">Could not load draw data. If you opened this file directly, run a local server
      from the site root (e.g. <code>python -m http.server</code>) — browsers block fetch on file://.</p></section>`;
    return;
  }
  buildShell();
  interceptLinks();
  render();
  autoUpdate();   // pull anything newer than the bundled data, then refresh
}
boot();
})();
