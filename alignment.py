#import file
lista = []
D = {}
X = {}
s = open("/share/data/day5/puzzle.txt")
lines = s.readlines()
for i in lines:
  m = i.split()
  lista = lista + m
#print lista[0][0:15]
stra = " ".join(lista)
#input the chunk you want to search for
#x = raw_input("enter chunk:  ")
for i in range(len(lines)):
  y = stra.split(",")
#  if x in lines[i]:
#    if x in y[i]:    
#   print lines[i][0:15]
for z in range(len(lista)-1):
    for zz in range(len(lista)-1):
        if lista[z][11:15] == lista[zz][0:4]:
            r = lista[z][0:11],
            t =  lista[zz]
            q = "".join(r)
            u = "".join(t)
            v = q + u
            D[v] = 1
        if lista[z][8:12] == lista[zz][8:12]:
            a = lista[z]
            b = lista[zz][13:15]
            c = "".join(a)
            d = "".join(b)
            e = c + d
            X[v] = 2
print D
#    if x in z:
#      print z
