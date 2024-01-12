n = int(input())

sc1 = 100
sc2 = 100

for i in range(n):
    a,b = map(int,input().split())
    
    if a == b:
        continue
    elif a > b:
        sc2 -= a
    else:
        sc1 -= b

print(sc1,sc2,sep='\n')
