import math

n = int(input())
m = int(input())

count = []

for i in range(n,m+1):
    if int(math.sqrt(i)) ** 2 == i :
        count.append(i)
        
if count:
    print(sum(count))
    print(min(count))
else :
  print(-1)

    