# Computer guesses what the password is and displays the number of guesses.

import random, time

# Set the execution limit to 60 seconds
t_end = time.time() + 60

characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",\
 "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print('Enter a 4 character password composed only of lower case letters.')
my_password = input('Enter password: ')
password_length = len(my_password)

# The crack() function creates a random combination from the characters list
# and compares it to the target password. It repeats this until it guesses the
# correct password.
def crack():
    global my_password, password_length
    guess_num = 0    
    done = False
    while not done:
        guessed_pw = ""
        # Create a string from randomly chosen characters
        while len(guessed_pw) < password_length:
            # Add a random index from the characters list
            guessed_pw += random.choice(characters)
        # Compare guess to the real password
        if guessed_pw == my_password:
            print("found it after ", guess_num, " tries")
            done = True
        else:
            guess_num += 1

while my_password != "" and time.time() <= t_end:
    done = False
    crack()
