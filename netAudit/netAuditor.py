import subprocess
import re
import socket
import platform
import sys

def get_network_interfaces():
    result = subprocess.run(['ip', 'link', 'show'], capture_output=True)
    output = result.stdout.decode('utf-8')
    lines = output.split('\n')

    interfaces = [re.search(r'^\d+:\s+(\S+):', line).group(1) for line in lines if re.search(r'^\d+:\s+(\S+):', line)]
    return interfaces

def get_public_ip():
    try:
        result = subprocess.run(['curl', 'ifconfig.me'], capture_output=True)
        public_ip = result.stdout.decode('utf-8').strip()
        return public_ip
    except subprocess.CalledProcessError:
        return None

def get_hostname():
    try:
        return socket.gethostname()
    except socket.error:
        return None

def check_listening_ports():
    print("\033[31mChecking current network connections and listening ports...\033[0m")
    try:
        result = subprocess.run(['ss', '-tunlp'], capture_output=True)
        output = result.stdout.decode('utf-8')
        print(output)
    except subprocess.CalledProcessError:
        print("Failed to retrieve network connections and listening ports.")

def run_network_audit(interface):
    print(f"\nRunning network audit on interface: {interface}")

    # Check internet connectivity using ping test
    print("\033[31mChecking internet connectivity...\033[0m")
    try:
        subprocess.run(['ping', '-c', '5', 'google.com'], check=True, capture_output=True)
        print("Internet connectivity: Available")
    except subprocess.CalledProcessError:
        print("Internet connectivity: Unavailable")

    # Get IP addresses
    print("Getting IP addresses...")
    result = subprocess.run(['ip', 'addr', 'show', 'dev', interface], capture_output=True)
    output = result.stdout.decode('utf-8')

    private_ip_match = re.search(r'inet\s+(\d+\.\d+\.\d+\.\d+/\d+)', output)
    if private_ip_match:
        private_ip = private_ip_match.group(1)
        print(f"Private IP address: {private_ip}")
    else:
        print("Private IP address: Not found")

    public_ip = get_public_ip()
    if public_ip:
        print(f"Public IP address: {public_ip}")
    else:
        print("Public IP address: Not found")

    hostname = get_hostname()
    if hostname:
        print(f"Hostname: {hostname}")
    else:
        print("Hostname: Not found")

    check_listening_ports()

    # Get operating system information
    print("Getting operating system information...")
    os_name = platform.system()
    os_version = platform.release()
    print(f"Operating System: {os_name} {os_version}")


def print_banner():
    author = "Djefferson Saintilus"
    banner = r"""
███╗   ██╗███████╗████████╗ █████╗ ██╗   ██╗██████╗ ██╗████████╗
████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║   ██║██╔══██╗██║╚══██╔══╝
██╔██╗ ██║█████╗     ██║   ███████║██║   ██║██║  ██║██║   ██║   
██║╚██╗██║██╔══╝     ██║   ██╔══██║██║   ██║██║  ██║██║   ██║   
██║ ╚████║███████╗   ██║   ██║  ██║╚██████╔╝██████╔╝██║   ██║   
╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝   ╚═╝   
                                                        
"""

    banner += f"\nNetwork Auditor v1.0\nAuthor: {author}\n"
    print(banner)

if __name__ == '__main__':
    # Print the banner
    print_banner()

    interfaces = get_network_interfaces()
    if not interfaces:
        print("No network interfaces found.")
        sys.exit(1)

    print("Available network interfaces:")
    for i, interface in enumerate(interfaces):
        print(f"{i+1}. {interface}")

    while True:
        try:
            selected_interface = int(input("Enter the interface number to audit: "))
            interface_index = selected_interface - 1

            if interface_index < 0 or interface_index >= len(interfaces):
                print("Invalid interface number. Please try again.")
            else:
                selected_interface = interfaces[interface_index]
                break

        except ValueError:
            print("Invalid input. Please enter a valid interface number.")

    try:
        run_network_audit(selected_interface)
    except Exception as e:
        print(f"An error occurred during network audit: {str(e)}")
