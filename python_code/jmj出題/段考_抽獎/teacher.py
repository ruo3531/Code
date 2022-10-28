
import random
for i in range(0,10):
   fin = open('{}.in'.format(i), 'w')
   fout = open('{}.out'.format(i), 'w', encoding='utf-8')
   n = random.randint(10,40)
   L = set()
   for _ in range(n):
       r = random.randint(0, 100)
       while r in L:
           r = random.randint(0, 100)
       L.add(r)
   L = list(L)
   print(n, *L, sep='\n', file=fin)
   #print(*L, sep='\n')
   for _ in range(5):
       r = random.randint(0, 100)
       while r in L:
           r = random.randint(0, 100)
       L.append(r)
   f = random.choice(L)
   print(f, file=fin)
   op=0
   for j in range(n):
       if L[j] == f : 
           s = j+1
           op = 1
   if op == 0 : s = -1
   #print(L)
   print(n, f, s)
   print(s, file=fout)
   fin.close()
   fout.close()