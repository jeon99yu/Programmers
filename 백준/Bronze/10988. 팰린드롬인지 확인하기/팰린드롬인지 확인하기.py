alpha = input()
new = alpha.lower()

if new == new[::-1]:
    print(1)
else:
    print(0)