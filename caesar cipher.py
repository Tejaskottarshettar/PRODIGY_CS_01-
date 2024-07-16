def caesar_cipher(text, shift, mode):
    result = ''
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
        elif char.isdigit():
            shifted_char = str((int(char) + shift) % 10)
        else:
            shifted_char = char
        result += shifted_charte
    return result

if __name__ == "__main__":
    message = input("Enter a message: ")
    shift = int(input("Enter shift value: "))
    mode = input("Enter mode (encrypt/decrypt): ")

    if mode.lower() == 'encrypt':
        encrypted_message = caesar_cipher(message, shift, 'encrypt')
        print("Encrypted message:", encrypted_message)
    elif mode.lower() == 'decrypt':
        decrypted_message = caesar_cipher(message, -shift, 'decrypt')
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid mode.")