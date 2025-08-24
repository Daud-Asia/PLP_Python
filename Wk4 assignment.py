def read_and_write_file():
    try:
        # Ask user for input filename
        input_file = input("Enter the name of the file to read from: ")

        # Try to open and read the file
        with open(input_file, 'r') as file:
            content = file.read()

        # Modify content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Write to a new file
        output_file = "modified_" + input_file
        with open(output_file, 'w') as file:
            file.write(modified_content)

        print(f"Modified content written to {output_file}")

    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: Could not read or write file.")

read_and_write_file()


