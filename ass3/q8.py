#8.	Write a Python program to check if a list is empty or not.
def is_list_empty(input_list):
    if not input_list:
        return True
    else:
        return False

# Test the function with an example
input_list = input("Enter a list of elements separated by space: ").split()
if is_list_empty(input_list):
    print("The list is empty.")
else:
    print("The list is not empty.")
