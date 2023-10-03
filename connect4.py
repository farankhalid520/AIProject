import numpy as np
import random


# Check for a winner
def winner(board):
    # Check horizontal locations for win
    for c in range(7 - 3):
        for r in range(6):
            if board[r][c] == board[r][c + 1] == board[r][c + 2] == board[r][c + 3] != "-":
                return True

    # Check vertical locations for win
    for c in range(7):
        for r in range(6 - 3):
            if board[r][c] == board[r + 1][c] == board[r + 2][c] == board[r + 3][c] != "-":
                return True

    # Check positively sloped diagonals
    for c in range(7 - 3):
        for r in range(3, 6):
            if board[r][c] == board[r - 1][c + 1] == board[r - 2][c + 2] == board[r - 3][c + 3] != "-":
                return True

    # Check negatively sloped diagonals
    for c in range(7 - 3):
        for r in range(6 - 3):
            if board[r][c] == board[r + 1][c + 1] == board[r + 2][c + 2] == board[r + 3][c + 3] != "-":
                return True


# Function to take a turn for a player
def take_turn(board, player_symbol):
    valid_selection = False

    while not valid_selection:
        try:
            col = int(input(f"Player {player_symbol}:"))
            if 0 <= col <= 6 and board[0][col] == "-":
                valid_selection = True
            else:
                print("Invalid selection, try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    for r in range(5, -1, -1):
        if board[r][col] == "-":
            board[r][col] = player_symbol
            break

    print(board)


# Function for player vs player game mode
def player_vs_player(board, game_over, turn):
    while not game_over:
        player_symbol = "x" if turn % 2 == 0 else "o"
        take_turn(board, player_symbol)
        if winner(board):
            print(f"Player {player_symbol} is the winner!")
            game_over = True
        else:
            turn += 1


# Function for random vs player game mode
def random_vs_player(board, game_over, turn):
    while not game_over:
        if turn % 2 == 0:
            take_turn(board, "x")
        else:
            col = random.randint(0, 6)
            while board[0][col] != "-":
                col = random.randint(0, 6)
            for r in range(5, -1, -1):
                if board[r][col] == "-":
                    board[r][col] = "o"
                    break
            print(board)

        player_symbol = "x" if turn % 2 == 0 else "o"
        if winner(board):
            print(f"Player {player_symbol} is the winner!")
            game_over = True
        else:
            turn += 1


# Main function to run the game
def main():
    while True:
        board = np.full((6, 7), "-", dtype=str)
        game_over = False
        turn = random.randint(0, 1)
        print("\n\nCONNECT 4\n")
        print(board)
        print("\nConnect4 Game Options:\n")
        print("1. Player vs. Player")
        print("2. Random Player vs. Player")
        print("3. AI vs. Player")
        print("4. Quit\n")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            player_vs_player(board, game_over, turn)
        elif choice == "2":
            random_vs_player(board, game_over, turn)
        elif choice == "3":
            # AI vs Player not implemented yet
            pass
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
