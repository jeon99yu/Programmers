mo = ['a', 'e', 'i', 'o', 'u', 'A','E','I','O','U']

while True:
    what = input()
    c = 0
    
    if what == '#':
        break
    
    for i in what:
        if i in mo:
            c += 1
    print(c)
