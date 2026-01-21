# test
from builtins import ValueError
from render import Board

# game execution flow
def main():
    # NEXT STEPS
    print("Welcome to TicTacToe Fuckers")
    caller = Board()

    print("Board is as follows, select numbers 1-9 to make a move")
    caller.render_board("_")
    print("Player 1 is X, Player 2 is O")


    sp = input("Input 1 to begin. All other input is invalid. Game automatically ends when one player wins: ")
    if sp.isdigit() and int(sp) == 1:
        print("Step off")
        
        # production note, I may have the win check function only execute after one player has made at least 3 moves, in which case
        # I might need a Player class, more to follow
        while True:
            choice = input("Player 1 make your move: ")
            caller.render_board("X", int(choice))
            choice = input("Player 2 make your move: ")
            caller.render_board("O", int(choice))
    else:
        print("Terminating")
        exit()

if __name__ == "__main__":
    main()