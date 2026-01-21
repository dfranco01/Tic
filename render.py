#import TicTacToe

class Board:
    main_board = [
            ["#", "#", "#"],
            ['#', '#', '#'],
            ["#", "#", "#"]
        ]
    #this function displays the clean board to players at the start of match and after each move
    def render_board(self, symbol, *selection):
        board = self.main_board
        if symbol == "O":
            match selection[0]:
                case 1:
                    board[0][0] = symbol
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
                case 2:
                    board[0][1] = symbol
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
                case 3:
                    board[0][2] = symbol
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
                case 4:
                    board[1][0] = symbol
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
                case 5:
                    board[1][1] = symbol
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
                case 6:
                    board[1][2]
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
                case 7:
                    board[2][0] = symbol
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
                case 8:
                    board[2][1] = symbol
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
                case 9:
                    board[2][2] = symbol
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
                case _:
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
        if symbol == "X":
            match selection[0]:
                case 1:
                    board[0][0] = symbol
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
                case 2:
                    board[0][1] = symbol
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
                case 3:
                    board[0][2] = symbol
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
                case 4:
                    board[1][0] = symbol
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
                case 5:
                    board[1][1] = symbol
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
                case 6:
                    board[1][2] = symbol
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
                case 7:
                    board[2][0] = symbol
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
                case 8:
                    board[2][1] = symbol
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
                case 9:
                    board[2][2] = symbol
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
                case _:
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
    #This function checks if a winner has been reached after each move
    def board_check():
        pass
    #this function ensures the same spot on the board isn't chosen twice
    def repeat_check():
        pass