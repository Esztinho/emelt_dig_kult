konyv_file = open("konyv.txt", "r", encoding="utf-8").read()
lines = open("konyv.txt", "r", encoding="utf-8").read().splitlines()
#print(lines)

print("1.feladat")
#print(konyv_file)


# 2. feladat
print("2. feladat")
ism = int(input("Kérem adja meg az ismétlések számát: ").strip())


max_w = 0
for line in lines:
    #print(line, len(line))
    if len(line) > max_w:
        max_w = len(line)
#print(max_w)

# Minden sort a max_w szélességre balra igazítunk (szóközzel kitöltve),
# így a " | " függőlegesen egy vonalban lesz.


for line in lines:
    szokozok_szama = max_w - len(line)
    cell = line + " " * szokozok_szama   # kipótoljuk a sort szóközökkel
    #print(cell*ism)
    print((" | ").join([cell] * ism) + " |")
    #Azért kellett a lista ([cell] * ism), mert a join függvény lista (vagy más iterálható) elemeit fűzi össze a megadott szeparátorral.


#3.feladat

def atalakit(sor: str) -> str:
    eredmeny = ""
    for i in range(0, len(sor), 2):   # kettesével lépkedünk: szám + karakter
        ismetleszam = int(sor[i])     # páros index → szám
        karakter = sor[i + 1]         # páratlan index → karakter
        eredmeny += karakter * ismetleszam
    return eredmeny

# Példa
#print(atalakit("934k"))


print("4.feladat")
tomoritett_file = open("szg_t.txt", "r", encoding="utf-8").read().splitlines()



tomoritetlen_output_file = open("szg.txt", "w", encoding="utf-8")
for sor in tomoritett_file:
    print(atalakit(sor))


print("5.feladat")
bekert_tomoritett =  "konyv_t.txt"          #input("Kérem adja meg a tömörített ábra fájlnevét:")
bekert_tomoritetlen =  "konyv.txt "       #input("Kérem adja meg a tömörítetlen ábra fájlnevét:")


def karakterszam_sorveg_nelkul(utvonal: str) -> int:
    """Visszaadja a fájlban lévő karakterek számát, sorvégeket nem számolva."""
    with open(utvonal, "r", encoding="utf-8") as f:
        return sum(len(sor) for sor in f.read().splitlines())

t_szam = karakterszam_sorveg_nelkul(bekert_tomoritett)
u_szam = karakterszam_sorveg_nelkul(bekert_tomoritetlen)

print(f"A(z) {bekert_tomoritett} állomány karakterszáma: {t_szam}")
print(f"A(z) {bekert_tomoritetlen} állomány karakterszáma: {u_szam}")

print(f"tomoritesi arany: {round(t_szam / u_szam, 2)}")


print("6.feladat")
konyv_t = open("konyv_t.txt", "r", encoding="utf-8").read().splitlines()


print(f"Az ábra magassága sorokban: {len(konyv_t)}")

blokkok_szama = 0
max_hossz = 0


for sor in konyv_t:
    blokkok_szama += len(sor) // 2
    hossz = 0
    for i in range(0, len(sor), 2):
        hossz += int(sor[i])
    if hossz > max_hossz:
        max_hossz = hossz


print(f"Az ábra szélessége karakterekben: {max_hossz}")
print(f"A blokkok száma: {blokkok_szama}")