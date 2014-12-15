#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys

def initialize():
	j = 0
	for i in range(base):
		j = (j + S[i] + T[i]) % base
		S[i],S[j] = S[j],S[i]

def crypt():
	a = i = j = 0
	C = []

	while a < len(K):
		i = (i + 1) % base
		j = (j + S[i]) % base
		S[i], S[j] = S[j], S[i]
		t = (S[i] + S[j]) % base
		K[a] = S[t]
		C.append(K[a] ^ P[a])
		a += 1

	return C

usage = """rc4.py <K> <P> <base>
K and P are in hexadecimal """

if __name__ == "__main__":
	if len(sys.argv) < 4:
		print(usage)
		exit()
	base = int(sys.argv[3])
	K = []
	P = []
	S = []
	T = []

	#K = [int(x,16) for x in list(sys.argv[1])]
	try:
		K = [int(x,base) for x in list(sys.argv[1])]
		P = [int(x,base) for x in list(sys.argv[2])]
		# print(K)
		# print(P)

		S = [x for x in range(base)]
		T = [K[x % len(K)] for x in range(base)]
		# print(S)
		# print(T)
		
		initialize()
		print("S: %s" % S)
		C = crypt()

		print("Results:")
		print("C: %s" % C)
		print("K: %s" % K)

	except ValueError as e:
		print("Enter valid K and P")
		print(e)


