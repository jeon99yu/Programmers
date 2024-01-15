l,p = map(int,input().split())
s = list(map(int,input().split()))
lp = l*p

for v in s:
    print(v-lp, end=' ')