#EMIRP:=NO. SHOULD BE A PRIME NO.,NO PALINDROME,REVERSE SHOULD BE PRIME
num = 13
count_fact = 0

for val in range(1, num + 1):
    if num % val == 0:
        count_fact = count_fact + 1

if count_fact == 2:

    ans = 0
    dup = num

    while num > 0:
        rem = num % 10
        ans = ans * 10 + rem
        num = num // 10

    if dup != ans:

        count_fact = 0

        for val in range(1, ans + 1):
            if ans % val == 0:
                count_fact = count_fact + 1

        if count_fact == 2:
            print(f'{dup} is a EMIRP')
        else:
            print(f'{dup} is not a EMIRP')

    else:
        print('Not EMIRP')

else:
    print('Not EMIRP')