import base64
import re
import os
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

def is_base64_encoded(data):
    try:
        decoded_data = base64.b64decode(data, validate=True)
        if decoded_data.decode('ascii'):
            return True
    except (base64.binascii.Error, UnicodeDecodeError):
        return False
    return False

def extract_base64_strings(file_path):
    # Base64 pattern: A sequence of 4 characters at a minimum, using Base64 characters
    base64_pattern = re.compile(r'([A-Za-z0-9+/]{4,}={0,2})')

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()

    matches = base64_pattern.findall(content)
    base64_strings = [match for match in matches if is_base64_encoded(match)]

    return base64_strings

def main():
    print(Fore.CYAN + Back.BLACK + Style.BRIGHT + "Welcome to the Automatic Base64 Scanner!" + Style.RESET_ALL)
    print(Fore.GREEN + Back.BLACK + "Because sometimes I don't have time for that." + Style.RESET_ALL)
    print()

    file_path = input(Fore.YELLOW + Back.BLACK + "Enter the file path to scan (relative or absolute): " + Style.RESET_ALL).strip()

    # Resolve to absolute path for clarity
    resolved_path = os.path.abspath(file_path)

    try:
        base64_strings = extract_base64_strings(resolved_path)
        if base64_strings:
            print(Fore.GREEN + Back.BLACK + "\nFound Base64 encoded strings:" + Style.RESET_ALL)
            for b64_str in base64_strings:
                decoded = base64.b64decode(b64_str).decode('ascii')
                print(Fore.WHITE + f"Encoded: {b64_str}" + Style.RESET_ALL)
                print(Fore.WHITE + f"Decoded: {decoded}" + Style.RESET_ALL)  # Removed yellow background
        else:
            print(Fore.RED + Back.BLACK + "No Base64 encoded strings found." + Style.RESET_ALL)
    except FileNotFoundError:
        print(Fore.RED + Back.BLACK + f"File not found: {resolved_path}. Please check the path and try again." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + Back.BLACK + f"An error occurred: {e}" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
