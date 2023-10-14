from connect4 import *

def run_tests():
    print("\nRunning tests...\n")
    times = []

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
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"]
            ]),
            "expected_col": 3,
            "description": "AI should place the first move in the middle"
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
        times.append(end_time - start_time)

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
    return times

def main():

        board = np.full((6, 7), "-", dtype=str)
        game_over = False
        turn = random.randint(0, 1)
        print("\n\nCONNECT 4 TESTS\n")

        times = run_tests()
        print(f"Average AI response time is: {sum(times)/len(times):.2f} seconds")


if __name__ == "__main__":
    main()
