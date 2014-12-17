#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 12 nov. 2014

@author: mathieu.rosser
'''

def expModMethode1(a, e, n):
    """ permet de calculer a^e mod n, méthode lente quand e grandit """
    c = 1
    for _ in range(0, e):
        c = (a * c) % n
        
    return c

def expModMethode2(a, e, n):
    """ permet de calculer a^e mod n, méthode beaucoup + rapide """
    c = 1
    a = a % n
    
    while e > 0:
        if (e % 2) == 1:
            c = (c * a) % n
            
        e = e >> 1
        a = (a * a) % n
        
    return c

if __name__ == '__main__':
    
    #a, e, n = 5317, 10000, 2119
    #expMod1 = expModMethode1(a, e, n)
    #expMod2 = expModMethode2(a, e, n)
    #print("%d^%d mod %d = %d / %d" %(a, e, n, expMod1, expMod2))
    #
    #a, e, n = 987654321, 123456789, 2038074743
    #expMod1 = expModMethode1(a, e, n)
    #expMod2 = expModMethode2(a, e, n)
    #print("%d^%d mod %d = %d / %d" %(a, e, n, expMod1, expMod2))
    #
    #a, e, n = 987654321, 1234567890000000000, 2038074743
    #expMod1 = 0 # expModMethode1(a, e, n)
    #expMod2 = expModMethode2(a, e, n)
    #print("%d^%d mod %d = %d / %d" %(a, e, n, expMod1, expMod2))
	
	a = int(input("a: "))
	e = int(input("e: "))
	n = int(input("n: "))
	expMod2 = expModMethode2(a, e, n)
	
	print("%d^%d mod %d = %d" % (a, e, n, expMod2))

