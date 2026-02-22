import string
def caesarCipher(s, k):
    result = ""
    for char in s:
        if char in string.ascii_uppercase:
            result += chr((ord(char) - ord('A') + k) % 26 + ord('A'))
        elif char in string.ascii_lowercase:
            result += chr((ord(char) - ord('a') + k) % 26 + ord('a'))
        else:
            result += char
    return result

# if __name__ == '__main__':
#     s = input()
#     k = int(input())
#     print(caesarCipher(s, k))