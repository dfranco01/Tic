# test
from builtins import ValueError
from player import Player
import render

board = [
        ["#", "#", "#"],
        ['#', '#', '#'],
        ["#", "#", "#"]
    ]
def main():
    print("Welcome to TicTacToe Fucker")
    caller = render.Board()


    caller.render_board("_")
    print("-" * 50)
    caller.render_board("O", 1)


    sp = input("Input 1 to begin. All other input is invalid. Game automatically ends when one player wins.")
    if sp.isdigit() and int(sp) == 1:
        print("Step off")
        
        p1 = Player.Player(1)
        p2 = Player.Player(2)
        while True:
            pass
    else:
        print("Terminating")
        exit()

if __name__ == "__main__":
    main()