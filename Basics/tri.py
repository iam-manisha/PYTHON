# num = 4
# star = 2 * num - 1
# space = 0
# for row in  range (1,num+1):
#     for col1 in range (1,space +1):
#         print (' ',end = ' ')
#     for col2 in range(1,star +1):
#         print('*',end =' ')
#     print()
#     star -=2
#     space +=1

num = 4
star = 2 * num -1
space = 0

for row in range (1, num + 1):
    for col1 in range(1, space + 1):
        print(' ', end = " ")
    for col2 in range(1, star + 1):
        print('*', end =' ')
    print()
    star -= 2
    space += 1