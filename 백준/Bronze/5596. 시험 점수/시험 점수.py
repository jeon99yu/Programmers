min = list(map(int, input().split()))
man = list(map(int, input().split()))

a = sum(min)
b = sum(man)

if a == b:
    print(a)
elif a > b:
    print(a)
else:
    print(b)