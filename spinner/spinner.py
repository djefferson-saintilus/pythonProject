import random
import time

# Prompt the user for the name of the file to read from
filename = input("Enter the name of the file with the list (press Enter for default one): ")
if filename == "":
    filename = "names.txt"

try:
    # Read names from file into a list
    with open(filename, 'r') as f:
        names = f.read().splitlines()

    # Shuffle the list to randomize the order
    random.shuffle(names)

    # Define the spinner animation
    spinner = ['-', '\\', '|', '/']

    # Print an ASCII art banner with the spinner animation
    print(r"""
 ██████╗ ██╗   ██╗███████╗███████╗███████╗██████╗ ██████╗ 
██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝╚════██╗╚════██╗
██║  ███╗██║   ██║█████╗  ███████╗███████╗  ▄███╔╝  ▄███╔╝
██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║  ▀▀══╝   ▀▀══╝ 
╚██████╔╝╚██████╔╝███████╗███████║███████║  ██╗     ██╗   
 ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝  ╚═╝     ╚═╝                                                                                           
    """)

    # Wait for 5 seconds while animating the spinner
    print("Choosing a random ...")
    for i in range(5):
        print(f"  {spinner[i % len(spinner)]}", end='\r')
        time.sleep(1)
    print()

    # Choose a random name and print it
    print(f"The chosen one is: {random.choice(names)}")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found")
except Exception as e:
    print(f"Error: {e}")
