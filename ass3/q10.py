#10.	Write a Python program to append a list to the second list.
def append_lists(list1, list2):
    list1.extend(list2)
    return list1

# Test the function with an example
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = append_lists(list1, list2)
print("List 1 after appending List 2:", result)
