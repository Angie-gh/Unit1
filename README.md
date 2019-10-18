# Unit 1 - Reflections: Programming in Python
[Return to Home](https://angie-gh.github.io/adix.github.io/)


*********************************************************************************** 


### Purpose of this page:
We have completed half of a semester in Python Programming and are reflecting on the scripting basics that we have just learned.  The below comments are specific to me.

### Overall reaction to Python computing:
I find python to be an incredibly forgiving scripting language. I have scripted in other formats such as: batch, bash, lotuscript, and javascript(with ajax), but the python environment has a faster learning curve and allows the coder to be a minimalist.    

### Ah-ha moments:
**Scripting languages use different techniques.  Below are some of my observed Python features (differences):**
- #### The colon is your friend
	With any kind of loop declaration or function definition, a colon (:) is needed to indicate that some decision making logic is about to follow.  As a python coder, remember you need to add a colon for these scenarios.  Note:  When the py source code is compiled, the runtime complier will let you know if an expected colon is missing.
- #### Semi-colons at the end of sentences are overrated
	If you have ever coded in C#, you will be thrilled to know that in Python scripting, a semi-colon is not used at the end of a line.  It is like having Christmas all year long.  No need to search for missing semi-colons in your code.
- #### Indents are sensitive
	*Don't panic when you get a compile error.  50% of the time it is an extra space after an indentation.*
	Although the single spaces can seem petty, visually it makes the code dependably easy to read.
- #### Numeric commas can't be taken for granted
	In many languages, the coder can often take for granted that the comma (,) in numeric values will automatically be displayed.  In Python, an additional formating command format(numeric_value,",d") needs to be included:
	<br/>Example:
	<br/>print (format(42500, ",d"))
- #### "While True" is a nice automatic loop
	When needing to generate a quick errorhandling loop, it is nice and simple to use a "While True" loop and then only exit by performing a "break" statement. 
- #### Built-In modules are timesavers
	max(mylist, key=len)
- #### Quickly changing lists into strings and vice versa
	One of the biggest timesavers so far has been learning how to quickly translate a list into a string and vice versa.
	<br/>Examples:
	<br/>"".join(x)    turns a list "x" into a string
	<br/>x.split    turns a string "x" into a list

### Useful modules to import into code:
- #### random
	For ability to randomly generate 1 or 0, which can be a yes/no 
	Randomly generate...
- #### getpass
	Extremely important to hide a user's input when they are typing a password or other secure piece of information.
- #### pyperclip

- #### sys

- #### time

### How my programs differ from other coders:

### Are these programs a reflection of my abilities?

### Sample Programs
- [Trees in Sacramento](https://github.com/Angie-gh/unit1/blob/master/week02_Trees_Angie.py)
- [Password Generator](https://angie-gh.github.io/adix.github.io/hackathon.md)
- [Rock, Paper Scissors Game](https://angie-gh.github.io/adix.github.io/hackathon.md)
- [Encrypting and Decrypting Passwords](https://angie-gh.github.io/adix.github.io/hackathon.md)
- [Menu driven Password Locker](https://angie-gh.github.io/adix.github.io/hackathon.md)

