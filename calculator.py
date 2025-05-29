# Simple Calculator
# Get number from user
first_number = float(input("Enter the first number: "))
# Get  number from user
second_number = float(input("Enter the second number: "))
# Ask user to choose an operation
print("\nChoose an operation:")
print("1 - Addition (+)")
print("2 - Subtraction (-)")
print("3 - Multiplication (*)")
print("4 - Division (/)")
choice = input("Enter your choice (1/2/3/4): ")
# Perform calculation based on choice
if choice == '1':
    result = first_number + second_number
    print("Result: ", result)
elif choice == '2':
    result = first_number - second_number
    print("Result: ", result)
elif choice == '3':
    result = first_number * second_number
    print("Result: ", result)
elif choice == '4':
    if second_number != 0:
        result = first_number / second_number
        print("Result: ", result)
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid choice. Please select 1, 2, 3, or 4.")
