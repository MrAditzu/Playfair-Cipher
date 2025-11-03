#criptarea si decriptarea cu o cheie
def encrypt(text,alfabet,key):
    result =""
    for litera in text:
        criptograma =(alfabet.index(litera) + key) % len(alfabet)
        result += alfabet[criptograma]
    return result
def decrypt(mesajul,alfabet,key):
    result = ""
    for litera in mesajul:
        criptograma=(alfabet.index(litera)-key) % len(alfabet)
        result += alfabet[criptograma]
    return result
#crearea noului alfabet
def encrypt_alfabet(alfabet,key2):
    result = ""
    for litera in key2 +alfabet:
        if litera not in result:
            result +=litera
    return result
#criptarea si decriptarea cu 2 chei
def encrypt2(text,new_alfabet,key):
    result = ""
    for litera in text:
        criptograma = (new_alfabet.index(litera)+key) % len(new_alfabet)
        result +=new_alfabet[criptograma]
    return result
def decrypt2(mesajul,new_alfabet,key):
    result = ""
    for litera in mesajul:
        criptograma = (new_alfabet.index(litera)-key)%len(new_alfabet)
        result +=new_alfabet[criptograma]
    return result

alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

choice = input("Alegeti c pentru Criptare sau d pentru Decriptare: ")
while True:
    print("Mesajul: ")
    text = input().upper()
    text = text.replace(" ", "")
    valid = True
    for litera in text:
        if litera not in alfabet:
            print(
                "Textul contine unul sau mai multe caractere ilegale folositi litere A - Z sau a-z"
            )
            valid = False
            break
    if valid == True:
        break

        
while True:
    print("Introdu cheia:")
    key = int(input())
    if key<1 or key>25:
        print("Introduceti o cheie cu un numar cuprins intre 1-25: ")
        key =int(input())
    else:
        break

while True:
    print("Introduceti cheia alfabetica(optional,minim 7 litere):")
    key2 = input().upper()
    if len(key2)==0:
        break
    while len(key2) < 7:
        print("Introduceti o cheie mai lunga")
        key2 = input().upper()
        if len(key2) == 0:
            break
        
    for litera in key2:
        if litera not in alfabet :
         print("Cheia contine una sau mai multe caractere care nu sunt permise.Folositi din diapazonul A-Z")
         valid = False
         break
    if valid:
        break
new_alfabet =encrypt_alfabet(alfabet,key2)
if choice =="d":
    if key2:
        print("Mesaj decriptat:",decrypt2(text,new_alfabet,key))
    else:
        print("Mesajul decriptat:",decrypt(text,alfabet,key))
else:
    if key2:
        print("Mesajul criptat:",encrypt2(text,new_alfabet,key))
    else:
        print("Mesajul criptat:",encrypt(text,alfabet,key))
    
        
    
    