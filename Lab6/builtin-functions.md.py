from functools import reduce

def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

# Example
numbers = [2, 3, 4, 5]
print(multiply_list(numbers))  # Output: 120

def count_case(s):
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = sum(1 for c in s if c.islower())
    return upper_count, lower_count

# Example
s = "Hello World"
upper, lower = count_case(s)
print(f"Uppercase letters: {upper}, Lowercase letters: {lower}")  
# Output: Uppercase letters: 2, Lowercase letters: 8

def is_palindrome(s):
    return s == s[::-1]

# Example
s = "madam"
print(is_palindrome(s))  # Output: True

import time
import math

def delayed_sqrt(number, delay):
    time.sleep(delay / 1000)  # Convert milliseconds to seconds
    return math.sqrt(number)

# Example
number = 25100
delay = 2123
result = delayed_sqrt(number, delay)
print(f"Square root of {number} after {delay} milliseconds is {result}")

def all_true(t):
    return all(t)

# Example
t = (True, True, False)
print(all_true(t))  # Output: False
