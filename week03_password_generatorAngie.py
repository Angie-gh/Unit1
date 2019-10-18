'''
1, Create a "traditional" password using lowercase characters, UPPERCASE characters, and numbers.

2. Follow the XKCD model of selecting four random words and concatenating them together to for your password.

3. Of course, the above password does not make the IT department of most colleges and businesses happy.
They still want you to have at least one capital letter and a number in your password.
We’ll learn more about this in a couple of chapters but it is easy to replace parts of a string with a
different string using the replace method.

For example "pool".replace('o', 'e') gives us peel
Once you have your final password you can replace some letters with number substitutions.
For example its common to replace the letter l with the number 1 or the letter e with the number 3 or the o with a 0.
You can get creative. For example, you can also easily capitalize a word using "myword".capitalize().
'''
# >>>>>>>>>> imports <<<<<<<<<<<
import random

# >>>>>>>>>> Validating the length of the password <<<<<<<<<<<
possibleLengths = ['4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
#>>>>>>>>>>>  Values allowed in the password <<<<<<<<<
ltrsNums = "abcdefghijklmnopqrstuvwxyz0123456789"
#>>>>>>>>>> String to hold the password value <<<<<<<<<<
simplePassword=''
#>>>>>>>>>> Boolean flag for testing that inputted value is valid <<<<<<<<<<
count1 = True

# >>>>>>>>>> Determining if Player 1 will play against the system or with another player <<<<<<<<<<
pwdLength = (input("\nHow long would you like the password? [Input number between 4-20]: "))

if pwdLength in possibleLengths:
    count1 = False

#>>>>>>>>>> Testing that inputted value is within the specified range <<<<<<<<<<
while count1:
    if pwdLength not in possibleLengths:
       print("Invalid Entry")
       pwdLength = input("Please input another value: ")
       if pwdLength in possibleLengths:
           count1 = False

#>>>>>>>>>> Convert the string input to an integer <<<<<<<<<<
pwdLength = int(pwdLength)

#>>>>>>>>>> Loop through a range to generate random password characters and numbers <<<<<<<<<<
for x in range(pwdLength):
    #>>>>>>>>>> Select a random entry for the allowable list <<<<<<<<<<
   # letter  = random.choice(ltrsNums)
    #>>>>>>>>>> Select a random integer <<<<<<<<<<
    alpha_choice = random.randrange(0, 36)
    #>>>>>>>>>> Select a 0 or 1 <<<<<<<<<<
    uplow_choice = random.randrange(0,2)
    #>>>>>>>>>> select a random alphanumeric character from list by uaing the random number <<<<<<<<<<
    entry = ltrsNums[alpha_choice]
    #>>>>>>>>>> If the user selects a 1, treat it as a request to uppercase the value <<<<<<<<<<
    if uplow_choice == 1:
        entry = entry.upper()
    #Concatenate the password with each additional character <<<<<<<<<<
    simplePassword = simplePassword + entry

print ("\nA randomly generated simple password:" , simplePassword)


print ("\n\n*************************************************************")
input ("Next we will create a 4 word password.  Press <Enter> to Continue\n")

nouns = ['tissue', 'processor', 'headquarters', 'favorite', 'cure', 'ideology', 'funeral', 'engine', 'isolation', 'perception', 'hat', 'mountain', 'session', 'case', 'legislature', 'consent', 'spread', 'shot', 'direction', 'data', 'tragedy', 'illness', 'serving', 'mess', 'resistance', 'basis', 'kitchen', 'mine', 'temple', 'mass', 'dot', 'final', 'chair', 'picture', 'wish', 'transfer', 'profession', 'suggestion', 'purse', 'rabbit', 'disaster', 'evil', 'shorts', 'tip', 'patrol', 'fragment', 'assignment', 'view', 'bottle', 'acquisition', 'origin', 'lesson', 'Bible', 'act', 'constitution', 'standard', 'status', 'burden', 'language', 'voice', 'border', 'statement', 'personnel', 'shape', 'computer', 'quality', 'colony', 'traveler', 'merit', 'puzzle', 'poll', 'wind', 'shelter', 'limit', 'talent']
verbs = ['represent', 'warm', 'whisper', 'consider', 'rub', 'march', 'claim', 'fill', 'present', 'complain', 'offer', 'provoke', 'yield', 'shock', 'purchase', 'seek', 'operate', 'persist', 'inspire', 'conclude', 'transform', 'add', 'boast', 'gather', 'manage', 'escape', 'handle', 'transfer', 'tune', 'born', 'decrease', 'impose', 'adopt', 'suppose', 'sell', 'disappear', 'join', 'rock', 'appreciate', 'express', 'finish', 'modify', 'keep', 'invest', 'weaken', 'speed', 'discuss', 'facilitate', 'question', 'date', 'coordinate', 'repeat', 'relate', 'advise', 'arrest', 'appeal', 'clean', 'disagree', 'guard', 'gaze', 'spend', 'owe', 'wait', 'unfold', 'back', 'waste', 'delay', 'store', 'balance', 'compete', 'bake', 'employ', 'dip', 'frown', 'insert']
adjs = ['busy', 'closer', 'national', 'pale', 'encouraging', 'historical', 'extreme', 'cruel', 'expensive', 'comfortable', 'steady', 'necessary', 'isolated', 'deep', 'bad', 'free', 'voluntary', 'informal', 'loud', 'key', 'extra', 'wise', 'improved', 'mad', 'willing', 'actual', 'OK', 'gray', 'little', 'religious', 'municipal', 'just', 'psychological', 'essential', 'perfect', 'intense', 'blue', 'following', 'Asian', 'shared', 'rare', 'developmental', 'uncomfortable', 'interesting', 'environmental', 'amazing', 'unhappy', 'horrible', 'philosophical', 'American']

# >>>>>>>>>> Make a four word password by combining words from the list of nouns, verbs and adjs <<<<<<<<<<

# >>>>>>>> Initializing variables <<<<<<<<<<
password2 = ''
value=''

for y in range(4):
        #>>>>>>>>>> Select a random integer - this will determine what table to rerieve from <<<<<<<<<<
        c1 = random.randrange(0, 3)
        if c1 ==0:
            value = random.choice(nouns)
        if c1 == 1:
            value = random.choice(verbs)
        else:
            value = random.choice(adjs)
        #>>>>>>>>>> Adding a capitalization randomly <<<<<<<<<<
        c2 = random.randrange(0, 2)
        if c2 == 1:
            value = value.capitalize()
        #print(c1)
        #print(value)
        #>>>>>>>>> Concatenate the selected list value to the password that is being created <<<<<<<<
        password2=password2 + value

# >>>>>>>>>> Replace some of the characters with other values <<<<<<<<<<
password2 = password2.replace('s','$')
password2 = password2.replace('o','0')
password2 = password2.replace('e','3')

# >>>>>>>>>> Replace values in the string with numeric values <<<<<<<<<<
print( "\nA password that is generated from 3 lists and replacing some chars:\n",password2 )        



