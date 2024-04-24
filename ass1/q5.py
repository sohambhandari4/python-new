#5.	Write a program which prints fibonacci series of a number.
def fibonacci_sequence(n):
    fibonacci_sequence = [0, 1] 
    
    for i in range(2, n):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    
    return fibonacci_sequence

num = int(input("Enter the number of terms for Fibonacci series: "))
result = fibonacci_sequence(num)
print("Fibonacci series of", num, "terms:", result)
