#7.	Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
def swap_first_two_chars(string1, string2):
    if len(string1) >= 2 and len(string2) >= 2:
        new_string1 = string2[:2] + string1[2:]
        new_string2 = string1[:2] + string2[2:]
        return new_string1 + ' ' + new_string2
    else:
        return "Strings should have at least two characters"

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
result = swap_first_two_chars(string1, string2)

# Display the result
print("Resulting string after swapping first two characters:", result)
