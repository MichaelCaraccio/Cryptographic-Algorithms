"""
Diffie-Hellman

Auteur : Jules Laville

Version avec deux personnes
"""

def modular_pow(a, exp, n):
    c = 1
    a = a % n
    while exp > 0:
        if exp % 2 == 1:
           c = (c * a) % n
        exp >>= 1
        a = (a * a) % n
    return c


class diffeHellman:
    def __init__(self, p, g ,a):
        self.__p = p
        self.__g = g
        self.__a = a
        self.__A = modular_pow(self.__g, self.__a, self.__p)
        self.__s =  self.__B = self.__opti = None

    def encrypte(self, m):
        return modular_pow(m * self.__s, 1, self.__p)

    def decrypte(self, e):
        return (e * self.__opti) % self.__p

    def getA(self):
        return self.__A

    def setB(self, B):
        self.__B = B
        self.__s = modular_pow(B, self.__a, self.__p)
        self.__opti = modular_pow(self.__B, self.__p - 1 - self.__a, self.__p)
        print("s = %d" % self.__s)

    @staticmethod
    def echange(a, b):
        a.setB(b.getA())
        b.setB(a.getA())


if __name__ == "__main__":
    alice = diffeHellman(2038074743, 97, 472882027)
    bob = diffeHellman(2038074743, 97, 160481183)

    diffeHellman.echange(alice, bob)

    m = 1246809753
    e1 = bob.encrypte(m)
    m1 = alice.decrypte(e1)

    e2 = bob.encrypte(m)
    m2 = alice.decrypte(e2)

    print("e1 = %d" % e1)
    print("e2 = %d" % e2)
    print("m0 = %d" % m)
    print("m1 = %d" % m1)
    print("m2 = %d" % m2)