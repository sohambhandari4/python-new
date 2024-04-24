#Write a program to check whether input number is divisible by 3 or 5 or both
def check_divisibility(number):
    if number % 3 == 0 and number % 5 == 0:
        print(number, "is divisible by both 3 and 5.")
    elif number % 3 == 0:
        print(number, "is divisible by 3.")
    elif number % 5 == 0:
        print(number, "is divisible by 5.")
    else:
        print(number, "is not divisible by either 3 or 5.")

# Accept the number from the user
number = int(input("Enter a number: "))
check_divisibility(number)
