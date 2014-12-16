#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 12 nov. 2014

@author: mathieu.rosser
'''

from RSA_diffiehellman.euclide import inverseModulaire
from RSA_diffiehellman.exponentiation_modulaire import expModMethode2

def rsa(m, p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = 41161739  # e et phi premiers entre eux, e < phi
    
    d = inverseModulaire(phi, e)
    
    c = expModMethode2(m, e, n)
    
    mTilda = expModMethode2(c, d, n)
    
    return (c, mTilda, e, d)

if __name__ == '__main__':
    
    m = 21645
    p = 22433
    q = 17123
    
    c, mTilda, e, d = rsa(m, p, q)
    print("M = %d / C = %d / MTILDA = %d" % (m, c, mTilda))
    print("E = %d / D = %d" % (e, d))