import string
from helpers import alphabet_position, rotate_character
alphabet_l = string.ascii_lowercase
alphabet_u = string.ascii_uppercase
def encrypt(message,code):
    code_length = len(code)
    code_index = 0
    rotated_text = []
    text = list(message)
    for item in range(len(text)):
        if code_index < code_length :
           if text[item] == ' ' or text[item].isalpha() == False:
               rotated_text.append(text[item])
           else:
               rot = alphabet_position(code[code_index])
               rotated_text.append(rotate_character(text[item], int(rot)))  
               code_index += 1
        elif code_index == code_length :
            if text[item] == ' ' or text[item].isalpha() == False:
                rotated_text.append(text[item])
            else:
                code_index = 0
                rot = alphabet_position(code[code_index])
                rotated_text.append(rotate_character(text[item], int(rot)))
                code_index += 1   
    return(''.join(rotated_text))

def main():
    # your main code (input and print statements)
    message = input("Type a message:")
    code = input("Encryption key:")
    encrypted_message = encrypt(message, code)
    return(encrypted_message)
if __name__ == "__main__":
    main() 