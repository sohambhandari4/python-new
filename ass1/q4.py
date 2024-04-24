#4.	Write a program which accepts 10 integers and prints "DUPLICATES" if any of the values entered are duplicates otherwise prints "ALL UNIQUE".
def check_duplicates(numbers):
    if len(numbers) == len(set(numbers)):
        print("ALL UNIQUE")
    else:
        print("DUPLICATES")

numbers = []
for i in range(10):
    num = int(input(f"Enter integer {i + 1}: "))
    numbers.append(num)

check_duplicates(numbers)
