ns = []

for _ in range(10):
    n = int(input())
    a = n % 42
    ns.append(a)
    
ns = set(ns)

print(len(ns))