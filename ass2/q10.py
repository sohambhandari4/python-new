#10.	Write a Python program to compute the sum of the digits in a given string.
def sum_of_digits_in_string(string):
    digit_sum = 0
    for char in string:
        if char.isdigit():
            digit_sum += int(char)
    return digit_sum

string = input("Enter a string: ")
result = sum_of_digits_in_string(string)

# Display the result
print("Sum of digits in the string:", result)
