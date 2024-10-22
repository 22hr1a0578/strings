Write a  Python Program to calculate the number of words and characters present in a string.
Input & Output Format:
Input consists of a string.
Output consists of two integers.
First output refers to the count of the words.
Second output refers to the count of the characters in a given string,
Sample Input:
Cyfuno
Sample Output:
Words: 1
Letters: 6
# Take input from the user
input_string = input("Enter a string: ")

# Count the number of words
word_count = len(input_string.split())

# Count the number of characters (excluding spaces)
character_count = len(input_string.replace(" ", ""))

# Print the results
print(f"Words: {word_count}")
print(f"Letters: {character_count}")
