# Program to add all digits in a number using while loop

inp = 345
sum_digits = 0
num = inp

print(f"Input number: {inp}")

while num > 0:
    digit = num % 10  # Extract last digit
    sum_digits += digit  # Add digit to sum
    num = num // 10  # Remove last digit

print(f"Sum of digits: {sum_digits}")
