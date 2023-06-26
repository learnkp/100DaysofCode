# write a python program, which converts text to morse code

MORSE_CODE_DICT = {
                   'A': '.-',
                   'B': '-...',
                   'C': '-.-.',
                   'D': '-..',
                   'E': '.',
                   'F': '..-.',
                   'G': '--.',
                   'H': '....',
                   'I': '..',
                   'J': '.---',
                   'K': '-.-',
                   'L': '.-..',
                   'M': '--',
                   'N': '-.',
                   'O': '---',
                   'P': '.--.',
                   'Q': '--.-',
                   'R': '.-.',
                   'S': '...',
                   'T': '-',
                   'U': '..-',
                   'V': '...-',
                   'W': '.--',
                   'X': '-..-',
                   'Y': '-.--',
                   'Z': '--..',
                   '1': '.----',
                   '2': '..---',
                   '3': '...--',
                   '4': '....-',
                   '5': '.....',
                   '6': '-....',
                   '7': '--...',
                   '8': '---..',
                   '9': '----.',
                   '0': '-----',
                   ',': '--..--',
                   '.': '.-.-.-',
                   '?': '..--..',
                   '/': '-..-.',
                   '-': '-....-',
                   '(': '-.--.',
                   ')': '-.--.-'
                   }


# function to convert string to morse code charector by charector
def encrypt_message(Message):
    cipher_text = ""
    for char in Message:
        if char in MORSE_CODE_DICT:
            # if charector in the MORSE_CODE_DICT
            # add 1 space along with replaced morse code, in order to identify strings separately.
            cipher_text += MORSE_CODE_DICT[char] + " "
        elif char == " ":
            # if charector itself is single space that means it's a space between 2 words
            # so add 2 spaces in the cipher text, in order to identify separation between words and characters.
            cipher_text += "  "
    return cipher_text


# function to convert morse code to string
def decrypt(message):
    decipher_text = ""
    # Store one string at a time, which means few symbols of morse code.
    # once you find space which means end of one string
    morsecode_letter = ""
    # Go through each morse code one by one
    for letter in message:
        if letter != " ":
            i = 0
            morsecode_letter += letter
        else:
            i += 1
            # when you find 2 consecutive spaces in morse code,
            # which means separation of 2 word and add single space in decipher_text
            if i == 2:
                decipher_text += " "
            else:
                # check morsecode_letter matches in MORSE_CODE_DICT and store the equivalent string in decipher_text
                for key, value in MORSE_CODE_DICT.items():
                    if morsecode_letter == value:
                        decipher_text += key
                # before taking a next letter in the morse code make it morsecode_letter variable empty,
                # in order to fetch next consecutive string in morse code
                morsecode_letter = ""

    return decipher_text


# keep perform operation, until you want to end the operation.
should_continue = False
while not should_continue:
    start = input("Welcome to Morse Code Converter."
                  " Type 'Encrypt' to encrypt a message or "
                  "'Decrypt' to decrypt a given message. \n").lower()
    if start != "encrypt" and start != "decrypt":
        print("Enter a valid input")
        break
    message = input("Type a message, which you wanna convert: \n").upper()
    if start == "encrypt":
        encrypted_text = encrypt_message(message)
        print(encrypted_text)
    elif start == "decrypt":
        result = decrypt(message)
        print(result)


    operation = input("You want to end the operation, Type 'Y' to continue or 'N' to exit. \n").lower()
    if operation == 'n':
        should_continue = True





