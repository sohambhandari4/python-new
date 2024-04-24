#6.	Write a Python program to get a string from a given string where 
#all occurrences of its first char have been changed to '$', except the first char itself
def replace_first_char(string):
    if len(string) <= 1:
        return string

    first_char = string[0]
    modified_string = first_char + string[1:].replace(first_char, '$')

    return modified_string


string = input("Enter a string: ")
modified_string = replace_first_char(string)

# Display the original and modified strings
print("Original string:", string)
print("Modified string:", modified_string)
