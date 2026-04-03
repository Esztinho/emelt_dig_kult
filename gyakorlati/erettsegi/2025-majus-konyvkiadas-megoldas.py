# 1. feladat: Beolvasás
# A feladat szerint a kiadas.txt vagy kiadas2.txt is használható

file = open("kiadas2.txt", "r", encoding="utf-8").read().splitlines()
konyvek = []
for sor in file:
    adat = sor.strip().split(";")
    konyv = {
        "ev": int(adat[0]),
        "negyedev": int(adat[1]),
        "nyelv": adat[2],
        "leiras": adat[3],
        "peldanyszam": int(adat[4])
    }
    konyvek.append(konyv)

# 2. feladat
print("2. feladat:")
bekert_szerzo = input("Szerző: ")
szamlalo = 0
for konyv in konyvek:
    if bekert_szerzo in konyv["leiras"]:
        szamlalo += 1

if szamlalo > 0:
    print(f"{szamlalo} könyvkiadás")
else:
    print("Nem adtak ki")

# 3. feladat
print("3. feladat:")
max_peldany = 0
for konyv in konyvek:
    if konyv["peldanyszam"] > max_peldany:
        max_peldany = konyv["peldanyszam"]

max_db = 0
for konyv in konyvek:
    if konyv["peldanyszam"] == max_peldany:
        max_db += 1

print(f"Legnagyobb példányszám: {max_peldany}, előfordult {max_db} alkalommal")

# 4. feladat
print("4. feladat:")
for konyv in konyvek:
    if konyv["nyelv"] == "kf" and konyv["peldanyszam"] >= 40000:
        print(f"{konyv['ev']}/{konyv['negyedev']}. {konyv['leiras']}")
        break  # Csak az első kell!

# 5. feladat
print("5. feladat:")
fejlec = "Év\tMagyar kiadás\tMagyar példányszám\tKülföldi kiadás\tKülföldi példányszám"
print(fejlec)

html_fajl = open("tabla.html", "w", encoding="utf-8")
print("<table>", file=html_fajl)
# HTML fejléc összeállítása
html_fejlec = "<tr><th>Év</th><th>Magyar kiadás</th><th>Magyar példányszám</th><th>Külföldi kiadás</th><th>Külföldi példányszám</th></tr>"
print(html_fejlec, file=html_fajl)


for ev in range(2020, 2024):
    m_db, m_peldany = 0, 0
    k_db, k_peldany = 0, 0

    for konyv in konyvek:
        if konyv["ev"] == ev:
            if konyv["nyelv"] == "ma":
                m_db += 1
                m_peldany += konyv["peldanyszam"]
            else:
                k_db += 1
                k_peldany += konyv["peldanyszam"]

    # Képernyőre tabulátorral
    print(f"{ev}\t\t{m_db}\t\t{m_peldany}\t\t{k_db}\t\t{k_peldany}")

    # HTML fájlba
    print(f"<tr><td>{ev}</td><td>{m_db}</td><td>{m_peldany}</td><td>{k_db}</td><td>{k_peldany}</td></tr>",
          file=html_fajl)

print("</table>", file=html_fajl)
html_fajl.close()

# 6. feladat
print("6. feladat:")
print("Legalább kétszer, nagyobb példányszámban újra kiadott könyvek:")


csoportok = {}
for konyv in konyvek:
    leiras = konyv["leiras"]
    if leiras not in csoportok:
        csoportok[leiras] = []
    csoportok[leiras].append(konyv["peldanyszam"])

for leiras, peldanyszamok in csoportok.items():
    if len(peldanyszamok) > 1:
        elso_kiadas = peldanyszamok[0]
        # Megszámoljuk, hányszor volt nagyobb a példányszám, mint az legelsőnél
        nagyobb_ujrakiadasok = 0
        for i in range(1, len(peldanyszamok)):
            if peldanyszamok[i] > elso_kiadas:
                nagyobb_ujrakiadasok += 1

        if nagyobb_ujrakiadasok >= 2:
            print(leiras)