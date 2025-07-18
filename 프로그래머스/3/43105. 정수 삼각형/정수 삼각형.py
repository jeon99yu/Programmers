def solution(triangle):
    depth = len(triangle)
    
    for i in range(1, depth):
        for j in range(i+1):
            if j == 0:  # 맨 왼쪽
                triangle[i][j] += triangle[i-1][j]
            elif j == i:  # 맨 오른쪽
                triangle[i][j] += triangle[i-1][j-1]
            else:  
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
    
    return max(triangle[-1])  


