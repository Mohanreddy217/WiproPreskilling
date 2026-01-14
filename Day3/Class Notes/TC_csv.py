# Reading from a file
with open("data.txt", "r") as file_obj:
    first_line = file_obj.readline()
    remaining_lines = file_obj.readlines()

print("First line:", first_line)
print("Remaining lines:", remaining_lines)

# Appending content
with open("data.txt", "a") as file_obj:
    file_obj.write("\nThis line is appended")

# Writing content (overwrite)
with open("data.txt", "w") as file_obj:
    file_obj.write("Python File Handling\n")
    file_obj.write("Write mode example")
