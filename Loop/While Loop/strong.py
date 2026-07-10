num = 145
sum = 0
dup = num

while num > 0:
    rem = num % 10
    fact = 1

    for val in range(1, rem + 1):
        fact *= val

    sum += fact
    num //= 10

if dup == sum:
    print(f"{dup} is a strong number")
else:
    print(f"{dup} is not a strong number")