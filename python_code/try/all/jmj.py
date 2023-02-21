n = int(input())
m = int(input())
x = max(n,m)
for i in range(2,x):
        while(n%i==0 and m%i==0):
            n=n//i
            m=m//i
print(n,'/',m,sep=' ')