import base64
import re

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
    file_path = input("Enter the name of the file to scan: ").strip()

    try:
        base64_strings = extract_base64_strings(file_path)
        if base64_strings:
            print("Found Base64 encoded strings:")
            for b64_str in base64_strings:
                print(f"Decoded: {base64.b64decode(b64_str).decode('ascii')}")
        else:
            print("No Base64 encoded strings found.")
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
