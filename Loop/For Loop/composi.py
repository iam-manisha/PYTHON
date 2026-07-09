for num in range(1,101):
    if num > 3:
        for val in range(2,int(num ** 0.5)+1):
            if num % val == 0 :
                print(num)
                break

            