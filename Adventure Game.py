"""The aim of this project is to make a story.

The reason is to be an adventure game.
"""
import time
import random


def print_pause(text):
    """Do print and wait for a while."""
    print(text)
    time.sleep(2)


def cave_password(total_score):
    """Do cave's treasure password."""
    password = input("Enter the password to open the treasure\n")
    if password == "Jeff Bezos":
        in_treasure = ["8 Dinar", " 1 diamond", "16 coins", "4 gems"]
        treasure_prize = random.choice(in_treasure)
        print_pause("Congratulations! The box is opened.")
        print_pause("You find the treasure which is " + treasure_prize + ".")
        total_score += 10
        print_pause("Your current score is: " + str(total_score))
        print_pause("You win the game!")
        print_pause("Game Over")
        return total_score
    else:
        print_pause("Wrong password. Please try again.")
        return cave_password(total_score)


def cave(total_score):
    """Return the cave's story."""
    print_pause("When you enter the cave, you find a black box.")
    print_pause("This black box is locked with a password.")
    print_pause("To open it, you need to write the password.")
    print_pause("The password is famous person name who founded Amazon.")
    total_score = cave_password(total_score)
    return total_score


def house_password(total_score):
    """Do house's treasure password."""
    password = input("Enter the password to open the treasure.\n")
    if password == "Kevin Ashton":
        print_pause("The box is opened and you don't find the treasure.")
        total_score -= 5
        print_pause("Your current score is: " + str(total_score))
        play_again_cave(total_score)
    else:
        print_pause("Wrong password. Please try again.")
        return house_password(total_score)


def house(total_score):
    """Return the house story."""
    print_pause("When you enter the house, you find a white box.")
    print_pause("This white box is locked with a password.")
    print_pause("To open it, you need to write the password.")
    print_pause("The password is famous person name who invented IoT.")
    total_score = house_password(total_score)
    return total_score


def second_main_choice(total_score):
    """Return the correct choice in main function."""
    print_pause("You have reached a fork in the road.")
    print_pause("To your left is a house.")
    print_pause("To your right is a cave.")
    print_pause("Which way will you go?")
    choice = input("Enter 1 to go house.\nEnter 2 to go cave.\n")
    if choice == 1 or choice == "1":
        total_score = house(total_score)
    elif choice == 2 or choice == "2":
        total_score = cave(total_score)
    else:
        second_main_choice(total_score)


def play_again_cave(total_score):
    """Return the correct choice in cave."""
    print_pause("Choose the correct choice")
    choice = input("Do you want to go to the cave? (y / n)\n")
    if choice == "y":
        total_score = cave(total_score)
    elif choice == "n":
        print_pause("You lose the game.")
        print_pause("Goodbye")
        return total_score
    else:
        play_again_cave(total_score)


def play_again():
    """Return play again in main function."""
    print_pause("Choose the correct choice")
    print_pause("Do you want to play again?")
    play_again_choice = input("Yes: y, No: n\n")
    if play_again_choice == "y":
        main()
    elif play_again_choice == "n":
        print_pause("See you next time.")
    else:
        play_again()


def main():
    """Return the main code."""
    total_score = 0
    print_pause("In the morning, you are moving on the beach.")
    print_pause("During your movement through the beach, you find a paper.")
    print_pause("You are in confusion whether you open paper or leave it.")
    print_pause("What will you do?")
    print_pause("Enter 1 to open the paper.")
    print_pause("Enter 2 to leave the paper as it is.")
    choice = input("Please enter 1 or 2\n")
    if choice == 1 or choice == "1":
        print_pause("You read the paper.")
        print_pause("Then, you found a map of a treasure.")
        total_score += 5
        print_pause("Your current score is: " + str(total_score))
    elif choice == 2 or choice == "2":
        print_pause("You left the paper as it is.")
        print_pause("you regret your decision and decide to open the paper.")
        print_pause("You read the paper.")
        print_pause("Then, you found a map of a treasure.")
        total_score += 5
        print_pause("Your current score is: " + str(total_score))
    else:
        print_pause("Please, choose the correct choice, try again")
        main()
    while True:
        second_main_choice(total_score)
        if total_score >= 30:
            print_pause("Score is " + str(total_score) + ". You win the game!")
            print_pause("Game Over")
            break
        elif total_score <= 0:
            print_pause("Score is " + str(total_score) + ".You lose the game.")
            print_pause("Game Over")
            break
        print_pause("Do you want to play again?")
        play_again_choice = input("Yes: y, No: n\n")
        if play_again_choice == "y":
            main()
        elif play_again_choice == "n":
            print_pause("See you next time.")
            break
        else:
            play_again()
        break


main()
