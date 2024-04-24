#7.	To print list of elements in sorted order
def print_sorted_list(input_list):
    sorted_list = sorted(input_list)
    print("List of elements in sorted order:", sorted_list)

# Test the function with an example
input_list = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]
print_sorted_list(input_list)
