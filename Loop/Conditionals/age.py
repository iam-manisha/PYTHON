age = int(input("Enter your Age: "))

if age < 0:
    print("Invalid Age")

elif age <= 12:
    print("Child")

elif age <= 19:
    print("Teenager")

elif age <= 59:
    print("Adult")

else:
    print("Senior Citizen")