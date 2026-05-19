# Tic Tac Toe Game

# This file will contain the main structure of the game.


def print_board(board):
    """Prints the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    """Check if there is a winner."""
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]

        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None


def is_full(board):
    """Check if the board is full."""
    return all(cell != " " for row in board for cell in row)


def play_game():
    """Run a single game session."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        print(f"{current_player}'s turn. Enter row and column (0, 1, 2):")

        try:
            row, col = map(int, input().split())

            if board[row][col] != " ":
                print("Cell already taken. Try again.")
                continue

            board[row][col] = current_player

        except (ValueError, IndexError):
            print("Invalid input. Enter row and column ")
            continue

        winner = check_winner(board)

        if winner:
            print_board(board)
            print(f"{winner} wins!")
            return winner

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            return None

        current_player = "O" if current_player == "X" else "X"


def main():
    """Main function to run the game."""
    print("Welcome to Tic Tac Toe!")
    scores = {"X": 0, "O": 0, "draws": 0}

    while True:
        winner = play_game()

        if winner:
            scores[winner] += 1
        else:
            scores["draws"] += 1

        print(
            f"Score - X: {scores['X']} | O: {scores['O']} | Draws: {scores['draws']}"
        )

        replay = input("Play again? (y/n): ").strip().lower()
        if replay != "y":
            break


if __name__ == "__main__":
    main()
