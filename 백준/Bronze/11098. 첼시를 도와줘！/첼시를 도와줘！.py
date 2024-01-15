n = int(input())


for i in range(n):
    p = int(input()) 
    price = []
    name = []  
    
    for j in range(p):
       
        t,s = map(str,input().split())
        t = int(t)
        
        price.append(t)
        name.append(s)
        
        re1 = price.index(max(price))
    print(name[re1])    