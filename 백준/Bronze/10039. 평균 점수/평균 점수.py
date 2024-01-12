won=int(input())
sae=int(input())
san=int(input())
son=int(input())
gan=int(input())

stu = [won,sae,san,son,gan]
    
for i in range(len(stu)):
    if stu[i] < 40:
        stu[i] = 40
    
avg = sum(stu) / 5
print(int(avg))