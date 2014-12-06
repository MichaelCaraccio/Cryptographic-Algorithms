#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 8 oct. 2014

@author: mathieu.rosser
'''

import random

class Vernam():

    def __init__(self):
        pass
    
    def crypter(self, fichier, nomSortie):
        with open(fichier, 'r', encoding='latin1') as file:
            
            message = ""
            
            carac = file.read(1)
            while carac != "":
                val = ord(carac)
                
                message += Vernam.versBinaire(val, 8)
                
                carac = file.read(1)
                            
            cle = Vernam.chaineAleatoireBinaire(len(message))
            cryptogramme = ''.join(Vernam.xor(message, cle))
                        
            Vernam.ecrireFichier(cryptogramme, nomSortie)

            return cle
            
    def decrypter(self, fichier, cle, nomSortie):
        with open(fichier, 'r', encoding='latin1') as file:            
            binaire = ""
            
            carac = file.read(1)
            while carac != '':
                binaire += Vernam.versBinaire(ord(carac), 8)
                carac = file.read(1)
                
            message = ''.join(Vernam.xor(binaire, cle))
            
            Vernam.ecrireFichier(message, nomSortie)
    
    @staticmethod
    def ecrireFichier(donnees, nomSortie):
        sortie = ""
        for i in range(0, len(donnees), 8):
            byte = donnees[i:i+8]
            sortie += chr(int(byte, 2))
        
        fileSortie = open(nomSortie, 'w', encoding='latin1')
        fileSortie.write(sortie)
        fileSortie.close()
        
    @staticmethod
    def chaineAleatoireBinaire(longueur):
        chaine = ""
        bit = ('0', '1')
        
        for _ in range(longueur):
            chaine += random.choice(bit)
        
        return chaine
         
    @staticmethod
    def versBinaire(valeur, longueur):
        # conversion en binaire sous forme de chaîne de caractères, complétée à gauche par des 0
        binaire = bin(valeur).lstrip('0b')
        binaire = list(binaire)
        
        while len(binaire) < longueur:
            binaire.insert(0, '0')
            
        return ''.join(binaire)
        
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

if __name__ == '__main__':
    vernam = Vernam()
    
    fichier = "test.pdf"
    sortieCrypt = fichier + ".vernam"
    sortieDecrypt = "decrypt." + fichier
    
    cle = vernam.crypter(fichier, sortieCrypt)
            
    vernam.decrypter(sortieCrypt, cle, sortieDecrypt)
    
    