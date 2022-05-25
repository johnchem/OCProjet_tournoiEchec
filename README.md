# OCProjet_chess_tournament
Projet 4 pour la formation developpeur python d'OpenClassrooms.

## comment utiliser environnement virtuel python
### Avec venv 
#### Initialiser
- dans le répertoire du projet, tapper la commande `python -m venv env`
- démarrer l'environnement avec la commande `env\Scripts\activate.bat` sur window
- installer les packages à partir du fichier requierement.txt : `pip install -r requirement.txt`

#### lancer l'environnement virtuel 
- taper la commande `env\Scripts\activate.bat` sur window

#### quitter l'environnement virtuel
- taper la commande `deactivate`

### Avec le gestionnaire de dependance Poetry
#### Initialiser
- installer le gestionnaire de dépendance poetry en suivant les instructions disponible à l'adresse : https://python-poetry.org/docs/#installation
- Aller dans le repertoire racine du project
- installer les packages à partir du fichier requierement.txt : `poetry install`

#### lancer l'environnement virtuel
avec poetry, le lancement explicite de l'environnement virtuel n'est pas nécéssaire si on lance l'application
via `poetry run`
- taper dans la console `poetry shell`

## Lancement du programme
- se placer dans le dossier racine du programme
- lancer le programme avec la commande `python -m chess_tournament.main` (sans poetry ou dans poetry shell), `poetry run python -m chess_tournament.main` (avec poetry hors du shell)

## Control peluchage avec flake8
- dans la console taper : `flake8 --exclude=.vscode --max-line-length=119 --format=html --htmldir=flake8_rapport chess_tournament`