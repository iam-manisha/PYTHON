# Program to check if a number is composite or not using for loop

num = int(input("Enter a number: "))

if num <= 1:
    print(f"{num} is neither composite nor prime")
else:
    is_composite = False
    
    # Check for divisors from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            is_composite = True
            break
    
    if is_composite:
        print(f"{num} is a composite number")
    else:
        print(f"{num} is a prime number")
