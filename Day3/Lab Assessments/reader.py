from writer import write_numbers_to_file

def read_file_content(filename):
    try:
        with open(filename, "r") as file:
            print("File content:")
            print(file.read())

    except FileNotFoundError:
        print("Error: File not found while reading")

    except PermissionError:
        print("Error: Permission denied while reading")


file_name = "numbers.txt"

write_numbers_to_file(file_name)
read_file_content(file_name)
