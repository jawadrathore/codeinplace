from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    while front_is_clear():
        turn_left()
        finish_single_column()
        jump_four()
    else:
        turn_left()
        finish_single_column()

# Karel will ascend and come back (after hitting top cieling) down while checking for beepers.

def finish_single_column():
    while front_is_clear():
        beeper_check()
    else:
        turn_around()
        beeper_check()
        move_to_wall()

# Karel will check if there is a beeper it will move otherwise it will put a beeper

def beeper_check():
   if beepers_present():
       move()
   else:
       put_beeper()

# Karel will turn 180 degrees

def turn_around():
    for i in range(2):
        turn_left()

# Karel will move spots if front is clear. Otherwise it will turn left

def move_to_wall():
    while front_is_clear():
            move()
    else:
        turn_left()

# Karel is skipping 3 coulmns as we need to check for every fourth column

def jump_four():
    move()
    move()
    move()
    move()

pass


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
