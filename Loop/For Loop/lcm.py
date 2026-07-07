num1 = 4
num2 = 10

high = max(num1, num2)
product = num1 * num2

for lcm in range(high, product + 1):

    if lcm % num1 == 0 and lcm % num2 == 0:
        print(lcm)
        break