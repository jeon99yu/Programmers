exam = int(input())
sub = list(map(int,input().split()))

maxsub=max(sub)
sejun = 0

for i in range(exam):
    new = (sub[i]/maxsub)*100
    sejun += new

average = sejun / exam
print(average)