#A=P×(1+100R​)T
p = float(input("enter principal amount: "))
r = float(input("enter rate amount: "))
t = float(input("enter time amount: "))
ci = p *(1 + r / 100) ** t
print("Compound Interest = ",ci)