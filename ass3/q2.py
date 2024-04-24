#2.	Write a Python program to multiply all the items in a list.
def multiply_list_items(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

numbers = input("Enter a list of numbers separated by space: ").split()
numbers = [int(num) for num in numbers]
result = multiply_list_items(numbers)

# Display the result
print("Result of multiplying all items in the list:", result)
