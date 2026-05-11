# 1. feladat: Beolvasás
# A fájlt UTF-8 kódolással érdemes megnyitni a biztonság kedvéért
file = open("taborok.txt", "r", encoding="utf-8").read().splitlines()

taborok = []
for sor in file:
    adat = sor.strip().split("\t")
    tabor = {
        "tol_honap": int(adat[0]),
        "tol_nap": int(adat[1]),
        "ig_honap": int(adat[2]),
        "ig_nap": int(adat[3]),
        "nevek": adat[4],
        "tema": adat[5],
    }

    """
    VAGY ÍGY: 
    tabor["tol_honap"] = int(adat[0])
    tabor["tol_nap"] = int(adat[1])
    tabor["ig_honap"] = int(adat[2])
    tabor["ig_nap"] = int(adat[3])
    tabor["nevek"] = adat[4]
    tabor["tema"] = adat[5]
    """
    taborok.append(tabor)

# 2. feladat
print("2. feladat")
print(f"Az adatsorok száma: {len(taborok)}")
print(f"Az először rögzített tábor témája: {taborok[0]['tema']}")
print(f"Az utoljára rögzített tábor témája: {taborok[-1]['tema']}")

# 3. feladat
print("\n3. feladat")
volt_e_zenei = False
for tabor in taborok:
    if tabor["tema"] == "zenei":
        print(f"Zenei tábor kezdődik {tabor['tol_honap']}. hó {tabor['tol_nap']}. napján.")
        volt_e_zenei = True

if volt_e_zenei == False:  # tehát nem futott le egyszer sem az if, így a változó értéke az eredetileg beállított False marad ez esetben
    print("Nem volt zenei tábor.")

# 4. feladat
print("\n4. feladat")
print("Legnépszerűbbek:")
# Első lépésben megkeressük, mi a maximum létszám
max_letszam = 0
for tabor in taborok:
    if len(tabor["nevek"]) > max_letszam:
        max_letszam = len(tabor["nevek"])

# Második körben kiírjuk az összes olyan tábort, ahol ennyien vannak
for tabor in taborok:
    if len(tabor["nevek"]) == max_letszam:
        print(f"{tabor['tol_honap']} {tabor['tol_nap']} {tabor['tema']}")


# 5. feladat: Függvény a napok sorszámának számításához
def sorszam(ho, nap):
    """
    Kiszámolja, hogy az adott dátum a nyári szünet hányadik napja.
    Június 16. = 1. nap
    """
    if ho == 6:
        return nap - 15  # Június 16 előtt 15 nap telt el a hónapból
    elif ho == 7:
        return 30 - 15 + nap  # Június maradéka (15 nap) + júliusi napok
    else:  # ho == 8
        return 30 - 15 + 31 + nap  # Június (15) + Július (31) + augusztusi napok


# 6. feladat
print("\n6. feladat")
bekert_ho = int(input("hó: "))
bekert_nap = int(input("nap: "))

szamlalo = 0
ma_sorszam = sorszam(bekert_ho, bekert_nap)

for tabor in taborok:
    # A tábor akkor tart, ha a kezdőnapja <= kért nap ÉS a végnapja >= kért nap
    kezdet = sorszam(tabor["tol_honap"], tabor["tol_nap"])
    vege = sorszam(tabor["ig_honap"], tabor["ig_nap"])

    if kezdet <= ma_sorszam <= vege:
        szamlalo += 1

print(f"Ekkor éppen {szamlalo} tábor tart.")

# 7. feladat
print("\n7. feladat")
bekert_nev = input("Adja meg egy tanuló betűjelét: ")

# Kigyűjtjük a diák táborait
diak_taborai = []
for tabor in taborok:
    if bekert_nev in tabor["nevek"]:
        diak_taborai.append(tabor)

# Fájlba írás és ütközésvizsgálat
# Mivel a fájl már alapból kezdési sorrendben van, nem kell külön rendezni
output_file = open("egytanulo.txt", "w")
for tabor in diak_taborai:
    print(
        f"{tabor['tol_honap']}.{tabor['tol_nap']}-{tabor['ig_honap']}.{tabor['ig_nap']}. {tabor['tema']}",
        file=output_file,
    )

# --- A legnehezebb rész: Ütközésvizsgálat ---

mehet_e = True  # feltételezzük, hogy el tud menni mindbe, és azt az esetet keressük, amikor ez a feltétel megbukik
# Összehasonlítjuk az egymás utáni táborokat
# A logikája: ha egy tábor előbb kezdődik, mint ahogy az előző véget ér, akkor ütközés van.
for i in range(0, len(diak_taborai) - 1):
    aktualis_vege = sorszam(diak_taborai[i]["ig_honap"], diak_taborai[i]["ig_nap"])
    kovetkezo_kezdete = sorszam(diak_taborai[i + 1]["tol_honap"], diak_taborai[i + 1]["tol_nap"])

    if kovetkezo_kezdete <= aktualis_vege:
        mehet_e = False
        break  # Elég egyetlen ütközést találni

if mehet_e:
    print("Elmehet mindegyik táborba.")
else:
    print("Nem mehet el mindegyik táborba.")
