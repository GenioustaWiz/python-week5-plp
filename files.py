
# File Creation
with open("my_file.txt", "w") as file:
    file.write("Line 1: This is a sample text file.\n")
    file.write("Line 2: The number 42 is a significant number in science fiction.\n")
    file.write("Line 3: Python is a popular programming language.\n")

# File Reading and Display
with open("my_file.txt", "r") as file:
    content = file.read()
    print("Contents of my_file.txt:")
    print(content)

# File Appending
with open("my_file.txt", "a") as file:
    file.write("Line 4: This line was appended to the file.\n")
    file.write("Line 5: Python is widely used for data analysis and machine learning.\n")
    file.write("Line 6: Have a great day!\n")

# Display the updated contents of the file
with open("my_file.txt", "r") as file:
    updated_content = file.read()
    print("\nUpdated contents of my_file.txt:")
    print(updated_content)
