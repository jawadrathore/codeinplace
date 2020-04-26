from karel.stanfordkarel import *
#
# Assumptions
#
# In solving this problem, you may count on the following facts about the world
# Karel starts at 1st row and 1st column, facing east, with an infinite number of beepers in its bag.
# The initial state of the world includes no interior walls or beepers.
# The world need not be square, but you may assume that it is at least as tall as it is wide.
# If the width of the world is odd, Karel must put the beeper in the center square.
# If the width is even, Karel may drop the beeper on either of the two center squares.
# It does not matter which direction Karel is facing at the end of the run.

def main():
    put_beeper()
    if front_is_clear():
        move()
        if front_is_clear():
            find_mid()
            remove_excess_beepers()
            move_to_mid()
        else:
            turn_around()
            move_to_mid()

def find_mid():
    place_beeper_wall()
    while no_beepers_present():
        is_mid()
        find_beeper()

def remove_excess_beepers():
    pick_beeper_Up()
    turn_around()
    move_to_mid()
    pick_beeper_Up()
    turn_around()

def pick_beeper_Up():
    while front_is_clear():
        move()
        pick_beeper()

def move_to_mid():
    while no_beepers_present():
        move()

def place_beeper_wall():
    while front_is_clear():
        move()
    put_beeper()
    spin_move()

def is_mid():
    move()
    if beepers_present():
        spin_move()
        put_beeper()

def find_beeper():
    if no_beepers_present():
        while no_beepers_present():
            move()
        spin_move()
        put_beeper()
        move()

# this function rotates karel to 180 degrees and then move one place
def spin_move():
    turn_around()
    move()

# this function rotates karel to 180 degrees
def turn_around():
    for i in range(2):
        turn_left()

if __name__ == "__main__":
    run_karel_program()
