# des_step1.py
# Implementare DES Step 1: subcheile K1..K16 din K (64b) exact ca în descriere.

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

# ---------- utilitare ----------
def hex_to_bits(h):
    h = h.strip().replace(" ", "").lower()
    return "".join(bin(int(c,16))[2:].zfill(4) for c in h)

def detect_and_parse_key(s):
    s = s.strip().replace(" ", "")
    if all(ch in "01" for ch in s):
        if len(s) != 64:
            raise ValueError("K trebuie să fie 64 de biți (șir binar).")
        return s
    # altfel presupunem hex (16 hex -> 64 biți)
    if len(s) != 16 or any(ch not in "0123456789abcdefABCDEF" for ch in s):
        raise ValueError("Întrodu 64 biți sau 16 hex.")
    return hex_to_bits(s)

def perm(bits, table):
    return "".join(bits[i-1] for i in table)  # tabele 1-indexate

def rol28(b, n):
    n %= 28
    return b[n:]+b[:n]

def group(s, n):
    return " ".join(s[i:i+n] for i in range(0, len(s), n))

def print_table(title, tbl, width):
    print(f"\n{title}")
    for i in range(0, len(tbl), width):
        row = " ".join(str(x).rjust(2) for x in tbl[i:i+width])
        print("  " + row)

# ---------- flux principal ----------
def main():
    print_table("PC-1 (64→56)", PC1, 7)
    print_table("Rotații (runde 1..16)", list(enumerate(ROT, start=1)), 8)
    print_table("PC-2 (56→48)", PC2, 6)

    raw = input("\nIntrodu K (64 biți binar) sau hex(16): ").strip()
    if raw == "":
        # default: exemplul clasic din text
        raw = "0001001100110100010101110111100110011011101111001101111111110001"
        print("(Folosit exemplul implicit din text)")

    K = detect_and_parse_key(raw)
    print("\nK (64b, grupat 8):")
    print(" ", group(K, 8))

    K_plus = perm(K, PC1)
    print("\nK+ (56b, grupat 7) = PC-1(K):")
    print(" ", group(K_plus, 7))

    C0, D0 = K_plus[:28], K_plus[28:]
    print("\nC0 (28b):", C0)
    print("D0 (28b):", D0)

    C, D = C0, D0
    Cs, Ds, Ks = [C0], [D0], []

    for r in range(16):
        C = rol28(C, ROT[r])
        D = rol28(D, ROT[r])
        Cs.append(C)
        Ds.append(D)
        K_r = perm(C + D, PC2)
        Ks.append(K_r)

    # Afișare C1..C16, D1..D16 (exact ca în step 1)
    print("\n--- Secvențe Cn/Dn ---")
    for i in range(0, 17):
        if i == 0:
            print(f"C0 = {Cs[i]}")
            print(f"D0 = {Ds[i]}")
        else:
            print(f"C{i} = {Cs[i]}")
            print(f"D{i} = {Ds[i]}")

    # Afișare K1..K16 în grupuri de 6 biți
    print("\n--- Subchei K1..K16 (48b, grupate 6) ---")
    for i, Ki in enumerate(Ks, start=1):
        print(f"K{i:<2} = {group(Ki, 6)}")

if __name__ == "__main__":
    main()
