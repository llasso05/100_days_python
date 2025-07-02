# 26 letters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number: \n"))


def encrypt():
    encrypted_index = []
    # iterating original message
    for letter in text:
        # adding shift to the indexes
        if letter in alphabet:
            letter_index = alphabet.index(letter) + shift
            # calculating index over z
            if letter_index > 25:
                new_letter_index = letter_index - 26
                encrypted_index.append(new_letter_index)
            # setting new encrypted index
            elif letter_index < 25:
                encrypted_index.append(letter_index)
    print(encrypted_index)
    encrypted_message = ""
    # encrypting message
    for i in encrypted_index:
        encrypted_message += alphabet[i]
    print(encrypted_message)


encrypt()

