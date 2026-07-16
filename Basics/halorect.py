num = 4
for row in range (1,num + 1):
    for col in range (1,num *2 +1):
        if row == 1 or col == 1 or row == num or col == num*2:
            print("*",end='  ' )
        else:
            print(' ',end = '  ')
    print()