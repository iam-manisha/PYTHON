num = 19

while num > 9:
    total = 0

    while num > 0:
        rem = num % 10
        total += rem ** 2
        num //= 10

    num = total

if num == 1 or num == 7:
    print("happy number")
else:
    print("not happy number")