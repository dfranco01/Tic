import TicTacToe

class Board:
    def render_board(symbol,*selection):
        board = TicTacToe.board
        if symbol == "O":
            match selection:
                case 1:
                    print(symbol)
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
                case 2:
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
                case 3:
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
                case 4:
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
                case 5:
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
                case 6:
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
                case 7:
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
                case 8:
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
                case 9:
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
        else:
            match selection:
                case 1:
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
                case 2:
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
                case 3:
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
                case 4:
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
                case 5:
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
                case 6:
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
                case 7:
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
                case 8:
                    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
                    print("--+---+--")
                    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
                    print("--+---+--")
                    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
                case 9:
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