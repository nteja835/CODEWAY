def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b == 0:
        return "Cannot divide by zero"
    return a/b

def calculator1():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    try:
        a1 = float(input("Enter the first number: "))
        a2 = float(input("Enter the second number: "))
        option = input("Enter the operation choice (1-4): ")

        if option == '1':
            result = add(a1, a2)
            print(f"Result: {result}")

        elif option == '2':
            result = sub(a1, a2)
            print(f"Result: {result}")

        elif option == '3':
            result = mul(a1, a2)
            print(f"Result: {result}")

        elif option == '4':
            result = div(a1, a2)
            print(f"Result: {result}")

        else:
            print("Invalid operation choice. Please enter a number between 1 and 4.")

    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

if __name__ == "__main__":
    calculator1()
