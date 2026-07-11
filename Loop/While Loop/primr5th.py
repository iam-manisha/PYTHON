num = 1
count = 0
inp = 5

while True:

    if num > 1:

        for i in range(2, int(num ** 0.5) + 1):

            if num % i == 0:
                break

        else:
            count += 1

            if count == inp:
                print(num)
                break

    num += 1