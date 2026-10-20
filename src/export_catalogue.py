"""Writes data/hales_turgus_irasai.csv and .json from src/items.js and src/pl.json."""
import json, csv, pathlib
here = pathlib.Path(__file__).resolve().parent; root = here.parent
src = (here / "items.js").read_text(encoding="utf8").strip()
items = json.loads(src[src.index("["):src.rindex("]") + 1]); pl = json.loads((here / "pl.json").read_text(encoding="utf8"))
base = "https://laikomasinos.lt/hales-turgus/"
rows = [{"id": i["id"], "rusis": i["kind"], "metai": i.get("year") or "", "data": i.get("date", ""), "tipas": i.get("type", ""), "pavadinimas": i["title"], "saugotojas": i.get("holder", ""),
         "kalba": i.get("lang", ""), "licencija": i.get("licence", ""), "aprasymas": i.get("notes", ""), "nuorodos": [{"pavadinimas": l, "url": u} for l, u in i.get("links", [])],
         "vaizdas": base + i["img"] if i.get("img") else "", "pavadinimas_pl": pl.get(i["id"], {}).get("title", ""), "aprasymas_pl": pl.get(i["id"], {}).get("notes", "")} for i in items]
(root / "data" / "hales_turgus_irasai.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1) + "\n", encoding="utf8")
with open(root / "data" / "hales_turgus_irasai.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader()
    for r in rows: w.writerow({**r, "nuorodos": " | ".join(f"{x['pavadinimas']}: {x['url']}" for x in r["nuorodos"])})
print("records", len(rows))
