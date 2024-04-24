#3.	Write a Python program to get the largest number from a list.
#a. without using standard function
#b. with using standard function
def find_largest_without_builtin(numbers):
    if not numbers:
        return None

    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


numbers = input("Enter a list of numbers separated by space: ").split()
numbers = [int(num) for num in numbers]
largest_without_builtin = find_largest_without_builtin(numbers)

if largest_without_builtin is not None:
    print("Largest number without using standard function:", largest_without_builtin)
else:
    print("The list is empty.")



#b. With using standard function:


def find_largest_number(lst):
    if not lst:
        return None
    return max(lst)

# Example usage:
numbers = [10, 5, 7, 20, 15]
largest = find_largest_number(numbers)
print("Largest number using standard function:", largest)






