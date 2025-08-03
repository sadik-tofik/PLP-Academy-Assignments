num1 = int (input("Enter the first number:  "))
num2 = int (input("Enter the second number:  "))

sum = num1 + num2
print("The sum of", num1, "and", num2, "is:", sum)
sub = num1 - num2
print("The difference of", num1, "and", num2, "is:", sub)
mul = num1 * num2
print("The product of", num1, "and", num2, "is:", mul)
if num2 != 0:
    div = num1 / num2
    print("The division of", num1, "by", num2, "is:", div)
else:
    print("Division by zero is not allowed.")
