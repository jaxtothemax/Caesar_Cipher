def rot(input_string, rot_x):
    arr=[]

    for char in input_string:
        character = ord(char)
        shiftModulo = int(rot_x) % 25
        characterShift = character + shiftModulo

        #Capital letters
        if 65 <= character <= 90:
            if characterShift <= 90:
                arr.append(chr(characterShift))
                
            else:
                arr.append(chr(65 + (characterShift % 90) - 1))

        #Small letters
        elif 97 <= character <= 122:
            if characterShift <= 122:
                arr.append(chr(characterShift))
            else:
                arr.append(chr(97 + (characterShift % 122) - 1))
        
        #Numbers letters, because why not?
        elif 48 <= character <= 57:
            if characterShift <= 57:
                arr.append(chr(characterShift))
            else:
                arr.append(chr(48 + (characterShift % 57) - 1))

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