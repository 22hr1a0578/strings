Write a Python Program to remove the nth index character from a non-empty string.
Input & Output Format:
Input consists of a string and one integer.
The first input consists of a string.
The second input refers to the index position.
The output consists of a string.
Sample Input:
cyfuno
4
Sample Output:
cyfuo
# Step 1: Take input from the user
input_string = input("Enter a string: ")
index_to_remove = int(input("Enter the index to remove: "))

# Step 2: Remove the character at the specified index
if 0 <= index_to_remove < len(input_string):
    new_string = input_string[:index_to_remove] + input_string[index_to_remove + 1:]
else:
    new_string = input_string  # If the index is out of range, keep the original string

# Step 3: Print the resulting string
print(new_string)


