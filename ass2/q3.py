#3.	Write a program to count the number of characters in a string.   
def count_characters(string):
    return len(string)


string = input("Enter a string: ")
char_count = count_characters(string)

# Display the result
print("Number of characters in the string:", char_count)
