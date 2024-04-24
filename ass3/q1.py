#1.	Get a list of numbers as input from a user and calculate the sum of it.
#a. without using standard function
#b. with using standard function
def sum_of_numbers_without_builtin(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

numbers = input("Enter a list of numbers separated by space: ").split()
numbers = [int(num) for num in numbers]
sum_without_builtin = sum_of_numbers_without_builtin(numbers)

# Display the result
print("Sum of numbers without using standard function:", sum_without_builtin)


#with using standard fuction

# Get input from the user
numbers = input("Enter a list of numbers separated by spaces: ").split()

# Convert the input strings to integers
numbers = [int(num) for num in numbers]

# Calculate the sum using the built-in sum() function
total = sum(numbers)

print("Sum of the numbers:", total)






