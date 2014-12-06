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
        ''' cryptage selon Vernam en binaire '''
        with open(fichier, 'rb') as file:
            tabBytes = file.read()
            # génération de la clé, sous forme de bytes, selon la longueur du tableau de bytes
            cle = [random.randint(0, 255) for _ in range(len(tabBytes))]
            # génération du cryptogramme
            cryptogramme = [byte ^ k for byte, k in zip(tabBytes, cle)]
            # écriture du fichier crypté
            self.ecrireFichier(cryptogramme, nomSortie)
            # cryptage symétrique, la clé est nécessaire pour décrypter
            return cle
        
    def decrypter(self, fichier, cle, nomSortie):
        ''' décryptage avec la clé selon Vernam en binaire '''
        with open(fichier, 'rb') as file:            
            tabBytes = file.read()
            # génération du message
            message = [byte ^ k for byte, k in zip(tabBytes, cle)]
            # écriture du fichier décrypté
            self.ecrireFichier(message, nomSortie)
        
    def ecrireFichier(self, donnees, nomSortie):
        ''' sortie d'un fichier en binaire '''
        with open(nomSortie, 'wb') as file:
            file.write(bytes(donnees))

if __name__ == '__main__':
    vernam = Vernam()
    
    fichier = "test.html"
    sortieCrypt = fichier + ".vernam"
    sortieDecrypt = "decrypt." + fichier
    
    cle = vernam.crypter(fichier, sortieCrypt)
            
    vernam.decrypter(sortieCrypt, cle, sortieDecrypt)
     
    