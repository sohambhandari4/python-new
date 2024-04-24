#7.	Write a program to accept 10 numbers, display the sum of odd numbers and sum of even numbers
def sum_of_odd_and_even(numbers):
    sum_even = 0
    sum_odd = 0

    for num in numbers:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num

    return sum_even, sum_odd


numbers = []
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)


sum_even, sum_odd = sum_of_odd_and_even(numbers)
print("Sum of even numbers:", sum_even)
print("Sum of odd numbers:", sum_odd)
