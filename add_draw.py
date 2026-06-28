#!/usr/bin/env python3
"""
Add a new Thai lottery draw, then rebuild the site's data files.

Two ways to use it:

  1) Guided prompts (easiest):
       python add_draw.py

  2) One-line, scriptable:
       python add_draw.py --date 2026-06-16 \
           --first 123456 \
           --front3 111 222 \
           --last3 333 444 \
           --last2 55 \
           --near 123455 123457

After it writes the draw it automatically runs build_data.py, so the website
picks up the new result the next time someone loads it. Just re-upload the
`assets/data/` folder (or the whole site) to your host.

Optional prize tiers (--second / --third / --fourth / --fifth) accept any number
of 6-digit values and are only needed if you want the "Did I Win?" checker and
search to cover those tiers for the new draw.
"""
import os, sys, argparse, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "data_src")


def write_draw(d):
    path = os.path.join(SRC, f"{d['date']}.txt")
    lines = [f"# added via add_draw.py", f"FIRST {d['first']}"]
    if d.get("front3"): lines.append("THREE_FIRST " + " ".join(d["front3"]))
    if d.get("last3"):  lines.append("THREE_LAST " + " ".join(d["last3"]))
    if d.get("last2"):  lines.append("TWO " + d["last2"])
    if d.get("near"):   lines.append("NEAR_FIRST " + " ".join(d["near"]))
    for tier in ("second", "third", "fourth", "fifth"):
        if d.get(tier): lines.append(tier.upper() + " " + " ".join(d[tier]))
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    return path


def prompt():
    print("Add a new draw — enter values (Enter to skip optional fields).\n")
    d = {}
    d["date"]   = input("Draw date (YYYY-MM-DD): ").strip()
    d["first"]  = input("First prize (6 digits): ").strip()
    d["front3"] = input("Front 3 digits (space-separated, e.g. 111 222): ").split()
    d["last3"]  = input("Last 3 digits  (space-separated, e.g. 333 444): ").split()
    d["last2"]  = input("Last 2 digits  (e.g. 55): ").strip()
    d["near"]   = input("Adjacent-to-first numbers (optional): ").split()
    for tier in ("second", "third", "fourth", "fifth"):
        d[tier] = input(f"{tier.capitalize()} prize numbers (optional): ").split()
    return d


def main():
    p = argparse.ArgumentParser(description="Add a Thai lottery draw and rebuild site data.")
    p.add_argument("--date"); p.add_argument("--first")
    p.add_argument("--front3", nargs="*", default=[])
    p.add_argument("--last3", nargs="*", default=[])
    p.add_argument("--last2")
    p.add_argument("--near", nargs="*", default=[])
    for tier in ("second", "third", "fourth", "fifth"):
        p.add_argument(f"--{tier}", nargs="*", default=[])
    a = p.parse_args()

    d = prompt() if not a.date else {
        "date": a.date, "first": a.first, "front3": a.front3, "last3": a.last3,
        "last2": a.last2, "near": a.near, "second": a.second, "third": a.third,
        "fourth": a.fourth, "fifth": a.fifth,
    }

    if not (d.get("date") and d.get("first")):
        sys.exit("A draw needs at least --date and --first.")
    if len(d["date"]) != 10 or d["date"][4] != "-":
        sys.exit("Date must be YYYY-MM-DD.")

    path = write_draw(d)
    print(f"\n✓ Wrote {path}")

    print("Rebuilding site data…")
    subprocess.run([sys.executable, os.path.join(HERE, "build_data.py")], check=True)
    print("Refreshing SEO pages & sitemap…")
    subprocess.run([sys.executable, os.path.join(HERE, "build_seo.py")], check=True)
    print("\n✓ Done. Re-upload the site (or just assets/data/) to publish the new draw.")


if __name__ == "__main__":
    main()
