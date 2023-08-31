import Function

print("Select An Operation:")
print("1. Add")
print("2. Substract")
print("3. Multiply")
print("4. Divide")

operation = int(input("Enter the operation number (1-4): "))
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = 0

if operation == 1:
    result = Function.add(num1, num2)
elif operation == 2:
    result = Function.substract(num1, num2)
elif operation == 3:
    result = Function.multiply(num1, num2)
elif operation == 4:
    result = Function.divide(num1, num2)
else:
    print("Invalid Operation Number, Please Try Again.")
    
print("Result:", result)
    
