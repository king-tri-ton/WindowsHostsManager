import os
import sys
import ctypes

HOSTS_PATH = r'C:\Windows\System32\drivers\etc\hosts'

def is_admin():
    try:
        return os.getuid() == 0
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

def read_hosts():
    with open(HOSTS_PATH, 'r') as file:
        return file.readlines()

def write_hosts(lines):
    with open(HOSTS_PATH, 'w') as file:
        file.writelines(lines)

def add_entry(ip, hostname):
    lines = read_hosts()
    entry = f"{ip} {hostname}\n"
    
    if entry not in lines:
        lines.append(entry)
        write_hosts(lines)
        print(f"Added: {entry.strip()}")
    else:
        print(f"Entry already exists: {entry.strip()}")

def remove_entry(hostname):
    lines = read_hosts()
    lines = [line for line in lines if not line.endswith(f"{hostname}\n")]
    write_hosts(lines)
    print(f"Removed entries for: {hostname}")

def list_entries():
    lines = read_hosts()
    if lines:
        print("Current entries in hosts file:")
        for line in lines:
            print(line.strip())
    else:
        print("No entries found in the hosts file.")

def print_help():
    print("Commands:")
    print("  add      - Add an entry (e.g., add <IP> <hostname>)")
    print("  remove   - Remove an entry (e.g., remove <hostname>)")
    print("  list     - List all entries in the hosts file")
    print("  clear    - Clear the terminal screen")
    print("  help     - Show this help message")
    print("  exit     - Exit the application")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        print("Enter command:", end=' ')
        command = input().strip().lower()

        if command.startswith('add'):
            _, ip, hostname = command.split(maxsplit=2)
            add_entry(ip, hostname)
        elif command.startswith('remove'):
            _, hostname = command.split(maxsplit=1)
            remove_entry(hostname)
        elif command == 'list':
            list_entries()
        elif command == 'help':
            print_help()
        elif command == 'clear':
            clear_screen()
        elif command == 'exit':
            print("Exiting the application...")
            break
        else:
            print("Invalid command. Type 'help' for a list of commands.")

if __name__ == "__main__":
    if not is_admin():
        print("This script needs to be run with administrator privileges.")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    else:
        main()
