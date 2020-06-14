def rot(input_string, rot_x):
    arr=[]

    for char in input_string:
        character = ord(char)
        shift_modulo = int(rot_x) % 25
        shift_modulo_numbers = int(rot_x) % 10
        character_shift = character + shift_modulo
        number_shift = character + shift_modulo_numbers

        #Capital letters
        if 65 <= character <= 90:
            if character_shift <= 90:
                arr.append(chr(character_shift))
            else:
                arr.append(chr(65 + (character_shift % 90) - 1))

        #Small letters
        elif 97 <= character <= 122:
            if character_shift <= 122:
                arr.append(chr(character_shift))
            else:
                arr.append(chr(97 + (character_shift % 122) - 1))
        
        #Numbers, because why not?
        elif 48 <= character <= 57:
            if number_shift <= 57:
                arr.append(chr(number_shift))
            else:
                arr.append(chr(48 + (number_shift % 57) - 1))

        #Space
        elif character == 32:
            arr.append(" ")

        
    return ''.join(arr)

# This was Cesar's Cipher 1.0, however, I figured it's bad practice to nest for loops, because it causes big O notation --> O(n²)

# alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
#             "V", "W", "X", "Y", "Z"]


# def rot(input_string, rot_x):
#     arr = []
#     input_string = input_string.upper()
#     for character in input_string:
#         for i in range(len(alphabet)):
#             if alphabet[i] == character:
#                 arr.append(alphabet[(i + int(rot_x)) % len(alphabet)])
#                 continue

#             elif character == " ":
#                 arr.append(" ")
#                 break

#     return "".join(arr).capitalize()


# input_string = input(str("Enter character: "))
# shift = int(input("Shift: "))