# ==========================================
# 1. feladat: Adatok beolvasása és tárolása
# ==========================================
# Figyelem: a feladat említi, hogy az adatok TABULÁTORRAL (\t) vannak elválasztva!
file = open("2024-oktober-autok-mozgasa-forras.txt", "r", encoding="utf-8").read().splitlines()

jeladasok = []
for sor in file:
    reszek = sor.split("\t")  # Tabulátor mentén darabolunk
    jel = {}
    jel["rendszam"] = reszek[0]
    jel["ora"] = int(reszek[1])
    jel["perc"] = int(reszek[2])
    jel["sebesseg"] = int(reszek[3])
    jeladasok.append(jel)

# ==========================================
# 2. feladat: Legutolsó jeladás
# ==========================================
print("2. feladat:")
# Mivel az adatok időrendben vannak, a lista utolsó elema [-1] a legutolsó jeladás
utolso = jeladasok[-1]
print(f"Az utolsó jeladás időpontja {utolso['ora']}:{utolso['perc']}, a jármű rendszáma {utolso['rendszam']}")

# ==========================================
# 3. feladat: Az legelső jármű adatai
# ==========================================
print("\n3. feladat:")
elso_rendszam = jeladasok[0]["rendszam"]
print(f"Az első jármű: {elso_rendszam}")

# Összegyűjtjük az első jármű időpontjait óra:perc formában
idopontok = []
for jel in jeladasok:
    if jel["rendszam"] == elso_rendszam:
        idopontok.append(f"{jel['ora']}:{jel['perc']}")

print("Jeladásainak időpontjai:", " ".join(idopontok))

# ==========================================
# 4. feladat: Jeladások száma adott időpontban
# ==========================================
print("\n4. feladat:")
bekert_ora = int(input("Kérem, adja meg az órát: "))
bekert_perc = int(input("Kérem, adja meg a percet: "))

db = 0
for jel in jeladasok:
    if jel["ora"] == bekert_ora and jel["perc"] == bekert_perc:
        db += 1

print(f"A jeladások száma: {db}")

# ==========================================
# 5. feladat: Legnagyobb sebesség és a járművek
# ==========================================
print("\n5. feladat:")
# Maximumkeresés
max_seb = 0
for jel in jeladasok:
    if jel["sebesseg"] > max_seb:
        max_seb = jel["sebesseg"]

# Összegyűjtjük azokat a rendszámokat, akik elértek ezt a sebességet
gyorsak = []
for jel in jeladasok:
    if jel["sebesseg"] == max_seb:
        gyorsak.append(jel["rendszam"])

print(f"A legnagyobb sebesség km/h: {max_seb}")
print("A járművek:", " ".join(gyorsak))

# ==========================================
# 6. feladat: Távolság kiszámítása (Szomszédos elemek logikája!)
# ==========================================
print("\n6. feladat:")
bekert_rendszam = input("Kérem, adja meg a rendszámot: ")

# Kiszűrjük egy külön listába csak a keresett autó jeladásait
auto_jelei = []
for jel in jeladasok:
    if jel["rendszam"] == bekert_rendszam:
        auto_jelei.append(jel)

if len(auto_jelei) == 0:
    print("Nem szerepel a bekért rendszámmal jármű.")
else:
    tavolsag = 0.0
    # Az első jeladáskor a távolság fixen 0.0 km (ezt még a ciklus előtt kiírjuk)
    print(f"{auto_jelei[0]['ora']}:{auto_jelei[0]['perc']} {tavolsag:.1f} km")

    # Itt jön az i és i+1 szomszédos elem logika!
    # range(0, len-1) -> Az első elemtől az utolsó előttiig megyünk
    for i in range(0, len(auto_jelei) - 1):
        # A szakasz kezdete (i) és a szakasz vége (i+1) percekben
        kezdet_perc_osszesen = auto_jelei[i]["ora"] * 60 + auto_jelei[i]["perc"]
        vege_perc_osszesen = auto_jelei[i + 1]["ora"] * 60 + auto_jelei[i + 1]["perc"]

        # Kiszámoljuk az i és i+1 között eltelt időt
        eltelt_ido_perc = vege_perc_osszesen - kezdet_perc_osszesen
        eltelt_ido_ora = eltelt_ido_perc / 60

        # A szakasz sebessége a szakasz elejéről, vagyis az i. elemből jön
        szakasz_sebesseg = auto_jelei[i]["sebesseg"]

        # s = v * t (hozzáadjuk a teljes távolsághoz)
        tavolsag += szakasz_sebesseg * eltelt_ido_ora

        # Kiírjuk a következő időpontot (i+1) és az addig elért új távolságot
        print(f"{auto_jelei[i + 1]['ora']}:{auto_jelei[i + 1]['perc']} {round(tavolsag, 1)} km")

# ==========================================
# 7. feladat: ido.txt fájl elkészítése
# ==========================================
# Szótárat használunk, ahol a kulcs a rendszám lesz.
# Mivel a fájl időrendben van, az első találkozás az első jelzés,
# a legutolsó frissítés pedig az utolsó jelzés lesz.
autok_idomero = {}

for jel in jeladasok:
    rsz = jel["rendszam"]
    if rsz not in autok_idomero:
        # Ha a rendszám még nincs a szótárban, az az autó legelső jelzése, így fixen elmentjük az indítási óra és perc értékeket.
        autok_idomero[rsz] = {
            "elso_ora": jel["ora"],
            "elso_perc": jel["perc"],
            "utolso_ora": jel["ora"],
            "utolso_perc": jel["perc"]
        }
    else:
        # Ha már szerepel az autó a listában: csak az utolsó ismert időpontokat felülírjuk a friss adattal
        autok_idomero[rsz]["utolso_ora"] = jel["ora"]
        autok_idomero[rsz]["utolso_perc"] = jel["perc"]

# Kiírás fájlba
out_file = open("ido.txt", "w", encoding="utf-8")
for rsz, idok in autok_idomero.items():
    out_file.write(f"{rsz} {idok['elso_ora']} {idok['elso_perc']} {idok['utolso_ora']} {idok['utolso_perc']}\n")

