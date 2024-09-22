size = int(input("Enter the size of the pattern: "))

row = 0

while row < size:
    for _ in range(size):
        print("*", end="")


    print()

# increment the row counter
    row +=1