answer = "yes"

while "yes" in answer.lower():
    x = int(input("Enter first number")) 
    y = int(input("Enter second number"))
    operation = input("Choose an operation: Addition '+', Subtraction '-', Multiplication '*', Division '/', Exponent '**'").strip()
    operations = ["+","-", "*", "/", "**"]
    
    if operation == "*":
        print(x*y)

    elif operation == "/":
        if y == int(0):
               print("Cannot divde by zero")
        else:
            print(x/y)

    elif operation == "**":
        print(x**y)

    elif operation == "+":
        print(x+y)

    elif operation == "-":
        print(x-y)

    else:
        print("Invalid Operation")
    
    answer = input("Would you like to perform another calculation?")

print("Calculator closed.")
