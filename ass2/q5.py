#5.	Write a Python program to get a string made of the first 2 and last 2 characters of a given string.
def get_first_and_last_two(string):
    if len(string) < 2:
        return "String is too short"
    else:
        return string[:2] + string[-2:]

string = input("Enter a string: ")
new_string = get_first_and_last_two(string)

# Display the original and new strings
print("Original string:", string)
print("String made of the first 2 and last 2 characters:", new_string)
