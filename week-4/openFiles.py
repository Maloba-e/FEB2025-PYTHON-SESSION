# Open file in read mode
file = open('example.txt', 'r')

# Read the contents
content = file.read()
file.seek(0)  # Reset file pointer to beginning
content_lines = file.readlines()
content_line = file.readline()
# Close the file
file.close()

# Print the contents
print("String content:")
print(content)
print("\nList content:")
print(content_lines)
print("\nSingle line content:")
print(content_line)

