import random
PC1 = [
    57,49,41,33,25,17,9,
    1,58,50,42,34,26,18,
    10,2,59,51,43,35,27,
    19,11,3,60,52,44,36,
    63,55,47,39,31,23,15,
    7,62,54,46,38,30,22,
    14,6,61,53,45,37,29,
    21,13,5,28,20,12,4
]  # 64 -> 56

ROT = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

PC2 = [
    14,17,11,24,1,5,
    3,28,15,6,21,10,
    23,19,12,4,26,8,
    16,7,27,20,13,2,
    41,52,31,37,47,55,
    30,40,51,45,33,48,
    44,49,39,56,34,53,
    46,42,50,36,29,32
]  # 56 -> 48

# convertește un șir hexazecimal într-un șir de biți
def hex_to_bits(h):
    h = h.strip().replace(" ", "").lower()
    return "".join(bin(int(c, 16))[2:].zfill(4) for c in h)

# Citește o cheie de la utilizator și o validează ca hex de 16 caractere.
def key_input():
    HEXSET = set("0123456789abcdefABCDEF")
    while True:
        k = input("\nIntrodu K hex(16). Enter pentru exemplul clasic: ")
        
        if k.strip() == "":
            k = "".join(random.choice("0123456789ABCDEF") for _ in range(16))
            print(f"Cheia generată este: {k}")
            return hex_to_bits(k)

        if any(ch not in HEXSET for ch in k):
            print("Cheie hex invalidă — folosește doar caractere 0–9 și A–F. Încearcă din nou.")
            continue
        if len(k) < 16:
            print(f"Cheia hex e prea scurtă (trebuie exact 16 caractere) . Încearcă din nou.")
            continue
        if len(k) > 16:
            print(f"Cheia hex e prea lungă (trebuie exact 16 caractere) . Încearcă din nou.")
            continue

        return hex_to_bits(k)

def perm(bits, table):
    return "".join(bits[i-1] for i in table)  # tabele 1-indexate

# Face o rotație circulară la stânga cu n poziții a unui șir de 28 biți
def rol28(b, n):
    n %= 28
    return b[n:] + b[:n]

def group(s, n):
    return " ".join(s[i:i+n] for i in range(0, len(s), n))

#Afișează un tabel cu un titlu dat și lățimea specificată,adica tabelel PC1,PC2,ROT
def print_table(title, tbl, width):
    print(f"\n{title}")
    for i in range(0, len(tbl), width):
        row = " ".join(str(x).rjust(2) for x in tbl[i:i+width])
        print("  " + row)

def main():
    
    K = key_input()
    print_table("PC-1 (64→56)", PC1, 7)
    print("\nK (64b, grupat 8):")
    print(" ", group(K, 8))
    
    # Aplică PC-1 asupra cheii: obții K+ (56 biți)
    K_plus = perm(K, PC1)
    print("\nK+ (56b, grupat 7) = PC-1(K):")
    print(" ", group(K_plus, 7))
    
    # Împarte K+ în C0 și D0 (fiecare 28 biți)
    C0, D0 = K_plus[:28], K_plus[28:]
    print("\nC0 (28b):", C0)
    print("D0 (28b):", D0)
    print_table("Rotații (runde 1..16)", ROT, 16)
    
    #Inițializează C și D pentru bucla de 16 runde.
    C, D = C0, D0
    Cs, Ds, Ks = [C0], [D0], []

    # bucla pentru runda 1..16
    for r in range(16):
        C = rol28(C, ROT[r])
        D = rol28(D, ROT[r])
        Cs.append(C)
        Ds.append(D)
        # Concatenează C_r,D_r (56 biți) și aplică PC-2 pentru a obține subcheia rundei (48 biți).
        K_r = perm(C + D, PC2)
        Ks.append(K_r)

    # Afișare C1..C16, D1..D16 (exact ca în step 1)
    print("\nSecvențe Cn/Dn ")
    for i in range(0, 17):
        if i == 0:
            print(f"C0 = {Cs[i]}")
            print(f"D0 = {Ds[i]}")
        else:
            print(f"C{i} = {Cs[i]}")
            print(f"D{i} = {Ds[i]}")

    # Afișare K1..K16 în grupuri de 6 biți
    print_table("PC-2 (56→48)", PC2, 6)
    print("\nSubchei K1..K16 (48b, grupate 6)")
    for i, Ki in enumerate(Ks, start=1):
        print(f"K{i:<2} = {group(Ki, 6)}")
        
main()