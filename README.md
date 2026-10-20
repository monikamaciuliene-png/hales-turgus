# Halės turgaus laiko mašina

Vilniaus Halės turgaus istorija nuo 1808 m. iki šių dienų: archyvų nuotraukos, spauda, tyrimai, balsai ir renginiai, lietuvių ir lenkų kalbomis. Dalis [laikomasinos.lt](https://laikomasinos.lt).

- Puslapis: `index.html` (sukuriamas iš `page.html` su `python3 build.py`)
- Šaltinis: `src/` (`template.html`, `items.js`, `datasets.js`, `climate.json`, `pl.json`); `python3 src/build_page.py` sukuria `page.html`
- Atviri duomenys: `data/` (įrašų katalogas CSV ir JSON, klimatas ERA5)
- Vaizdai: `img/`, kiekvieno licencija nurodyta prie įrašo
