def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            result += chr((ord(char.lower()) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

file_name = input("Enter file name: ")

try:
    with open(file_name, "r") as f:
        content = f.read()

    choice = input("1. Encrypt  2. Decrypt: ")
    shift = 3

    if choice == "1":
        result = encrypt(content, shift)
        new_file = "encrypted_" + file_name
    else:
        result = decrypt(content, shift)
        new_file = "decrypted_" + file_name

    with open(new_file, "w") as f:
        f.write(result)

    print("Saved as:", new_file)

except FileNotFoundError:
    print("File not found!")
