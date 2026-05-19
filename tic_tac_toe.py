# Tic Tac Toe Game

# This file will contain the main structure of the game.


def print_board(board):
    """Prints the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def main():
    """Main function to run the game."""
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("Welcome to Tic Tac Toe!")
    print_board(board)


if __name__ == "__main__":
    main()
