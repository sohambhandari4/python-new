#8.	Write a program to accept a number 'n', and display the following pattern (Floyd's triangle)n=3
#	1
#	2 3
#   4 5 6

def floyds_triangle(n):
    num = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1
        print()

# Accept the number 'n' from the user
n = int(input("Enter the value of 'n': "))
floyds_triangle(n)
