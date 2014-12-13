__author__ = 'michaelcaraccio'
import operator

# EXEMPLE DU PROF
k = ['01','02','03','06']
p = ['01','02','02','02']
s = ['00','01','02','03','04','05','06','07']
t = ['01','02','03','06','01','02','03','06']

# EXERCICE 2
#k = ['F', '1', 'A', '8', '2', 'B', '0', '3']
#p = ['B', 'A', 'F', 'E', 'C', 'D', '2', '5']
#s = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15']
#t = ['F', '1', 'A', '8', '2', 'B', '0', '3', 'F', '1', 'A', '8', '2', 'B', '0', '3']

print("\nClé K     : ", k, end='')
print("\nMessage P : ", p, end='')
print("\nInit S    : ", s, end='')
print("\nInit T    : ", t, end='\n')

# Si exercice du prof, alors mettre N_BITS = 8
N_BITS = 8

# ***********************************
# ETAPE 1
# ***********************************

j = 0
for i in range(0, N_BITS):
    j = (int(str(j), N_BITS) + int(s[i], N_BITS) + int(t[i], N_BITS)) % N_BITS
    s[i], s[j] = s[j], s[i]

# ***********************************
# ETAPE 2
# ***********************************

i = j = a = 0

scale = 16
num_of_bits = N_BITS

while a < (N_BITS / 2):
    i = (i + 1) % N_BITS
    j = (int(str(j), 16) + int(s[i], 16)) % N_BITS
    s[i], s[j] = s[j], s[i]

    t = (int(str(s[i]), 16) + int(str(s[j]), 16)) % N_BITS
    k[a] = s[t]

    conv1 = bin(int(p[a], scale))[2:].zfill(8)
    conv2 = bin(int(k[a], scale))[2:].zfill(8)

    #print("P:", conv1, "(", int(conv1, 2), ")", "K:", conv2, "(", int(conv1, 2), ")", "    XOR: ", operator.xor(int(conv1, 2), int(conv2, 2)))

    conv1 = int(conv1, 2)
    conv2 = int(conv2, 2)

    p[a] = operator.xor(int(conv1), int(conv2))
    a += 1

print("\nClé finale : K : ", k, end='')
print("\nCypher Text: C : ", p, end='\n')