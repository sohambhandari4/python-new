#8.	Write a Python program to print the index of a character in a string.
#Sample string: welcome
#Expected output:
#Current character w position at 0
#Current character e position at 1
#Current character l position at 2
#Current character c position at 3
#Current character o position at 4
#Current character m position at 5
#Current character e position at 6

def print_character_indices(string):
    for index, char in enumerate(string):
        print("Current character", char, "position at", index)

sample_string = "welcome"
print("Sample string:", sample_string)
print("Expected output:")
print_character_indices(sample_string)
print("- " * 20)  # Separator line

# Sample string with different format
sample_string2 = "soham"
print("Sample string:", sample_string2)
print("Expected output:")
print_character_indices(sample_string2)
