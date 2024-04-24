#1.	Write a program to accept and convert string in uppercase or vice versa.
def convert_case(string):
    converted_string = ""
    
    for char in string:
        if char.islower():
            converted_string += char.upper()
        elif char.isupper():
            converted_string += char.lower()
        else:
            converted_string += char
    return converted_string

string = input("Enter a string: ")
converted_string = convert_case(string)

# Display the converted string
print("Original string:", string)
print("Converted string:", converted_string)
