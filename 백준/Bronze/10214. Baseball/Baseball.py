ining = int(input())

for _ in range(ining):
    yon = 0
    kor = 0
    
    for i in range(9):
        y,k = map(int,input().split())
        yon+=y
        kor+=k
    
    if yon > kor:
        print('Yonsei')
    elif yon < kor:
        print('Korea')
    else:
        print('Draw')
        
    