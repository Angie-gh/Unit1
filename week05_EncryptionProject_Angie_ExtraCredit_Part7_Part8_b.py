
"""
Finally, only a few truly amazing people are going to remember a random ording of 26 letters. We would like to have a way to use a password of around 7 characters. How can we use a password to scramble our alphabet into some order? Its not as bad as you might think at first. Do the following:

Remove any duplicate letters from the password.
Now split the alphabet into two halves The letters up to and including the last letter in the password and the rest of the alphabet.
Remove any letters in your password from the two halves of the alphabet.
The key is the concatenation of the password (without duplicate letters) followed by the second part of the split alphabet followed by the first part of the alphabet.
Part 7: Implement the algorithm outlined above assuming that the user entered ‘python’ for their password. Store the key in a variable called ‘key’. For testing purposes, assume that no spaces or punctuation are included in the alphabet or the password.

Part 8: Finally, work with your partner so that you can ask for a password and a message, using the password, construct the key, encrypt/decrypt the message and then print out the result.

"""
# >>>>>>>>>> imports <<<<<<<<<<<
import getpass

#>>>>>Initializing variables <<<<<
alpha_input = ''
plaintext_input = ''
ciphertext =''
plaintext=''
mapped_dict = {}
userchoice =0

#>>>>> Populating the alpha list <<<<<<<<<< 
alpha_str = 'abcdefghijklmnopqrstuvwxyz'
alpha_list = list(alpha_str)


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

#>>>>> Asking user to provide a password that will be used to generate the key.  The same key is used to encrypt and decrypt <<<<<
while True:
        cipher_input = getpass.getpass(prompt = "\nInput your password that will be used as the key to encrypt your phrase: ")
        if len(cipher_input.strip())<6:
             print ("The password must be at least 6 characters.")
        else:
             break
#>>>>>Removing any duplicate characters in the password that is provided by the user <<<<<
strClnPwd=removeDuplicates(cipher_input.strip())

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
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


#>>>>> Inquiring with user whether they want to encrypt or decrypt a phrase <<<<<
while True:
        userchoice = input('\nInput 1=Encrypt or 2=Decrypt: (1 or 2)')
        if userchoice not in ['1','2']:
             print ("Please choose one of the options.")
        else:
             break

#>>>>> Below: User indicated they want to encrypt a phrase <<<<<
if userchoice =='1':
        #>>>>> Requesting from user a phrase they want to encrypt <<<<<
        while True:
                plaintext_input = input('\nInput a phrase to encrypt: ').lower()
                if len(plaintext_input.strip())==0:
                     print ("The phrase must be at least 1 character.")
                else:
                     break

        plaintext = plaintext_input        

        #>>>>> Creating a dictionary that maps the normal alphabet to the scrambled alphabet (aka "key") <<<<<
        for i in range(len(alpha_list)):
                mapped_dict[alpha_list[i]] = key[i]

        #>>>>> Loop through each character of the plaintext string, and replace each character with the encrypted value 
        #>>>>> Concatenate the individual encrypted characters into an encrypted string
        #>>>>> Getting encrypted mappings from dictionary.
        #>>>>> If no entry found in dictionary, such as for a blank space, concatenate a space to the string via the "get" method
        for character in plaintext:
            ciphertext += mapped_dict.get(character,' ')

        #>>>>> Display the inputted plain text, the password, the altered alphabet KEY, and the encrypted phrase <<<<<
        print("\nThe inputted plain text:\n" + plaintext)
        print("\nThe inputted 'Password':\n"+ cipher_input)
        print("\nThe'Key':\n"+ "".join(key))
        print("\nThe encrypted output:\n" + ciphertext)

#>>>>> Below: User indicated they want to decrypt a phrase <<<<<
else:
        #>>>>> Requesting from user the string they want to decrypt <<<<<
        while True:
                cipher_text_input = input('\nInput an encrypted sentence that needs to be decrypted: ').lower()
                if len(cipher_text_input.strip())==0:
                     print ("The encrypted string must minimally have one character.")
                else:
                     break

        cipher_text = cipher_text_input        

        #>>>>> The looping range is determined by the number of entries in the list that are being encrypted <<<<
        #>>>>> Creating a dictionary that maps the scrambled alphabet (aka "key") to the original alphabet <<<<<
        for i in range(len(alpha_list)):
                mapped_dict[key[i]] = alpha_list[i]

        #>>>>> Loop through each character of the cipher_text string, and replace each character with the unencrypted value
        #>>>>> Concatenate the individual unencrypted characters into a plaintext string
        #>>>>> Getting decrypted mappings from dictionary.
        #>>>>> If no entry found in dictionary, such as for a blank space, concatenate a space to the string
        for character in cipher_text:
            plaintext += mapped_dict.get(character,' ')

        #>>>>> Display the inputted encrypted message, the password, the altered alphabet KEY, and the decrypted phrase <<<<<
        print("\nThe inputted encrypted text:\n" + cipher_text)
        print("\nThe inputted 'Password':\n"+ cipher_input)
        print("\nThe'Key':\n"+ "".join(key))
        print("\nThe decrypted output:\n" + plaintext)




