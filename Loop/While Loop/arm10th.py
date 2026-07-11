num = 1
count = 0
inp = 10

while True:
    dup = num
    digits = len(str(num))
    res = 0

    while num > 0:
        rem = num % 10
        res = res + rem ** digits
        num = num // 10

    if dup == res:
        count += 1

        if count == inp:
            print(dup)
            break

    num = dup
    num += 1