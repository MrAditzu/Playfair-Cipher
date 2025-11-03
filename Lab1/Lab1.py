def encrypt(text, alphabet, key):
    """Criptare cu o singură cheie (Cezar)"""
    result = ""
    for ch in text:
        idx = (alphabet.index(ch) + key) % len(alphabet)
        result += alphabet[idx]
    return result


def decrypt(text, alphabet, key):
    """Decriptare cu o singură cheie (Cezar)"""
    result = ""
    for ch in text:
        idx = (alphabet.index(ch) - key) % len(alphabet)
        result += alphabet[idx]
    return result


def encrypt_alphabet(alphabet, key2):
    """Creare alfabet nou pe baza cheii alfabetice"""
    result = ""
    for ch in key2 + alphabet:
        if ch not in result:
            result += ch
    return result


def encrypt2(text, new_alphabet, key):
    """Criptare cu alfabet nou"""
    result = ""
    for ch in text:
        idx = (new_alphabet.index(ch) + key) % len(new_alphabet)
        result += new_alphabet[idx]
    return result


def decrypt2(text, new_alphabet, key):
    """Decriptare cu alfabet nou"""
    result = ""
    for ch in text:
        idx = (new_alphabet.index(ch) - key) % len(new_alphabet)
        result += new_alphabet[idx]
    return result


# --- Program principal ---
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

choice = input("Alegeți 1. Criptare sau 2. Decriptare: ").strip()
text = input("Mesajul: ").upper().replace(" ", "")

# validare text
if any(ch not in alphabet for ch in text):
    print("Textul conține caractere nepermise. Folosiți doar litere A-Z.")
    exit()

# citire cheie numerică
while True:
    try:
        key = int(input("Cheia (0-25): "))
        if 0 <= key < len(alphabet):
            break
        else:
            print("Introduceți o valoare între 0 și 25.")
    except ValueError:
        print("Introduceți un număr valid.")

# citire cheie alfabetică (opțională)
key2 = input("Cheia alfabetică (opțional, minim 7 litere): ").upper()
if key2 and len(key2) < 7:
    print("Cheia alfabetică trebuie să fie mai lungă de 6 caractere.")
    exit()

# creăm alfabetul nou dacă avem key2
new_alphabet = encrypt_alphabet(alphabet, key2) if key2 else alphabet

# rulare criptare/decriptare
if choice == "2":  # Decriptare
    if key2:
        print("Mesaj decriptat:", decrypt2(text, new_alphabet, key))
    else:
        print("Mesaj decriptat:", decrypt(text, alphabet, key))
else:  # Criptare
    if key2:
        print("Mesaj criptat:", encrypt2(text, new_alphabet, key))
    else:
        print("Mesaj criptat:", encrypt(text, alphabet, key))
