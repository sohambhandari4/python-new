#5.	Write a Python program to remove duplicates from a list.
def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Test the function with an example
input_list = input("Enter a list of elements separated by space: ").split()
result = remove_duplicates(input_list)
print("List after removing duplicates:", result)
