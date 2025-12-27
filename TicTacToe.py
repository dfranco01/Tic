# test
from builtins import ValueError
print("Welcome to TicTacToe Fucker")
def nested_loop_demo(data):
    for i in data:
        print("Outer iteration")
        for j in i:
            print(j)

board = [
    ["#", "#", "#"],
    ['#', '#', '#'],
    ["#", "#", "#"]
]
def render_board():
    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
    print("--+---+--")
    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("--+---+--")
    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")

render_board()

class Player:
    def __init__(self, ID):
        self.ID = ID


sp = input("Input 1 to begin. All other input is invalid. Game automatically ends when one player wins.")
if int(sp) == 1:
    print("Step off")
    #I don't want the user to think in indexes when selecting a spot on the board, so options are 1-9
    #I'll have to calculate how to take a user selection and find the correct spot on the board
    menu = {"1st Row": [1, 2, 3], "2nd Row": [1, 2, 3], "3rd Row": [1, 2, 3]}
    p1 = Player(1)
    p2 = Player(2)
    while True:
        pass
else:
    print("Terminating")
    exit()