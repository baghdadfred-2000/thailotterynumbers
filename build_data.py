"""Parse the GLO archive (.txt per draw) into site data: draws.json + stats.json."""
import os, glob, json
from collections import Counter
from datetime import date, timedelta

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data_src")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "data")
os.makedirs(OUT, exist_ok=True)

def parse(path):
    d = {"date": os.path.basename(path)[:-4], "first": "", "near": [],
         "front3": [], "last3": [], "last2": "",
         "second": [], "third": [], "fourth": [], "fifth": []}
    with open(path, encoding="utf-8") as f:
        for line in f:
            p = line.split()
            if not p or not p[0].isupper():
                continue
            k, v = p[0], p[1:]
            if k == "FIRST" and v: d["first"] = v[0]
            elif k == "THREE_FIRST": d["front3"] = v
            elif k == "THREE_LAST": d["last3"] = v
            elif k == "THREE": d["last3"] = v  # legacy: 4 last-3 winners
            elif k == "TWO" and v: d["last2"] = v[0]
            elif k == "NEAR_FIRST": d["near"] = v
            elif k == "SECOND": d["second"] = v
            elif k == "THIRD": d["third"] = v
            elif k == "FOURTH": d["fourth"] = v
            elif k == "FIFTH": d["fifth"] = v
    return d

draws = [parse(p) for p in sorted(glob.glob(os.path.join(SRC, "*.txt")))]
draws = [d for d in draws if d["first"]]
draws.sort(key=lambda x: x["date"], reverse=True)

# ---- frequency stats
def freq(items):
    c = Counter(items)
    return c

last2 = freq(d["last2"] for d in draws if d["last2"])
front3_draws = [d for d in draws if d["front3"]]
front3 = freq(n for d in front3_draws for n in d["front3"])
last3 = freq(n for d in draws for n in d["last3"])

def grid100():
    return [{"n": f"{i:02d}", "c": last2.get(f"{i:02d}", 0)} for i in range(100)]

def ranked(counter):
    return [{"n": n, "c": c} for n, c in
            sorted(counter.items(), key=lambda kv: (-kv[1], kv[0]))]

# trend: per-year count for a given 2-digit number handled client-side; ship year tags
stats = {
    "generated": date.today().isoformat(),
    "totalDraws": len(draws),
    "dateRange": [draws[-1]["date"], draws[0]["date"]],
    "front3Draws": len(front3_draws),
    "front3Since": min(d["date"] for d in front3_draws) if front3_draws else None,
    "last3Slots": sum(len(d["last3"]) for d in draws),
    "grid": grid100(),
    "last2": ranked(last2),
    "front3": ranked(front3),
    "last3": ranked(last3),
}

with open(os.path.join(OUT, "draws.json"), "w") as f:
    json.dump(draws, f, separators=(",", ":"))
with open(os.path.join(OUT, "stats.json"), "w") as f:
    json.dump(stats, f, separators=(",", ":"))

print("draws:", len(draws), "| range:", stats["dateRange"])
print("front3 since", stats["front3Since"], "(", len(front3_draws), "draws )")
print("hot last2:", stats["last2"][:3])
print("hot front3:", stats["front3"][:3])
print("hot last3:", stats["last3"][:3])
sz = lambda n: os.path.getsize(os.path.join(OUT, n))
print("draws.json", round(sz("draws.json")/1024), "KB | stats.json", round(sz("stats.json")/1024), "KB")
