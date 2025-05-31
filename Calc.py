# Function to add all numbers in the list
def add(numbers):
    return sum(numbers)

# Function to subtract all numbers from the first number in the list
def subtract(numbers):
    # Start with the first number
    result = numbers[0]
    
    # Subtract the rest of the numbers one by one
    for num in numbers[1:]:
        result -= num
        
    return result

# Function to multiply all numbers in the list
def multiply(numbers):
    # Start with 1, because multiplying by 1 doesn't change the result
    result = 1
    
    # Multiply each number in the list by the current result
    for num in numbers:
        result *= num
        
    return result

# Function to divide the first number by the rest of the numbers in the list
def divide(numbers):
    # Start with the first number
    result = numbers[0]
    
    # Try dividing by each number in the list
    for num in numbers[1:]:
        if num == 0:
            # Check if we are dividing by zero
            return "Error! Division by zero is not allowed."
        result /= num
        
    return result

# Function to safely gather input from the user
def get_numbers():
    while True:
        try:
            # Ask the user for the number of numbers they want to input
            n = int(input("Enter the number of elements: "))
            
            # Ensure the number of elements is at least 1
            if n < 1:
                print("Please enter at least one number.")
                continue
            
            numbers = []
            # Collect the numbers from the user
            for i in range(n):
                num = float(input(f"Enter number {i+1}: "))
                numbers.append(num)
            
            # Return the list of numbers once they are all collected
            return numbers
        
        except ValueError:
            # If the user enters something that's not a valid number
            print("Invalid input! Please enter a valid number.")

# Display available operations to the user
print("Select an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Ask the user to choose an operation
choice = input("Enter choice (1/2/3/4): ")

# Get the list of numbers from the user
numbers = get_numbers()

# Perform the chosen operation based on user input
if choice == '1':
    # If the user chose addition, call the add function
    print(f"Result: {add(numbers)}")
elif choice == '2':
    # If the user chose subtraction, call the subtract function
    print(f"Result: {subtract(numbers)}")
elif choice == '3':
    # If the user chose multiplication, call the multiply function
    print(f"Result: {multiply(numbers)}")
elif choice == '4':
    # If the user chose division, call the divide function
    print(f"Result: {divide(numbers)}")
else:
    # If the user entered an invalid option
    print("Invalid choice! Please select a valid operation.")