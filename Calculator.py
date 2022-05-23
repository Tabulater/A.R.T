loop = True
while loop == True:

    print("*****************")
    print("Select operation")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")

    choice = input("Enter choice(1/2/3/4/5): ")

    if choice == '5':
        print("Thank you for using the Calculator")
        exit()

    if choice not in ('1', '2', '3', '4', '5'):
        print('Invalid choice')
    else:
        num1 = input("Enter first number: ")
        
        num2 = input("Enter second number: ")

        if choice == '1':
            result = float(num1) + float(num2)
            print(num1, "+", num2, "=", result)

        if choice == '2':
            result = float(num1) - float(num2)
            print(num1, "-", num2, "=", result)

        if choice == '3':
            result = float(num1) * float(num2)
            print(num1, "*", num2, "=", result)

        if choice == '4':
            result = float(num1) / float(num2)
            print(num1, "/", num2, "=", result)