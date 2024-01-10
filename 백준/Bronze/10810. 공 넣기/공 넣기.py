n,m = map(int,input().split())

baskets = [0] * n

for l in range(m):
    i,j,k = map(int,input().split())
    
    for x in range(i,j+1):
        baskets[x-1] = k

for x in range(n):
    print(baskets[x], end=' ')