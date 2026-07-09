for num in range (1,1001):
    dup = num
    digit = len(str(num))
    res = 0
    while num > 0:
        rem = num % 10
        res = res + rem ** digit
        num = num // 10
    if res == dup:
        print(res)