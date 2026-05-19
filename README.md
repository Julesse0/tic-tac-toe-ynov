# tic-tac-toe-ynov

## Description
This project implements a simple Tic Tac Toe game in Python. The game allows two players to take turns and play on a 3x3 grid. The first player to align three of their symbols (horizontally, vertically, or diagonally) wins. If the grid is full and no player has aligned three symbols, the game ends in a draw.

## Features
- Two-player gameplay
- Input validation for player moves
- Detection of win and draw conditions
- Replay option at the end of each game
- Persistent score tracking while replaying

## Requirements
- Python 3.6 or higher

## How to Run
1. Clone the repository.
2. Navigate to the project directory.
3. Run the game using the following command:
   ```
   python tic_tac_toe.py
   ```

## Pre-commit Hooks
This project uses the `pre-commit` framework to ensure code quality. The following hooks are configured:
- Trailing whitespace removal
- End-of-file fixer
- YAML file checks
- Python code formatting with `black`
- Linting with `flake8`

To install the hooks, run:
```
pre-commit install
```

## Semantic Versioning
This project follows semantic versioning. Tags will be created for each release.

## Contribution
All commits must follow the conventional commit format. Please create merge requests or pull requests for any changes, and ensure discussions are documented.

