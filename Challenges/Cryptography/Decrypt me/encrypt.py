def encrypt(string, key):
    cipher = ''
    for char in string:
        if char == ' ' or char == "_":
            cipher += char
        elif ord(char) >= 48 and ord(char) <= 57:
            cipher += char
        elif char.isupper():
            cipher += chr((ord(char) + key - 65) % 26 + 65)
        else:
            cipher += chr((ord(char) + key - 97) % 26 + 97)

    cipher = cipher.encode("utf-8").hex()

    return cipher

text = input("Enter string: ")
s = int(input("Enter key: "))
print("\nOriginal string: ", text)
print("After encryption: ", encrypt(text, s))




