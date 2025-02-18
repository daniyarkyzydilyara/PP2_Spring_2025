def square_generator(n):
    for i in range(n + 1):
        yield i ** 2

# task2
N = int(input("Enter a number: "))
for square in square_generator(N):
    print(square, end=" ")
def even_generator(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Enter a number: "))
print(",".join(str(num) for num in even_generator(n)))
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# task3
n = int(input("Enter a number: "))
for num in divisible_by_3_and_4(n):
    print(num, end=" ")
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

# task4
a = int(input("Enter start value: "))
b = int(input("Enter end value: "))
for sq in squares(a, b):
    print(sq)
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

# task5
n = int(input("Enter a number: "))
for num in countdown(n):
    print(num, end=" ")
