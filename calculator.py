
def add(x, y):
    """This function adds two numbers"""
    return x + y

def subtract(x, y):
    """This function subtracts two numbers"""
    return x - y

def multiply(x, y):
    """This function multiplies two numbers"""
    return x * y

def divide(x, y):
    """
    This function divides two numbers.
    It handles the case of division by zero.
    """
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

# --- Main Program Loop ---

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    # Take input from the user for the operation choice
    choice = input("Enter choice(1/2/3/4): ")

    # Check if the choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            # Skip the rest of this loop iteration and start over
            continue

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
        
        # Ask the user if they want to perform another calculation
        next_calculation = input("Do you want to do another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            print("Exiting calculator. Goodbye!")
            break
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")