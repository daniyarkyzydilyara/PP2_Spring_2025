#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re

text = "aaaabbbbbbbbbb"
x = re.search('a*b*', text)
print(x)

#Write a Python program that matches a string that has an 'a' followed by two to three 'b'
import re

text = "msdfnsjandaasacaabbbsdfsdsd"
x = re.search('abb|abbb', text)
print(x)

#Write a Python program to find sequences of lowercase letters joined with a underscore.
import re

text = 'shdhiwi_jd_ij_di_dksdkals_smam'

x = re.findall('[a-z]*_', text)
print(x)

#Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re

text = "AhsjduhduiwhudhuwhdihwidNhiwhn"
x = re.findall('[A-Z][a-z]+', text)
print(x)

#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'
import re

text = "hdsbbadhbd_dyg3gs56s5habhbdhjbahab"
x = re.findall('^.*a.*b$', text)   #. -- Any character (except newline character)
print(x)

#Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re

text = 'uduahwudhuahd idnwaundunaund,ad udwna..undunau'
x = re.sub("[.]|[,]|[ ]", ":", text)   #[] return a match for any character of string
print(x)

#Write a python program to convert snake case string to camel case string.
import re
def snake_camel(s):
    res = ''
    res += (s.group(1)).upper()
    return res

str = input()
camel = re.sub(r'(_[a-z])', snake_camel, str)
camel = camel.replace('_', '')
print(camel)


    #Write a Python program to split a string at uppercase letters.
import re

text = "SdnidamodsmoGsamdasS"

x = re.split('[A-Z]', text)
print(x)

#Write a Python program to insert spaces between words starting with capital letters
import re
def space(x):
    return ' '.join(re.findall('[A-Z][a-z]*', x))

x = "INDINidsmaoidmisdiaimJMos"
y = space(x)
print(y)  

#Write a Python program to convert a given camel case string to snake case.
import re
def com(s):
    res = ''
    if s.group(1):
        res += (s.group(1)).lower()
    else:
        res += ('_' + s.group(2)).lower()
    return res

s = input()
snake = re.sub(r'(^[A-Z]| [A-Z])|([A-Z])', com, s) 
print(snake)
