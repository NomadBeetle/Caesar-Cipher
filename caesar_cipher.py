from art import logo  
print(logo)  # Display the ASCII logo

# Alphabet list for shifting letters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function to decrypt text
def decrypt(original_text, shift_amount):
    decrypted_text = ""
    for letter in original_text:
        if letter.isalpha():  # Only shift letters
            is_upper = letter.isupper()
            letter = letter.lower()
            shifted_position = (alphabet.index(letter) - shift_amount) % len(alphabet)
            decrypted_text += alphabet[shifted_position].upper() if is_upper else alphabet[shifted_position]
        else:
            decrypted_text += letter  # Keep non-letters unchanged
    print(f"Here is the decoded result: {decrypted_text}")

# Function to encrypt text
def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter.isalpha():
            is_upper = letter.isupper()
            letter = letter.lower()
            shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            cipher_text += alphabet[shifted_position].upper() if is_upper else alphabet[shifted_position]
        else:
            cipher_text += letter
    print(f"Here is the encoded result: {cipher_text}")

# Main function to handle user input
def caesar(task):
    if task == "encode":
        text = input("Type your message:\n")
        shift = int(input("Type the shift number:\n"))
        encrypt(text, shift)
    elif task == "decode":
        text = input("Type your message:\n")
        shift = int(input("Type the shift number:\n"))
        decrypt(text, shift)
    else:
        print("Invalid task, Try again please!")

# Loop to allow multiple uses
ans = "yes"
while ans == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    caesar(direction)
    ans = input("Type 'yes' if you want to go again. Otherwise, type 'no':\n").lower()

print("GOODBYE!")  # Exit message
