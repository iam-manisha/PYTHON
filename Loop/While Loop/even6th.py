num = 1
count = 0
inp = 6

while True:

    if num % 2 == 0:
        count += 1

        if count == inp:
            print(num)
            break

    num += 1