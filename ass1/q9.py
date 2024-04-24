#9.	Write a program to display the following pattern.                                     		
#      1     2     3    4
#      1     2     3
#      1     2
#      1 

def display_pattern(rows):
    for i in range(rows, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Accept the number of rows from the user
rows = int(input("Enter the number of rows: "))
display_pattern(rows)
