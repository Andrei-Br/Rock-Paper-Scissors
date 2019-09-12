#  function handling different scenarios
def rock_paper_scissors(player_one, player_two):
    # Player one choses ROCK
    if (player_one.lower() == 'rock') and (player_two.lower() == 'paper'):
        print('Player one chose: ' + player_one + '\n')
        print('Player two chose: ' + player_two + '\n')
        print('Player two won!\n')
    elif (player_one.lower() == 'rock') and (player_two.lower() == 'scissors'):
        print('Player one chose: ' + player_one + '\n')
        print('Player two chose: ' + player_two + '\n')
        print('Player one won!\n')

    # Player one choses PAPER
    elif (player_one.lower() == 'paper') and (player_two.lower() == 'rock'):
        print('Player one chose: ' + player_one + '\n')
        print('Player two chose: ' + player_two + '\n')
        print('Player one won!\n')
    elif (player_one.lower() == 'paper') and (player_two.lower() == 'scissors'):
        print('Player one chose: ' + player_one + '\n')
        print('Player two chose: ' + player_two + '\n')
        print('Player two won!\n')

        # Player one choses SCISSORS
    elif (player_one.lower() == 'scissors') and (player_two.lower() == 'rock'):
        print('Player one chose: ' + player_one + '\n')
        print('Player two chose: ' + player_two + '\n')
        print('Player two won!\n')
    elif (player_one.lower() == 'scissors') and (player_two.lower() == 'paper'):
        print('Player one chose: ' + player_one + '\n')
        print('Player two chose: ' + player_two + '\n')
        print('Player one won!\n')

        #DRAW
    elif (player_one.lower() == player_two.lower()):
        print('Player one chose: ' + player_one + '\n')
        print('Player two chose: ' + player_two + '\n')
        print("It's a draw!\n")