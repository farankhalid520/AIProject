import numpy as np
import random
import time


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


# We decided on using minmax also used alpha-beta pruning
def minimax(board, depth, maximizing_player, alpha, beta):
    if depth == 0 or winner(board):
        return evaluate_board(board)

    if maximizing_player:
        max_eval = float('-inf')
        for col in range(7):
            new_board = board.copy()
            if is_valid_location(new_board, col):
                make_move(new_board, col, "o")
                eval = minimax(new_board, depth - 1, False, alpha, beta)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  # beta cut-off
        return max_eval
    else:
        min_eval = float('inf')
        for col in range(7):
            new_board = board.copy()
            if is_valid_location(new_board, col):
                make_move(new_board, col, "x")
                eval = minimax(new_board, depth - 1, True, alpha, beta)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # alpha cut-off
        return min_eval


def evaluate_board(board):
    score = 0

    # Check for a win for either player
    if winner(board):
        score = 1000 if winning_player(board) == "o" else -1000
        return score

    # Check for 3 in a row for AI
    for c in range(7 - 3):
        for r in range(6):
            if np.array_equal(board[r, c:c + 3], ["o", "o", "o"]):
                score += 5

    # Check for 3 in a row for opponent
    for c in range(7 - 3):
        for r in range(6):
            if np.array_equal(board[r, c:c + 3], ["x", "x", "x"]):
                score -= 5

    # Check for 2 in a row for AI
    for c in range(7 - 2):
        for r in range(6):
            if np.array_equal(board[r, c:c + 2], ["o", "o"]):
                score += 2

    # Check for 2 in a row for opponent
    for c in range(7 - 2):
        for r in range(6):
            if np.array_equal(board[r, c:c + 2], ["x", "x"]):
                score -= 2

    # Center column control
    center_array = [i for i in list(board[:, 3])]
    center_count = center_array.count("o")
    score += center_count * 3

    return score


def winning_player(board):
    # Check horizontal locations for win
    for c in range(7 - 3):
        for r in range(6):
            if board[r][c] == board[r][c + 1] == board[r][c + 2] == board[r][c + 3] != "-":
                return board[r][c]

    # Check vertical locations for win
    for c in range(7):
        for r in range(6 - 3):
            if board[r][c] == board[r + 1][c] == board[r + 2][c] == board[r + 3][c] != "-":
                return board[r][c]

    # Check positively sloped diagonals
    for c in range(7 - 3):
        for r in range(3, 6):
            if board[r][c] == board[r - 1][c + 1] == board[r - 2][c + 2] == board[r - 3][c + 3] != "-":
                return board[r][c]

    # Check negatively sloped diagonals
    for c in range(7 - 3):
        for r in range(6 - 3):
            if board[r][c] == board[r + 1][c + 1] == board[r + 2][c + 2] == board[r + 3][c + 3] != "-":
                return board[r][c]

    # No winner
    return None


def is_valid_location(board, col):
    return board[0][col] == "-"


def make_move(board, col, player_symbol):
    for r in range(5, -1, -1):
        if board[r][col] == "-":
            board[r][col] = player_symbol
            break


def ai_vs_player(board, game_over, turn):
    while not game_over:
        if turn % 2 == 0:
            take_turn(board, "x")
        else:
            start_time = time.time()

            best_score = float('-inf')
            best_col = None
            for col in range(7):
                new_board = board.copy()
                if is_valid_location(new_board, col):
                    make_move(new_board, col, "o")
                    score = minimax(new_board, 3, False, float('-inf'), float('inf'))  # Depth 3
                    if score > best_score:
                        best_score = score
                        best_col = col

            make_move(board, best_col, "o")
            print(board)

            end_time = time.time()
            print(f"AI response time: {end_time - start_time:.2f} seconds")

        player_symbol = "x" if turn % 2 == 0 else "o"
        if winner(board):
            print(f"Player {player_symbol} is the winner!")
            game_over = True
        else:
            turn += 1


def run_tests():
    print("\nRunning tests...\n")

    test_cases = [
        {
            "board": np.array([
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["o", "o", "o", "-", "-", "-", "-"],
                ["x", "x", "x", "-", "-", "-", "x"]
            ]),
            "expected_col": 3,
            "description": "AI should block player from creating 4 in a row horizontally"
        },
        {
            "board": np.array([
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "x", "x", "-", "-", "-"],
                ["-", "x", "o", "o", "-", "-", "-"],
                ["x", "o", "x", "o", "o", "-", "-"]
            ]),
            "expected_col": 3,
            "description": "AI should block player from creating 4 in a row diagonally"
        },
        {
            "board": np.array([
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["x", "o", "x", "x", "-", "-", "-"],
                ["x", "o", "o", "o", "-", "-", "-"],
                ["x", "o", "x", "o", "o", "-", "-"]
            ]),
            "expected_col": 0,
            "description": "AI should block player from creating 4 in a row vertically"
        },
        {
            "board": np.array([
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["x", "x", "x", "-", "-", "-", "-"],
                ["o", "o", "o", "-", "-", "-", "-"]
            ]),
            "expected_col": 3,
            "description": "AI should win the game horizontally"
        },
        {
            "board": np.array([
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["o", "x", "-", "-", "-", "-", "-"],
                ["o", "x", "x", "-", "-", "-", "-"],
                ["o", "x", "o", "-", "-", "-", "-"]
            ]),
            "expected_col": 0,
            "description": "AI should win the game vertically"
        },
        {
            "board": np.array([
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "o", "o", "-", "-", "-"],
                ["-", "o", "x", "x", "-", "-", "-"],
                ["o", "x", "o", "x", "x", "-", "-"]
            ]),
            "expected_col": 3,
            "description": "AI should win the game diagonally"
        }
    ]

    for i, test_case in enumerate(test_cases):
        board = test_case["board"].copy()
        expected_col = test_case["expected_col"]

        start_time = time.time()

        best_score = float('-inf')
        best_col = None
        for col in range(7):
            new_board = board.copy()
            if is_valid_location(new_board, col):
                make_move(new_board, col, "o")
                score = minimax(new_board, 3, False, float('-inf'), float('inf'))
                if score > best_score:
                    best_score = score
                    best_col = col

        end_time = time.time()

        if best_col != expected_col:
            print(f"Test {i + 1} FAILED: {test_case['description']}")
            print(f"Expected column: {expected_col}, AI chose: {best_col}")
            print(board)
            all_tests_pass = False
        else:
            make_move(board, best_col, "o")
            print(board)
            print(f"Test {i + 1} passed")

        print(f"AI response time for Test {i + 1}: {end_time - start_time:.2f} seconds")


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
        print("4. Run AI tests")
        print("5. Quit\n")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            player_vs_player(board, game_over, turn)
        elif choice == "2":
            random_vs_player(board, game_over, turn)
        elif choice == "3":
            ai_vs_player(board, game_over, turn)
        elif choice == "4":
            run_tests()
        elif choice == "5":
            print("Bye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()
