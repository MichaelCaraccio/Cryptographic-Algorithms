#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Classe permettant le chiffrement selon l'algo. DES

@author: mathieu.rosser
'''

class DES():

    def __init__(self, message, cle):
        # entrées
        self.message = DES.versBinaire(message, 64)
        self.K = DES.versBinaire(cle, 64)
                
        # génération des clés
        self.creerKprime()
        self.creerCnDn()
        self.creerKn()
        
        # encodage des blocs
        self.creerIPL0R0()
        self.iterationsLnRn()
        self.creerCrytpogrammeIP1()
        # sortie accessible par getCryptogramme()
                    
    def creerKprime(self):
        self.Kprime = list()
        # permutations selon table
        for i in DES.TABLE_PC1:     
            self.Kprime.append(self.K[i - 1])   
            
    def creerCnDn(self):
        self.Cn = list()
        self.Dn = list()
        # on coupe en 2
        self.Cn.append(self.Kprime[0:28])
        self.Dn.append(self.Kprime[28:56])
        # calcul par décalage à gauche des autres CnDn
        for i in range(17): 
            self.Cn.append(DES.decalageAGauche(self.Cn[i], DES.TABLE_SHIFTLEFT[i]))
            self.Dn.append(DES.decalageAGauche(self.Dn[i], DES.TABLE_SHIFTLEFT[i]))
    
    def creerKn(self):
        self.Kn = list()
        # création des clés par concaténation et permutation selon table
        for i in range(1, 17):
            CnDn = self.Cn[i] + self.Dn[i]
            Ki = [CnDn[i - 1] for i in DES.TABLE_PC2]
            self.Kn.append(Ki)
    
    def creerIPL0R0(self):
        self.IP = list()
        # permutation du message
        for i in DES.TABLE_IP:
            self.IP.append(self.message[i - 1])
                
        self.Ln = list()
        self.Rn = list()
        # découpage en L0 et R0
        self.Ln.append(self.IP[0:32])
        self.Rn.append(self.IP[32:64])
    
    def iterationsLnRn(self):
        # création des LnRn selon formule
        for i in range(1, 17):
            self.Ln.append(list(self.Rn[i - 1]))
            self.Rn.append(DES.xor(self.Ln[i - 1], self.f(self.Rn[i - 1], self.Kn[i - 1]))) # XOR entre 2 listes
        
    def f(self, RnMinus1, Kn):
        # permutation table E
        E = [RnMinus1[i - 1] for i in DES.TABLE_E]
        # XOR entre les 2 listes
        KnPlusE = DES.xor(E, Kn)
        # passe de 8*6 bits à 8*4 bits
        S = self.appliquerSBox(KnPlusE)
        
        # permutation avec la table P
        P = [S[i - 1] for i in DES.TABLE_P]
        return P
    
    def appliquerSBox(self, KnPlusE):
        S = ''
        
        for i in range(0, 48, 6):
            # récupère le bloc courant
            Bi = KnPlusE[i:i + 6]
            
            # calculs des numéros ligne/colonne
            noLigne = int(Bi[0] + Bi[5], 2)
            noColonne = int(''.join(Bi[1:5]), 2)
            
            # accède à la table des sbox selon ligne/colonne
            indiceTable = noLigne * 16 + noColonne
            valeurTable = DES.TABLE_SBOX[int(i / 6)][indiceTable]
            
            # mise à jour de S avec les 4 nouveaux bits
            S += ''.join(DES.versBinaire(valeurTable, 4))
                        
        return list(S)

    def creerCrytpogrammeIP1(self):
        # création du cryptogramme avec R16 et L16 & permutations IP inverse
        R16L16 = self.Rn[16] + self.Ln[16]
        cryptogramme = [R16L16[i - 1] for i in DES.TABLE_IP1]
        # stockage sous forme d'entier
        self.cryptogramme = int(''.join(cryptogramme), 2)
        
    def getCryptogramme(self):
        return self.cryptogramme
        
    @staticmethod
    def xor(list1, list2):
        # XOR bit à bit sur 2 listes de bits stockés sous forme de caractère
        result = list()
        for bit1, bit2 in zip(list1, list2):
            if (bit1, bit2) == ('1', '1') or (bit1, bit2) == ('0', '0'):
                result.append('0')
            else:
                result.append('1')
                
        return result
        
    @staticmethod
    def decalageAGauche(binaire, nbDecalage):
        # décalage cyclique à gauche dans une liste: on prend le + à gauche, on le met à droite
        binaireDecalage = list(binaire)
        
        for i in range(nbDecalage):
            gauche = binaireDecalage.pop(0)
            binaireDecalage.append(gauche)
            
        return binaireDecalage

    @staticmethod
    def versBinaire(valeur, longueur):
        # conversion en binaire sous forme de chaîne de caractères, complétée à gauche par des 0
        binaire = bin(valeur).lstrip('0b')
        binaire = list(binaire)
        
        while len(binaire) < longueur:
            binaire.insert(0, '0')
            
        return binaire

    # table spécifiant le nb de décalage à gauche pour les CnDn
    TABLE_SHIFTLEFT = [
        1, 1, 2, 2, 2,
        2, 2, 2, 1, 2, 2,
        2, 2, 2, 2, 1, 0  # ajout 0 final
    ]

    # tables de permutations : l'élément i est remplacé par celui spécifié à l'indice i de la table
    TABLE_PC1 = [
        57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4,
    ]
    
    TABLE_PC2 = [
        14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32,
    ]
    
    TABLE_IP = [
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7,
    ]
    
    TABLE_E = [
        32, 1, 2, 3, 4, 5,
        4, 5, 6, 7, 8, 9,
        8, 9, 10, 11, 12, 13,
        12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21,
        20, 21, 22, 23, 24, 25,
        24, 25, 26, 27, 28, 29,
        28, 29, 30, 31, 32, 1,
    ]
        
    TABLE_P = [
        16, 7, 20, 21,
        29, 12, 28, 17,
        1, 15, 23, 26,
        5, 18, 31, 10,
        2, 8, 24, 14,
        32, 27, 3, 9,
        19, 13, 30, 6,
        22, 11, 4, 25,
    ]
    
    TABLE_IP1 = [
        40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25,
    ]
    
    # fonctions S-Box de S1 à S8, au format 4 lignes [0-3] & 16 colonnes [0-15]
    TABLE_SBOX = [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
         0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
         4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
         15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
                  
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
        3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
        0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
        13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
                  
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
        13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
        13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
        1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
                  
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
        13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
        10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
        3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
                  
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
        14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
        4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
        11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
                  
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
        10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
        9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
        4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
                   
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
        13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
        1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
        6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
                  
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
        1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
        7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
        2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
    ]
        
if __name__ == '__main__':
    # test de chiffrement avec l'exemple du cours
    message = 0x0123456789ABCDEF
    cle = 0x133457799BBCDFF1
    
    des = DES(message, cle)
    
    print("Chiffrement DES par mathieu.rosser")
    print("Message: " + hex(message))
    print("Clé: " + hex(cle))
    print("Cryptogramme: " + hex(des.getCryptogramme()))
    
    
