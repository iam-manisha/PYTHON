num = 192
ans = str(num * 1) + str(num * 2) + str(num * 3)

for val in range(1, 10):
    if str(val) not in ans:
        print('Not Fascinating No')
        break

else:
    print('Fascinating')