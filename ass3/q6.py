#6.	Write a Python program to print the numbers of a specified list after removing even numbers from it.
def remove_even_numbers(input_list):
    odd_numbers = [num for num in input_list if num % 2 != 0]
    return odd_numbers

# Test the function with an example
input_list = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]
result = remove_even_numbers(input_list)
print("List after removing even numbers:", result)
