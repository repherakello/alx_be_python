number = eval(input("Enter a number to see its multiplication table:"))


for i in range(11):
    product = number * i

    print(f"{number} * {i} = {product}")

