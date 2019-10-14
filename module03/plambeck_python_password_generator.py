# Password generator

import random

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

# Original password
old_password = 'pumpkin5piceSPAM'

words = [nouns, verbs, adjs]
# Four random words from the list of nouns, verbs and adjs
word1 = random.choice(nouns)
word2 = random.choice(verbs)
word3 = random.choice(adjs)
word4 = random.choice(random.choice(words))

# First new password option
new_password1 = word1 + word2 + word3 + word4

# First new password option with two middle words capitalized
capWord2 = word2.capitalize()       # Second word is capitalized
capWord3 = word3.capitalize()       # Third word is capitalized
password_cap = word1 + capWord2 + capWord3 + word4

# A function that will replace the first two occurrences of l, e, o. or a in the
# password with 1, 3, 0, or @ respectively
def replaceNum(mainString, toReplace):
    # Iterate over the strings to be replaced
    for elem in toReplace:
        # Checks if l, e, or o are in the new password
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

# Second new password option
new_password2 = replaceNum(password_cap, ['l', 'e', 'o', 'a'])

# Prints results
print('Your current password is: ' + old_password)
print()
print('Choose one of the following new passwords.')
print('New Password 1: ' + new_password1)
print()
print('New Password 2: ' + new_password2)
