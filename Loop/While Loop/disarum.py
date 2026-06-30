#DISARUM NUMBER:-the sum of the digits raised to the power of an number is equal to the number itself e.g:- 135 i.e 1^1+3^2+5^3=135.
num = 155
dup = 155
digi = len(str(num))
sum = 0
while num > 0:
    rem = num % 10
    sum = sum + rem ** digi
    num = num// 10
    digi = digi - 1
if sum == dup:
    print(f"{dup} is a Disarum Number")
else:
    print(f"{dup} is not a Disarum Number")