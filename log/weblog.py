import re
from collections import Counter
import os

# Define ANSI escape codes for red text
RED = '\033[91m'
RESET = '\033[0m'

# Define a regular expression pattern to match the log format
pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(.*?)" (\d+) (\d+) "(.*?)" "(.*?)"')

# Print banner and instructions for running with administrator or root privileges
print("=== Web Server Log Analyzer ===")
if os.name == 'nt':
    print(f"{RED}Note: Run the program with administrator privileges for best results on Windows.{RESET}")
else:
    print(f"{RED}Note: Run the program with root privileges for best results on Linux.{RESET}")

# Ask the user to select their operating system
os_choice = input("Enter 'W' for Windows or 'L' for Linux: ").lower()

# Set the appropriate log file based on the user's choice
if os_choice == 'w':
    # diretory log path  windows: 'C:\\path\\to\\access.log'
    log_file = '.\\access.log'
else:
    # diretory log path linux : '/var/log/apache2/access.log'
    log_file = './access.log'

# Open the log file and read its contents into a list of strings
with open(log_file, 'r') as f:
    logs = f.readlines()

# Use the regular expression pattern to extract information from each log entry
requests = []
for log in logs:
    match = pattern.match(log)
    if match:
        ip = match.group(1)
        timestamp = match.group(2)
        request = match.group(3)
        status = match.group(4)
        size = match.group(5)
        referer = match.group(6)
        user_agent = match.group(7)
        requests.append((ip, timestamp, request, status, size, referer, user_agent))

# Count the number of requests from each IP address
ip_counts = Counter(request[0] for request in requests)

# Calculate the average size of each response
sizes = [int(request[4]) for request in requests]
average_size = sum(sizes) / len(sizes)

# Print the results
print(f'Total requests: {len(requests)}')
print(f'Unique IP addresses: {len(ip_counts)}')
print('Top 10 IP addresses by request count:')
for ip, count in ip_counts.most_common(10):
    print(f'{ip}: {count} requests')
print(f'Average response size: {average_size:.2f} bytes')
