def solution(dots):
    for a, b, c, d in [(0,1,2,3), (0,2,1,3), (0,3,1,2)]:
        (x1, y1), (x2, y2) = dots[a], dots[b]
        (x3, y3), (x4, y4) = dots[c], dots[d]
        
        if (y2 - y1) * (x4 - x3) == (y4 - y3) * (x2 - x1):
            return 1
    return 0
