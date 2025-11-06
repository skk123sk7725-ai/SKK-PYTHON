# User se values lena
num1 = float(input("enter num1: "))
operator = input("Operator enter: ")
num2 = float(input("enter num2 : "))

# Operator ke according calculation
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Zero se divide नहीं कर सकते"
else:
    result = "Invalid operator"

print("Result:", result)
