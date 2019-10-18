"""
Angie Melody

Review the Password Locker project in Chapter 6 in ATBS.
You should recreate the code and add your comments noting and predicting functionality.

Next, revisit your Python Password Generator and Encryption projects.
Using your Password Locker starter code, see if you can reuse and/or modify your code to:

1) Encrypt and decrypt the passwords saved in the dictionary.
2) A master password is required for decryption.
3) Handle the conditionals and exception handlers for incorrect passwords.
4) Create a "menu" consisting of nicely formatted strings that provide the user options to:
    - add new passwords to the dictionary,
    - retrieve passwords, and
    - generate random passwords that are "strong" according to XKCD.
5a) Lastly, design a feature of your own choosing!  This is the "create" portion of the project.
   You may want to look at
       - https://www.lastpass.com/ and
       - https://keepass.info/ for inspiration.
5b) It is VERY important that you provide a multi-line comment that thoroughly explains your feature.
"""


#! python3
# pw.py - An insecure password locker program.

# >>>>>>>>>> imports <<<<<<<<<<<
import sys, pyperclip, getpass
import random  #>>>>> Used by password generator function <<<<<

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>> FUNCTIONS  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def genRandomPwd():
    # >>>>>>>>>> Below list used for validating the length of the password <<<<<<<<<<<
    possibleLengths = ['20','21','22','23','24','25','26','27','28','29','30']

    #>>>>>>>>>>>  Values allowed in the password <<<<<<<<<
    #ltrsNums = "abcdefghijklmnopqrstuvwxyz 0123456789_-!@#$&ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #>>>>>>>>>> String to hold the password value <<<<<<<<<<
    simplePassword=''
    #>>>>>>>>>> Boolean flag for testing that inputted value is valid <<<<<<<<<<
    count1 = True

    # >>>>>>>>>> Determining length of password <<<<<<<<<<
    pwdLength = (input("\nHow many characters would you like in the password? [Input # from 20-30]: "))

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
        #entry = ltrsNums[alpha_choice]
        entry = alpha_str[alpha_choice]
        #>>>>>>>>>> If the user selects a 1, treat it as a request to uppercase the value <<<<<<<<<<
        if uplow_choice == 1:
            entry = entry.upper()
        #Concatenate the password with each additional character <<<<<<<<<<
        simplePassword = simplePassword + entry

    #print ("\nA randomly generated simple password:" , simplePassword)
    return simplePassword

def removeDuplicates(x):
  #>>>>>Passing a "string" parameter, turned into list, then dict and returned as a "string" <<<<<
        temp_list=list(dict.fromkeys(list(x)))
        nonDup_string = "".join(temp_list)
        return(nonDup_string) 

def removeDupsBtwnStrings(x,y):
  #>>>>>Passing two string parameters, removing string chars of first from second and returning second <<<<<
        str=''
        for z in x:
             y=y.replace(z, '')
        return(y) 


try:

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #>>>>>>>>>>>>>>>>>>>> Initializing Variables >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    alpha_input = ''
    plaintext_input = ''
    ciphertext =''
    plaintext=''
    mapped_dict = {}
    userchoice =0
    account_password = ''
    encrypted_password = ''
    loopTheMenu = True

    #>>>>> Populating the alpha list that will be used for generating a cryptic key, as well as for encrypting and decrypting logic <<<<<<<<<< 
    alpha_str = 'abcdefghijklmnopqrstuvwxyz 0123456789_-!@#$&?ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha_list = list(alpha_str)

    #>>>>> Populating some initial Passwords in the Dictionary with ENCRYPTED passwords <<<<<
    PASSWORDS = {'email': '?f33foTyFa4fSagfCralqNannRyoeTjaPTy?fjadpfe',
                 'yahoo':'TjlnGnTjfTlrfTyYajyy8MoEyyiqf'}

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #>>>>>>>>>>>>>>>>>>>>>>>>>> Prompt user to provide Master Password before allowing any other interaction >>>>>>>
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    #>>>>> Asking user to provide a password that will be used to generate the key.  The same key is used to encrypt and decrypt <<<<<
    while True:
            passwd_input = getpass.getpass(prompt = "\n\nInput your Master password: \n")
            if len(passwd_input.strip())<9:
                 print ("The password must be at least 9 characters.")
            else:
                 break
    #>>>>>Removing any duplicate characters in the password that is provided by the user <<<<<
    strClnPwd=removeDuplicates(passwd_input.strip())

    #>>>>>Locating the last character of the password and finding the index for this in the alphabetical list <<<<<
    lastCharPwd = strClnPwd[-1:]
    indexvalue = alpha_list.index(lastCharPwd)

    #>>>>>Creating two sliced lists based on the index associated with the last character of the password <<<<<
    alpha_list1 = alpha_list[:indexvalue]
    alpha_list2 = alpha_list[indexvalue:]

    #>>>>>Cleaning each sliced list of any duplicate letters that are in the password <<<<<
    strClnAlpha1=removeDupsBtwnStrings(strClnPwd,"".join(alpha_list1))
    strClnAlpha2=removeDupsBtwnStrings(strClnPwd,"".join(alpha_list2))


    #>>>>>Concatenating the sliced lists and the password to create a scrambled alphabetic KEY list <<<<< 
    key = list(strClnAlpha1+strClnPwd+strClnAlpha2)

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #>>>>>>>>>>>>>>>>>>>>>>>>>> Prompt user with a Menu >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    while loopTheMenu:        
        while True:
            Menu = ['1 - Add a password to locker (manual or random)',
                    '2 - Retrieve an account password to your clipboard',
                    '3 - Use clipboard to add a new password',
                    '4 - Display list of accounts that are in the system',
                    '5 - Delete an account that is in the system',
                    '6 - Exit']
            print("\nChoose a numeric option:")
            for i in range(len(Menu)):
                print(Menu[i])
            print("")
            selected_option = str( input())
            if selected_option not in ['1','2','3','4','5','6']:
                print ("That was not a valid entry.")
            else:
                break

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        #>>>>>>>>>>>>>>>>>>>>>>> User wants to Add a password to the Dictionary >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        if selected_option == '1':
            while True:
                accountname = input("\nInput Account Name: ").lower()
                if len(accountname.strip())==0:
                     print ("Invalid Account Name inputted.")
                elif accountname in PASSWORDS.keys():
                        print ("There is already a password associated with this account name.")
                else:
                     break
            #>>>>> Determine if user wants to create their own passphrase or if they want a random entry generated <<<<<
            while True:
                Menu = ['1 - Provide a pass-phrase (min 20 characters)',
                        '2 - Let system generate a random lengthy password']
                print("\nChoose a numeric option:")
                for i in range(len(Menu)):
                    print(Menu[i])
                print("")
                userchoice = str( input())
                if userchoice not in ['1','2']:
                    print ("That was not a valid entry.")
                else:
                    break

            #>>>>> Below: User indicated they want to provide the passphrase to encrypt <<<<<
            if userchoice =='1':
                    #>>>>> Requesting from user a phrase they want to encrypt <<<<<
                    while True:
                           account_password = input('''
Input a passphrase that is at least 20 characters
Allowable characters: a-z, A-Z, 0-9 and the symbols: _ - ! ? @ # $ &  \n''')
                           invalid_chars = False
                           for character in account_password:
                                if character not in alpha_str:
                                    print ("'" + character + "' is not an allowable entry in the passphrase.")
                                    invalid_chars=True
                           if len(account_password.strip())<20:
                                print ("The phrase must be at least 20 character.")
                           elif invalid_chars == False:
                                break
            else:
                #>>>>> Generate a random password for this account <<<<<
                account_password = genRandomPwd()

            print(account_password)
            
            #>>>>> Encrypt the newly created password <<<<<
             #>>>>> Creating a dictionary that maps the existing alpha_list into a scrambled list of alphanumeric (aka "key") <<<<<
            for i in range(len(alpha_list)):
                    mapped_dict[alpha_list[i]] = key[i]

            #>>>>> Loop through each character of the unencrypted password, and replace each character with the encrypted value 
            #>>>>> Concatenate the individual encrypted characters into an encrypted string
            #>>>>> Getting encrypted mappings from dictionary.
            #>>>>> If no entry found in dictionary, such as for a blank space, concatenate a space to the string via the "get" method
            encrypted_password=''
            for character in account_password:
                encrypted_password += mapped_dict.get(character,' ')

            PASSWORDS[accountname]= encrypted_password
            print (PASSWORDS.items())
            print("\nA password has been added for '"+ accountname+"'\n")
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        #>>>>>>>>>>>>>>>>>>>>>>> User wants to Retrieve a password from the Dictionary >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        if selected_option == '2':
            while True:
                accountname = input("\nInput Account Name: ").lower()
                if len(accountname.strip())==0:
                     print ("Invalid Account Name inputted.")
                elif accountname in PASSWORDS.keys():
                     break   
                else:
                     print ("'" + accountname + "'" + " is not in the system.")
             
            encrypted_password = PASSWORDS[accountname]
            print("Encrypted Password: "+encrypted_password)
            
            #>>>>> The looping range is determined by the number of entries in the list that are being encrypted <<<<
            #>>>>> Creating a dictionary that maps the scrambled alph/numbers (aka "key") to the original alphabet <<<<<
            for i in range(len(alpha_list)):
                    mapped_dict[key[i]] = alpha_list[i]

            #>>>>> Loop through each character of the encrypted password, and replace each character with the unencrypted value
            #>>>>> Concatenate the individual unencrypted characters into a plaintext string
            #>>>>> Getting decrypted mappings from dictionary.
            #>>>>> If no entry found in dictionary, such as for a blank space, concatenate a space to the string
            decrypted_password =''
            for character in encrypted_password:
                decrypted_password += mapped_dict.get(character,' ')


            #print("Decrypted Password: " + decrypted_password)
            pyperclip.copy(decrypted_password)
            print("\nPassword for '" + accountname + "' has been copied to your clipboard.")
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        #>>>>>>>>>>>>>>>>>>>>>>> User wants to add a Password via their Clipboard >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # This is an added feature to allow the user to copy and paste a passphrase
        # The user can copy their passphrase before or during the process
        # The user must still provide a valid non-used account name but then they can use their clipboard as a source for the password
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        if selected_option == '3':
            while True:
                accountname = input("\nInput Account Name: ").lower()
                if len(accountname.strip())==0:
                     print ("Invalid Account Name inputted.")
                elif accountname in PASSWORDS.keys():
                        print ("There is already a password associated with this account name.")
                else:
                     break

            while True:
               input('Capture the phrase you wish to use in your clipboard, then press the <Enter> key ')
               account_password = pyperclip.paste()
               #print(account_password)
               invalid_chars = False
               for character in account_password:
                    if character not in alpha_str:
                        print ("'" + character + "' is not an allowable entry in the passphrase.")
                        invalid_chars=True
               if len(account_password.strip())<20:
                    print ("The phrase must be at least 20 character.")
               elif invalid_chars == False:
                    break

            #print(account_password)
            
            #>>>>> Encrypt the newly created password <<<<<
             #>>>>> Creating a dictionary that maps the existing alpha_list into a scrambled list of alphanumeric (aka "key") <<<<<
            for i in range(len(alpha_list)):
                    mapped_dict[alpha_list[i]] = key[i]

            #>>>>> Loop through each character of the unencrypted password, and replace each character with the encrypted value 
            #>>>>> Concatenate the individual encrypted characters into an encrypted string
            #>>>>> Getting encrypted mappings from dictionary.
            #>>>>> If no entry found in dictionary, such as for a blank space, concatenate a space to the string via the "get" method
            encrypted_password=''
            for character in account_password:
                encrypted_password += mapped_dict.get(character,' ')

            PASSWORDS[accountname]= encrypted_password
            #print (PASSWORDS.items())

            print("\nA password has been added via your clipboard for '"+ accountname+"'\n")
           
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        #>>>>>>>>>>>>>>>>>>>>>>> User wants to see a list of all accounts that are in the Dictionary >>>>>>>>>>>>>>>>>>
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # This is an added feature to allow the user to see all of their existing account names
        # This is useful so that they can delete an existing entry if they have created a new password
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        if selected_option == '4':
           print("\nAccount Names:")
           for v in sorted(PASSWORDS.keys()):
               print("  - "+ v)
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        #>>>>>>>>>>>>>>>>>>>>>>> User wants to delete an account from the Dictionary >>>>>>>>>>>>>>>>>>
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # This is an added feature to allow the user to delete an account entry
        # The user inputs a specific account name (case insensitive)
        # The entry is removed from the dictionary
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        if selected_option == '5':
           while True:
                accountname = input("\nInput Account Name that you wish to delete: ").lower()
                if len(accountname.strip())==0:
                     print ("Invalid Account Name inputted.")
                elif accountname in PASSWORDS.keys():
                     break   
                else:
                     print ("\n'" + accountname + "'" + " is not in the system.")
           if len(accountname.strip())>0:
                del PASSWORDS[accountname]
                print ("\n'" + accountname + "'" + " has been successfully removed from the system.\n")
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        #>>>>>>>>>>>>>>>>>>>>>>> User wants to exit program >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        if selected_option == '6':
           loopTheMenu = False
           print("Have a wonderful day.")
           sys.exit()

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        #>>>>>>>>>>>>>>>>>>>>>>> Give user the opportunity to perform more Menu actions >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>           

        promptToContinue = input("\nPerform more actions? (Y/N): ")
        if promptToContinue.lower() == 'n':
            loopTheMenu = False


except ValueError:
    print('Error: Only the option 1, 2, 3, 4,5 or 6 is accepted.')

