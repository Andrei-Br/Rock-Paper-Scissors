import os
from scenarios import rock_paper_scissors

class MyException(Exception):
    """ Exception in case of input not 'rock', 'paper', 'scissors' """

#function for playing the game
def play_rps():
    print('Welcome to Rock, Paper, Scissors!\n')

    while True:
        try:
            #  ask the first player for his choice
            player_one = input('Player one (rock, paper or scissors): ')
            #  if the input is invalid, raise exception
            if player_one.lower() not in ['rock', 'paper', 'scissors']:
                raise MyException
            #  clear the screen, so the second player doesn't cheat
            os.system('cls')

            player_two = input('Player two (rock, paper or scissors): ')
            if player_two.lower() not in ['rock', 'paper', 'scissors']:
                raise MyException
            os.system('cls')

        except MyException:
            # error message
            print("Invalid input. Please enter 'rock', 'paper' or 'scissors'\n")

        else:
            #  if both inputs are valid, play the game
            print()
            rock_paper_scissors(player_one, player_two)

            #  ask for another round
            play_again = input('Do you want to play again? Y/N: ')
            if play_again == 'Y' or play_again == 'y':
                os.system('cls')
                continue
            else: 
                break

#  main function
def main():
    play_rps()

if __name__ == '__main__':
    main()
