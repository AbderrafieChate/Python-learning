# Given two integer numbers, write a Python code to return their product only
# if the product is equal to or lower than 1000. Otherwise, return their sum 


number1 = float(input("Enter the first Number : "))
number2 = float(input("Enter the second Number : "))

multiplied = number1 * number2
sum = number1 + number2

if multiplied <= 1000:
    print("The result is : ", multiplied)
else:
    print("The result : ", sum)
