# List with different types of elements
elements = [42, "Hello", 3.14, "World", True, [1, 2, 3], "Python"]

# Initialize a counter for string elements
string_count = 0

# Loop through the elements in the list
for element in elements:
    # Check if the element is of type str
    if isinstance(element, str):
        string_count += 1

# Output the result
print(f'The number of string elements in the list is: {string_count}')
