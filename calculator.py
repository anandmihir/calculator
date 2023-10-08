# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

while True:
    # Display menu options
    print("\nCalculator Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    # Get user choice
    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "5":
        print("Exiting the calculator.")
        break

    if choice in ("1", "2", "3", "4"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", add(num1, num2))
        elif choice == "2":
            print("Result:", subtract(num1, num2))
        elif choice == "3":
            print("Result:", multiply(num1, num2))
        elif choice == "4":
            result = divide(num1, num2)
            if type(result) == str:
                print(result)
            else:
                print("Result:", result)
        else:
            print("Invalid input. Please select a valid option.")
    else:
        print("Invalid input. Please select a valid option.")

