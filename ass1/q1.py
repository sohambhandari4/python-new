#1.	Write a program which finds sum of digits of a number
def sum_of_digits(number):
    number_str = str(number)
    digit_sum = 0
    
    for digit in number_str:
        digit_sum += int(digit)
    return digit_sum

number = int(input("Enter a number: "))
result = sum_of_digits(number)
print("Sum of digits:", result)
