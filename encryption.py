import random
import string

def encrypt(sentence):
    mapping = string.ascii_letters 
        

    encrypted_sentence = ''
    for letter in sentence:
        encrypted_sentence += mapping

    return encrypted_sentence

# Example usage
input_sentence = input("Enter a password ")
encrypted_result = encrypt(input_sentence)
print("Encrypted password:", encrypted_result)
