try:
    a = int(input("Enter a first number: "))
    b = int(input("Enter a second number: "))
    print("what lind of operation do you want to perform. press + for addition\n - for subtraction\n * for multiplication\n  / for division")
    operation = input("Enter an operation (+, -, *, /): ")

    match operation:
            
        case "+":
            print(f"The result is: {a + b}")
        case "-":
            print(f"The result is: {a - b}")
        case "*":
            print(f"The result is: {a * b}")
        case "/":
            print(f"The result is: {a / b}")
        case default: 
            print(f"There was an error")
            
except Exception as e:
    print("Invalid operation. Please try again.")
        
