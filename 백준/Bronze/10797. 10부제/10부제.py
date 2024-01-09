date_digit = int(input())
car_digits = list(map(int, input().split()))

violating_cars = 0

for car_digit in car_digits:
    if (date_digit == car_digit) or (date_digit == 0 and car_digit == 10):
        violating_cars += 1

print(violating_cars)