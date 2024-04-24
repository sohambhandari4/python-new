#9.	Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
#Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#Expected Output : ['Green', 'White', 'Black']

def remove_elements(input_list):
    indices_to_remove = [0, 4, 5]
    modified_list = [input_list[i] for i in range(len(input_list)) if i not in indices_to_remove]
    return modified_list

# Test the function with the sample list
sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
result = remove_elements(sample_list)
print("List after removing specified elements:", result)
