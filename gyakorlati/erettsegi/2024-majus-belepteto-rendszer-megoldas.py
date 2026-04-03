file = open("bedat.txt", "r", encoding="utf-8").read().splitlines()

tanulok = []
for sor in file:
    sor = sor.split()
    tanulo = {}
    tanulo["kod"] = sor[0]
    tanulo["ido"] = sor[1]
    tanulo["esemeny"] = int(sor[2])
    tanulok.append(tanulo)

#print(tanulok)  # ellenőrzéshez

# 2. Feladat: első belépő és utolsó kilépő
elso = tanulok[0]["ido"]
utolso = tanulok[-1]["ido"]
print("2. feladat")
print(f'Az első tanuló {elso}-kor lépett be a főkapun.')
print(f'Az utolsó tanuló {utolso}-kor lépett ki a főkapun.')

# 3. Feladat: késők listája
output_file = open("kesok.txt", "w", encoding="utf-8")
for t in tanulok:
    if t["esemeny"] == 1:  # csak belépések
        ido_float = float(t["ido"].replace(":", "."))
        if 7.50 < ido_float <= 8.15:
            output_file.write(f"{t['ido']} {t['kod']}\n")
output_file.close()

# 4. Feladat: menzán ebédelők száma
menza = 0
for t in tanulok:
    if t["esemeny"] == 3:
        menza += 1
print("4. feladat")
print(f'A menzán aznap {menza} tanuló ebédelt.')

# 5. Feladat: könyvtári kölcsönzések és összehasonlítás
konyvtarosak = set()
for t in tanulok:
    if t["esemeny"] == 4:
        konyvtarosak.add(t["kod"])

print("5. feladat")
print(f'Aznap {len(konyvtarosak)} tanuló kölcsönzött a könyvtárban.')

if len(konyvtarosak) > menza:
    print("Többen voltak, mint a menzán.")
else:
    print("Nem voltak többen, mint a menzán.")

# 6. Feladat: szünetben hátul távozók (10:50 után 11:00-ig visszajöttek)


bentlevok = []
erintettek = []
for t in tanulok:
    # belépés = 1, kilépés = 2
    if t["esemeny"] == 1 and t["ido"] < "10:50":
        bentlevok.append(t["kod"])
    elif t["esemeny"] == 2 and t["ido"] < "11:00":
        bentlevok.remove(t["kod"])
    if t["esemeny"] == 1 and  '10:50'< t["ido"] < "11:00" :
        if t["kod"] in bentlevok:
            erintettek.append(t["kod"])


print("6. feladat")
print("Az érintett tanulók:")
print(" ".join(erintettek))

# 7. Feladat: egy tanuló tartózkodási ideje


# pl hany perc telik el 08:40 és 09:10 kozott?  -> 30perc
# ehhez segédfüggvényt kell írnunk
def percbe(ora, perc):
    return int(ora)*60 + int(perc)


bekert_azonosito = input("7. feladat\nEgy tanuló azonosítója=").strip()

bejovetelek = []
kilepesek = []
volt_ilyen = False
for t in tanulok:
    if t["kod"] == bekert_azonosito:
        volt_ilyen = True
        if t["esemeny"] == 1:
            bejovetelek.append(t["ido"])
        elif t["esemeny"] == 2:
            kilepesek.append(t["ido"])

if volt_ilyen == False:
    print("Ilyen azonosítójú tanuló aznap nem volt az iskolában.")
else:
    # Első belépés és utolsó kilépés meghatározása
    elso_bejovetel = min(bejovetelek)
    utolso_kilepes = max(kilepesek)

    # Óra és perc különválasztása
    elso_be = elso_bejovetel.split(":")
    utolso_ki = utolso_kilepes.split(":")


    # Tartózkodási idő percben
    kulonbseg_percben = percbe(utolso_ki[0], utolso_ki[1]) - percbe(elso_be[0], elso_be[1])

    # Óra és perc formátum
    ora = kulonbseg_percben // 60
    perc = kulonbseg_percben % 60

    print(f"A tanuló érkezése és távozása között {ora} óra {perc} perc telt el.")