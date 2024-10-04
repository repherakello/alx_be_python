def perform_operation(num1:float, num2:float,operation:str):
    if operation not in ["add", "subtract","multiply","divide"]:
        return "Error Invalid operation"
    
    if operation == "add":
        return num1 + num2
    elif operation =="subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    

result = perform_operation(10,5,"subtract")
print(result)