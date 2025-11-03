alfabet = [
    "A","Ă","Â","B","C","D","E","F","G","H","I","J","K","L",
    "M","N","O","P","Q","R","S","Ș","T","Ț","U","V","W","X","Y","Z"
]

matrix_rows = 5
matrix_cols = 6
inserare = "X"

def creare_matrice_playfair(cheie: str):
    cheie = cheie.upper()
    # eliminăm caractere nevalide și duplicate
    cheie_curata = ""
    for letter in cheie:
        if letter in alfabet and letter not in cheie_curata:
            cheie_curata += letter
    # completăm cu literele alfabetului român care nu sunt în cheie
    for letter in alfabet:
        if letter not in cheie_curata:
            cheie_curata += letter
    # construim matricea 5x6
    matrice = [[cheie_curata[i * matrix_cols + j] for j in range(matrix_cols)] for i in range(matrix_rows)]
    return matrice
# afișăm matricea
def afisare_matrice(matrice):
    print("Matricea Playfair 5x6:")
    for row in matrice:
        print(" ".join(row))
    print("\n")
# găsim poziția unei litere în matrice   
def gasire_locatie(matrice, char):
    for i in range(matrix_rows):
        for j in range(matrix_cols):
            if matrice[i][j] == char:
                return i, j
    return -1, -1
# pregătim mesajul pentru criptare
def pregatire_mesaj(mesaj):
    msg = "".join(letter for letter in mesaj.upper() if letter in alfabet)
    i = 0
    rezultat = ""
    while i < len(msg):
        a = msg[i]
        if i + 1 < len(msg):
            b = msg[i + 1]
            if a == b:
                rezultat += a + inserare
                i += 1
            else:
                rezultat += a + b
                i += 2
        else:
            rezultat += a + inserare
            i += 1
    return rezultat
# criptăm o pereche de litere în funcție de regulile Playfair
def criptare_pereche(matrice, m1, m2):
    r1, c1 = gasire_locatie(matrice, m1)
    r2, c2 = gasire_locatie(matrice, m2)

    if r1 == r2:
        # dacă sunt pe aceeași linie, mutăm la dreapta
        c1_new = (c1 + 1) % matrix_cols
        c2_new = (c2 + 1) % matrix_cols
        return matrice[r1][c1_new], matrice[r2][c2_new]

    elif c1 == c2:
        # dacă sunt pe aceeași coloană, mutăm în jos
        r1_new = (r1 + 1) % matrix_rows
        r2_new = (r2 + 1) % matrix_rows
        return matrice[r1_new][c1], matrice[r2_new][c2]

    else:
        # dacă sunt pe rânduri și coloane diferite, formăm un dreptunghi
        return matrice[r1][c2], matrice[r2][c1]

# decriptăm o pereche de litere în funcție de regulile Playfair
def decriptare_pereche(matrice, c1, c2):
    r1, col1 = gasire_locatie(matrice, c1)
    r2, col2 = gasire_locatie(matrice, c2)
    if r1 == r2:
        # Dacă sunt pe aceeași linie, mutăm la stânga
        return matrice[r1][(col1 - 1) % matrix_cols], matrice[r2][(col2 - 1) % matrix_cols]

    elif col1 == col2:
        # Dacă sunt pe aceeași coloană, mutăm în sus
        return matrice[(r1 - 1) % matrix_rows][col1], matrice[(r2 - 1) % matrix_rows][col2]
    else:
        # Dacă sunt pe rânduri și coloane diferite, formăm un dreptunghi
        return matrice[r1][col2], matrice[r2][col1]

# funcția principală pentru criptare și decriptare
def playfair_criptare(mesaj: str, cheie: str) -> str:
    matrice = creare_matrice_playfair(cheie)
    afisare_matrice(matrice)  # afișăm matricea
    mesaj = pregatire_mesaj(mesaj)
    criptograma = ""
    for i in range(0, len(mesaj), 2):
        a, b = mesaj[i], mesaj[i+1]
        c1, c2 = criptare_pereche(matrice, a, b)
        criptograma += c1 + c2
    return criptograma
def playfair_decriptare(criptograma: str, cheie: str) -> str:
    matrice = creare_matrice_playfair(cheie)
    afisare_matrice(matrice) 
    mesaj = ""
    for i in range(0, len(criptograma), 2):
        a, b = criptograma[i], criptograma[i+1]
        m1, m2 = decriptare_pereche(matrice, a, b)
        mesaj += m1 + m2

    i = 0
    while i < len(mesaj) - 2:
        if mesaj[i] == mesaj[i+2] and mesaj[i+1] == inserare:
            mesaj = mesaj[:i+1] + mesaj[i+2:]
        i += 1

    if len(mesaj) > 0 and mesaj[-1] == inserare: 
        mesaj = mesaj[:-1]

    return mesaj

choice = input("Alegeti c pentru Criptare sau d pentru Decriptare: ")
while True:
    print("Mesajul: ")
    text = input().upper()
    text = text.replace(" ", "")
    valid = True
    for letter in text:
        if letter not in alfabet:
            print(
                "Textul contine unul sau mai multe caractere ilegale folositi litere A - Z sau a-z"
            )
            valid = False
            break
    if valid == True:
        break
while True:
    print("Introduceti cheia alfabetica(minim 7 litere):")
    key2 = input().upper()
    valid = True
    while len(key2) < 7:
        print("Introduceti o cheie mai lunga")
        key2 = input().upper()
       
    for litera in key2:
        if litera not in alfabet :
          print("Cheia contine una sau mai multe caractere care nu sunt permise.Folositi din diapazonul A-Z")
          valid = False
          break
    if valid:
        break
if choice =="d":
    print("Mesajul decriptat:",playfair_decriptare(text,key2))
else:
    print("Mesajul criptat:",playfair_criptare(text,key2))