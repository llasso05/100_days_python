print("""
           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88        
""")
# 26 letters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', " "]
direction = ""
quit = ""


def encrypt(original_text, shift_amount):
    encrypted_message = ""
    # iterating original message
    for letter in original_text:
        # adding shift to the indexes
        if letter in alphabet:
            letter_index = alphabet.index(letter) + shift_amount
            letter_index %= len(alphabet)
            encrypted_message += alphabet[letter_index]
    print(f"here is the encrypted message {encrypted_message}")


# encrypt(text, shift)

# TODO-1 : Create a function called decrypt() that takes original text and shift the amount of inputs
def decrypt(original_text, shift_amount):
    decrypted_message = ""
    # iterate index
    for letter in original_text:
        letter_index = alphabet.index(letter) - shift_amount
        letter_index %= len(alphabet)
        decrypted_message += alphabet[letter_index]
    print(f"here is the encrypted message {decrypted_message}")


def caesar(original_text, shift_amount):
    if direction == 'encode':
        encrypt(original_text, shift_amount)
    elif direction == 'decode':
        decrypt(original_text, shift_amount)


while quit != "Y":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction not in ("decode", "encode"):
        print("Please type 'Decode' or 'Encode'")
        continue
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number: \n"))
    caesar(text, shift)
    quit = input("Do you want to quit (Y) for Yes, (N) for No\n")

