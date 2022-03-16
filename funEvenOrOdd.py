def evenOrOdd(num):
    """
    This Function is used to check if the number is even or odd
    this is commented
    """
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")


num = int(input("Enter your Number to check : "))
evenOrOdd(num)
