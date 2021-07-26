from abc import abstractproperty
import string
import collections


message = "Mijn email _adress- is kirenp.2004@gmail.com"

encrypted = "qefpfphfobkpxidlPlmq`hpdlo`-dguhvv_`lv`nluhqs^2004~jpdlo^frp"

recognition_key = "qefpfphfobkpxidl"


def Algorithm(message, s):

    result = ""

    for i in range(len(message)):
        char = message[i]

        if char.isdigit():  
            result += char
        elif char.isspace():
            result += "`"
        elif char == "`":
            result += " "
        elif char == "@":
            result += "~"
        elif char == "~":
            result += "@"
        elif char == ".":
            result += "^"
        elif char == "^":
            result += "."
        elif char == "-":
            result += "_"
        elif char == "_":
            result += "-"
        
        elif char.isupper():
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s -97) % 26 + 97)
        
    return result
    
#decides if to encrypt or decrypt
def Tool(message, s):
    if s < 0:
        if message.startswith(recognition_key):
            to_decrypt = message[len(recognition_key):]
            decrypted = Algorithm(to_decrypt, s)
            return decrypted
        else:
            print("niet van kiren")
    elif s > 0:
        result = Algorithm(message, s)
        encrypted = recognition_key + result
        return encrypted



print(Tool(encrypted, -3))

