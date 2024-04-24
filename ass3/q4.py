#4.	Write a Python program to count the number of strings from a given list of strings. 
#The string length is 2 or more and the first and last characters are the same.
def count_strings_with_same_first_last(strings):
    count = 0
    for string in strings:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count


strings = input("Enter a list of strings separated by space: ").split()
count = count_strings_with_same_first_last(strings)

# Display the result
print("Number of strings with length 2 or more and first and last characters the same:", count)
