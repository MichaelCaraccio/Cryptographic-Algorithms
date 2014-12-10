"""
Alghorythme de Viginère
"""
import string

def checkIsString(s, minLen=-1, maxLen=-1):
    if not isinstance(s, str):
        raise ValueError("Not a string")
    if minLen > 0 and len(s) < minLen:
        raise ValueError("Too small string !")
    if maxLen > 0 and len(s) > maxLen:
        raise ValueError("Too big string !")

__lettres = list(string.ascii_uppercase)

def crypte(msg, key):
    checkIsString(msg, minLen=1)
    checkIsString(key, minLen=1)
    ret = ""
    indexKey = 0;
    for l in msg:
        if not l in __lettres:
            raise ValueError("Not a valid message !")
        ret += __lettres[(__lettres.index(l) + __lettres.index(key[indexKey])) % len(__lettres)]
        indexKey = (indexKey + 1) % len(key)
    return ret

def decrypte(msg, key):
    checkIsString(msg, minLen=1)
    checkIsString(key, minLen=1)
    ret = ""
    indexKey = 0;
    for l in msg:
        if not l in __lettres:
            raise ValueError("Not a valid message !")
        ret += __lettres[(__lettres.index(l) - __lettres.index(key[indexKey])) % len(__lettres)]
        indexKey = (indexKey + 1) % len(key)
    return ret

if __name__ == "__main__":
    print(crypte("JADOREECOUTERLARADIOTOUTELAJOURNEE", "MUSIQUE"))
    print(decrypte(crypte("JADOREECOUTERLARADIOTOUTELAJOURNEE", "MUSIQUE"),"MUSIQUE"))

    print(decrypte("PVSRAC", "NEUCH"))
    print(crypte("TRAVAIL", "GARE"))