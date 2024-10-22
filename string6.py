 Write a Python Program to form a new string made of the first 2 characters and last 2 characters from a given string.
Problem Description:
The program takes a string and forms a new string made of the first 2 characters and last 2 characters from a given string.
Problem Solution:
1. Take a string from the user and store it in a variable.
2. Initialize a count variable to 0.
3. Use a for loop to traverse through the characters in the string and increment the count variable each time.
4. Form the new string using string slicing.
5. Print the newly formed string.
6. Exit.
Sample Input:
Hello World
Sample Output:
Held
# Step 1: Take a string input from the user
input_string = input("Enter a string: ")

# Step 2: Check the length of the string
if len(input_string) < 2:
    print("String is too short to form a new string.")
else:
    # Step 3: Form the new string using string slicing
    new_string = input_string[:2] + input_string[-2:]

    # Step 4: Print the newly formed string
    print(new_string)
