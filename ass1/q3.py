#3.	Write a program to accept one number and check that number is positive , negative or zero.  
def check_number(number):
    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

number = int(input("Enter a number: "))
check_number(number)
