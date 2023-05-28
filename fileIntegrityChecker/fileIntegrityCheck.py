import hashlib
import sys

def calculate_md5(file_path):
    # Initialize the hash object
    md5_hash = hashlib.md5()

    try:
        # Read the file in chunks and update the hash object
        with open(file_path, 'rb') as file:
            for chunk in iter(lambda: file.read(4096), b''):
                md5_hash.update(chunk)

        # Get the hexadecimal representation of the hash
        md5_digest = md5_hash.hexdigest()

        return md5_digest
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied to access file '{file_path}'.")
        sys.exit(1)
    except:
        print("An error occurred while reading the file.")
        sys.exit(1)

def calculate_sha256(file_path):
    # Initialize the hash object
    sha256_hash = hashlib.sha256()

    try:
        # Read the file in chunks and update the hash object
        with open(file_path, 'rb') as file:
            for chunk in iter(lambda: file.read(4096), b''):
                sha256_hash.update(chunk)

        # Get the hexadecimal representation of the hash
        sha256_digest = sha256_hash.hexdigest()

        return sha256_digest
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied to access file '{file_path}'.")
        sys.exit(1)
    except:
        print("An error occurred while reading the file.")
        sys.exit(1)

def print_banner(file_name, author_name):
    banner = f"""
====================================
File Integrity Checker
====================================
File: {file_name}
Author: {author_name}
====================================
"""
    print(banner)

def print_help():
    help_message = """
Usage: python file_integrity_checker.py <file_path>

Arguments:
  file_path    Path to the file for which to calculate the MD5 and SHA-256 hashes.

Example:
  python file_integrity_checker.py /path/to/file
"""
    print(help_message)

# Extract the command-line arguments
arguments = sys.argv[1:]

# Check if the required arguments are provided
if len(arguments) != 1:
    print_help()
    sys.exit(1)

# Extract the file path from the command-line argument
file_path = arguments[0]

# Set your name as the author
author_name = "Djefferson Saintilus"

# Extract the file name from the file path
file_name = file_path.split("/")[-1]

# Print the program banner
print_banner(file_name, author_name)

# Calculate the MD5 and SHA-256 hashes of the file
try:
    md5_hash = calculate_md5(file_path)
    sha256_hash = calculate_sha256(file_path)

    # Print the calculated hashes
    print(f"MD5: {md5_hash}")
    print(f"SHA-256: {sha256_hash}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
