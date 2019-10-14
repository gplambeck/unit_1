# Part 1 Substitution Cipher
    # Secret Message: B K F T A Z D A O W E
    # Decoded:        p y t h o n r o c k s

#  Part 2 Caesar Cipher Encrypt lowercase characters
def encrypt(text, shift):
    cipher = ''
    for i in range(len(text)):
        char = text[i]
        # chr() takes an integer ordinal and returns a single-character string.
        # ord() takes a single-character string and returns the integer ordinal value.
        cipher += chr((ord(char) - 97 + shift) % 26 + 97)   # ASCII value of 'a' is 97
    return cipher

plaintext = 'thequickbrownfoxjumpsoverthelazydog'
shift = 13
print('Message:     ' + plaintext)
print('Shift:       ' + str(shift))
print('Encrypted:   ' + encrypt(plaintext, shift))

#  Part 3 Caesar Cipher Decrypt lowercase characters
def decrypt(text, shift):
    result = ''
    for i in range(len(text)):
        char = text[i]
        result += chr((ord(char) - 97 - shift) % 26 + 97)   # ASCII value of 'a' is 97
    return result

ciphertext = 'dzeevjfkrlezkvuwffksrcctcls'
i = 0
while i < 25:
    shift = i + 1
    print('Shift of ' + str(i + 1) + ' results: ' + decrypt(ciphertext,shift))
    i += 1

# The plaintext message is minnesotaunitedfootballclub and the shift is 17.

# Part 4 Scrambled Key Encrypt lowercase message by substitution
import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz '
key =      'mwgp bdzxrylacsokjfhtnueivq'
plaintext = 'of shoes and ships and sealing wax of cabbages and kings'

# This function makes sure that the key has every letter in the alphabet and
# each letter is used once.
def checkValidKey(Key):
     keyList = list(Key)
     alphabetList = list(alphabet)
     keyList.sort()
     alphabetList.sort()
     if keyList != alphabetList:
         sys.exit('There is an error in the key or symbol set.')

# Translates the letters in the message to their corresponding replacement.
def translateMessage(Key, message):
    translated = ''
    charsA = alphabet
    charsB = Key
    # loop through each symbol in the message
    for char in message:
        if char.lower() in charsA:
            charIndex = charsA.find(char.lower())
            translated += charsB[charIndex].lower()
        # if character is not in alphabet, just add it
        else:
            translated += char
    return translated

# The encrypt function.
def encrypt(Key, message):
    return translateMessage(Key, message)

checkValidKey(key)

ciphertext = encrypt(key, plaintext)
print('The message is: ' + plaintext)
print('Encrypted:      ' + ciphertext)

# Part 5 Scrambled Key Decrypt lowercase message by substitution
import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz '
key =      'mwgp bdzxrylacsokjfhtnueivq'
ciphertext = 'hz qftcqumfqfzxcxcdqscqhz qf mqfzxcxcdquxhzqmllqzxfqaxdzh'

# This function makes sure that the key has every character in alphabet
# and each character is used once.
def checkValidKey(Key):
     keyList = list(Key)
     alphabetList = list(alphabet)
     keyList.sort()
     alphabetList.sort()
     if keyList != alphabetList:
         sys.exit('There is an error in the key or symbol set.')

# Translates the characters in ciphertext to their corresponding replacement.
def translateMessage(Key, Ciphertext):
    translated = ''
    charsA = alphabet
    charsB = Key
    # loop through each symbol in ciphertext
    for char in Ciphertext:
        if char.lower() in charsB:
            charIndex = charsB.find(char.lower())
            translated += charsA[charIndex].lower()
        # if character is not in key, just add it
        else:
            translated += char
    return translated

# The decrypt function.
def decrypt(Key, Ciphertext):
    return translateMessage(Key, Ciphertext)

checkValidKey(key)

plaintext = decrypt(key, ciphertext)
print('ciphertext is: ' + ciphertext)
print('plaintext is:  ' + plaintext)

# Part 6 Scrambled Key Encrypt/Decrypt scrambled alphabet program
import sys

print('Make all entries lowercase characters a-z and a space.')

alphabet = 'abcdefghijklmnopqrstuvwxyz '

# choosing to encrypt or decrypt
selection = ['e', 'd']
mode = input('Enter e to encrypt or d to decrypt: ')
while mode not in selection:
    mode = input('Enter e to encrypt or d to decrypt: ')

key = input('Enter a key using each letter a-z and a space once: ')

# This function makes sure that the key has every character in the alphabet and
# each character is used once.
def checkValidKey(Key):
     keyList = list(Key)
     alphabetList = list(alphabet)
     keyList.sort()
     alphabetList.sort()
     if keyList != alphabetList:
         sys.exit('There is an error in the key set.')

# Translates the letters in the message to their corresponding replacement.
def translateMessage(Key, message, mode):
    translated = ''
    charsA = alphabet
    charsB = Key
    # For decrypting swap where the key and alphabet strings are used.
    if mode == 'd':
        charsA, charsB = charsB, charsA
    # loop through each symbol in the message
    for char in message:
        if char.lower() in charsA:
            charIndex = charsA.find(char.lower())
            translated += charsB[charIndex].lower()
        # if character is not in alphabet, just add it
        else:
            translated += char
    return translated

# The encrypt function.
def encrypt(Key, message):
    return translateMessage(Key, message, 'e')

# The decrypt function.
def decrypt(Key, Ciphertext):
     return translateMessage(Key, Ciphertext, 'd')

checkValidKey(key)

if mode == 'e':
    plaintext = input('Enter a message: ')
    translated = encrypt(key, plaintext)
    print('Encrypted: ' + translated)
else:
    ciphertext = input('Enter ciphertext: ')
    translated = decrypt(key, ciphertext)
    print('The message is: ' + translated)
    