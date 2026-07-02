#PALYPRIME NUMBER:- THE NUMBER SHOULD BE PALINDROME AS WELL AS PRIME NUMBER.
num = 11
dup = num
count_fact = 0

for val in range(1, num + 1):
    if num % val == 0:
        count_fact = count_fact + 1

if count_fact == 2:
    ans = 0
    while num > 0:
        rem = num % 10
        ans = ans * 10 + rem
        num = num // 10

    if dup == ans:
        print(f'{dup} is a palyprime')
    else:
        print(f'{dup} is not a palyprime')

else:
    print(f'{dup} not a palyprime')