num1  = eval(input("Enter the first number:"))
num2 = eval(input("Enter the second number:"))
operation = input("choose the operation (+, -, *, /):")

match operation:
    case ("+"):
        print("The result is",num1 + num2)
    case ("-"):
        print("The result is",num1 - num2)
    case ("*"):
        print("The result is",num1 * num2)
    case ("/"):
        print("The result is",num1 / num2)