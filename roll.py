# roll a "die" some number of times.
# roll - run it once and go into a loop
# roll 1 - produce a number 1-6 random and print it
# roll 2 - produce two numbers 1-6 and print them
# roll 3 - produce three numbers and print them.
#
import random
import sys

val = sys.argv


def handling_the_length_of_sysargv(x) -> int:
    if type(x) == int:
        return x
    elif len(x) > 1:
        return x[1]
    else:
        return 1


def user() -> str:
    return input('How many die will you roll? ')


def roll(number) -> str:
    number_of_times = handling_the_length_of_sysargv(number)
    if int(number_of_times) <= 1:
        return str(random.randint(1, 6))
    else:
        return roll(int(number_of_times) - 1) + ', ' + str(random.randint(1, 6))


def game():
    enter = input('Would you like to roll again? ')
    if enter.lower().find('y') != -1:
        roll(int(user()))
    else:
        print('Thanks for Playing')


print(roll(val))
game()
