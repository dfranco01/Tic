from builtins import ValueError
from render import Board
            
# game execution flow
def main():
    player1_choice = ""
    player2_choice = ""
    print("Welcome to TicTacToe!")
    caller = Board()

    # Displaying empty board
    print("Board is as follows, select numbers 1-9 to make a move")
    caller.render_board("_")
    print("Player 1 is X, Player 2 is O")


    sp = input("Input 1 to begin. All other input is invalid. Game automatically ends when one player wins: ")
    if sp.isdigit() and int(sp) == 1:
        print("Step off")
        
        while True:
            winner_found = False
            player = "player 1"
            player1_choice = input("Player 1 make your move: ")

            #Ensuring player 1 chooses a proper position on the board from 1-9
            while not player1_choice.isdigit() or int(player1_choice) < 1 or int(player1_choice) > 9:
                print("Invalid selection, choose a number between 1 and 9")
                player1_choice = input("Player 1 make your move: ")

            #Ensuring player 1 doesn't choose an already occupied spot on the board
            while(player1_choice == player2_choice):
                print("That spot is already occupied, choose a vacant spot")
                player1_choice = input("Player 2 make your move: ")
            
            caller.render_board("X", int(player1_choice))

            # checking for a winner after player 1's move
            for i in range(7):
                if caller.win_check(i):
                    winner_found = True
                    break
            if winner_found:
                break

            player = "player 2"
            player2_choice = input("Player 2 make your move: ")

            #Ensuring player 1 chooses a proper position on the board from 1-9
            while not player2_choice.isdigit() or int(player2_choice) < 1 or int(player2_choice) > 9:
                print("Invalid selection, choose a number between 1 and 9")
                player2_choice = input("Player 1 make your move: ")

            # ensuring player 2 doesn't choose an already occupied spot on the board
            while(player1_choice == player2_choice):
                print("That spot is already occupied, choose a vacant spot")
                player2_choice = input("Player 2 make your move: ")
            
            caller.render_board("O", int(player2_choice))
            
            # checking for a winner after player 2's move
            for i in range(7):
                if caller.win_check(i):
                    winner_found = True
                    break
            if winner_found:
                break
        
        print(f'Congrats {player}, you have won')
        exit()
    else:
        print("Terminating")
        exit()

if __name__ == "__main__":
    main()