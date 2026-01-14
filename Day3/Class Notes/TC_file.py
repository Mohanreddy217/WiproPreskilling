# Reading from a file
file_obj = open("data.txt", "r")
first_line = file_obj.readline()
remaining_lines = file_obj.readlines()
print("First line:", first_line)
print("Remaining lines:", remaining_lines)
file_obj.close()
# Appending 
file_obj = open("data.txt", "a")
file_obj.write("\nThis line is appended to the file")
file_obj.close()
# Writing
file_obj = open("data.txt", "w")
file_obj.write("Python File Handling\n")
file_obj.write("This is an example of write mode")
file_obj.close()
