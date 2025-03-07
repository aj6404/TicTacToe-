import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


def print_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def take_turn(player, is_computer=False):
    print(player + "'s turn.")
    if is_computer:
        available_positions = [i for i, mark in enumerate(board) if mark == "-"]

        # Check for winning move
        for pos in available_positions:
            board[pos] = player  
            if check_game_over() == "win":
                position = pos
                break
            board[pos] = "-"  
        else:
            # Check for opponent's winning move to block
            opponent = "X" if player == "O" else "O"
            for pos in available_positions:
                board[pos] = opponent  # Try opponent's move
                if check_game_over() == "win":
                    position = pos
                    break
                board[pos] = "-"  
            else:
                # No winning or blocking moves
                if board[4] == "-":
                    position = 4
                else:
                    #choose a corner position
                    corners = [0, 2, 6, 8]
                    available_corners = [pos for pos in corners if board[pos] == "-"]
                    if available_corners:
                        position = random.choice(available_corners)
                    else:
                        position = random.choice(available_positions)

    else:
        position = input("Choose a position from 1-9: ")
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1-9: ")
        position = int(position) - 1
        while board[position] != "-":
            position = int(input("Position already taken. Choose a different position: ")) - 1
    board[position] = player
    print_board()





def check_game_over():
    if (board[0] == board[1] == board[2] != "-") or \
       (board[3] == board[4] == board[5] != "-") or \
       (board[6] == board[7] == board[8] != "-") or \
       (board[0] == board[3] == board[6] != "-") or \
       (board[1] == board[4] == board[7] != "-") or \
       (board[2] == board[5] == board[8] != "-") or \
       (board[0] == board[4] == board[8] != "-") or \
       (board[2] == board[4] == board[6] != "-"):
        return "win"
    elif "-" not in board:
        return "tie"
    else:
        return "play"


def play_game():
    print_board()
    current_player = "X"
    game_over = False
    while not game_over:
        is_computer = current_player == "O"
        take_turn(current_player, is_computer)
        game_result = check_game_over()
        if game_result == "win":
            print(current_player + " wins!")
            game_over = True
        elif game_result == "tie":
            print("It's a tie!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"


play_game()
