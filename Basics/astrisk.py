num = 7
for row in range(1, num + 1):
    for col in range(1, num+ 1):
        if row == col or row+col == num +1 or row == num // 2 +1 or col == num//2 + 1: 
            print('*', end=' ')
        else:
            print(' ', end=' ')

    print()
    