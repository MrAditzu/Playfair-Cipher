PC1 = [
    57,49,41,33,25,17,9,   1,58,50,42,34,26,18,
    10,2,59,51,43,35,27,   19,11,3,60,52,44,36,
    63,55,47,39,31,23,15,  7,62,54,46,38,30,22,
    14,6,61,53,45,37,29,   21,13,5,28,20,12,4
]
ROTATIONS = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
PC2 = [
    14,17,11,24,1,5, 3,28,15,6,21,10,
    23,19,12,4,26,8, 16,7,27,20,13,2,
    41,52,31,37,47,55, 30,40,51,45,33,48,
    44,49,39,56,34,53, 46,42,50,36,29,32
]
#elimină dintr-un șir toate caracterele care nu sunt cifre hexazecimale.
def only_hex(s):
    out = ""
    for ch in s:
        c = ch.lower()
        if ('0' <= c <= '9') or ('a' <= c <= 'f'):
            out += ch
    return out

#convertește un șir hexazecimal într-un șir binar.
def hex_to_bin(h):
    v = 0
    for ch in h:
        c = ch.lower()
        if '0' <= c <= '9':
            d = ord(c) - ord('0')
        else:
            d = 10 + ord(c) - ord('a')
        v = (v << 4) | d
    b = bin(v)[2:]
    need = len(h)*4 - len(b)
    return ("0"*need) + b

#Aplică o permutare asupra unui șir de biți
def permute(bits, table):
    return "".join(bits[i-1] for i in table)

#Face o rotație circulară la stânga cu k poziții a unui șir
def left_rotate(s, k):
    k %= len(s)
    return s[k:] + s[:k]

def group_bits(bits, size):
    res, cur = [], ""
    for i, ch in enumerate(bits, 1):
        cur += ch
        if i % size == 0:
            res.append(cur); cur = ""
    if cur: res.append(cur)
    return " ".join(res)

def byte_parity_is_odd(b8):
    ones = 0
    for ch in b8:
        if ch == '1': ones += 1
    return (ones % 2) == 1

def println(s=""):
    print(s, flush=True)

# „Random” fără importuri – LCG pe seed introdus de utilizator (sau implicit)
def lcg_next(x):  # 32-bit LCG
    return (1664525 * x + 1013904223) % (1<<32)

def random_key_64(seed_text):
    if seed_text == "": seed_text = "seed-implicita"
    x = 0
    for ch in seed_text:
        x = (x * 131 + ord(ch)) % (1<<32)
    bits = ""
    for _ in range(2):         # 2 * 32 = 64 biți
        x = lcg_next(x)
        part = bin(x)[2:]
        bits += ("0"*(32-len(part))) + part
    return bits