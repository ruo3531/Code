r, c, K, m = map(int,input().split())
imove = [-1,0,1,0]
jmove = [0,1,0,-1]
arr = [[-1]*(c+2)] + [[-1]+[int(j) for j in input().split()]+[-1]for i in range(r)] + [[-1]*(c+2)]
Next = [[0 for j in range(c+2)] for i in range(r+2)]
for _ in range(m) :
    for i in range(r+2) :
        for j in range(c+2) :
            Next[i][j] = arr[i][j]
    for i in range(r+2) :
        for j in range(c+2) :
            if arr[i][j] != -1 :
                sum = 0
                for k in range(4) :
                    if Next[i+imove[k]][j+jmove[k]] !=-1 :
                        t = arr[i][j] // K
                        Next[i+imove[k]][j+jmove[k]] += t
                        sum += t
                Next[i][j] -= sum
    for i in range(r+2) :
        for j in range(c+2) :
            arr[i][j] = Next[i][j]
Max = []
Min = 99999
for i in range(r+2) :
    Max.append(max(arr[i]))
    for j in range(1,c+1) :
        if arr[i][j] <= Min and arr[i][j] != -1 :
            Min = arr[i][j]     
print(Min)
print(max(Max))