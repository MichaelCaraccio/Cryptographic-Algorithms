#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 24 sept. 2014

@author: mathieu.rosser
'''

class RC4():
    
    def __init__(self, base):
        self.base = base if base in (8, 16) else 16
        self.convert = oct if base == 8 else hex
        self.symboleBase = '0o' if base == 8 else '0x'
        
    def declareST(self):
        self.S = list(range(self.base))
        self.T = list()
        
        longueurCle = len(self.cle)
        for i in range(self.base):
            self.T.append(int(self.cle[i % longueurCle], self.base)) # conversion base vers numérique
            
    def initS(self):
        j = 0
        for i in range(self.base):
            j = (j + self.S[i] + self.T[i]) % self.base
            self.S[i], self.S[j] = self.S[j], self.S[i]
                
    def creerCryptogramme(self):
        nouvelleCle = list()
        messageCrypte = list()
        
        a = i = j = 0
        longueurMessage = len(self.message)
        while a < longueurMessage:
            i = (i + 1) % self.base
            j = (j + self.S[i]) % self.base
            
            self.S[i], self.S[j] = self.S[j], self.S[i]
            
            t = (self.S[i] + self.S[j]) % self.base
            caseCle = self.S[t]
            
            nouvelleCle.append(self.convert(caseCle).split(self.symboleBase).pop())
            messageCrypte.append(self.convert(int(self.message[a], self.base) ^ caseCle).split(self.symboleBase).pop()) # XOR
            
            a += 1   
            
        return (''.join(messageCrypte).upper(), ''.join(nouvelleCle).upper())
        
    def crypter(self, message, cle):
        self.cle = cle
        self.message = message
        
        self.declareST()
        
        self.initS()
        
        return self.creerCryptogramme()

if __name__ == '__main__':
    print("Message à envoyer: ", end="")
    message = input()
    
    print("Clé de cryptage: ", end="")
    cle = input()
    
    print("Base: ", end="")
    base = int(input())
    
    RC4 = RC4(base)
    messageCrypte, clefModifiee = RC4.crypter(message, cle)
    print("Message crypté: %s\nClé de cryptage: %s" % (messageCrypte, clefModifiee))
    
    
    