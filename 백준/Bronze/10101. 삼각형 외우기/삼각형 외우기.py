first = int(input())
second = int(input())
third = int(input())

if first == second == third == 60:
    print('Equilateral')
elif first + second + third == 180:
    if first == second or second == third or first == third:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')