import sys
import binascii

try:
    # Get the filename from command-line argument
    filename = sys.argv[1]

    # Open the file and read its contents
    with open(filename, 'rb') as f:
        content = f.read()

    # Convert the file content to hexadecimal
    hex_content = binascii.hexlify(content)

    # Convert the hexadecimal content to string and output it
    print(hex_content.decode())

except IndexError:
    print("Please specify the filename as a command-line argument!")
except FileNotFoundError:
    print("File not found!")
except IOError:
    print("Failed to read the file!")

