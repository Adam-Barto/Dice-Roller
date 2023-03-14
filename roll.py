# roll a "die" some number of times.
# roll - run it once and go into a loop
# roll 1 - produce a number 1-6 random and print it
# roll 2 - produce two numbers 1-6 and print them
# roll 3 - produce three numbers and print them.
#
import random
import sys


def die():
    return random.randint(1, 6)


# print(die())

number_of_times = 1

val = sys.argv


def roll():
    print(die())


def rolln(number):
    print_this = ""
    while number > 0:
        print_this.join(str(die()))
        number = number - 1
    print(print_this)


if len(val) == 2:
    rolln(int(val[1]))
else:
    roll()

