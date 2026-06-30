#Armstrong number:-the sum of the cubes of its digits is equal to the number its self e.g-153
num = 153
dup = 153
digi = len(str(num))
sum = 0
while num > 0:
    rem = num % 10
    sum = sum + rem ** digi
    num = num //10
if sum == dup:
    print(f"{dup} is a Armstrong Number")
else:
    print(f"{dup} is not a Armstrong Number")
