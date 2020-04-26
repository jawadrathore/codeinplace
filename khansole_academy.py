"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""
import random


MIN_RANDOM = 0
MAX_RANDOM = 5
CORRECT_ANSWER = 0


def main():
   khan_sole()

def khan_sole():
    correct_counter = 0
    while correct_counter < 10:
        number_one = random.randint(MIN_RANDOM, MAX_RANDOM)
        number_two = random.randint(MIN_RANDOM, MAX_RANDOM)
        print("number_one = " + str(number_one))
        print("number_two = " + str(number_two))
        total = int(number_one + number_two)
        sum = input("Sum of number_one and number_two = ")
        if sum == "":
            print("Thank You")
            break
        sum = int(sum)
        if total == sum:
            correct_counter=correct_counter+1
            print("Your answer is correct.")
            print("Total " + str(correct_counter) + " correct answers.")
            print("Keep going!")
        else:
            print("Incorrect. The expected answer is " + str(total))
            print("Please note that counter has restarted.")
            print("You need 10 consecutive correct answers to pass this module.")
            print("If you feel you need to exit this program. Please press enter.")
            print("Good Luck!")
            correct_counter = 0

    if correct_counter == 10:
        print("mastered")




pass


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
