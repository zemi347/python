Question5:
Guess the number game
Write a program which randomly generate a number between 1 to 30 and ask the user in input field to guess the correct number. Give three chances to user guess the number and also give hint to user if hidden number is greater or smaller than the number he given to input field.


import random
it=random.randint(1, 30)
def main():
    x=int(input('Guess a number one through one hundred'))
    if x == it:
        print("You got it!")
    elif x > it:
        print("too high")
        main()
    else:
        print("too low")
        main()
main()