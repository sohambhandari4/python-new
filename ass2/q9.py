#9.	Write a Python program to lowercase the first 3 characters in a string.
def lowercase_first_three(string):
    if len(string) >= 3:
        return string[:3].lower() + string[3:]
    else:
        return "String should have at least three characters"

string = input("Enter a string: ")
modified_string = lowercase_first_three(string)

# Display the original and modified strings
print("Original string:", string)
print("Modified string with first three characters in lowercase:", modified_string)
