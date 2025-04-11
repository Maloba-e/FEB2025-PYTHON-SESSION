# File writing operations in Python

# Writing to a file using 'w' mode (overwrites existing content)
with open('output.txt', 'w') as file:
    file.write('Hello, this is a new file!\n')
    file.write('This is the second line.\n')

# Appending to a file using 'a' mode
with open('output.txt', 'a') as file:
    file.write('This line will be appended to the file.\n')

# Writing multiple lines at once
lines = [
    'First line of multiple lines',
    'Second line of multiple lines',
    'Third line of multiple lines'
]

with open('multiple_lines.txt', 'w') as file:
    file.writelines(line + '\n' for line in lines)

# Writing numbers and other data types
with open('numbers.txt', 'w') as file:
    file.write(str(42) + '\n')  # Convert number to string before writing
    file.write(f'The value of pi is approximately {3.14159}\n')

print('Files have been created and written successfully!') 