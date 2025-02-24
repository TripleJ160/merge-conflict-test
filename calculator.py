def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def power(x, y):
    return x ** y

def is_valid_number(num_str):
    try:
        float(num_str)
        return True
    except ValueError:
        return False

def calculator():
    print("Enhanced Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power (x^y)")
    
    while True:
        choice = input("Enter choice (1/2/3/4/5): ")
        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice! Please enter 1, 2, 3, 4, or 5")
            continue
        
        num1_str = input("Enter first number: ")
        if not is_valid_number(num1_str):
            print("Invalid input! Please enter a valid number")
            continue
            
        num2_str = input("Enter second number: ")
        if not is_valid_number(num2_str):
            print("Invalid input! Please enter a valid number")
            continue
            
        num1 = float(num1_str)
        num2 = float(num2_str)
        
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
        elif choice == '5':
            print(f"{num1} ^ {num2} = {power(num1, num2)}")
        
        break

if __name__ == "__main__":
    calculator()