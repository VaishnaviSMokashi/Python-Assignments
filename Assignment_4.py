#Task 1: Read a File and Handle Errors
file1 = open('sample.txt','r')
reading_file = file1.read()
print(reading_file)
file1.close()

try:
    file1 = open('sample.txt', 'r')
    reading_file = file1.read()
    print(reading_file)
    file1.close()
except FileNotFoundError:
    print('The file sample.txt was not found.')
finally:
    print('The file sample.text was found.')

#Task 2: Write and Append Data to a File
# Step 1: Take input from user and write to file
text_to_write = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(text_to_write + "\n")
print("Data successfully written to output.txt.")

# Step 2: Take additional input and append to file
text_to_append = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(text_to_append + "\n")
print("Data successfully appended.")

# Step 3: Read and display the final content
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    print(file.read())

