num = 13

count = 0

while num > 0:
    rem = num % 2

    if rem == 1:
        count += 1

    num = num // 2

if count % 2 == 0:
    print("Evil")
else:
    print("Odeous")