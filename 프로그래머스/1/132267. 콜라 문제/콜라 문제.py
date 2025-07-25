def solution(a, b, n):
    cola = 0
    
    while n >= a:
        new = (n // a) * b  
        cola += new
        n = new + (n % a)   
    return cola