import string
from helpers import alphabet_position, rotate_character
alphabet_l = string.ascii_lowercase
alphabet_u = string.ascii_uppercase

def encrypt(message,rot):
    rotated_text = []
    text = list(message)
    for item in range(len(text)):
        if text[item] == ' ' or text[item].isalpha() == False:
            rotated_text.append(text[item])
        else:
            rotated_text.append(rotate_character(text[item], int(rot)))
    return(''.join(rotated_text))

def main():
    # your main code (input and print statements)
    m = input("Type a message:")
    rotate = input("Rotate by:")
    encrypted_message = encrypt(m, rotate)
    return(encrypted_message)
if __name__ == "__main__":
    main()
        