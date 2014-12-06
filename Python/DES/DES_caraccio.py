import numpy as np


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def split_list(list):
    return list[0:6], list[6:12], list[12:18], list[18:24], list[24:30], list[30:36], list[36:42], list[42:48]


def S(xB1, xB2, xB3, xB4, xB5, xB6, xB7, xB8):
    S1 = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
          0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
          4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
          15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    S2 = [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
          3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
          0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
          13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    S3 = [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
          13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
          13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
          1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    S4 = [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
          13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
          10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
          3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    S5 = [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
          14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
          4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
          11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    S6 = [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
          10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
          9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
          4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    S7 = [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
          13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
          1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
          6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    S8 = [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
          1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
          7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
          2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]

    tempx = [int(xB1[0]), int(xB1[5])]
    x = ''.join([str(x) for x in tempx])
    x = int(x, 2)
    y = ''.join([str(x) for x in xB1])
    y = int(y[1:5], 2)
    POS1 = bin(S1[(x) * 16 + y])[2:].zfill(4)

    tempx = [int(xB2[0]), int(xB2[5])]
    x = ''.join([str(x) for x in tempx])
    x = int(x, 2)
    y = ''.join([str(x) for x in xB2])
    y = int(y[1:5], 2)
    POS2 = bin(S2[(x) * 16 + y])[2:].zfill(4)

    tempx = [int(xB3[0]), int(xB3[5])]
    x = ''.join([str(x) for x in tempx])
    x = int(x, 2)
    y = ''.join([str(x) for x in xB3])
    y = int(y[1:5], 2)
    POS3 = bin(S3[(x) * 16 + y])[2:].zfill(4)

    tempx = [int(xB4[0]), int(xB4[5])]
    x = ''.join([str(x) for x in tempx])
    x = int(x, 2)
    y = ''.join([str(x) for x in xB4])
    y = int(y[1:5], 2)
    POS4 = bin(S4[(x) * 16 + y])[2:].zfill(4)

    tempx = [int(xB5[0]), int(xB5[5])]
    x = ''.join([str(x) for x in tempx])
    x = int(x, 2)
    y = ''.join([str(x) for x in xB5])
    y = int(y[1:5], 2)
    POS5 = bin(S5[(x) * 16 + y])[2:].zfill(4)

    tempx = [int(xB6[0]), int(xB6[5])]
    x = ''.join([str(x) for x in tempx])
    x = int(x, 2)
    y = ''.join([str(x) for x in xB6])
    y = int(y[1:5], 2)
    POS6 = bin(S6[(x) * 16 + y])[2:].zfill(4)

    tempx = [int(xB7[0]), int(xB7[5])]
    x = ''.join([str(x) for x in tempx])
    x = int(x, 2)
    y = ''.join([str(x) for x in xB7])
    y = int(y[1:5], 2)
    POS7 = bin(S7[(x) * 16 + y])[2:].zfill(4)

    tempx = [int(xB8[0]), int(xB8[5])]
    x = ''.join([str(x) for x in tempx])
    x = int(x, 2)
    y = ''.join([str(x) for x in xB8])
    y = int(y[1:5], 2)
    POS8 = bin(S8[(x) * 16 + y])[2:].zfill(4)

    tabn = [POS1, POS2, POS3, POS4, POS5, POS6, POS7, POS8]

    ToutLesPos = ''.join([str(x) for x in tabn])

    P = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11,
         4, 25]

    P_tab = []

    for i in range(0, 32):
        P_tab.append(ToutLesPos[P[i] - 1])

    return P_tab


def f(list1, list2):

    E = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20,
         21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

    list3 = []

    for i in range(0, 48):
        list3.append(list1[E[i] - 1])

    for i in range(0, 48):
        list3[i] = int(list3[i]) ^ int(list2[i])

    B1, B2, B3, B4, B5, B6, B7, B8 = split_list(list3)

    valeur = S(B1, B2, B3, B4, B5, B6, B7, B8)

    return valeur


if __name__ == "__main__":

    # M : Message and K : Key
    M = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', 'A', 'B', 'C', 'D', 'E', 'F']
    K = ['01', '03', '03', '04', '05', '07', '07', '09', '09', 'B', 'B', 'C', 'D', 'F', 'F', '1']

    # Convert M and K to binary
    M_Bin = []
    K_Bin = []
    MArray = ""

    N_BITS = 16

    for i in range(0, N_BITS):
        M_Bin.append(bin(int(M[i], N_BITS))[2:].zfill(4))
        MArray = MArray + M_Bin[i]

    tab = ""
    for i in range(0, N_BITS):
        K_Bin.append(bin(int(K[i], N_BITS))[2:].zfill(4))
        tab = tab + K_Bin[i]

    print(bcolors.WARNING + "\nStep 1: Create 16 subkeys, each of which is 48-bits long"+bcolors.ENDC)
    print("K Hexa:\t\t", K)
    print("K Binary:\t", K_Bin)
    print("M Hexa:\t\t", M)
    print("M Binary:\t", M_Bin)

    PC1 = [57, 49, 41, 33, 25, 17, 9, 1,
           58, 50, 42, 34, 26, 18, 10, 2,
           59, 51, 43, 35, 27, 19, 11, 3,
           60, 52, 44, 36, 63, 55, 47, 39,
           31, 23, 15, 7, 62, 54, 46, 38,
           30, 22, 14, 6, 61, 53, 45, 37,
           29, 21, 13, 5, 28, 20, 12, 4]

    KPlus = []
    count = 0
    print("PC1: \t\t", PC1)
    for i in PC1:
        KPlus.append(tab[i - 1])
        count += 1

    print(bcolors.WARNING + "\nFrom the original 64-bit key we get the 56-bit permutation :"+bcolors.ENDC)
    print("K+:\t\t\t", end='')
    for element in KPlus:
        print(element, end='')
    print("\n")

    C = []
    D = []
    Shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 1]

    print(bcolors.WARNING + "Split this key into left and right halves, C0 and D0, where each half has 28 bits. \n"
          "The we create sixteen blocks Cn and Dn, 1<=n<=16. \n"
          "\n"
          "Each pair of blocks Cn and Dn is formed from the previous pair Cn-1 and Dn-1, \n"
          "respectively, for n = 1, 2, ..., 16, using the following schedule of \"left shifts\"\n"
          "of the previous block. To do a left shift, move each bit one place to the left,\n"
          "except for the first bit, which is cycled to the end of the block \n"+bcolors.ENDC)
    # BOUCLE DE C
    for i in range(0, 17):
        C.append(KPlus[0:28])

        # Le premiere boucle sert à faire le nombre de shift vers la gauche
        # La deuxième sert a shifter de 0 à 27
        for k in range(0, Shifts[i]):
            temp = KPlus[0]
            for j in range(0, 27):
                KPlus[j] = KPlus[j + 1]
            KPlus[27] = temp

    # BOUCLE DE D
    for i in range(0, 17):
        D.append(KPlus[28:56])

        # Le premiere boucle sert à faire le nombre de shift vers la gauche
        # La deuxième sert a shifter de 0 à 27
        for k in range(0, Shifts[i]):
            temp = KPlus[28]
            for j in range(28, 55):
                KPlus[j] = KPlus[j + 1]
            KPlus[55] = temp

    # AFFICHAGE EN CONSOLE
    for i in range(0, 17):
        print("C[", i, "]: \t", end='')
        print("[", end='')
        for element in C[i]:
            print(element, end='')
        print("]")

    # AFFICHAGE EN CONSOLE
    for i in range(0, 17):
        print("D[", i, "]: \t", end='')
        print("[", end='')
        for element in D[i]:
            print(element, end='')
        print("]")

    print(bcolors.WARNING + "\nWe now form the keys Kn, for 1<=n<=16, by applying the following permutation \n"
          "table to each of the concatenated pairs CnDn. Each pair has 56 bits, but PC-2 \n"
          "only uses 48 of these. \n"+bcolors.ENDC)
    PC2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47,
           55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

    print("PC2: ")
    for i in range(0, 48, 8):
        print('\t'.join(str(j) for j in PC2[i:i+8]))

    print(bcolors.WARNING + "\nTherefore, the first bit of Kn is the 14th bit of CnDn, the second bit the 17th,\n"
          "and so on, ending with the 48th bit of Kn being the 32th bit of CnDn.\n"+bcolors.ENDC)

    count = 0
    K = []

    for j in range(1, 17):
        tempArray = []
        temp = C[j] + D[j]
        for i in PC2:
            tempArray.append(temp[i - 1])
        count += 1
        K.append(tempArray)

    for i in range(0, 16):
        print("K[", i + 1, "]: \t", end='')
        print("[", end='')
        for element in K[i]:
            print(element, end='')
        print("]")

    print(bcolors.OKGREEN + "\n\nStep 2: Encode each 64-bit block of data.\n\n"+bcolors.ENDC)

    IP_Tab = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

    print("IP: ")
    for i in range(0, 64, 8):
        print('\t'.join(str(j) for j in IP_Tab[i:i+8]))

    IP = []
    R = []
    L = []

    for i in IP_Tab:
        IP.append(MArray[i - 1])
        count += 1

    print("\nIP: ")
    for i in range(0, 64, 8):
        print(''.join(str(j) for j in IP[i:i+8]))


    L.append(IP[0:32])
    R.append(IP[32:64])

    print(bcolors.OKGREEN +"\nThe Feistel (F) function\n"+bcolors.ENDC)

    # Le premiere boucle sert à faire le nombre de shift vers la gauche
    # La deuxième sert a shifter de 0 à 27
    for k in range(1, 17):
        L.append(R[k - 1])

        f_calculee = f(R[k - 1], K[k - 1])
        LMoinsUn = L[k - 1]

        print("F(R[", k - 1, "], K[", k - 1, "]:\t\t", end='')
        print("[", end='')
        for element in f_calculee:
            print(element, end='')
        print("]")

        print("L[", k - 1, "]:\t\t\t\t\t", end='')
        print("[", end='')
        for element in LMoinsUn:
            print(element, end='')
        print("]")

        f_resultat = []

        for i in range(0, 32):
            f_resultat.append(int(LMoinsUn[i]) ^ int(f_calculee[i]))

        print("R[", k, "]:\t\t\t\t\t", end='')
        print("[", end='')
        for element in f_resultat:
            print(element, end='')
        print("]\n")

        R.append(f_resultat)

    IP_1 = [40, 8, 48, 16, 56, 24, 64, 32,
            39, 7, 47, 15, 55, 23, 63, 31,
            38, 6, 46, 14, 54, 22, 62, 30,
            37, 5, 45, 13, 53, 21, 61, 29,
            36, 4, 44, 12, 52, 20, 60, 28,
            35, 3, 43, 11, 51, 19, 59, 27,
            34, 2, 42, 10, 50, 18, 58, 26,
            33, 1, 41, 9, 49, 17, 57, 25]

    R16L16 = np.concatenate((R.pop(), L.pop()))

    FINAL = []
    for i in range(0, 64):
        FINAL.append(R16L16[IP_1[i]-1])

    concat = ""
    for i in range(0, 64):
        concat = concat + str(FINAL[i])

    print(bcolors.OKBLUE + "Result:", hex(int(concat, 2))+bcolors.ENDC)