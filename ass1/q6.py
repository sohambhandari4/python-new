#6.	Write a program which accepts an integer value 'n' and prints all prime numbers till 'n'.
def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def print_prime_numbers(n):
    print("Prime numbers up to", n, ":")
    for i in range(2, n + 1):
        if is_prime(i):
            print(i, end=" ")

n = int(input("Enter a number: "))
print_prime_numbers(n)
