#	Write a program to calculate the factorial of a number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter a number to calculate its factorial: "))
result = factorial(number)
print("Factorial of", number, "is", result)
