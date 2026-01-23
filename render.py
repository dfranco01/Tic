#import TicTacToe

class Board:
    # board to be played on
    main_board = [
            ["#", "#", "#"],
            ['#', '#', '#'],
            ["#", "#", "#"]
        ]
    #this function displays the clean board to players at the start of match and after each move
    def render_board(self, symbol, *selection):
        board = self.main_board
        # updating the baord with the appropraite symbol on the selected spot
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
        elif symbol == "X":
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
        else:
            print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
            print("--+---+--")
            print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
            print("--+---+--")
            print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
    
    #This function checks if a winner has been reached after each move
    def win_check(self, win_scenario):
        match win_scenario:
            case 0:
                return (Board.main_board[0][0] == 'X' or Board.main_board[0][0] == 'O') and (Board.main_board[0][0] == Board.main_board[1][0] == Board.main_board[2][0])
            case 1:
                return (Board.main_board[0][1] == 'X' or Board.main_board[0][1] == 'O') and (Board.main_board[0][1] == Board.main_board[1][1] == Board.main_board[2][1])
            case 2:
                return (Board.main_board[0][2] == 'X' or Board.main_board[0][2] == 'O') and (Board.main_board[0][2] == Board.main_board[1][2] == Board.main_board[2][2])
            case 3:
                return (Board.main_board[0][0] == 'X' or Board.main_board[0][0] == 'O') and (Board.main_board[0][0] == Board.main_board[0][1] == Board.main_board[0][2])
            case 4:
                return (Board.main_board[1][0] == 'X' or Board.main_board[1][0] == 'O') and (Board.main_board[1][0] == Board.main_board[1][1] == Board.main_board[1][2])
            case 5:
                return (Board.main_board[2][0] == 'X' or Board.main_board[2][0] == 'O') and (Board.main_board[2][0] == Board.main_board[2][1] == Board.main_board[2][2])
            case 6:
                return (Board.main_board[0][0] == 'X' or Board.main_board[0][0] == 'O') and (Board.main_board[0][0] == Board.main_board[1][1] == Board.main_board[2][2])
            case 7:
                return (Board.main_board[2][0] == 'X' or Board.main_board[2][0] == 'O') and (Board.main_board[2][0] == Board.main_board[1][1] == Board.main_board[0][2])