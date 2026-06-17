# tic-tac-toe-ynov

## Description
Ce projet implémente un jeu de Morpion (Tic Tac Toe) simple en Python. Le jeu permet à deux joueurs de jouer à tour de rôle sur une grille de 3x3. Le premier joueur à aligner trois de ses symboles (horizontalement, verticalement ou en diagonale) gagne. Si la grille est pleine et qu'aucun joueur n'a aligné trois symboles, la partie se termine par un match nul.

## Fonctionnalités
- Jeu à deux joueurs
- Validation des entrées pour les coups des joueurs
- Détection des conditions de victoire et de match nul
- Option pour rejouer à la fin de chaque partie
- Suivi persistant des scores lors des nouvelles parties

## Prérequis
- Python 3.6 ou supérieur

## Comment lancer le jeu
1. Clonez le dépôt.
2. Naviguez vers le répertoire du projet.
3. Lancez le jeu en utilisant la commande suivante :
   ```
   python tic_tac_toe.py
   ```


# Partie 2 - Conteneurisation avec Docker

L'image Docker est conçue pour la version CLI du jeu : elle utilise une image de base légère, ne copie que les fichiers nécessaires et s'exécute sans les privilèges root.

### Ce que fait le Dockerfile
- Utilise l'image officielle `python:3.12-slim` comme base légère.
- Désactive la génération de bytecode et force une sortie non-buferisée pour simplifier le débogage.
- Copie uniquement `tic_tac_toe.py` dans l'image finale.
- Crée un utilisateur non-root dédié pour exécuter l'application.
- Définit la commande du conteneur sur `python tic_tac_toe.py`.
- N'expose aucun port réseau car l'application est un outil en ligne de commande (CLI) et ne fournit pas de service réseau.

### Ce que fait le .dockerignore
- Exclut les fichiers Git, les environnements virtuels, les caches Python et les artefacts de test.
- Évite d'inclure des fichiers locaux dans le contexte de build.
- Réduit la taille du contexte de build Docker et améliore les performances du cache.

### Construire et lancer l'image
```bash
docker build -t tic-tac-toe-ynov .
docker run -it --rm tic-tac-toe-ynov
```

### Alternative Windows si `docker` n'est pas reconnu
```powershell
$env:Path = 'C:\Program Files\Docker\Docker\resources\bin;' + $env:Path
docker build -t tic-tac-toe-ynov .
docker run -it --rm tic-tac-toe-ynov
```

### Docker Compose (compose.yaml)

- Un fichier `compose.yaml` a été ajouté pour simplifier l'exécution locale et les tests.
- Le fichier ne déclare que le service `app` (aucune base de données externe n'est requise pour ce CLI).
- Aucune configuration sensible n'est codée en dur dans `compose.yaml` : toutes les valeurs sont fournies via des variables d'environnement.
- Un fichier `.env.example` commité montre la structure de variables attendue. Créez un `.env` local (non commité) pour vos tests.
- Le dépôt ignore `.env` dans `.gitignore` afin d'éviter de commiter des secrets locaux.
- Le service `app` définit un `healthcheck` minimal et monte le répertoire du projet en lecture seule dans le conteneur pour protéger les fichiers source.

Pour démarrer la stack (si Docker est installé) depuis la racine du projet :

```bash
docker compose up --build
```

Variables d'exemple présentes dans `.env.example` : `APP_CONTAINER_NAME`, `APP_IMAGE_NAME`, `APP_WORKDIR`, `APP_USER`, `APP_COMMAND`, `APP_ENV`, `PYTHONDONTWRITEBYTECODE`, `PYTHONUNBUFFERED`.

Note : si Docker n'est pas disponible sous Windows, ajoutez le binaire Docker à votre `PATH` (voir la section « Alternative Windows » ci-dessus), puis relancez `docker compose`.

## Part 3 - Kubernetes & Helm (Atelier)

### Architecture et Justification des choix techniques
L'application `tic-tac-toe-ynov` est un jeu en ligne de commande (CLI) pur. Elle n'expose aucun port réseau et attend des interactions de l'utilisateur via l'entrée standard (`stdin`).

Par conséquent, les manifestes Kubernetes ont été adaptés à cette réalité :
- **Deployment** : Utilise les directives `stdin: true` et `tty: true` pour garder le processus Python ouvert et interactif.
- **Service, Ingress & PVC** : Volontairement ignorés. S'agissant d'un jeu interactif dans le terminal sans interface web, les objets `Service` et `Ingress` sont inapplicables car il n'y a aucun service réseau à exposer. De plus, l'application étant sans état (stateless), un `PersistentVolumeClaim` (PVC) n'est pas requis.
- **ConfigMap** : Externalise la configuration environnementale non-sensible (ex: `PYTHONUNBUFFERED`, `APP_ENV`).
- **Secret** : Ajouté pour démontrer la capacité à sécuriser des données (ex: fausses clés API ou variables sensibles injectées dans le conteneur).
- **Probes (Liveness/Readiness)** : Une commande `cat tic_tac_toe.py` est exécutée. Si le fichier est présent et accessible, le conteneur est considéré comme sain.

### Déploiement étape 1 : manifestes classiques

1. Assurez-vous d'avoir construit l'image et de l'avoir importée dans votre cluster K3D :
   ```bash
   docker build -t tic-tac-toe-ynov:latest .
   k3d image import tic-tac-toe-ynov:latest -c <nom-de-votre-cluster-k3d>
   ```
2. Appliquez les manifestes :
   ```bash
   kubectl apply -f k8s/classic/
   kubectl get all -n tic-tac-toe
   ```
3. **Jouer au jeu** : comme il s'agit d'un jeu CLI, attachez-vous au Pod pour jouer :
   ```bash
   kubectl get pods -n tic-tac-toe # Copiez le nom du pod
   kubectl attach -it <nom-du-pod> -n tic-tac-toe
   ```

### Déploiement étape 2 : chart Helm

Le chart Helm permet de packager et de paramétrer facilement ce déploiement.

1. Vérification et génération des manifests :
   ```bash
   helm lint k8s/helm/tic-tac-toe
   helm template k8s/helm/tic-tac-toe
   ```
2. Installation :
   ```bash
   helm install mon-jeu k8s/helm/tic-tac-toe -n tic-tac-toe --create-namespace
   ```
3. Mise à jour (upgrade) via surcharge de `values.yaml` :
   ```bash
   helm upgrade mon-jeu k8s/helm/tic-tac-toe -n tic-tac-toe --set replicaCount=2 --set config.APP_ENV=staging
   ```
4. Désinstallation :
   ```bash
   helm uninstall mon-jeu -n tic-tac-toe
   ```

## Pre-commit Hooks
Ce projet utilise le framework `pre-commit` pour garantir la qualité du code. Les hooks configurés sont :
- Suppression des espaces en fin de ligne
- Correction de la fin de fichier
- Vérification des fichiers YAML
- Formatage du code Python avec `black`
- Linting avec `flake8`

Pour installer les hooks, exécutez :
```
pre-commit install
```

## Semantic Versioning
Ce projet suit le versioning sémantique. Des tags seront créés pour chaque version.

## Contribution
Tous les commits doivent respecter le format des conventional commits. Merci de créer des merge requests ou des pull requests pour toute modification, et de documenter les échanges.
