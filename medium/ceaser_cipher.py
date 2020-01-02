"""
transform a string using the Caesar Cipher.
"""

def transform_string(str,shift):
    cipher = ''
    for char in str:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
    return cipher


if __name__ == '__main__':
    res = transform_string("the crazy programmer", 2)
    print(res)
