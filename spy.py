num = 256
sum_digits = 0
product_digits = 1

for digit in str(num):
    d = int(digit)
    sum_digits += d
    product_digits *= d

if sum_digits == product_digits:
    print(f"{num} is a spy number")
else:
    print(f"{num} is not a spy number")
