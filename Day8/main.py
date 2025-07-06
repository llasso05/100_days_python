# 26 letters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', " "]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number: \n"))


def encrypt(original_text, shift_amount):
    encrypted_index = []
    # iterating original message
    for letter in original_text:
        # adding shift to the indexes
        if letter in alphabet:
            letter_index = alphabet.index(letter) + shift_amount
            # calculating index over z
            if letter_index > 26:
                new_letter_index = letter_index - 27
                encrypted_index.append(new_letter_index)
            # setting new encrypted index
            elif letter_index < 26:
                encrypted_index.append(letter_index)
    print(encrypted_index)
    encrypted_message = ""
    # encrypting message
    for i in encrypted_index:
        encrypted_message += alphabet[i]
    print(f"here is the encrypted message {encrypted_message}")


# encrypt(text, shift)
# jiraibqniwneibnab

# TODO-1 : Create a function called decrypt() that takes original text and shift the amount of inputs
def decrypt(original_text, shift_amount):
    decrypted_message = ""
    # iterate index
    for letter in original_text:
        letter_index = alphabet.index(letter) - shift_amount
        letter_index %= len(alphabet)
        decrypted_message += alphabet[letter_index]

    print(decrypted_message)


decrypt(text, shift)


# TODO-2 : inside the decrypt function shift each letter of the "original text forward in the alphabeth
# and backwards the shift amount
# TODO-3 combine the encryp and decrypt funcions into a single function called caesar
# Use the value of the user chosen fuunctin direction variable to determine which functionality to use
# call thecaesar function isntead of the encrypt/Decrypt and pass all 3 variables.

# def caesar(original_text, shift, direction)
#
# if direction == 'encrypt':
#     encrypt(text, shift)
# elif direction == 'decrypt':
#     decrypt(text, shift)

