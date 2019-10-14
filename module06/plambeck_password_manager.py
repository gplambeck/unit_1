#! python3                      (Windows shebang line)
#! /usr/bin/env python3         (OS X shebang line)
# plambeck_password_manager.py - A quasi-secure password manager.

import sys, pprint, pyperclip, random

menuItems = {'Encrypt password': 'e',
             'Decryt password': 'd',
             'Add new password to the dictionary': 'a',
             'Retrieve password': 'r',
             'Generate a new password': 'g',
             'Exit': 'x'}
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}
alphanum = '0123456789abcdefghijklmnopqrstuvwxyz'
nouns = ['tissue', 'processor', 'headquarters', 'favorite', 'cure', 'ideology',
         'funeral', 'engine', 'isolation', 'perception', 'hat', 'mountain',
         'session', 'case', 'legislature', 'consent', 'spread', 'shot',
         'direction', 'data', 'tragedy', 'illness', 'serving', 'mess',
         'resistance', 'basis', 'kitchen', 'mine', 'temple', 'mass', 'dot',
         'final', 'chair', 'picture', 'wish', 'transfer', 'profession',
         'suggestion', 'purse', 'rabbit', 'disaster', 'evil', 'shorts', 'tip',
         'patrol', 'fragment', 'assignment', 'view', 'bottle', 'acquisition',
         'origin', 'lesson', 'Bible', 'act', 'constitution', 'standard',
         'status', 'burden', 'language', 'voice', 'border', 'statement',
         'personnel', 'shape', 'computer', 'quality', 'colony', 'traveler',
         'merit', 'puzzle', 'poll', 'wind', 'shelter', 'limit', 'talent']
verbs = ['represent', 'warm', 'whisper', 'consider', 'rub', 'march', 'claim',
         'fill', 'present', 'complain', 'offer', 'provoke', 'yield', 'shock',
         'purchase', 'seek', 'operate', 'persist', 'inspire', 'conclude',
         'transform', 'add', 'boast', 'gather', 'manage', 'escape', 'handle',
         'transfer', 'tune', 'born', 'decrease', 'impose', 'adopt', 'suppose',
         'sell', 'disappear', 'join', 'rock', 'appreciate', 'express', 'finish',
         'modify', 'keep', 'invest', 'weaken', 'speed', 'discuss', 'facilitate',
         'question', 'date', 'coordinate', 'repeat', 'relate', 'advise',
         'arrest', 'appeal', 'clean', 'disagree', 'guard', 'gaze', 'spend',
         'owe', 'wait', 'unfold', 'back', 'waste', 'delay', 'store', 'balance',
         'compete', 'bake', 'employ', 'dip', 'frown', 'insert']
adjs = ['busy', 'closer', 'national', 'pale', 'encouraging', 'historical',
        'extreme', 'cruel', 'expensive', 'comfortable', 'steady', 'necessary',
        'isolated', 'deep', 'bad', 'free', 'voluntary', 'informal', 'loud',
        'key', 'extra', 'wise', 'improved', 'mad', 'willing', 'actual', 'OK',
        'gray', 'little', 'religious', 'municipal', 'just', 'psychological',
        'essential', 'perfect', 'intense', 'blue', 'following', 'Asian',
        'shared', 'rare', 'developmental', 'uncomfortable', 'interesting',
        'environmental', 'amazing', 'unhappy', 'horrible', 'philosophical',
        'American']

# Function that displays the menu
def printMenu(itemsDict, leftWidth, rightWidth):
    print('MENU'.center(leftWidth + rightWidth, '='))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
    
# This function makes sure that the key has every character in alphanum and
# each character is used once.
def checkValidKey(Key):
    keyList = list(Key)
    alphanumList = list(alphanum)
    keyList.sort()
    alphanumList.sort()
    if keyList != alphanumList:
        sys.exit('There is an error in the key set.')

# Function that translates the characters in the message to their
# corresponding replacement.
def translateMessage(Key, message, mode):
    translated = ''
    charsA = alphanum
    charsB = Key
    # for decrypting swap where the key and alphanum strings are used.
    if mode == 'd':
        charsA, charsB = charsB, charsA
    # loop through each symbol in the message
    for char in message:
        if char.lower() in charsA:
            # encrypt/decrypt starts here
            charIndex = charsA.find(char.lower())   
            if char.islower():
                translated += charsB[charIndex].lower()
            else:
                translated += charsB[charIndex].upper()
            # encrypt/decrypt ends here
        # if character is not in alphanum, just add it
        else:
            translated += char
    return translated

# Encrypt function.
def encrypt(Key, message):
    return translateMessage(Key, message, 'e')

# Decrypt function.
def decrypt(Key, Ciphertext):
    return translateMessage(Key, Ciphertext, 'd')
    
# Function adds new passwords to the PASSWORDS dictionary
def addPW():
    dictKey = input('Enter a key label: ')
    dictValue = input('Enter a password: ')
    PASSWORDS[dictKey] = dictValue
    pprint.pprint(PASSWORDS)

# Function retrieves password and copies it to the dictionary
def retrievePW():
    print('Enter the account you wish to retreive:')
    account = input()
    if account in PASSWORDS:
        print('Password for ' + account + ' is: ' + str(PASSWORDS[account]))
        pyperclip.copy(PASSWORDS[account])
        print('Password for ' + account + ' copied to clipboard.')
    else:
        print('There is no account named ' + account + '.')

# A function that will replace the first two occurrences of l, e, o. or a in the
# password with 1, 3, 0, or @ respectively
def replaceNum(mainString, toReplace):
    # Iterate over the strings to be replaced
    for elem in toReplace:
        # Checks if l, e, o or a are in the new password
        if elem == 'l' in mainString:
            # Replaces first two occurrences of l in the string with 1
            mainString = mainString.replace(elem, '1', 2)
        elif elem == 'e' in mainString:
            # Replaces first two occurrences of e in the string with 3
            mainString = mainString.replace(elem, '3', 2)
        elif elem == 'o' in mainString:
            # Replaces first two occurrences of o in the string with 0
            mainString = mainString.replace(elem, '0', 2)
        elif elem == 'a' in mainString:
            # Replaces first two occurrences of a in the string with @
            mainString = mainString.replace(elem, '@', 2)
    
    return  mainString

"""Feature:
Must provide a username and password to enter the program. If the username
and/or password is incorrect, the while loop will continue until the username
and password are both correct.
After each task is done the user will have the option to continue with another
task or exit the program."""
while True:
    username = 'lumberjack'
    password = 'spamPumpkinSpice'
        
    entry1 = input('Enter your username: ')
    if entry1 != username:
        continue
    entry2 = input('Enter your password: ')
    if entry2 == password:
        break
print('Access granted.')

while True:
    # prints the menu options
    printMenu(menuItems, 40, 6)
    print()

    # choosing mode
    selection = ['e', 'd', 'a', 'r', 'g', 'x']
    mode = input('Enter a menu selection (e, d, a, r, g, x): ')
    mode = mode.lower()
    while mode not in selection:
        mode = input('Enter a menu selection (e, d, a, r, g, x): ')

    # run encryption/decryption
    if mode == 'e' or mode == 'd':
        key = input('Enter a key using each letter a-z and number 0-9 once: ')
    
        checkValidKey(key)

        if mode == 'e':
            for k, v in PASSWORDS.items():
                print(k + ': ' + str(v))
                translated = encrypt(key, str(v))
                print('Enctrypted: ' + translated)
        else:
            while True:
                print('Enter your password to run decryption:')
                decryptPassword = input()
                if decryptPassword == 'swordfish':
                    break
            ciphertext = input('Enter ciphertext: ')
            translated = decrypt(key, ciphertext)
            print('The password is: ' + translated)
    
    # run add password to dictionary
    elif mode == 'a':
        addPW()

    # run retrieve password
    elif mode == 'r':
        retrievePW()
    
    # Password Generator
    elif mode == 'g':
        words = [nouns, verbs, adjs]
        # four random words from the list of nouns, verbs and adjs
        word1 = random.choice(nouns)
        word2 = random.choice(verbs)
        word3 = random.choice(adjs)
        word4 = random.choice(random.choice(words))

        # password with two middle words capitalized
        capWord2 = word2.capitalize()       # Second word is capitalized
        capWord3 = word3.capitalize()       # Third word is capitalized
        password_cap = word1 + capWord2 + capWord3 + word4

        # new password option
        new_password = replaceNum(password_cap, ['l', 'e', 'o', 'a'])
        # prints result
        print('Password is: ' + new_password)
    
    # exit program immediately
    else:
        break

    # continue/exit the program
    ans_choice = ['y', 'n']
    answer = input('Do you want to exit? (y/n): ')
    answer = answer.lower()         # converts uppercase to lowercase

    # takes care of an invalid answer
    while answer not in ans_choice:
        answer = input('Enter y or n: ')
        answer = answer.lower()
    print()

    # if answer is y then condition is True
    if answer == 'y':
        break

# Exiting the program
print('\nGoodbye!')
