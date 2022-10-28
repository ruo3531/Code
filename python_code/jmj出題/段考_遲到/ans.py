
h = int(input())
m = int(input())
T=h*60+m
t = int (input())
T-=t
H=T//60
M=T%60
print(H, M)
