#Write a Python program to list only directories, files and all directories, files in a specified path.
import os

def list(x):
    print("Directories:")
    for item in os.listdir(x):
        if os.path.isdir(os.path.join(x, item)):
            print(item)
    
    print()
    print("Files:")
    for item in os.listdir(x):
        if os.path.isfile(os.path.join(x, item)):
            print(item)
    
pp=os.path.join(os.getcwd(), "")
list(pp)

#Write a Python program to check for access to a specified path. 
#Test the existence, readability, writability and executability of the specified path
import os
def access(path):
    if os.path.exists(path):
        print(path, "is exist")
    else:
        print(path, "is gone")
    if os.access(path, os.R_OK):
        print(path, "is readability")
    else:
        print(path, "is not readability")
    if os.access(path, os.W_OK):
        print(path, "is writability")
    else:
        print(path, "is not writability")
    if os.access(path, os.X_OK):
        print(path, "is executability")
    else:
        print(path, "is not executability")

pp=os.path.join(os.getcwd(), "")
pp1=os.path.join(os.getcwd(), r"C:\Users\user\Desktop\pp2\TSIS6\dir_files")
access(pp)
access(pp1)

#Write a Python program to test whether a given path exists or not. 
#If the path exist find the filename and directory portion of the given path.
import os

def check(path):
    if os.path.exists(path):
        print(path, "is exist")
        if os.path.isfile(path):
            print("Filename:", os.path.basename(path))
            print("Directory portion:", os.path.dirname(path))
        elif os.path.isdir(path):
            print("Directory:", os.path.basename(path))
            print("Directory portion:", os.path.dirname(path))
    else:
        print(path, "I don't know , where is it")
    
if __name__ == "__main__":
    pp=input()
    check(pp)

    #Write a Python program to count the number of lines in a text file.
file = open('dilyara.txt', 'r')

cnt = 0
for _ in file:
    cnt+=1

print(cnt)

#Write a Python program to count the number of lines in a text file.
file = open('dilyara.txt', 'r')

cnt = 0
for _ in file:
    cnt+=1

print(cnt)

#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
import string
for i in string.ascii_uppercase:
    with open(f'{i}.txt', 'w'):
        pass

    #Write a Python program to copy the contents of a file to another file
import os
import shutil

def copy(f1, f2):
    if os.path.isfile(f1):
        shutil.copyfile(f1, f2)
        print('copied')
    else:
        print('file doesnt exists')
    
f1 = 'C:/Users/user/Desktop/pp2/TSIS6/dir_files/7file.txt'
f2 = 'C:/Users/user/Desktop/pp2/TSIS6/dir_files/7file_new.txt'
copy(f1, f2)

#Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
import os

if os.path.exists('ex.txt'):
    os.remove('ex.txt')