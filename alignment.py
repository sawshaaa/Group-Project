#import file
lista = []
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
    if lista[z][12:15] == lista[z+1][1:4]:
       print lista[z+1]
#    if x in z:
#      print z
