#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 8 nov. 2014

@author: mathieu.rosser
'''

def pgcd(a, b):
    """ Algorithme d'Euclide pour trouver le PGCD 
        assertion: A > B """
    r0 = abs(a)
    r1 = abs(b)
    
    while r1 > 0:
        r = r0 % r1
        r0 = r1
        r1 = r
        
    return r0

def pgcdRecursive(a, b):
    """ Algorithme d'Euclide récursif pour trouver le PGCD 
        assertion: A > B """
    if b == 0:
        return a
    else:
        return pgcdRecursive(b, a % b)

def euclideEtendu(bNombre, aModulo):
    """ Algorithme d'Euclide étendu, permettant de connaître:
        PGCD
        Coefficients de Bézout (u, v)
        Inverse modulaire de B modulo A ---> B * B^-1 mod A = 1 
        """
    modulo = aModulo
    
    x = 0
    y = 1
    u = 1
    v = 0
    
    while bNombre != 0:
        q = aModulo // bNombre
        r = aModulo % bNombre
        
        m = x - u * q
        n = y - v * q
        
        aModulo = bNombre
        bNombre = r
        x = u
        y = v
        u = m
        v = n
    
    ' retourne (pgcd, u, v, inverse modulaire '
    return (aModulo, x, y, x % modulo)

def inverseModulaire(aModulo, bNombre):
    """ Algorithme d'Euclide étendu pour trouver l'inverse modulaire 
        Inverse modulaire de B modulo A ---> B * B^-1 mod A = 1 """
    
    modulo = aModulo
    
    x = 0
    y = 1
    u = 1
    v = 0
    
    while bNombre != 0:
        q = aModulo // bNombre
        r = aModulo % bNombre
        
        m = x - u * q
        n = y - v * q
        
        aModulo = bNombre
        bNombre = r
        x = u
        y = v
        u = m
        v = n
        
    return x % modulo if aModulo == 1 else 0

if __name__ == '__main__':
    
    """ PGCD - Algorithme d'Euclide """
    
    pgcd1 = pgcd(325, 145)
    pgcd2 = pgcdRecursive(325, 145)
    
    print("PGCD(325, 145) = %d (itératif) et %d (récursif)" % (pgcd1, pgcd2))

    pgcd1 = pgcd(542284229916, 231414210846)
    print("PGCD(542284229916, 231414210846) = %d " % pgcd1)
    
    pgcd1 = pgcd(6289078768087500, 223092870)
    print("PGCD(6289078768087500, 223092870) = %d " % pgcd1)
    
    pgcd1 = pgcd(86822723, 7436429)
    print("PGCD(86822723, 7436429) = %d " % pgcd1)
    
    print()
    
    """ Algorithme d'Euclide Etendu, Coefficient de Bézout et inverse modulaire """
        
    pgcd1, u, v, inverseMod = euclideEtendu(542284229916, 231414210846)
    print("a = %d, b = %d : u = %d, v = %d, pgcd = %d" %(542284229916, 231414210846, u, v, pgcd1))

    pgcd1, u, v, inverseMod = euclideEtendu(6289078768087500, 223092870)
    print("a = %d, b = %d : u = %d, v = %d, pgcd = %d" %(6289078768087500, 223092870, u, v, pgcd1))

    pgcd1, u, v, inverseMod = euclideEtendu(86822723, 7436429)
    print("a = %d, b = %d : u = %d, v = %d, pgcd = %d" %(86822723, 7436429, u, v, pgcd1))

    inverse = inverseModulaire(108, 37)
    print("Inverse modulaire de %d modulo %d = %d" % (37, 108, inverse))

    inverse = inverseModulaire(10, 57)
    print("Inverse modulaire de %d modulo %d = %d" % (57, 10, inverse))

    inverse = inverseModulaire(20, 57)
    print("Inverse modulaire de %d modulo %d = %d" % (57, 20, inverse))

    inverse = inverseModulaire(30, 57)
    print("Inverse modulaire de %d modulo %d = %d" % (57, 30, inverse))

    inverse = inverseModulaire(47, 57)
    print("Inverse modulaire de %d modulo %d = %d" % (57, 47, inverse))

    inverse = inverseModulaire(231414210847, 542284229916)
    print("Inverse modulaire de %d modulo %d = %d" % (542284229916, 231414210847, inverse))

    inverse = inverseModulaire(19394489, 1234567)
    print("Inverse modulaire de %d modulo %d = %d" % (1234567, 19394489, inverse))

    inverse = inverseModulaire(22801763489, 15485863)
    print("Inverse modulaire de %d modulo %d = %d" % (15485863, 22801763489, inverse))

