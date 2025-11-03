# Playfair pentru limba română (30 litere, fără Î)
# Matrice 5x6
# Fără sys și re

ROMANIAN_ALPHABET = [
    "A","Ă","Â","B","C","D","E","F","G","H","I","J","K","L",
    "M","N","O","P","Q","R","S","Ș","T","Ț","U","V","W","X","Y","Z"
]
# Am eliminat litera "Î"

MATRIX_ROWS = 5
MATRIX_COLS = 6
FILLER = "Q"  # literă de umplere pentru perechi duble

def normalize_text(tx):
    """Transformă textul în majuscule, elimină caracterele nepermise și litera Î."""
    tx = tx.strip().upper()
    cleaned = ""
    for ch in tx:
        if ch == "Î":
            continue  # eliminăm complet Î
        elif ch in ROMANIAN_ALPHABET:
            cleaned += ch
        # ignorăm alte caractere (spații, semne etc.)
    return cleaned

def build_matrix_from_key(key):
    """Construiește matricea Playfair pe baza cheii."""
    used = []
    for ch in key:
        if ch not in used and ch in ROMANIAN_ALPHABET:
            used.append(ch)
    for ch in ROMANIAN_ALPHABET:
        if ch not in used:
            used.append(ch)
    matrix = []
    k = 0
    for i in range(MATRIX_ROWS):
        row = []
        for j in range(MATRIX_COLS):
            row.append(used[k])
            k += 1
        matrix.append(row)
    return matrix

def find_pos(matrix, ch):
    """Găsește poziția (r, c) a unui caracter în matrice."""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == ch:
                return (i, j)
    return (-1, -1)

def prepare_digraphs(text):
    """Împarte textul în perechi (digrafuri), adăugând filler unde e nevoie."""
    digraphs = []
    i = 0
    while i < len(text):
        a = text[i]
        if i + 1 < len(text):
            b = text[i + 1]
            if a == b:
                filler = FILLER if FILLER != a else "X"
                digraphs.append((a, filler))
                i += 1
            else:
                digraphs.append((a, b))
                i += 2
        else:
            filler = FILLER if FILLER != a else "X"
            digraphs.append((a, filler))
            i += 1
    return digraphs

def encrypt_pair(matrix, a, b):
    ra, ca = find_pos(matrix, a)
    rb, cb = find_pos(matrix, b)
    if ra == rb:  # aceeași linie
        return (matrix[ra][(ca + 1) % MATRIX_COLS], matrix[rb][(cb + 1) % MATRIX_COLS])
    elif ca == cb:  # aceeași coloană
        return (matrix[(ra + 1) % MATRIX_ROWS][ca], matrix[(rb + 1) % MATRIX_ROWS][cb])
    else:  # dreptunghi
        return (matrix[ra][cb], matrix[rb][ca])

def decrypt_pair(matrix, a, b):
    ra, ca = find_pos(matrix, a)
    rb, cb = find_pos(matrix, b)
    if ra == rb:
        return (matrix[ra][(ca - 1) % MATRIX_COLS], matrix[rb][(cb - 1) % MATRIX_COLS])
    elif ca == cb:
        return (matrix[(ra - 1) % MATRIX_ROWS][ca], matrix[(rb - 1) % MATRIX_ROWS][cb])
    else:
        return (matrix[ra][cb], matrix[rb][ca])

def encrypt(matrix, plaintext):
    digraphs = prepare_digraphs(plaintext)
    res = ""
    for a, b in digraphs:
        x, y = encrypt_pair(matrix, a, b)
        res += x + y
    return res

def decrypt(matrix, ciphertext):
    res = ""
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i + 1]
        x, y = decrypt_pair(matrix, a, b)
        res += x + y
    return res

def print_matrix(matrix):
    print("Matricea Playfair (5x6):")
    for row in matrix:
        print(" ".join(row))

def main():
    print("Playfair – alfabet românesc (fără Î, 30 litere)")
    op = input("Alege operația (E = criptare, D = decriptare): ").strip().upper()

    key_raw = input("Introdu cheia: ")
    key = normalize_text(key_raw)
    if len(key) < 5:
        print("Cheia este prea scurtă!")
        return

    matrix = build_matrix_from_key(key)
    print_matrix(matrix)

    if op == "E":
        text = input("Introdu textul clar: ")
        txt = normalize_text(text)
        if len(txt) == 0:
            print("Textul este gol sau conține caractere nepermise.")
            return
        result = encrypt(matrix, txt)
        print("Criptograma:", result)
    elif op == "D":
        text = input("Introdu criptograma: ").strip().upper()
        if len(text) % 2 != 0:
            print("Criptograma are lungime impară!")
            return
        result = decrypt(matrix, text)
        print("Text decriptat (cu filler-uri):", result)
    else:
        print("Operație necunoscută!")

# rulare
main()
