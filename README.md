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

# Partie 2 - Conteneurisation Docker

Le conteneur Docker est pensé pour l’image du jeu en mode CLI, avec une base légère, une copie minimale des fichiers utiles et une exécution sans privilèges root.

### Ce que fait le Dockerfile
- Utilise l’image officielle `python:3.12-slim` comme base légère.
- Désactive la génération de fichiers bytecode et force la sortie immédiate pour faciliter le debug.
- Copie uniquement `tic_tac_toe.py` dans l’image finale.
- Crée un utilisateur non-root dédié pour exécuter l’application.
- Définit la commande de lancement de l’application avec `python tic_tac_toe.py`.
- N’expose aucun port réseau, car l’application fonctionne en ligne de commande et ne fournit pas de service réseau.

### Ce que fait le fichier .dockerignore
- Exclut les fichiers Git, environnements virtuels, caches Python et artefacts de test.
- Évite d’embarquer des fichiers locaux inutiles dans le contexte de build.
- Réduit la taille du contexte Docker et améliore le cache de build.

### Construire et lancer l’image
```bash
docker build -t tic-tac-toe-ynov .
docker run -it --rm tic-tac-toe-ynov
```

### Alternative Windows si `docker` n’est pas reconnu
```powershell
$env:Path = 'C:\Program Files\Docker\Docker\resources\bin;' + $env:Path
docker build -t tic-tac-toe-ynov .
docker run -it --rm tic-tac-toe-ynov
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

