#Write a Python program with builtin function to multiply all the numbers in a list
l = [1, 2, 3, 4, 3, 2]
multiple = 1
for i in l:
    multiple *= i

print(multiple)

#Write a Python program with builtin function that accepts a string and calculate 
#the number of upper case letters and lower case letters
s = input()
upper_count = 0
lower_count = 0
for char in s:
    if char.isupper():
        upper_count += 1
for char in s:
    if char.islower():
        lower_count += 1

print(upper_count)
print(lower_count)
    

    #Write a Python program with builtin function that checks whether a passed string is palindrome or not.
s = input()
s = s.replace(' ', '') 
if s == s[::-1]:
    print("Oh yea")
else:
    print("nope")

    #Write a Python program that invoke square root function after specific milliseconds
#Sample Input:
"""
25100
2123
Sample Output:
Square root of 25100 after 2123 miliseconds is 158.42979517754858
"""
import time

number = int(input())
milliseconds = int(input())
time.sleep(milliseconds/1000)
square = number ** 0.5
print('Square root of', number, 'after', milliseconds, 'is', square)

tup = (True, 1, 1, True)
print(all(tup))