
#===========================================================
# SZÓKERESŐ PROGRAM - Profi Matplotlib Vizualizációval
#===========================================================

import matplotlib.pyplot as plt

#--- #1 TÁBLA DEFINÍCIÓJA ---
tabla = [
"SKCFÖHDBFKVTZ",
"ZESERONEEIIAS",
"ÁMEKERYRHSLPI",
"REREGTEEÉKLOT",
"ANMTTOPTROOLV",
"ZCEEÚBETKNNCA",
"ÜELKRÁRYÖDGAK",
"ÍUYÖRGEÓRAÓRU",
"ODERAYBJÖIJÁT",
"KÖRÖSIKISRÁBA",
"BÁRSONYOSBÓAS"
]

sorok = len(tabla)
oszlopok = len(tabla[0])

#--- #2 KERESENDŐ SZAVAK ÉS IRÁNYOK ---
szavak = [
"BÁRSONYOS","BERETTYÓ","CSERMELY","DNYEPER",
"FEHÉRKÖRÖS","FEKETEKÖRÖS","HORTOBÁGY",
"KEMENCE","KISKONDAI","KISRÁBA","KÖRÖS",
"KUTAS","ODERA","ÖREGTÚR","RÁBA","SZÁRAZ",
"TAPOLCA","VILLONGÓ","ZSITVA"
]

iranyok = [
(-1,0),(1,0),(0,-1),(0,1),
(-1,-1),(-1,1),(1,-1),(1,1)
]

# Egy 12 színből álló lista a különböző szavakhoz
szin_paletta = ['red', 'blue', 'green', 'purple', 'cyan', 'magenta', 
                'orange', 'gold', 'lime', 'teal', 'indigo', 'deeppink']

#--- #3 A SZÓKERESÉS FOLYAMATA (A háttérben fut le először) ---
print("=== KERESÉS INDÍTÁSA ===")

# Ide mentjük a megtalált betűk koordinátáit ÉS a hozzájuk tartozó színt
# Formátum: {(sor, oszlop): szin}
cella_szinek = {} 
szin_index = 0

for szo in szavak:
    megtalalt = False
    for r in range(sorok):
        for c in range(oszlopok):
            if tabla[r][c] == szo[0]:
                for dr, dc in iranyok:
                    jo = True
                    for i in range(len(szo)):
                        uj_r = r + dr*i
                        uj_c = c + dc*i
                        if uj_r < 0 or uj_r >= sorok or uj_c < 0 or uj_c >= oszlopok:
                            jo = False; break
                        if tabla[uj_r][uj_c] != szo[i]:
                            jo = False; break
                    
                    if jo:
                        print(f"MEGVAN: {szo:12} | Sor: {r+1}, Oszlop: {c+1}")
                        # Ha megvan a szó, hozzárendelünk egy színt és elmentjük a betűkhöz
                        # Ha egy betű már színes volt, az új szín felülírja a régit (utolsó megtalált)
                        aktualis_szin = szin_paletta[szin_index % len(szin_paletta)]
                        szin_index += 1 # Következő szóhoz következő szín
                        
                        for i in range(len(szo)):
                            cella_szinek[(r + dr*i, c + dc*i)] = aktualis_szin
                        
                        megtalalt = True; break
                if megtalalt: break
        if megtalalt: break
    if not megtalalt:
        print(f"HIÁNYZIK: {szo}")

#--- #4 KETTŐS GRAFIKUS MEGJELENÍTÉS (Matplotlib) ---
print("\n=== DIAGRAM LÉTREHOZÁSA... ===")

# Létrehozunk egy széles ablakot, benne 1 sorban 2 db ábrával (ax1, ax2)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
fig.suptitle("Szókereső Algoritmus Eredménye", fontsize=20, fontweight='bold', y=0.95)

# Mindkét ábrán (ax1 és ax2) megrajzoljuk a rácsot
for ax in (ax1, ax2):
    ax.set_xlim(0, oszlopok)
    ax.set_ylim(sorok, 0) # Y tengely megfordítása
    ax.axis('off') # Keret kikapcsolása
    
    # Rácsvonalak
    for r_vonal in range(sorok + 1):
        ax.hlines(r_vonal, 0, oszlopok, colors='black', linewidth=1)
    for c_vonal in range(oszlopok + 1):
        ax.vlines(c_vonal, 0, sorok, colors='black', linewidth=1)

# BAL OLDAL: Eredeti feladvány
ax1.set_title("1. Eredeti Feladvány", fontsize=16, pad=10)
for r in range(sorok):
    for c in range(oszlopok):
        ax1.text(c + 0.5, r + 0.5, tabla[r][c], color='black', fontsize=14, fontweight='bold', ha='center', va='center')

# JOBB OLDAL: Kiemelt megoldás
ax2.set_title("2. Megtalált Szavak (Színesben)", fontsize=16, pad=10)
for r in range(sorok):
    for c in range(oszlopok):
        # A betű a színét az utolsó megtalált szó alapján kapja (a cella_szinek szótárból)
        if (r, c) in cella_szinek:
            betu_szine = cella_szinek[(r, c)]
            ax2.text(c + 0.5, r + 0.5, tabla[r][c], 
                     color=betu_szine, fontsize=14, fontweight='bold', ha='center', va='center')
        else:
            # Ha nem nyertes: Halvány szürkére tesszük, hogy a lényeg kiugorjon!
            ax2.text(c + 0.5, r + 0.5, tabla[r][c], color='lightgray', fontsize=14, ha='center', va='center')

plt.tight_layout()
plt.show() # Ez nyitja meg a grafikus ablakot
