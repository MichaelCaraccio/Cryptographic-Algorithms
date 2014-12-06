"""
    Cryptage d'une chaine en hexadécimal avec l'algorythme DES
    Auteur : Jules Laville
    Version python : 3.4.1
"""
__pc1 = [
    56, 48, 40, 32, 24, 16,  8,
    0, 57, 49, 41, 33, 25, 17,
    9,  1, 58, 50, 42, 34, 26,
    18, 10,  2, 59, 51, 43, 35,
    62, 54, 46, 38, 30, 22, 14,
    6, 61, 53, 45, 37, 29, 21,
    13,  5, 60, 52, 44, 36, 28,
    20, 12,  4, 27, 19, 11,  3
]
__left_rotations = [
    1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1
]
__pc2 = [
    13, 16, 10, 23,  0,  4,
    2, 27, 14,  5, 20,  9,
    22, 18, 11,  3, 25,  7,
    15,  6, 26, 19, 12,  1,
    40, 51, 30, 36, 46, 54,
    29, 39, 50, 44, 32, 47,
    43, 48, 38, 55, 33, 52,
    45, 41, 49, 35, 28, 31
]
__ip = [
    57, 49, 41, 33, 25, 17, 9,  1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7,
    56, 48, 40, 32, 24, 16, 8,  0,
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6
]
__expansion_table = [
    31,  0,  1,  2,  3,  4,
    3,  4,  5,  6,  7,  8,
    7,  8,  9, 10, 11, 12,
    11, 12, 13, 14, 15, 16,
    15, 16, 17, 18, 19, 20,
    19, 20, 21, 22, 23, 24,
    23, 24, 25, 26, 27, 28,
    27, 28, 29, 30, 31,  0
]
__sbox = [
    # S1
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
     0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
     4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
     15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],

    # S2
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
     3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
     0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
     13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],

    # S3
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
     13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
     13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
     1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],

    # S4
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
     13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
     10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
     3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],

    # S5
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
     14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
     4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
     11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],

    # S6
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
     10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
     9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
     4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],

    # S7
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
     13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
     1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
     6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],

    # S8
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
     1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
     7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
     2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
]
__p = [
    15, 6, 19, 20, 28, 11,
    27, 16, 0, 14, 22, 25,
    4, 17, 30, 9, 1, 7,
    23, 13, 31, 26, 2, 8,
    18, 12, 29, 5, 21, 10,
    3, 24
]
__ip1 = [
    39,  7, 47, 15, 55, 23, 63, 31,
    38,  6, 46, 14, 54, 22, 62, 30,
    37,  5, 45, 13, 53, 21, 61, 29,
    36,  4, 44, 12, 52, 20, 60, 28,
    35,  3, 43, 11, 51, 19, 59, 27,
    34,  2, 42, 10, 50, 18, 58, 26,
    33,  1, 41,  9, 49, 17, 57, 25,
    32,  0, 40,  8, 48, 16, 56, 24
]


def hexToBoolArray(hexa):
    """
    Crée un tableau de boolean selon la chaine hexadécimale
    :param hexa: Source en hexadécimale
    :return: Tableau de boolean
    """
    return fromInt(int(hexa, 16), 4 * len(hexa))


def printBoolArray(tab, l=8, pref=""):
    """
    Affiche un tableau de boolean sous la forme d'une chaine binaire
    :param tab: Tableau de boolean
    :param l: taille du regroupement des bytes
    :param pref: Texte affiché avant
    :return: None
    """
    i = 0
    print(pref, end="")
    for t in tab:
        print('1' if t else '0', end="")
        i += 1
        if i >= l:
            i = 0
            print(" ", end="")
    print("")


def printBoolArrayArray(tab, pref, l=8):
    """
    Affiche un tableau de tableau de boolean
    :param tab: tableau de tableau de boolean
    :param pref: Texte affiché avant
    :param l: taille du regroupement des bytes
    :return: None
    """
    i = 0
    for t in tab:
        printBoolArray(t, l, "%s%2d = " % (pref, i))
        i += 1


def permutter(tab, rule):
    """
    Fait un permuttation de tab selon le tableau rule
    :param tab: Tableau a permutter
    :param rule: Tableau référence
    :return: Tableau permutté
    """
    newTab = [False] * len(rule)
    i = 0
    for j in rule:
        newTab[i] = tab[j]
        i += 1
    return newTab


def createcd(cd0):
    """
    Crére le tableau C[0..17] ou D[0..17]
    récupere le C[n-1] et aplique les shifts
    :param cd0: C0 ou D0
    :return: tableau C[0..17] ou D[0..17]
    """
    cds = [cd0] * 17
    cds[0] = cd0
    for i in range(1, 17):
        cds[i] = cds[i - 1]
        for j in range(0, __left_rotations[i-1]):
            cds[i] = leftShift(cds[i])
    return cds


def leftShift(t):
    """
    Rotation à gauche des bytes
    :param t: Tabelau a shifter
    :return: Tableau shifté
    """
    return t[1:] + [t[0]]


def createK(C, D):
    """
    Crée un tableau de K[n] selon C[n] + D[n]
    puis permutte K[n] selon PC-2
    :param C: C[n]
    :param D: D[n]
    :return: K[n]
    """
    K = [None] * 17
    for i in range(0, 17):
        K[i] = C[i] + D[i]
        printBoolArray(K[i], 7, "C%2dD%2d = " % (i, i))
        K[i] = permutter(K[i], __pc2)

    return K


def f(Rn1, Kn):
    """
    Encodage des bytes selon les S-BOX
    :param Rn1: Valeur de R à n-1
    :param Kn: Valeur de K à n
    :return: Valeur avec encdage par S-BOX et P
    """
    ERn1 = permutter(Rn1, __expansion_table)
    printBoolArray(ERn1, 6, "ERN1=")

    xorRes = xorArray(ERn1, Kn)
    printBoolArray(xorRes, 6, "xorRes")
    r = []
    for i in range(8):
        r += fromInt(__sbox[i][toInt(
            xorRes[i * 6: i * 6 + 1] +
            xorRes[i * 6 + 5: i * 6 + 6] +
            xorRes[i * 6 + 1: i * 6 + 5]
        )], 4)
    printBoolArray(r, 4, "f = ")
    r = permutter(r, __p)
    printBoolArray(r, 8, "ps = ")
    return r


def xorArray(A, B):
    """
    Fait un XOR entre les tableaux A et B
    :param A:
    :param B:
    :return: XOR
    """
    l = len(A)
    R = [None] * l
    for i in range(l):
        R[i] = A[i] ^ B[i]
    return R


def fromInt(val, size):
    """
    Créer un tableau de boolean de taille size représentant la valeur en binaire
    :param val: Valeur
    :param size: Taille du tableau
    :return: Tableau de boolean
    """
    tab = [False] * size
    i = 0
    while val > 0:
        tab[size - i - 1] = val % 2 == 1
        val //= 2
        i += 1
    return tab


def toInt(tab):
    """
    Retourne la valeur en int du tableau
    :param tab: Tabeau en binaire
    :return: valeur en int
    """
    val = 0
    for t in tab:
        val *= 2
        if t:
            val += 1
    return val


def toHex(tab):
    """
    Retourne la valeur en hexadécimale d'un tableau de boolean
    :param tab: Tableau source
    :return: Valeur hexadécimale
    """
    r = ""
    for i in range(len(tab) // 4):
        r += "%X" % toInt(tab[4 * i:4 * i + 4])
    return r


def des(message, mykey):
    """
    Crypte la valeur de message selon la clé key avec l'algo DES
    :param message: Message (hexadécimal)
    :param mykey: Clé (hexadécimal)
    :return: Valeur (hexadécimale)
    """
    K = hexToBoolArray(mykey)
    M = hexToBoolArray(message)
    printBoolArray(K, pref="K = ")

    kp = permutter(K, __pc1)
    printBoolArray(kp, 7, "K' = ")

    C0 = kp[:len(kp)//2]
    D0 = kp[len(kp)//2:]

    printBoolArray(C0, 7, "C0 = ")
    printBoolArray(D0, 7, "D0 = ")

    Cn = createcd(C0)
    printBoolArrayArray(Cn, "C", 7)
    Dn = createcd(D0)
    printBoolArrayArray(Dn, "D", 7)

    Kn = createK(Cn, Dn)
    printBoolArrayArray(Kn, "K", 6)

    printBoolArray(M, 8, "M  = ")
    IP = permutter(M, __ip)
    printBoolArray(IP, pref="IP = ")

    L0 = IP[:len(IP)//2]
    R0 = IP[len(IP)//2:]
    printBoolArray(L0, 4, "L0 = ")
    printBoolArray(R0, 4, "R0 = ")

    L = [L0] * 17
    R = [R0] * 17
    for n in range(1, 17):
        L[n] = R[n-1]
        R[n] = xorArray(f(R[n-1], Kn[n]), L[n-1])
        printBoolArray(L[n], 8, "L[%d] =" % n)
        printBoolArray(R[n], 8, "R[%d] =" % n)

    R16L16 = R[16] + L[16]
    printBoolArray(R16L16, 8, "R16L16 =")

    IP1R16L16 = permutter(R16L16, __ip1)
    printBoolArray(IP1R16L16, 8, "IP1R16L16 =")

    cryped = toHex(IP1R16L16)
    print("")
    print("")
    print("Value cryped = '%s'" % cryped)
    return cryped


if __name__ == "__main__":
    msg = "0123456789ABCDEF"
    key = "133457799BBCDFF1"
    des(msg, key)
