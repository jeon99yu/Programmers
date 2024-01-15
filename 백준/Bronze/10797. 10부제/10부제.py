d = int(input())
cars = list(map(int,input().split()))
count = 0

for car in cars:
    if d == car:
        count+=1
print(count)