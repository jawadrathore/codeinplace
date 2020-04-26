from karel.stanfordkarel import *

# Assumptions
# Karel will always start facing west at the upper right corner of the leftmost building.
# Karel will have infinite beepers in his beeper bag.
# Although buildings may be of varying sizes.
# There will always be exactly three of them, and their relative position to one another will always be the same

def main():
    while facing_west():
            turn_left()
            beeper_till_end()
    while facing_south():
            turn_left()
            beeper_till_end()
    while facing_east():
        if front_is_clear():
            put_beeper()
            move()
        else:
            turn_right()
    while facing_south():
        turn_left()
        beeper_till_end()
    while facing_east():
        turn_left()
        beeper_till_end()
    while facing_north():
        turn_left()
        if front_is_blocked():
            turn_right()
            put_beeper()
            move()
        else:
            turn_right()
            put_beeper()
            turn_right()
    move()
    while facing_east():
        turn_left()
        beeper_till_end()
    while facing_north():
        turn_left()
        beeper_till_end()
    while facing_west():
        turn_left()
        if front_is_blocked():
            put_beeper()
            turn_right()
            move()
    turn_right()


def turn_around():
    turn_left()
    turn_left()

#this function results in beepers put in a line untill the conditions fails

def beeper_till_end():
    if front_is_blocked():
        put_beeper()
        turn_right()
        move()
    else:
        move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()


pass


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
