num1 = int(input("Enter 1st Number"))
num2 = int(input("Enter 2nd Number"))
num3 = int(input("Enter 3rd Number"))
if num1 > num2 and num1 > num3:
    print(f"{num1} is the largest")
elif num2 > num3 :
    print(f"{num2} is the largest")
else:
    print(f"{num3} is the largest")

