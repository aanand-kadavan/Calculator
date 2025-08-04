while True:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice=input("Enter choice: ")
    if choice == '1':
        print("Result:", a + b)
    elif choice == '2':
        print("Result:", a - b)
    elif choice == '3':
        print("Result:", a * b)
    elif choice == '4':
        print("Result:", a / b)
    else:
        print("Invalid choice.")
    print("Do you want to perform another calculation? (yes/no)")
    val= input().strip().lower()
    if val != 'yes':
        print("Exiting the calculator.")
        break