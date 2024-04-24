#2.	Write a program which reverses a string and displays both original and reversed string.
def reverse_string(string):
    reversed_string = string[::-1]
    return reversed_string

string = input("Enter a string: ")
reversed_string = reverse_string(string)

# Display the original and reversed strings
print("Original string:", string)
print("Reversed string:", reversed_string)
