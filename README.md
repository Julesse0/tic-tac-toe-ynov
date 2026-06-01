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


# Part 2 - Docker containerization

The Docker image is designed for the CLI version of the game: it uses a lightweight base image, copies only the required files, and runs without root privileges.

### What the Dockerfile does
- Uses the official `python:3.12-slim` image as a lightweight base.
- Disables bytecode generation and forces unbuffered output to simplify debugging.
- Copies only `tic_tac_toe.py` into the final image.
- Creates a dedicated non-root user to run the application.
- Sets the container command to `python tic_tac_toe.py`.
- Does not expose network ports because the application is a CLI tool and does not provide a network service.

### What the .dockerignore does
- Excludes Git files, virtual environments, Python caches and test artifacts.
- Avoids including local files in the build context.
- Reduces the size of the Docker build context and improves cache performance.

### Build and run the image
```bash
docker build -t tic-tac-toe-ynov .
docker run -it --rm tic-tac-toe-ynov
```

### Windows alternative if `docker` is not recognized
```powershell
$env:Path = 'C:\Program Files\Docker\Docker\resources\bin;' + $env:Path
docker build -t tic-tac-toe-ynov .
docker run -it --rm tic-tac-toe-ynov
```

### Docker Compose (compose.yaml)

- A `compose.yaml` file was added to simplify local execution and testing.
- The file declares only the `app` service (no external database is required for this CLI).
- No sensitive configuration is hard-coded in `compose.yaml`: all values are provided via environment variables.
- A committed `.env.example` file shows the expected variable structure. Create a local `.env` (not committed) for your tests.
- The repository ignores `.env` in `.gitignore` to avoid committing local secrets.
- The `app` service defines a minimal `healthcheck` and mounts the project directory read-only in the container to protect source files.

To bring the stack up (if Docker is installed) from the project root:

```bash
docker compose up --build
```

Example variables present in `.env.example`: `APP_CONTAINER_NAME`, `APP_IMAGE_NAME`, `APP_WORKDIR`, `APP_USER`, `APP_COMMAND`, `APP_ENV`, `PYTHONDONTWRITEBYTECODE`, `PYTHONUNBUFFERED`.

Note: if Docker is not available on Windows, add the Docker binary to your `PATH` (see the "Windows alternative" section above) and then rerun `docker compose`.

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
