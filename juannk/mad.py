# MADLIB
"""adj = input("Adjectfive: ")
verb1 = input("verb: ")
verb2 = input("verb: ")
famouse_person = input("famouse person: ")
madlib = f"computer programming is so{adj}! it makes me so excited all the time because \
I love to {verb1}. stay hydrated and {verb2} like you are {famouse_person}!"

print(madlib)
"""


"""
# guessing game
import random

def guess(x):
    random_num = random.randint(1,x)
    guess = 0
    while guess != random_num:
        guess = int(input(f"guess a number between 1 and {x}: "))
        print(guess)
        if guess < random_num:
            print("sorry guess to low")
        elif guess > random_num:
            print("to high guess a bit low")
        else:
            print(f"you have WON! you have guessed {random_num}")

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback !="c":
        if low!= high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f"is {guess} too high (h), too low (l), or correctly(c)  : ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f"\n\nyeee i am correct, I have guessed {guess}, correctly")

computer_guess(1000)
"""
"""
#rock paper scissor
import random
def player():
    user = input("rock,paper,scissors: \n")
    computer = random.choice(["r","p","s"])

    if user == computer:
        return "it is a tie "
    if is_winner(user,computer):
        return "you won!"
    return "you lost!"

def is_winner (player,opponent):
    if (player =="r"and opponent=="s")or (player=="s"and opponent=="p") \
        or (player=="p"and opponent =="r"):
        return True


print(player())
"""
"""
def counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        return count

    return increment


xver = counter()
print(xver())
print(xver())
"""
"""
# accepting arguments
import argparse

parser = argparse.ArgumentParser(
    description='this progrsm prints the name of my dogs'
)

parser.add_argument('-c', '--color', metavar='color'\
                    , required= True,choices={"yellow", "red"}, help='the color to search for')

args = parser.parse_args()

print(args.color)
"""
"""
#map() , filter(), reduce()
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]
result = map(lambda a: a * 2, numbers)
print(list(result))

result = filter(lambda n: n % 2 != 0,numbers)
print(list(result))
expenses = [
    ('dinner',89),
    ('car repair', 2000),
    ('bonking bed', 3000)
]

sum = reduce(lambda a,b,c: a[1]+b[1]+c[1], expenses)
print(sum)"""  # please check why the last one is not properly working and what i should to fix it
# #decorators
# def logtime(func):
#     def wrapper():
#         print("*******")  # do something before
#         val = func()
#         print("*******")  # do something after
#         return val
#     return wrapper()
#
#
# @logtime
# def hello():
#     print("hello")
# try to understand more about its use
# # annotations
#
# def increment(n: int) -> int:
#     return n+1
#
#
# count: int = 0

# exception
#
# try:
#     # some line of code
# except <ERROR1>:
#     # handler <error1>
# except <ERROR2>:
#     #handler <error2>
# except:
#     # no exceptions were raised. the code ran successfully
# # finally:
# #     # do something in any case
#
# try:
#     result = 2/0
# except ZeroDivisionError:
#     print('can not divide by zero!')
# finally:
#     result = 1
# print(result)
#
# try:
#     raise Exception('an error!')
# except Exception as error:
#     print(error)
#
# class dog_not_found(Exception):
#     print("this is an error boo pipi")
#     pass
#
# try:
#     raise dog_not_found()
# except dog_not_found:
#     print('dog not found')

# # polymorphism
#
# class Dog:
#     def eat(self):
#         print('eating dog food')
#
#
# class cat:
#     def eat(self):
#         print('eating cat food')
#
#
# animal1 = Dog()
# animal2 = cat()
#
# animal1.eat()
# animal2.eat()
# needs more explanation

# # operator overloading
# class Dog:
#     # the dog class
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __gt__(self, other):
#         return True if self.age < other.age else False
#
#
# brook = Dog('Brook', 5)
# berte = Dog('Berte', 9)
#
# print(brook < berte)
# seems useful

