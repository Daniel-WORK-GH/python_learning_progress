#key : value pairs, use : { }
#dictionary.items() - returns list of items in dict
#dic.get(value, defualt_value) get value safely from dict

#exercise answer :
def decrypt(value : str, key : dict):
    msg = ""
    for c in value:
        msg += key.get(c," ")
    return msg

encryption_key = {
    'T': '1', 'F': '6', 'W': 'c', 'Y': 'h', 'B': 'k',
    'P': '~', 'H': 'q', 'S': 's', 'E': 'w', 'Q': '@',
    'U': '$', 'M': 'i', 'I': 'l', 'N': 'o', 'J': 'y',
    'Z': 'z', 'G': '!', 'L': '#', 'A': '&', 'O': '+',
    'D': ',', 'R': '-', 'C': ':', 'V': '?', 'X': '^', 
    'K': '|',
}

SONG = """
l1's ih #l6w
l1's o+c +- ow?w-
l &lo'1 !+oo& #l?w 6+-w?w-
l y$s1 c&o1 1+ #l?w cql#w l'i &#l?w
(l1's ih #l6w)
ih qw&-1 ls #l|w &o +~wo ql!qc&h
#l|w 6-&o|lw s&l,
l ,l, l1 ih c&h
l y$s1 c&o1 1+ #l?w cql#w l'i &#l?w
l1's ih #l6w
"""

decryption_key = {}
for key, value in encryption_key.items():
    decryption_key[value] = key

print(decrypt(SONG, decryption_key))