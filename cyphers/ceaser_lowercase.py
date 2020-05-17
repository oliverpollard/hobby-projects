import numpy as np

def cypher(x, key):
    char_len = len(x)
    out = ""

    count = 0
    while count < char_len:
        char_code = ord(x[count])

        if (char_code >= 97) and (char_code <= 122):
            if char_code + key > 122:
                mod = 122 - char_code
                char_code = 96 + key - mod
            else:
                char_code = char_code + key

        out = out + chr(char_code)
        count = count + 1

    return out


message = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()#input().lower()
key = 27#int(input())
if key > 26:
    key = key - 26*int(key/26)
encrypted = cypher(message, key)

print(encrypted)
print(cypher(encrypted,-key))
