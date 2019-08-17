import string
alphabet_l = string.ascii_lowercase
alphabet_u = string.ascii_uppercase

def alphabet_position(letter):
    if letter.islower() == True:
        x = alphabet_l.index(letter)
    elif letter.isupper() == True:
        x = alphabet_u.index(letter)
    return(x)

def rotate_character(char, rot):  
    rotated_char = ''
    if char == ' ' or char.isalpha() == False:
        rotated_char = char
    else:
        rotated_index = alphabet_position(char) + rot
        if rotated_index < 26:
            if char.islower() == True:
                rotated_char = alphabet_l[rotated_index]
            elif char.isupper() == True:
                rotated_char = alphabet_u[rotated_index]
        else:
            if char.islower() == True:
                rotated_char = alphabet_l[rotated_index % 26]
            elif char.isupper() == True:
                rotated_char = alphabet_u[rotated_index % 26]
    return(rotated_char)      