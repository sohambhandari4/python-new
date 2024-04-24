#4.	Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
def exchange_first_and_last(string):
    if len(string) <= 1:
        return string
    else:
        return string[-1] + string[1:-1] + string[0]

string = input("Enter a string: ")
new_string = exchange_first_and_last(string)

# Display the original and changed strings
print("Original string:", string)
print("String with exchanged first and last characters:", new_string)
