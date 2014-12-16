#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 12 nov. 2014

@author: mathieu.rosser
'''

from RSA_diffiehellman.exponentiation_modulaire import expModMethode2

def diffieHellman(m, p, g, a, b):
    A = expModMethode2(g, a, p)
    B = expModMethode2(g, b, p)
    
    S = expModMethode2(B, a, p)
    
    e = (m * S) % p
    
    d = (e * expModMethode2(A, p - 1 - b, p)) % p
    
    return e, d, S

if __name__ == '__main__':
    
    m = 1246809753
    p = 2038074743
    g = 97 
    a = 472882027 
    b = 160481183
    
    e, d, S = diffieHellman(m, p, g, a, b)
    
    print("M = %d / E = %d / D = %d / S = %d" %(m, e, d, S))
    
    