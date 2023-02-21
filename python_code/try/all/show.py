'''平方&map(?????)
a = float(input())
b = float(input())
c = float(input())
#b = map(int, input().split())
s = (b ** 2)-4*a*c
ans = (-1*b+(s ** (0.5)))/(2*a)
ans1 = (-1*b-(s ** (0.5)))/(2*a)
print(ans, ans1, sep='\n')
'''

'''小數點後位數
x=1.23456
print(round(x,3))
'''

'''陣列中隨機不重複的數
import random
for i in range(0,10):
   fin = open('{}.in'.format(i), 'w')
   fout = open('{}.out'.format(i), 'w', encoding='utf-8')
   n = random.randint(30,40)
   L = []
   for _ in range(n):
       r = random.randint(0, 100)
       while r in L:
           r = random.randint(0, 100)
       L.append(r)
   j = random.randint(1,n)
   ans = len([s for s in L if s > L[j-1]])
   print(n, j, ans)
   print(L)
   print(n, *L, j, sep='\n', file=fin)
   print(ans+1, file=fout)
   fin.close()
   fout.close()
'''

'''list用法
arr = [random.randint(1, 100) for i in range(n)]   f = random.choice(arr)
a = list(map(int, input().split())) #輸入多個數字，以空格分開
a[1:5:2] #begin:end:間隔
num_list = [i for i in range(1, 11)]
num_list = [i for i in range(1, 11) if i % 2 == 0]
#資料組 = [自訂變數 for 自訂變數 in 資料組 if 關係運算式]
#二維陣列,橫排m直排n
test = [[0 for j in range(m)] for i in range(n)]
#輸入版
arr = []
for i in range(r) :
    arr.append([])
    arr[i] = [int(j) for j in input().split()]


'''
'''小技巧
a = b = c = 50
print(a,b,c)

a , b = 50 , 60
print(a,b)
a , b = b , a
print("After swapping",a,b)

#反轉
my_string = "MY STRING"
rev_string = my_string[::-1]
print(rev_string)

my_list = ['This' , 'is' , 'a' , 'string' , 'in' , 'Python']
my_string = " ".join(my_list)
#This is a string in Python

my_string = "This is a string in Python"
my_list = my_string.split(' ')
print(my_list)
#['This ', 'is ', 'a ', 'string ', 'in ', 'Python']

n = int(input("How many times you need to repeat:"))
my_string = "Python\n"
print(my_string*n)

'''
'''
try:
    while(True):
        b,p,m = map(int, input().split())
        print(pow(b, p, m))
except EOFError:
    pass
'''